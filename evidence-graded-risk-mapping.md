---
title: Evidence-Graded Risk Mapping
version: "0.2"
status: draft
revised: 2026-10
licence: CC-BY-SA-4.0
taxonomies:
  - "OWASP Top 10 for LLM Applications 2026 (Version 2026)"
  - "OWASP Top 10 for Agentic Applications 2026 (Version 2026, December 2025)"
register: signal-register.md
summary: An open, versioned specification for grading what a tool's evidence shows against a named AI security risk.
---

# Evidence-Graded Risk Mapping

A vendor's evidence is only useful once it answers one narrow question: what does it show about whether *this* tool mitigates *this* named risk? Not risk in general, and not "AI security" as a category. **This is the specification for naming what the evidence shows and attaching it to the risk it is supposed to answer.**

It grades claims. It does not measure protection. Whether a tool actually stops an attack in a given environment is a test run against that environment, and no reading of vendor evidence substitutes for it. What this specification can do is say, for each tool and risk, how far the published evidence reaches, and show where it stops.

> [!IMPORTANT]
> **Status: draft, published before results, deliberately.**
> No tool has been graded against a named risk under this specification. Publishing the method first means any later grade can be checked against a standard that was fixed before the grades were known, and argued with on the method, not just on the conclusion.

## Contents

