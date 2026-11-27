"""Checks for the deterministic pipeline. Run: python3 -I tools/test_pipeline.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P

EV = "[Code at release v1.0, https://example.com/a.py#L1-L3]\nif spent > cap:\n    raise Stop()\n"
ok = lambda ans, ev=EV, pb=None: P.check_answer(ans, ev, pb) == []

# who mapped it
assert not ok({"outcome": "wrong risk entry", "entry": "ASI02:2026"})
assert ok({"outcome": "wrong risk entry", "entry": "ASI02:2026"}, pb="directory category")
assert not ok({"outcome": "Code A"})

# marks
assert not ok({"outcome": "claimed only", "polarity": "mitigates", "marks": ["off by default"]})
assert ok({"outcome": "explained by vendor", "polarity": "mitigates", "marks": ["off by default"]})
assert not ok({"outcome": "explained by vendor", "polarity": "mitigates", "marks": ["made up"]})

# code-confirmed
yes = {"outcome": "explained by vendor", "polarity": "mitigates", "code_confirms": True, "code_line": "raise Stop()"}
assert ok(yes)
assert not ok(dict(yes, code_line="raise Halt()"))
assert not ok(yes, ev="Plain documentation, no code.")
assert P.code_confirmed(dict(yes, _problems=[]), dict(yes, _problems=[]))
assert not P.code_confirmed(dict(yes, _problems=[]), dict(yes, code_confirms=False, _problems=[]))

# marks must match to publish
a = {"outcome": "explained by vendor", "polarity": "mitigates", "marks": ["off by default"]}
b = {"outcome": "explained by vendor", "polarity": "mitigates", "marks": []}
assert P.route(a, b, [])[0] == "person"
assert P.route(a, dict(a), [])[0] == "publish"
assert P.route(dict(a, entry=""), dict(a, entry=None), [])[0] == "publish"

# a person's decision stands until the quotes, sources or register entry change
k = P.decision_key("ASI03:2026", [("https://x/doc#L1", "Each runtime gets  its own token.")], "signal v1")
assert k == P.decision_key("ASI03:2026", [("https://x/doc#L1", "Each runtime gets its own token.")], "signal v1")
assert k != P.decision_key("ASI03:2026", [("https://x/doc#L1", "Each runtime gets its own token.")], "signal v2")
assert k != P.decision_key("ASI03:2026", [("https://x/doc#L2", "Each runtime gets its own token.")], "signal v1")
assert P.route(a, b, [], standing={"outcome": "claimed only"})[0] == "reviewed"

# replaced decisions come back to a person when the answer differs
old = {"outcome": "explained by vendor", "polarity": "mitigates", "marks": ["off by default"]}
assert P.route(a, dict(a), [], replaced=old)[0] == "publish"
assert P.route(b, dict(b), [], replaced=old)[0] == "person"

# cross-references
assert P.cross_references("See ASI04:2026. Product-SBOM presets.", "LLM04:2026") == ["ASI04:2026"]
assert P.cross_references("The firewall (ASI02:2026), lists (ASI03:2026) and ASI02:2026 again", "LLM03:2026") == ["ASI02:2026", "ASI03:2026"]
assert P.cross_references("LLM05:2026 is not covered.", "LLM05:2026") == []
assert P.cross_references("See ASI08 for the kill switch.", "ASI10:2026") == ["ASI08:2026"]
assert P.cross_references("Formerly LLM07:2025.", "LLM08:2026") == []

print("all pipeline checks pass")
