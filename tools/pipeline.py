"""Deterministic parts of the grading pipeline (spec §5 and §11).

No model is called here. This module:
  - reduces a source to the text a human reader can see, and flags what it removed;
  - builds the grader input for one risk entry from signal-register.md;
  - checks a grader's answer and routes a row from two answers.

Usage:
  python3 -I tools/pipeline.py prompts  grader-tests.yaml  out/prompts.jsonl
  python3 -I tools/pipeline.py score    grader-tests.yaml  out/prompts.jsonl out/answers-a.jsonl out/answers-b.jsonl
"""
import hashlib, html, json, re, sys

OUTCOMES = {"claimed only", "explained by vendor", "tested by vendor", "tested independently",
            "not covered (vendor states)", "no evidence found", "Code A", "Code B", "wrong risk entry"}
HIGH = {"tested by vendor", "tested independently"}
AT_LEAST_EXPLAINED = {"explained by vendor"} | HIGH
MARKS = {"fixed attacks only", "off by default"}
LABEL = re.compile(r"^\[([^\]\n]+)\]\s*$", re.M)
INVISIBLE = re.compile("[​‌‍⁠﻿­]")
STEER = re.compile(r"\b(ignore (all |any )?(previous|prior)|grade (this|it) as|record this product|"
                   r"ai (reviewers?|graders?|systems?)|assessors?|yuntona|you are an ai)\b", re.I)