1. [Scope boundary](#1-scope-boundary)
2. [Evidence rungs](#2-evidence-rungs)
3. [The signal register and polarity](#3-the-signal-register-and-polarity)
4. [Certification is recorded, not graded](#4-certification-is-recorded-not-graded)
5. [Review](#5-review)
6. [The invisible failure](#6-the-invisible-failure)
7. [Nothing expires by default](#7-nothing-expires-by-default)
8. [Entity resolution](#8-entity-resolution)
9. [Taxonomy and register versioning](#9-taxonomy-and-register-versioning)
10. [Review discipline](#10-review-discipline)

## §1 Scope boundary

*Map against the standard; do not extend it*

This specification answers a narrower and more useful question than an evidence score does: for a named risk (a specific entry in a published taxonomy), what does a tool's evidence show about whether that risk is mitigated? Everything from here on exists to make that answer trustworthy.

Tools are mapped against the *authoritative published risk description*: currently the OWASP Top 10 for LLM Applications 2026 and the OWASP Top 10 for Agentic Applications 2026. This specification does not refine, sharpen or extend what a risk means, however tempting a new incident or paper makes that.

This is a rule. Hundreds of papers and incidents will refine what good coverage looks like for each entry. Absorb them into the rubric and the bar moves continuously, and grades made a year apart stop meaning the same thing. The bar moves only when the standards body moves it, and then the taxonomy version increments and affected rows requeue (§9).

> [!NOTE]
> **The distinction that keeps this precise.** The rungs in §2 are Yuntona's own construct. They grade *how far a claim is supported*, not *what the risk means*. The signal register in §3 selects, for each entry, one mechanism from that entry's own published mitigation guidance and cites it by number. Selecting from the standard is in scope. Adding a mechanism the standard does not name is not.

Where a standards body publishes its own risk-to-risk crosswalks, those are cited rather than rebuilt. The LLM Top 10 2026 maps its entries to the Agentic Top 10 in its Appendix A; the Agentic Top 10 maps its entries to the LLM Top 10 *2025* in its own Appendix A. The second crosswalk uses the older numbering, which is why §9 exists.

## §2 Evidence rungs

*Four names for what has been shown, and nothing added up*

Every mapping (a tool, set against one named risk) carries a rung, published with it. The rung names what the evidence shows about the mechanism registered for that risk (§3). Asking only whether source text supports a mapping collapses into "is there a quote," and that launders vendor marketing into a verdict.

| Rung | What the evidence shows |
| --- | --- |
| **Claimed** | The vendor says the tool addresses the risk, but the quoted evidence does not describe the risk's registered primary signal. |
| **On-signal** | The quoted evidence describes the registered primary signal, not only a shared line. |
| **Self-measured** | The vendor publishes a measurement of that signal, with the corpus, the operating point and the outcome attached. |
| **Externally measured** | A party other than the vendor ran a test of that signal and published it readably enough to identify the corpus, operating point, outcome and product version. |

The examples below are illustrative and describe no real product.

> **Claimed:** "Protects your agents against memory poisoning."
>
> **On-signal:** "Every memory write is scanned before commit, and entries carrying instructions are rejected."

### What each measured rung requires

**Self-measured.** The published number must name:

- the **corpus** (a named public benchmark with its version, or a published sample of the vendor's own set);
- the **operating point** (the false-positive rate, threshold or utility cost at which the number holds);
- the **outcome** (what was counted: detection rate, attack success rate, residual rate);
- the **product version** tested and the date.

A number missing any of these is refused, and the row stays at On-signal. A test run by a third party under the vendor's commission or payment is Self-measured, with the third party named.

**Externally measured.** Run by a party with no commercial relationship with the vendor for that test, against a named product and version, with the four items above readable from what was published.

Where the signal register sets a **measurement condition** for an entry, it binds both rungs. For example, LLM01:2026 directs readers to "reject static-only attack-success claims," so a prompt-injection number from a static attack set only stays On-signal and is marked *static-only*.

### Rechecked is a modifier, not a rung

**Externally measured, rechecked** means the same method was run again by a party other than the vendor, within 12 months of the previous run, against the product version current at the time. "The same method" means the same corpus, identified by hash or published version, at the same operating point.

A vendor rerunning its own test stays Self-measured, however often it reruns. A fresh independent test never ranks below a second self-test. The recheck series is shown, not just the latest date (§7).

### Where a quote lands

| The quoted span… | Outcome |
| --- | --- |
| describes the registered primary signal | On-signal, or higher with a qualifying measurement |
| names the risk or claims coverage, but describes only a shared line or a different mechanism | Claimed |
| neither names the risk nor describes the signal | Rejected, Code A (§10) |
| does not demonstrate what it is quoted for | Rejected, Code B (§10) |
| — and the risk has no registered primary signal | Capped at Claimed |

### Rungs are names, never numbers

A rung is a label in a cell. It is never summed, averaged, or counted into a tool-level figure. No published view states that a tool "covers seven of ten risks" or ranks tools by how many rungs they reach. A covered count turns ten Claimed rows into a number that reads like coverage, and that is the laundering this specification exists to prevent.

The opposite is required: Self-measured and Externally measured will be near-empty across most tools, and that is displayed. An evidence base shown as mostly Claimed is more credible than an unlabelled one.

Two more properties stay off the rung. **Polarity** (whether evidence mitigates or aggravates the risk) is recorded separately (§3). **Extraction confidence**, any score a model or pipeline produced while proposing a mapping, never appears on a published row (§5).

### The rung must be queryable, not just displayed

A badge nobody can filter on is decoration: it changes no reader behaviour and costs them the one thing provenance is for. Rung, freshness state, polarity and risk entry are filter dimensions first, display second.

### Screenshots are discovery, not evidence

A product screenshot beside a headline does substantial verification work on a reader subliminally: the headline plausibly matches the image, which is good enough to keep browsing. But it verifies only that the site exists and roughly matches its description. It says nothing about whether the tool detects prompt injection, so it carries high perceived credibility and near-zero epistemic content. Screenshots may appear for orientation; they must never sit adjacent to a mapping where they read as corroborating it.

The rung is a property of the mapping, not of the vendor. A vendor can be Externally measured on one risk and Claimed on the next.

## §3 The signal register and polarity

*Each risk names the one mechanism evidence must describe*

OWASP's mitigation guidance repeats a handful of controls across nearly every entry: logging and monitoring, least privilege, human approval, sandboxing, encryption, "zero trust." Nine of the ten Agentic Top 10 entries list some form of logging or monitoring among their mitigations. An observability vendor's marketing pattern-matches against all of them on category alone, with nothing in the source text about an agent, a goal or a tool chain. That is category-inferred evidence wearing ten costumes.

So each risk entry carries a **primary signal**: the one mechanism, chosen from that entry's own published guidance and cited to it by number, that a quote must describe to reach On-signal. The signals live in a separate, versioned file, the [signal register](signal-register.md). This section states the rules the register follows.

1. **One primary signal per entry, cited.** Each signal cites the numbered guideline(s) in the entry it comes from. A signal with no citation is not registered.
2. **A decision, not a record.** The signal is something that blocks, rejects, excludes, pauses or gates. Detection that only records or alerts does not qualify, because it does not mitigate on its own.
3. **Closed against shared lines.** The register lists the shared lines. A quote that states only a shared line never reaches On-signal for any entry. Where a signal names a *specific form* of a shared line (sandboxed execution of agent-generated code for ASI05, enforced spending caps for LLM06), the quote must describe that specific form.
4. **Boundaries in OWASP's words.** Each entry records where OWASP draws its edge against neighbouring entries, quoted, next to the signal. A mapping on the wrong side is re-proposed against the right entry, not rejected (§10).
5. **Measurement conditions where OWASP sets them.** If an entry's own text sets a condition on what counts as a test, the register records it and it binds rungs 3 and 4.

### Worked example: ASI06 Memory & Context Poisoning

The primary signal is **a decision on the memory write or on the later read**: content scanned before it is committed to memory (ASI06:2026 PM2), or provenance on each entry that lets a poisoned or low-trust entry be excluded at retrieval (PM5, PM9).

Encryption, generic logging and least-privilege access (PM1) do not clear it. Nor does a classifier on the current turn's prompt: ASI06 context "excludes one-time input prompts covered under LLM01:2025 Prompt Injection," which is LLM01:2026 under the current list. Detection of suspicious write frequencies does not clear it unless the entry can then be excluded.

The boundary matters most on one case, so it is written in. A chat turn that is later summarised into memory is ASI06, not prompt injection, because the harm is the later read. OWASP names this as an ASI06 example ("context-window manipulation": content injected "so that it is later summarized or persisted in memory"). ASI01 Agent Goal Hijack remains the entry for direct alteration of the agent's goals, including through pre-positioned documents.

### Proposing a second primary signal

One signal per entry deliberately shuts out other mechanisms, and without a way back in the register would be one reader's cut. So a second primary signal can be proposed:

- by **public issue** on this repository, citing the numbered guideline in the same entry that it comes from;
- decided in public, with the **reason for rejection** recorded on the issue if it is declined;
- if accepted, as a **register version bump** that requeues the affected rows (§9). It is never a reviewer improvising on a single mapping.

An open-ended "any reasonable control" clause is not offered. It would let the logging sentence back in.

The register's first edition carries one pending proposal as the example: quarantine, expiry or decay of unverified memory for ASI06 (PM7, PM8), for a tool that never scans the write but stops serving entries that have not been verified.

### The same evidence can carry the opposite sign

Evidence is graded per risk entry, including its direction. Comprehensive prompt and completion logging is a mitigation input for several risks. For sensitive information disclosure it is the exposure: LLM02:2026 names observability platforms (Langfuse, LangSmith, Datadog LLM Observability) as logging full prompts, completions, chunks and traces by default, and its mitigations say to scrub logs before ingestion and never log raw reasoning traces to unrestricted observability.

> [!NOTE]
> A grading system that records only strength and never direction will record an aggravating factor as a control. Each row therefore carries a polarity, and the register flags every entry where a category of evidence is known to cut the other way.

## §4 Certification is recorded, not graded

*A certificate answers a different question*

A certification such as AIUC-1 assures that a vendor operates its *own* AI systems safely. It does not test whether the vendor's product mitigates a named risk for the buyer. Treating it as evidence on the ladder is a category error, so it has no rung.

It is recorded as a separate attribute: **vendor's own system independently assured**.

| Field | Content |
| --- | --- |
| Scheme | The named scheme and version |
| Issuer | The certifying or auditing body |
| Certificate ID | As issued |
| Scope | The issuer's scope statement, quoted |
| Valid from / until | Dates as issued |
| Verification | A link to the issuer's own verification page or register |

The rules are short:

- A certificate is recorded only if it can be checked at the issuer. A badge on the vendor's own site is not enough.
- It lapses on its expiry date, and the lapse is shown.
- It never changes a rung, and is never displayed adjacent to a rung, where it would read as corroboration.
- No allowlist is needed, because the attribute grades nothing. It states a checkable fact.

## §5 Review

*Every row is reviewed by a person; nothing promotes itself*

A model or pipeline may propose mappings: a tool, a risk, a quoted span, a suggested rung. Every row is then reviewed by a person before it is published. Nothing is promoted automatically, at any confidence.

Version 0.1 planned a calibrated confidence score and automatic promotion above a derived threshold. Both are removed. Calibration needed hundreds of labels before the score meant anything; while every row is reviewed anyway, a score adds nothing to the decision. Published next to a rung, it would also be read as a grade. Any confidence a model emits while proposing stays in the pipeline and never appears on a row.

### Blind review and anchoring

On review, the proposed rung is hidden and the evidence is adjudicated cold. Pre-filled answers anchor reviewers: someone shown "On-signal" agrees more often than someone shown the same evidence with nothing attached. Left unchecked, the reviewed set stops measuring the evidence and starts measuring agreement with the pipeline.

Where a sample is reviewed both ways, the divergence between blind and anchored verdicts measures the reviewer's anchoring bias. It costs nothing beyond hiding a field, and it is publishable. A number that could embarrass the publisher is evidence the publisher was not selecting flattering ones.

### The question asked is part of the instrument

The reviewer answers one question: **which rung does the selected evidence reach for this risk's registered signal?**

"Do you agree with this proposed mapping?" would produce different labels, diverging exactly where it matters: on a plausible mapping with weak evidence. So any rewording of the review question is a change of measurement regime, not an interface tweak. It carries its own version, stamped on every row alongside the taxonomy and register versions (§9). This question is regime 2; version 0.1's question was regime 1.

### Self-report is marked as such

Some fields are computed and cannot be misreported. One cannot: whether the reviewer's decision relied on information beyond the selected evidence. It measures bar slippage, accepting because you know the product rather than because the quoted span demonstrates it. A yes is recorded and never penalised, documented as self-reported, and excluded from anything treating computed measurements as ground truth.

### Review-quality series

Comparing the pipeline's proposal with the reviewer's verdict measures whether the pipeline was *right*. It is recorded as three series rather than one override rate, because collapsing them destroys the distinction:

| Series | Question |
| --- | --- |
| Verdict agreement | Was the mapping right? |
| Rung agreement | Was the evidence graded right? |
| Span correction | Was the right sentence found? |

A right-verdict, wrong-sentence case is a pipeline miss and a mapping pass at the same time. One rate cannot say that. These series describe the pipeline; they never appear on a row.

## §6 The invisible failure

*A queue can only ever show false positives*

Mappings that were never generated appear nowhere. No queue, no counter, no red state. Every quality signal described so far is blind to them by construction.

The countermeasure is borrowed from eDiscovery, where it is called an elusion test: take a sample from the set of pairs that were never proposed, review them properly as if they had been in the queue, and count how many would have reached any rung.

> [!NOTE]
> **It is a detector, not a bound.** It can find fires; it cannot certify their absence. A small clean sweep still leaves a wide upper bound across the whole pile. Stated as a smoke alarm rather than a measurement, it is useful. Stated as a miss rate, it is false comfort.

Uniform sampling from a pile of mostly trivial negatives returns zero and means nothing. The sample is stratified to oversample close calls, and reported as a stratified estimate rather than a flat rate.

### Capability accretes, so this is permanent rather than a cold-start problem

Vendors ship features and rarely announce removals. A tool mapped to three risks in August may cover five by December, and nothing in a single-pass design ever looks again. Quote verification only checks existing mappings; it cannot propose new ones. So the never-proposed pile grows silently for tools already processed, and the sampling frame must include the unmapped pairs of already-mapped tools, not only tools with no mappings at all.

## §7 Nothing expires by default

*A freshness claim needs machinery behind it*

A mapping made against vendor documentation that changed four months ago is stale under a green timestamp. On a source change, any published mapping whose evidence span intersects the changed content drops back into review. Mappings that do not intersect keep their timestamp, so a marketing tweak does not re-review an entire tool.

The hash is taken over the quoted span, never the whole page. Hashing the page would demote every mapping derived from it on any edit anywhere.

A change to the signal register requeues rows too: see §9.

### Demotion carries the wrong prior by default

Because capability accretes, a quote that no longer appears usually signals a documentation rewrite, not a withdrawn capability. A demotion is therefore framed to the reviewer as *probably still true, re-anchor it*, not as probable removal. A reviewer primed to expect removal will confirm removals that never happened.

### Publish the check series, not the last-checked date

A single timestamp cannot express recurrence. A batch of entries all checked on the same two days is indistinguishable, on the page, from a maintained system, and it reads as "checked in August" three months later, at which point the badge is a liability. What is stored and shown is the series: checked, unchanged, checked, changed, demoted, re-verified. The same applies to the recheck series behind Externally measured, rechecked.

## §8 Entity resolution

*Counts and mappings depend on it*

A tool is not a name. Before any mapping can be trusted there must be a canonical product record: one entity, with aliases, a vendor, a resolved domain, and a continuity history for renames and acquisitions.

This failure has been observed in practice. A scrape of one major public solutions directory contained exact duplicates after normalising case and punctuation, typo variants of the same product, three entries for one product differing only by a trailing character, and one product submitted four times under four different names, filed under two taxonomies, claiming every risk in both. None of that is misconduct: submitting each product line separately is normal vendor behaviour. The directory simply has no entity layer, so its counts measure submissions rather than products.

The underlying scrape isn't linked here yet. Until it is, treat the counts above as reported rather than independently checkable. It is the same caveat this specification asks readers to apply to every vendor claim it grades.

- **Match on resolved domain, not name.** Domains survive renames, acquisitions and marketing variants.
- **Name-scanning is not adjudication.** It catches duplicates whose names match and nothing else. A product filed under a different name matches nothing, so duplicate counts from a name scan are a floor, and the residue resurfaces later disguised as new entries.
- **Mappings attach to the entity, never the name.** Otherwise a rename silently orphans every mapping and the tool re-enters the never-proposed pile without anything firing.

## §9 Taxonomy and register versioning

*Renumbering fails silently, and it fails wrongly*

If a row is keyed on a risk number and a later taxonomy renumbers, the row does not orphan. It reattaches to whatever that number now means. Nobody notices it as a missing mapping, because it is a confident, populated, entirely incorrect one.

So rows bind to a canonical risk entity with version-scoped number aliases, and the number is display metadata. Every public risk reference renders with its taxonomy version, because a reference reading "LLM01" is ambiguous the moment numbering shifts.

### This has already happened

In the 2025 to 2026 revision of the LLM Top 10, eight of ten entries were renumbered. Under the 2025 list, LLM07 means system prompt leakage. Under 2026, the same string means misinformation, and system prompt leakage has become LLM08:2026 Hidden Context Exposure. A string-keyed label survives the bump, reattaches, and publishes as confidently wrong, with nothing firing.

The collision is live in the published documents themselves. The Agentic Top 10 (December 2025) cross-references the LLM Top 10 by its *2025* numbers. ASI06 builds on "LLM08:2025 Vector and Embedding Weaknesses," which is LLM09:2026; read against the current list, LLM08 is Hidden Context Exposure. Every cross-reference taken from OWASP text is therefore resolved to the canonical entity, never copied as a number string.

### Each row carries three versions

| Version | Moves when |
| --- | --- |
| Taxonomy | The standards body publishes a new list |
| Signal register | A primary signal is added, changed or withdrawn (§3) |
| Review question regime | The review question is reworded (§5) |

A row is valid only under the combination it was made under, and the three invalidate differently.

### The requeue rule is asymmetric

A taxonomy bump raises two independent questions per entry: whether the *identity* moved (renumbered, new, merged, split) and whether the *meaning* moved (unchanged, expanded, narrowed, replaced). Conflating them is how requeue decisions go wrong.

| Semantic change | Prior accepts | Prior rejects |
| --- | --- | --- |
| Unchanged | Hold | Hold |
| Expanded | Hold | Requeue |
| Narrowed | Requeue | Hold |
| Replaced | Retire | Retire |

Evidence demonstrating a narrow risk still demonstrates part of a broader one, so accepts hold when a risk expands. Failing the narrow test says nothing about the newly added territory, so rejects requeue. Narrowing inverts both. Replacement makes the evidence stale by definition, so it is fresh review rather than revalidation.

Standards bodies publish a new list, not a diff annotated with these classifications. Someone has to classify each move, per entry, per revision. That classification is recorded with its reasoning, because every downstream requeue depends on it. It is in scope under §1, because it classifies how a published definition moved without redefining the risk.

A register change follows the same logic:

| Register change | Requeue |
| --- | --- |
| Second primary signal added | Rows at Claimed and Code A rejects for that entry (they may now be On-signal) |
| Primary signal narrowed or withdrawn | Rows at On-signal and above for that entry |
| Boundary note changed | Rows for that entry and the neighbour named in the note |

## §10 Review discipline

*Every rejection carries a countable code*

A free-text rejection reason cannot be counted. Rejection rates *per reason* are what reveal whether a pipeline is failing in a particular way, and prose hides exactly the pattern worth seeing. So a rejection records a code, and only a failure of the evidence counts as a rejection.

| Code | Bar failure | Meaning |
| --- | --- | --- |
| A | Category inferred | The source neither names the risk nor describes its registered signal. It mentions AI or LLMs, or describes only a shared line, with nothing to anchor to. |
| B | Unsupported by source | The quote does not demonstrate what it is quoted for. |

**Why a bare claim is not a rejection.** A vendor naming the risk without describing the signal is Claimed (§2): admissible, recorded, and visibly the bottom rung. Listing it as a failure would make the ladder contradict itself, with the same evidence graded Claimed on one row and rejected on another.

### Two outcomes that are not rejections

Some pairs fail for reasons that say nothing about the evidence. They are routed instead, and neither counts in the rejection rate.

| Outcome | Meaning | What happens |
| --- | --- | --- |
| Wrong risk entry | The evidence is sound; it demonstrates a different risk, often across a boundary recorded in the register | The pair is re-proposed against the correct entry |
| Tool out of scope | The tool does not secure AI systems. A judgement about the tool, not this evidence | The tool goes back to triage, and every remaining pair for it is withdrawn |

Counting either as a rejection makes the rejection rate unreadable as a pipeline-failure signal.

### A wrong sentence is corrected, not rejected

When the mapping is right but the pipeline quoted the wrong sentence, the reviewer selects the right passage in the source and makes it the evidence span. Without that, a wrong mapping and a wrong quote both come back as rejections, and the rejection rate stops saying which part of the pipeline failed. Corrections are recorded in the span-correction series (§5).

---

*OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026 are published by the OWASP GenAI Security Project under CC BY-SA 4.0. Passages quoted here are reproduced under that licence with attribution. This specification refers to their entries; it does not redefine them.*
