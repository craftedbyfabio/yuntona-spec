---
title: Evidence-Graded Risk Mapping
version: "0.1"
status: draft
revised: 2026-09
licence: CC-BY-SA-4.0
taxonomies:
  - OWASP Top 10 for LLM Applications 2026
  - OWASP Top 10 for Agentic Applications (ASI) 2026
summary: An open, versioned specification for mapping graded evidence to the AI security risks it claims to mitigate.
---

# Evidence-Graded Risk Mapping

A vendor's evidence is only useful once it answers one narrow question: does it show that *this* tool mitigates *this* named risk? Not risk in general, and not "AI security" as a category. **This is the specification for grading that evidence and attaching it to the risk it's supposed to answer.**

> [!IMPORTANT]
> **Status: draft, published before results, deliberately.**
> No tool has been mapped against a named risk under this specification yet. Zero gold labels exist, no calibration has been fitted, and no threshold has been set. Publishing the method first means the mapping can be checked against a standard that was fixed before the results were known, and that any later finding can be argued with on the method, not just on the conclusion.

## Contents

1. [Scope boundary](#1-scope-boundary)
2. [Evidence classes](#2-evidence-classes)
3. [Risk signal and polarity](#3-risk-signal-and-polarity)
4. [Confidence is derived, not asked for](#4-confidence-is-derived-not-asked-for)
5. [What calibration actually is](#5-what-calibration-actually-is)
6. [Thresholds and published tolerance](#6-thresholds-and-published-tolerance)
7. [Blind review and anchoring](#7-blind-review-and-anchoring)
8. [The invisible failure](#8-the-invisible-failure)
9. [Nothing expires by default](#9-nothing-expires-by-default)
10. [Entity resolution](#10-entity-resolution)
11. [Taxonomy versioning](#11-taxonomy-versioning)
12. [Review discipline](#12-review-discipline)

## §1 Scope boundary

*Map against the standard; do not extend it*

This specification answers a narrower and more useful question than an evidence score does: for a named risk (a specific entry in a published taxonomy), does a tool's evidence show that risk is mitigated? Everything from here on, including the evidence-class ladder in §2, exists to make that answer trustworthy. Grading evidence with nothing to attach it to is not the point.

Tools are mapped against the *authoritative published risk description*: currently the OWASP LLM Top 10 (2026) and the OWASP Agentic (ASI) Top 10 (2026). This specification does not refine, sharpen or extend what a risk means, however tempting a new incident or paper makes that.

This is a rule. Hundreds of papers and incidents will refine what good coverage looks like for each entry. Absorb them into the rubric and the bar moves continuously, at which point labels stop being comparable across time, refits fit a moving target, and any published error rate silently changes meaning. The bar moves only when the standards body moves it, and then the taxonomy version increments and affected labels retire from the fitting set.

> [!NOTE]
> **The distinction that keeps this precise.** The evidence-class ladder in §2 is Yuntona's own construct and stays. It grades *how well a claim is supported*, not *what the risk means*. Extending the evidence axis is in scope. Extending the risk axis is not.

Where a standards body publishes its own risk-to-risk crosswalks, those are ingested and cited rather than rebuilt. Mapping tools to risks is the job; mapping risks to each other is someone else's published work.

## §2 Evidence classes

*Four grades for whether a claim reaches a named risk*

Every mapping (a tool, set against one named risk) carries a class, published alongside it, because not all source text is equal. Asking only whether source text supports a mapping collapses into "is there a quote," and that launders vendor marketing into a verdict.

### Class 1: Assertion

The vendor states coverage without describing how. Admissible as evidence, but cannot reach the auto-promotion threshold on its own.

> "Maps to the OWASP LLM Top 10."

### Class 2: Mechanism

The vendor describes how the capability works in enough detail to reason about. Still vendor-authored, so not truth, but much harder to fake vaguely.

> "Inspects prompts against a classifier trained on injection patterns."

### Class 3: Third-party

Independent testing, benchmark or audit by someone other than the vendor, assessed once, with nothing committed to checking it again. Admissible for the day it was produced, and after that day it is a historical record.

### Class 4: Currently verified

Independently checked, and something keeps checking. Either an open repository under active re-check (the mapping demotes automatically the moment the source changes), or a named, accredited certification with a tracked validity date, demoted the same way the moment it lapses. What earns this class is not who looked, but that someone is still looking.

The open-source path has two limits. First, confirming a capability by reading code only reaches open-source tools, and most commercial AI security tools are closed-source. Second, an open core does not mean the hosted product behaves like the repository.

The certification path qualifies only where the certifying body and scheme are named on an explicit, versioned allowlist, not any badge a vendor prints on its own homepage. AIUC-1 is the first documented case; extending the list is a deliberate decision, never a default. No such allowlist document exists yet as a published artifact. Until it does, treat the AIUC-1 reference as a stated intention, not a verifiable list.

---

Classes 3 and 4 will be near-empty across most of any directory, and that should be displayed. An all-assertion evidence base shown as such is more credible than an unlabelled one.

### The class must be queryable, not just displayed

A badge nobody can filter on is decoration: it changes no reader behaviour and costs them the one thing provenance is for. Evidence class, freshness state and risk entry are filter dimensions first, display second.

### Screenshots are discovery, not evidence

A product screenshot beside a headline does substantial verification work on a reader subliminally: the headline plausibly matches the image, which is good enough to keep browsing. But it verifies only that the site exists and roughly matches its description. It says nothing about whether the tool detects prompt injection, so it carries high perceived credibility and near-zero epistemic content. Screenshots may appear for orientation; they must never sit adjacent to a mapping where they read as corroborating it.

None of this produces a number in isolation. A Class 2 mechanism means nothing on its own. It means something once it is checked against the specific risk entity in §3 it is meant to answer. The class is a property of the mapping, not a property of the vendor.

## §3 Risk signal and polarity

*Each risk names the observable property evidence must anchor to*

Every one of the ten Agentic Top 10 entries lists logging and monitoring among its mitigations, phrased generically: maintain comprehensive logging, detect drift, monitor anomalous execution rates. A pure-play observability vendor's marketing pattern-matches against all ten on category alone, with nothing in the source text about an agent, a goal or a tool chain. That is category-inferred evidence wearing ten different costumes.

So each risk entity carries a second field beyond its definition: a short line naming the specific observable property that mitigation-class evidence must anchor to.

| Risk entity | Signal the evidence must anchor to |
| --- | --- |
| Agent goal hijack | Goal-state and tool-use-pattern baselines — not logging in general |
| Memory and context poisoning | Source attribution and write-frequency anomalies |
| Cascading failures | Blast-radius fan-out and lineage metadata |

A quote reading "full visibility into metrics, logs and traces" and nothing else satisfies none of these. It is Class 1 at best against every entry it is checked against, and should not be proposed as evidence for most of them at all.

### The same evidence can carry the opposite sign

Evidence is graded per risk entity, including its direction. Comprehensive prompt and completion logging is a mitigation for several risks. For sensitive information disclosure it is the exposure: the 2026 LLM Top 10 names excessive telemetry and monitoring leakage as a weakness in its own right, and cites observability platforms by name as the disclosure surface. Mitigation there is to restrict observability, not adopt it.

> [!NOTE]
> A grading system that scores only strength and never direction will record an aggravating factor as a control. Stored definitions therefore carry a polarity flag wherever a category of evidence is known to cut the other way for that entity.

## §4 Confidence is derived, not asked for

*Asking a model for its confidence measures its introspection*

Confidence is not a property of a tool, and not a property of a piece of evidence on its own. It is a property of one mapping (this evidence, checked against this risk), and it has to be earned the same way the mapping itself is.

Asking a model how confident it is produces a number that is not calibrated and cannot be prompted into being calibrated. Scoring it measures the model's introspection, and it shifts with every prompt edit. Confidence is instead derived from observable signals.

| Signal | What it measures |
| --- | --- |
| S1 | Sample agreement — same question asked N times, varying sampling only |
| S2 | Cross-framing agreement — the same question asked two ways, varying wording |
| S3 | Evidence density — graded by the class ladder in §2, not by presence of a quote |
| S4 | Per-entry prior — historical accuracy on that specific risk entry |
| S6 | Model-versus-human disagreement, recorded as three separate series |

### The agreement family has a known weakness

Supplying verbatim risk definitions as context on every call is almost certainly right for mapping quality. Without it, a model answers from whatever taxonomy snapshot it absorbed in training, with no version to attach to the label. But grounding *degrades the agreement signals*, in a predictable order: S1 is worst hit and should be expected to saturate and stop discriminating; S2 mostly converges; only evidence class and per-entry prior are untouched, because they are properties of the source document and of human verdicts respectively.

This is a trade-off: better context makes the model more reliable *and* makes the measure of its reliability less informative, simultaneously. If every agreement signal flattens under grounding, none of them belongs in the calibrator, and the system reduces to evidence class and prior, which is cheaper and simpler than what it replaces.

### S6 measures correctness, not stability

Agreement signals measure whether a model was *stable*. Comparing the model's proposal against the human verdict measures whether it was *right*. S6 is recorded as three series rather than one override rate, because collapsing them destroys the distinction that makes it useful:

| Series | Question |
| --- | --- |
| Verdict agreement | Was the mapping right? |
| Class agreement | Was the evidence graded right? |
| Span correction | Was the right sentence found? |

A right-verdict, wrong-sentence case is a pipeline miss and a mapping pass at the same time. One rate cannot say that.

## §5 What calibration actually is

*Everything above assumes it*

Every mapping proposal (a tool, a named risk, and the evidence connecting them) carries the signals from §4. Review three hundred of them and each becomes a row: a set of numbers, and an outcome. Then look for the pattern: of all pairs whose numbers looked roughly like that, how many were accepted? If seventy-two of a hundred were, that combination *means* 72%, because that is what happened.

Before labels exist, the numbers are just numbers. A sample-agreement score of 0.8 says the model agreed with itself 80% of the time. It does not say the mapping is 80% likely to be right. The labels are what connect the two.

> [!NOTE]
> **And note what three hundred labels buys.** It calibrates a confidence score. It does not train a system to do the mappings itself; that needs ten thousand or more, and a team. At three hundred the outcome is a working review band, not an autonomous mapper.

## §6 Thresholds and published tolerance

*The tolerance is published; the threshold is derived from it*

Once confidence means something, two thresholds follow from the labelled set at a stated false-mapping tolerance: above the upper threshold a mapping may promote automatically, between the two it enters the review queue, and below the lower one it is rejected and logged with its signals intact, never deleted.

The upper threshold is not chosen. It is the point where the historical accept rate matches the error rate that is acceptable to publish.

**Worked example, with illustrative numbers (nothing has been calibrated yet).** Say the published tolerance is 5%: Yuntona is willing to let one in twenty auto-promoted mappings turn out wrong. In the labelled set, every mapping scoring 0.82 confidence or above was correct at least 95% of the time; below 0.82, the error rate was worse than that. τ_hi is set at 0.82, read directly off that line in the data. If the next refit finds that 0.78 now clears the same 5% bar, τ_hi moves to 0.78. The tolerance, 5%, stays fixed across refits. The threshold (0.82, then 0.78) is whatever number currently satisfies it.

> [!NOTE]
> What gets published is the *tolerance*, the false-mapping rate held constant, and never the threshold itself. The threshold falls as calibration tightens, and a published number that silently moves week to week is exactly the provenance failure this specification exists to name. The threshold is a derived, versioned artifact.

Auto-promoted mappings are sampled and reviewed anyway, with an absolute floor on the number of audits per cycle rather than a bare percentage: five percent of a small weekly batch is one audit, which calibrates nothing. The audit sample is structurally required: without it, labels come only from the hard middle band and the calibration is fitted on a biased sample.

## §7 Blind review and anchoring

*The reviewer is the ruler, and rulers bend*

On the audit pile, the proposed verdict and the confidence are hidden and the evidence is adjudicated cold. Pre-filled answers anchor reviewers: someone shown "true, 0.91" agrees more often than someone shown the same evidence with nothing attached. Left unchecked, the labelled set stops measuring the mapping and starts measuring agreement with the model, and the calibration is then fitted against a contaminated ruler.

Divergence between blind and anchored verdicts is itself a measurement of the reviewer's anchoring bias. It costs nothing beyond hiding two fields, and it is publishable. A number that could embarrass the publisher is evidence the publisher was not selecting flattering ones.

### The question asked is part of the instrument

"Do you agree with this proposed mapping?" and "does the selected evidence demonstrate the capability?" produce different labels, and they diverge exactly where it matters: on a plausible mapping with weak evidence. A reviewer answering the first accepts what the second rejects.

So any rewording of the review question is a measurement regime change, not an interface tweak, and carries its own version stamped on every label alongside the taxonomy version. A label is valid only under the pair, and the two invalidate differently.

### Self-report is marked as such

Some fields are computed server-side and cannot be misreported. One cannot: whether the reviewer's decision relied on information beyond the selected evidence. It measures bar slippage: accepting because you know the product, rather than because the quoted span demonstrates it. A yes is recorded and never penalised, documented in the schema as self-reported, and excluded from anything treating computed measurements as ground truth. Mixing the two is how a self-declared number quietly acquires the authority of a measured one.

## §8 The invisible failure

*A queue can only ever show false positives*

Mappings that were never generated appear nowhere. No queue, no counter, no red state. Every quality signal described so far is blind to them by construction.

The countermeasure is borrowed from eDiscovery, where it is called an elusion test: take a sample from the set of pairs that were never proposed, review them properly as if they had been in the queue, and count how many would have been accepted.

> [!NOTE]
> **It is a detector, not a bound.** It can find fires; it cannot certify their absence. A small clean sweep still leaves a wide upper bound across the whole pile. Stated as a smoke alarm rather than a measurement, it is useful. Stated as a miss rate, it is false comfort.

Uniform sampling from a pile of mostly trivial negatives returns zero and means nothing. The sample is stratified to oversample close calls, and reported as a stratified estimate rather than a flat rate.

### Capability accretes, so this is permanent rather than a cold-start problem

Vendors ship features and rarely announce removals. A tool mapped to three risks in August may cover five by December, and nothing in a single-pass design ever looks again. Quote verification only checks existing mappings; it cannot propose new ones. So the never-proposed pile grows silently for tools already processed, and the sampling frame must include the unmapped pairs of already-mapped tools, not only tools with no mappings at all.

## §9 Nothing expires by default

*A freshness claim needs machinery behind it*

A mapping made against vendor documentation that changed four months ago is stale under a green timestamp. On a source change, any published mapping whose evidence span intersects the changed content drops back into review, which changes its state. Mappings that do not intersect keep their timestamp, so a marketing tweak does not re-review an entire tool.

The hash is taken over the quoted span, never the whole page. Hashing the page would demote every mapping derived from it on any edit anywhere.

### Demotion carries the wrong prior by default

Because capability accretes, a quote that no longer appears usually signals a documentation rewrite, not a withdrawn capability. A demotion is therefore framed to the reviewer as *probably still true, re-anchor it*, not as probable removal. The framing matters because a reviewer primed to expect removal will confirm removals that never happened.

### Publish the check series, not the last-checked date

A single timestamp cannot express recurrence. A batch of entries all checked on the same two days is indistinguishable, on the page, from a maintained system, and it reads as "checked in August" three months later, at which point the badge is a liability. What is stored and shown is the series: checked, unchanged, checked, changed, demoted, re-verified. A mapping shown surviving four re-checks makes a claim that cannot be copied without having done the work.

The same check has to run on the gold labels used to calibrate confidence, not only on what a reader sees. A gold label is itself a quote from a vendor's page at a point in time, so it can go stale exactly like a published mapping can, but nothing currently watches for that. Left unchecked, a stale label keeps getting used every time the threshold is recalculated, so the threshold ends up fitted against evidence that's no longer true, even while every mapping on the page still carries a fresh-looking timestamp. Checking freshness on the output and not on the calibration inputs protects the wrong half of the system.

## §10 Entity resolution

*Counts and mappings depend on it*

A tool is not a name. Before any count, overlap or mapping can be trusted there must be a canonical product record: one entity, with aliases, a vendor, a resolved domain, and a continuity history for renames and acquisitions.

This failure has been observed in practice. A scrape of one major public solutions directory contained exact duplicates after normalising case and punctuation, typo variants of the same product, three entries for one product differing only by a trailing character, and one product submitted four times under four different names, filed under two taxonomies, claiming every risk in both. None of that is misconduct: submitting each product line separately is normal vendor behaviour. The directory simply has no entity layer, so its counts measure submissions rather than products.

The underlying scrape isn't linked here yet. Until it is, treat the counts above as reported rather than independently checkable. It is the same caveat this specification asks readers to apply to every vendor claim it grades.

- **Match on resolved domain, not name.** Domains survive renames, acquisitions and marketing variants.
- **Name-scanning is not adjudication.** It catches duplicates whose names match and nothing else. A product filed under a different name matches nothing, so duplicate counts from a name scan are a floor, and the residue resurfaces later disguised as new entries.
- **Mappings attach to the entity, never the name.** Otherwise a rename silently orphans every mapping and the tool re-enters the never-proposed pile without anything firing.

## §11 Taxonomy versioning

*Renumbering fails silently, and it fails wrongly*

If a label is keyed on a risk number and a future taxonomy renumbers, the label does not orphan. It reattaches to whatever that number now means. Nobody would notice it as a missing mapping, because it is a confident, populated, entirely incorrect one.

So labels bind to a canonical risk entity with version-scoped number aliases, and the number is display metadata. Every public risk reference renders with its taxonomy version, because a reference reading "LLM01" is ambiguous the moment numbering shifts.

### This has already happened

In the 2025 to 2026 revision of the LLM Top 10, eight of ten entries renumbered and five expanded. A label keyed to the string LLM07 under the 2025 list means system prompt leakage. Under 2026 the same string means misinformation, an unrelated risk. A string-keyed label survives the bump, reattaches, and publishes as confidently wrong, with nothing firing. There were eight such collisions in a single revision.

These counts were measured while migrating the data behind Yuntona's earlier tool directory from the 2025 list to the 2026 list. That dataset is not published, so treat the counts as reported rather than independently checkable.

### The requeue rule is asymmetric

A version bump raises two independent questions per entry: whether the *identity* moved (renumbered, new, merged, split) and whether the *meaning* moved (unchanged, expanded, narrowed, replaced). Conflating them is how requeue decisions go wrong.

| Semantic change | Prior accepts | Prior rejects |
| --- | --- | --- |
| Unchanged | Hold | Hold |
| Expanded | Hold | Requeue |
| Narrowed | Requeue | Hold |
| Replaced | Retire | Retire |

Evidence demonstrating a narrow risk still demonstrates part of a broader one, so accepts hold when a risk expands. Failing the narrow test says nothing about the newly added territory, so rejects requeue. Narrowing inverts both. Replacement makes the evidence stale by definition, so it is fresh review rather than revalidation.

Standards bodies publish a new list, not a diff annotated with these classifications. Someone has to classify each move, per entry, per revision. That classification is recorded with its reasoning, because every downstream requeue depends on it. It is in scope under §1, because it classifies how a published definition moved without redefining the risk.

## §12 Review discipline

*Every rejection carries a countable code*

A free-text rejection reason cannot be counted. Rejection rates *per reason* are what reveal whether a pipeline is failing in a particular way, and prose hides exactly the pattern worth seeing. So a rejection records a code, and only a failure of the evidence counts as a rejection.

The reviewer answers one question: does the selected evidence demonstrate that this tool addresses this risk? When it does not, the reason is one of two bar failures.

| Code | Bar failure | Meaning |
| --- | --- | --- |
| A | Category inferred | The source mentions LLMs or AI but describes no specific mitigation. There is nothing to anchor to. |
| B | Unsupported by source | The quote does not demonstrate the claimed capability. |

**Why assertion is not a rejection reason.** A bare vendor claim is Class 1 on the ladder in §2: admissible evidence that cannot reach the auto-promotion threshold on its own. Listing it as a failure would make the ladder contradict itself, with the same evidence graded Class 1 on an accept and a failure on a reject. A bare claim is accepted at Class 1, capped.

### Two outcomes that are not rejections

Some pairs fail for reasons that say nothing about the evidence. They are routed instead, and neither writes a gold label.

| Outcome | Meaning | What happens |
| --- | --- | --- |
| Wrong risk entry | The evidence is sound; it demonstrates a different risk | The pair is re-proposed against the correct entry |
| Tool out of scope | The tool does not secure AI systems. A judgement about the tool, not this evidence | The tool goes back to triage, and every remaining pair for it is withdrawn |

Counting either as a rejection makes the rejection rate unreadable as a pipeline-failure signal. Recording a wrong-risk pair as a rejection does further damage: it teaches the calibrator that sound evidence is a negative example, which is exactly backwards.

### A wrong sentence is corrected, not rejected

When the mapping is right but the pipeline quoted the wrong sentence, the reviewer selects the right passage in the source and makes it the evidence span. Without that, a wrong mapping and a wrong quote both come back as rejections, and the rejection rate stops saying which part of the pipeline failed. Corrections are recorded as the span-correction series in §4.