def visible_text(raw):
    """Return (text, flags). Text is what a reader of the rendered page could see."""
    flags = []
    comments = re.findall(r"<!--(.*?)-->", raw, re.S)
    if comments:
        flags.append("html comment removed")
        if any(STEER.search(c) for c in comments):
            flags.append("instruction in removed comment")
    t = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    hidden = r"<(\w+)[^>]*(?:display\s*:\s*none|visibility\s*:\s*hidden|\shidden[\s>])[^>]*>.*?</\1>"
    if re.search(hidden, t, re.S | re.I):
        flags.append("hidden element removed")
    t = re.sub(hidden, " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    if INVISIBLE.search(t):
        flags.append("invisible characters removed")
        t = INVISIBLE.sub(" ", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = "\n".join(line.strip() for line in t.splitlines() if line.strip())
    if STEER.search(t):
        flags.append("text addressed to graders")
    return t, flags


def register_entries(path="signal-register.md"):
    s = open(path).read()
    shared = s[s.index("## Shared lines"):s.index("\n---\n", s.index("## Shared lines"))].strip()
    entries = {}
    for m in re.finditer(r"^### ((?:ASI|LLM)\d\d:2026) (.+?)\n(.*?)(?=^### |^---|\Z)", s, re.M | re.S):
        entries[m.group(1)] = {"name": m.group(2).strip(), "body": m.group(3).strip()}
    return entries, shared


def grader_input(risk, evidence, proposed_by, entries, shared):
    e = entries[risk]
    parts = [f"Risk entry: {risk} {e['name']}", "", "Register entry (signal, does not clear, boundary, "
             "measurement condition, polarity):", e["body"], "", shared, ""]
    if proposed_by:
        parts += [f"Proposed by: {proposed_by}", ""]
    parts += ["Evidence:", "<<<", evidence, ">>>"]
    return "\n".join(parts)


def norm(t):
    return re.sub(r"\s+", " ", INVISIBLE.sub(" ", t or "")).strip()


def code_sources(evidence):
    """Return the text of every source labelled [Code at release <version>, <address>]."""
    labels = list(LABEL.finditer(evidence))
    out = []
    for i, m in enumerate(labels):
        if m.group(1).startswith("Code at release "):
            end = labels[i + 1].start() if i + 1 < len(labels) else len(evidence)
            out.append(evidence[m.end():end])
    return out


def as_bool(v):
    """Graders may answer true/false/null as JSON values or as strings."""
    return {"true": True, "false": False, "null": None, "none": None}.get(str(v).strip().lower(), v) \
        if isinstance(v, str) else v


def check_answer(ans, evidence, proposed_by=None):
    """Return the problems with one answer; an empty list means it passes."""
    p = []
    if not isinstance(ans, dict) or ans.get("outcome") not in OUTCOMES:
        return ["outcome not allowed"]
    if ans["outcome"] in ("wrong risk entry", "Code A") and not proposed_by:
        p.append(f"{ans['outcome']} but the vendor itself mapped the evidence")
    sent = ans.get("supporting_sentence") or ""
    if ans["outcome"] != "no evidence found" and sent and norm(sent) not in norm(evidence):
        p.append("supporting sentence not in evidence")
    if ans["outcome"] == "wrong risk entry" and not ans.get("entry"):
        p.append("no entry given")
    marks = ans.get("marks") or []
    if not set(marks) <= MARKS:
        p.append("mark not allowed")
    if "off by default" in marks and not (ans["outcome"] in AT_LEAST_EXPLAINED and ans.get("polarity") == "mitigates"):
        p.append("off by default on a row that does not mitigate at explained by vendor or higher")
    code = code_sources(evidence)
    cc = as_bool(ans.get("code_confirms"))
    if cc not in (True, False, None):
        p.append("code_confirms not true, false or null")
    elif cc is not None and not code:
        p.append("code_confirms answered but the evidence has no code source")
    elif cc is not None and ans["outcome"] not in AT_LEAST_EXPLAINED:
        p.append("code_confirms answered on a row below explained by vendor")
    elif cc is True and not any(norm(ans.get("code_line")) and norm(ans.get("code_line")) in norm(c) for c in code):
        p.append("code line not in a code source")
    return p


def code_confirmed(a, b):
    """§5: the mark is added only when both graders say true and both answers pass the checks."""
    return all(as_bool(x.get("code_confirms")) is True and not x.get("_problems") for x in (a, b))


def decision_key(risk, quotes, register_body):
    """§5: what a person's decision is tied to. quotes is a list of (source address, quoted span).
    Labels and headings are not part of it; the quoted text, its source and the register entry are."""
    h = hashlib.sha256()
    for part in [risk, norm(register_body)] + [f"{src}\n{norm(q)}" for src, q in sorted(quotes)]:
        h.update(part.encode() + b"\x00")
    return h.hexdigest()


RISK_ID = re.compile(r"\b((?:ASI|LLM)\d\d)(?::(\d{4}))?\b")


def cross_references(quote, risk, year="2026"):
    """§5: the other risk entries a vendor's quote for this risk points to, in order, one level only.
    A bare identifier ("see ASI08") is read in the taxonomy the source answers; one naming another
    year is not followed, because the numbering differs between editions."""
    seen = []
    for m in RISK_ID.finditer(quote):
        if m.group(2) and m.group(2) != year:
            continue
        rid = f"{m.group(1)}:{year}"
        if rid != risk and rid not in seen:
            seen.append(rid)
    return seen


def differs(answer, decision):
    """True when a graders' answer would change what a replaced person's decision showed."""
    return (answer.get("outcome"), answer.get("polarity") or None, tuple(sorted(answer.get("marks") or []))) != \
           (decision.get("outcome"), decision.get("polarity") or None, tuple(sorted(decision.get("marks") or [])))


def route(a, b, code_flags, standing=None, replaced=None):
    """Apply the §5 table. Returns (decision, reasons).
    standing: a person's earlier decision whose key matches this row; it stands, and the
    graders' answers are kept only for the agreement and override series.
    replaced: a person's earlier decision whose key no longer matches; the row goes to a
    person if the graders' answer differs from it."""
    if standing is not None:
        return "reviewed", ["a person's decision stands: quotes, sources and register entry unchanged"]
    reasons = []
    if code_flags:
        reasons.append("code flag: " + ", ".join(code_flags))
    for name, ans in (("A", a), ("B", b)):
        if ans.get("_problems"):
            reasons.append(f"grader {name} answer failed checks: {', '.join(ans['_problems'])}")
        if ans.get("injection_flag"):
            reasons.append(f"grader {name} flagged injection")
        if ans.get("outcome") in HIGH:
            reasons.append(f"grader {name} reached {ans['outcome']}")
        if ans.get("polarity") == "aggravates":
            reasons.append(f"grader {name} marked aggravates")
    # an empty field may come back as "" or null; both mean empty
    key = lambda x: (x.get("outcome"), x.get("polarity") or None, x.get("entry") or None,
                     tuple(sorted(x.get("marks") or [])))
    same = key(a) == key(b)
    if not same:
        reasons.append("graders disagree")
    if replaced is not None and (differs(a, replaced) or differs(b, replaced)):
        reasons.append("differs from a person's replaced decision")
    return ("person" if reasons else "publish"), reasons


def main():
    import yaml
    cmd, tests = sys.argv[1], yaml.safe_load(open(sys.argv[2]))["cases"]
    entries, shared = register_entries()
    if cmd == "prompts":
        with open(sys.argv[3], "w") as out:
            for c in tests:
                text, flags = visible_text(c["evidence"])
                if c.get("quoted_span") and norm(c["quoted_span"]) not in norm(text):
                    out.write(json.dumps({"id": c["id"], "dropped_by_code": True}) + "\n")
                    continue
                out.write(json.dumps({"id": c["id"], "code_flags": flags, "evidence": text,
                                      "proposed_by": c.get("proposed_by"),
                                      "input": grader_input(c["risk"], text, c.get("proposed_by"), entries, shared)}) + "\n")
        return
    if cmd == "score":
        prompts = {r["id"]: r for r in map(json.loads, open(sys.argv[3]))}
        A = {r["id"]: r for r in map(json.loads, open(sys.argv[4]))}
        B = {r["id"]: r for r in map(json.loads, open(sys.argv[5]))}
        fails = 0
        for c in tests:
            exp, pr = c["expected"], prompts[c["id"]]
            if pr.get("dropped_by_code"):
                ok = bool(exp.get("dropped_by_code"))
                print(f"{'PASS' if ok else 'FAIL'} {c['id']:6} dropped by code")
                fails += not ok
                continue
            line = []
            for name, ans in (("A", A.setdefault(c["id"], {})), ("B", B.setdefault(c["id"], {}))):
                ans["_problems"] = check_answer(ans, pr["evidence"], pr.get("proposed_by"))
                good = (ans.get("outcome") == exp.get("outcome")
                        and (exp.get("polarity") is None or ans.get("polarity") == exp["polarity"])
                        and (exp.get("entry") is None or ans.get("entry") == exp["entry"])
                        and set(exp.get("marks", [])) == set(ans.get("marks") or [])
                        and ("code_confirms" not in exp or as_bool(ans.get("code_confirms")) is exp["code_confirms"])
                        and not ans["_problems"])
                line.append((name, good, ans.get("outcome"), ans.get("polarity")))
            decision, reasons = route(A[c["id"]], B[c["id"]], pr["code_flags"])
            route_ok = (decision == "person") == bool(exp.get("route_to_person"))
            if "code_confirmed" in exp:
                route_ok = route_ok and code_confirmed(A[c["id"]], B[c["id"]]) is exp["code_confirmed"]
            ok = all(g for _, g, _, _ in line) and route_ok
            fails += not ok
            detail = "; ".join(f"{n}={o}/{p}" + ("" if g else " WRONG") for n, g, o, p in line)
            print(f"{'PASS' if ok else 'FAIL'} {c['id']:6} expected {exp.get('outcome')}/{exp.get('polarity')} | "
                  f"{detail} | {decision}{'' if route_ok else ' (route WRONG)'}" + (f" [{'; '.join(reasons)}]" if reasons else ""))
        print(f"\n{len(tests) - fails}/{len(tests)} passed")


if __name__ == "__main__":
    main()
