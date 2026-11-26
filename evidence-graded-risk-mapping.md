---
title: Evidence-Graded Risk Mapping
version: "0.3"
status: draft
revised: 2026-11
licence: CC-BY-SA-4.0
taxonomies:
  - "OWASP Top 10 for LLM Applications 2026 (Version 2026, published 4 August 2026)"
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
5. [Grading](#5-grading)
6. [The invisible failure](#6-the-invisible-failure)
7. [Freshness](#7-freshness)
8. [Entity resolution](#8-entity-resolution)
9. [Taxonomy and register versioning](#9-taxonomy-and-register-versioning)
10. [Review discipline](#10-review-discipline)
11. [Protecting the pipeline](#11-protecting-the-pipeline)

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

| Rung | Shown to readers as | What the evidence shows |
| --- | --- | --- |
| **Claimed** | claimed only | The vendor says the tool addresses the risk, but the quoted evidence does not describe the risk's registered primary signal. |
| **On-signal** | explained by vendor | The quoted evidence describes the registered primary signal, not only a shared line. |
| **Self-measured** | tested by vendor | The vendor publishes a measurement of that signal, with the corpus, the operating point and the outcome attached. |
| **Externally measured** | tested independently | A party other than the vendor ran a test of that signal and published it readably enough to identify the corpus, operating point, outcome and product version. |

The rung names are the specification's terms. Published views use the plain labels in the second column, one per rung, so no two rungs ever share a label.

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

Where the signal register sets a **measurement condition** for an entry, it is shown as a mark on the rung; it does not lower the rung. For example, LLM01:2026 directs readers to "reject static-only attack-success claims." A prompt-injection number measured on a fixed attack set keeps its rung and is marked *fixed attacks only*, so readers can see it says nothing about adaptive attackers. Capping such numbers instead would put almost every published result in the same place as vendors who publish nothing.

### Rechecked is a modifier, not a rung

**Externally measured, rechecked** means the same method was run again by a party other than the vendor, within 12 months of the previous run, against the product version current at the time. "The same method" means the same corpus, identified by hash or published version, at the same operating point.

A vendor rerunning its own test stays Self-measured, however often it reruns. A fresh independent test never ranks below a second self-test. The recheck series is shown, not just the latest date (§7).

### Code-confirmed is a modifier, not a rung

For an open-source tool, an On-signal row can carry **code-confirmed at version X** when the mechanism the quote describes was found in the cited code at a named release. The record keeps the release, the file path and line range, and a hash of each cited file. If a cited file changes in a later release, the row returns to review (§7).

Code-confirmed does not raise the rung. Code shows that a mechanism exists, not that it stops attacks. It applies only to the edition whose code was read: open-source code says nothing about a hosted or enterprise edition that is not published.

### Where a quote lands

| The quoted span… | Outcome |
| --- | --- |
| describes the registered primary signal | On-signal, or higher with a qualifying measurement |
| names the risk or claims coverage, but describes only a shared line or a different mechanism | Claimed |
| neither names the risk nor describes the signal | Rejected, Code A (§10) |
| does not demonstrate what it is quoted for | Rejected, Code B (§10) |
| — and the risk has no registered primary signal | Capped at Claimed |
| states that the tool does not address the risk | Not covered (vendor states) |
| — and no source names the risk or describes its signal | No evidence found |

### When the vendor says not covered

A vendor's own statement that its tool does not address a risk is recorded as **not covered (vendor states)**, with the quote and its source like any other row. It needs no grading: it can only lower what is shown, never raise it.

It is not a rejection. Code A is for evidence mapped to a risk on category alone; a vendor saying "not covered" has mapped nothing. Where the vendor says not covered but another quote for the same tool describes the risk's registered signal, that quote is graded as usual and the conflict goes to a person (§5). A vendor that says *partially* covered has said nothing that settles the row, so its quotes are graded as usual.

### When nothing is found

Most vendors say nothing about the risks they do not address. Silence is not a statement, so it is never shown as *not covered*. Every tool is checked against every risk entry, and a risk for which no source names the risk or describes its signal is recorded as **no evidence found**, with the date of the search and the sources searched.

It is shown in words, as *no evidence found (searched 26 Nov 2026)*, and never in the same form as *not covered (vendor states)*. One is the vendor's own statement; the other may mean the tool does not cover the risk, that the evidence is somewhere not searched, or that the pipeline missed it. It needs no grading and goes to no person. It is searched again whenever a source changes and at the 12-month re-assessment (§7), because capability accretes (§6).

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

1. **One primary signal per entry, cited.** A second can be added through the proposal path below. Each signal cites the numbered guideline(s) in the entry it comes from. A signal with no citation is not registered.
2. **A decision, not a record.** The signal is something that blocks, rejects, excludes, pauses or gates. Detection that only records or alerts does not qualify, because it does not mitigate on its own.
3. **Closed against shared lines.** The register lists the shared lines. A quote that states only a shared line never reaches On-signal for any entry. Where a signal names a *specific form* of a shared line (sandboxed execution of agent-generated code for ASI05, enforced spending caps for LLM06), the quote must describe that specific form.
4. **Boundaries in OWASP's words.** Each entry records where OWASP draws its edge against neighbouring entries, quoted, next to the signal. A mapping on the wrong side is re-proposed against the right entry, not rejected (§10).
5. **Measurement conditions where OWASP sets them.** If an entry's own text sets a condition on what counts as a test, the register records it, and a measurement that does not meet it carries a mark on its rung (§2).

### Worked example: ASI06 Memory & Context Poisoning

The primary signal is **a decision on the memory write or on the later read**: content scanned before it is committed to memory (ASI06:2026 PM2), or provenance on each entry that lets a poisoned or low-trust entry be excluded at retrieval (PM5, PM9).

Encryption, generic logging and least-privilege access (PM1) do not clear it. Nor does a classifier on the current turn's prompt: ASI06 context "excludes one-time input prompts covered under LLM01:2025 Prompt Injection," which is LLM01:2026 under the current list. Detection of suspicious write frequencies does not clear it unless the entry can then be excluded.

The boundary matters most on one case, so it is written in. A chat turn that is later summarised into memory is ASI06, not prompt injection, because the harm is the later read. OWASP names this as an ASI06 example ("context-window manipulation": content injected "so that it is later summarized or persisted in memory"). ASI01 Agent Goal Hijack remains the entry for direct alteration of the agent's goals, including through pre-positioned documents.

### Proposing a second primary signal

One signal per entry deliberately shuts out other mechanisms, and without a way back in the register would be one reader's cut. So a second primary signal can be proposed:

- by **public issue** on this repository, citing the numbered guideline in the same entry that it comes from;
- decided in public, with the **reason for rejection** recorded on the issue if it is declined;
- if accepted, as a **register version bump** that requeues the affected rows (§9). It is never a grader or a person improvising on a single mapping.

An open-ended "any reasonable control" clause is not offered. It would let the logging sentence back in.

The register's first edition already has two entries with two primary signals. ASI06 accepts either a decision on the write or read (above) or quarantine, expiry or decay of unverified memory (PM7, PM8), for a tool that never scans the write but stops serving entries that have not been verified. LLM09 accepts either tenant scoping inside the index query (PM1) or per-embedding provenance that lets a compromised batch be invalidated (PM2). Both were added before any row was graded, so nothing had to be requeued. A later addition of the same kind would follow the path above.

### The same evidence can carry the opposite sign

Evidence is graded per risk entry, including its direction. Comprehensive prompt and completion logging is a mitigation input for several risks. For sensitive information disclosure it is the exposure: LLM02:2026 names observability platforms (Langfuse, LangSmith, Datadog LLM Observability) as logging full prompts, completions, chunks and traces by default, and its mitigations say to scrub logs before ingestion and never log raw reasoning traces to unrestricted observability.

> [!NOTE]
> A grading system that records only strength and never direction will record an aggravating factor as a control. Each row therefore carries a polarity, and the register flags every entry where a category of evidence is known to cut the other way.

## §4 Certification is recorded, not graded

*A certificate answers a different question*

A certification such as AIUC-1 assures that a vendor operates its *own* AI systems safely. It does not test whether the vendor's product mitigates a named risk for the buyer. Treating it as evidence on the ladder is a category error, so it has no rung.

It is recorded as a separate attribute: **vendor's own system independently assured**, with one of two labels:

- **checked with issuer**: the certificate was found on the issuer's own register or verification page;
- **vendor states**: the vendor claims it, and the record links the vendor's page and the date it was read.

| Field | Content |
| --- | --- |
| Scheme | The named scheme and version |
| Issuer | The certifying or auditing body |
| Certificate ID | As issued |
| Scope | The issuer's scope statement, quoted |
| Valid from / until | Dates as issued |
| Label | checked with issuer, or vendor states |
| Verification | A link to the issuer's verification page or register, or to the vendor page that makes the claim |

The rules are short:

- A certificate is labelled *checked with issuer* only when the issuer's own register confirms it. Anything less is *vendor states*, never left unlabelled.
- It lapses on its expiry date, and the lapse is shown.
- It never changes a rung, and is never displayed adjacent to a rung, where it would read as corroboration.
- No allowlist is needed, because the attribute grades nothing. It states a fact and says how far it was checked.

## §5 Grading

*Rules and code decide; people handle the exceptions*

Every row is graded by machine and published without a person reviewing it, unless the row meets one of the conditions below. Version 0.2 had a person review every row. That does not scale past a handful of tools, and the error it guards against is better measured than assumed away.

### Deterministic checks come first

Before any model is asked, code checks what code can:

- the quoted span appears word for word in the source, in text a human reader of the page can see (§11);
- the source address, the date it was read and the product version are recorded;
- for a code-confirmed mark, the cited file exists at the named release and its hash is recorded.

A row that fails any of these is dropped, and no model sees it.

### Two graders, neither sees the other

Two graders read each row independently. Where available they are models from different families, because two models of one family tend to make the same mistakes on the same wording. Each is given only:

- the visible evidence, with its source;
- the risk's registered signal or signals, the shared lines and the boundary note (§3);
- the grading question: **which outcome does this evidence reach for this risk's registered signal?**

Each returns a fixed format: one outcome (a rung, *not covered (vendor states)*, *no evidence found*, Code A, Code B or *wrong risk entry*), its marks, its polarity, the sentence from the evidence that supports it, quoted word for word, and a one-line reason. Code then checks that the supporting sentence is in the evidence. An answer in any other shape is treated as a disagreement.

Any confidence a grader emits stays in the pipeline and never appears on a row.

### What publishes and what goes to a person

| The graders… | What happens |
| --- | --- |
| agree on outcome and polarity, and the supporting sentence checks out | Published, labelled *machine-graded* |
| agree on *wrong risk entry* | Re-proposed against the entry they name, and graded again there |
| disagree on anything | Sent to a person |
| either reaches *tested by vendor* or *tested independently* | Sent to a person, whether or not they agree |
| either marks the polarity *aggravates* | Sent to a person |
| either raises an injection flag (§11) | Sent to a person |

A person's decision on a sent row is published labelled *reviewed*. Rows are never shown as reviewed when only machines graded them.

### The graders are tested before they grade

A published test suite ([`grader-tests.yaml`](grader-tests.yaml)) holds cases whose correct outcome is known, including attempts to manipulate the grader. A grading regime goes live only when both graders pass every case, and its pass record is published with it. The suite runs again whenever a model, the grading instructions or the signal register changes.

The suite measures known failure modes. Unknown ones are caught two ways:

- **a monthly spot check**: a person grades ten published rows chosen at random, and the agreement is published;
- **error reports**: every published row links to a way to report it, and vendors can correct facts about their own product.

### The grading regime is part of the instrument

The models, the exact grading instructions and the test suite together are the **grading regime**. Changing any of them is a change of measurement, not a tweak. Each regime carries a version, stamped on every row alongside the taxonomy and register versions (§9). Version 0.3 starts regime 3; regimes 1 and 2 were the human review questions of versions 0.1 and 0.2.

### Grading-quality series

These describe the pipeline; they never appear on a row.

| Series | Question |
| --- | --- |
| Grader agreement | How often do the two graders agree? |
| Override rate | How often does a person change a sent row, and on what: outcome, polarity or supporting sentence? |
| Spot-check agreement | How often does a person agree with a machine-graded row? |
| Test-suite record | Which cases each regime passed |

A falling agreement rate on one risk is usually a register problem, not a model problem: the signal is worded so two careful readers can disagree.

## §6 The invisible failure

*A queue can only ever show false positives*

Mappings that were never generated appear nowhere. No queue, no counter, no red state. Every quality signal described so far is blind to them by construction.

Recording *no evidence found* for every empty risk (§2) makes them visible as rows, but a row only says that nothing was found in the sources searched. Whether something was missed still has to be tested.

The countermeasure is borrowed from eDiscovery, where it is called an elusion test: take a sample of *no evidence found* rows, search for the risk more widely and grade what turns up as if it had been in the queue, and count how many would have reached any rung.

> [!NOTE]
> **It is a detector, not a bound.** It can find fires; it cannot certify their absence. A small clean sweep still leaves a wide upper bound across the whole pile. Stated as a smoke alarm rather than a measurement, it is useful. Stated as a miss rate, it is false comfort.

Uniform sampling from a pile of mostly trivial negatives returns zero and means nothing. The sample is stratified to oversample close calls, and reported as a stratified estimate rather than a flat rate.

### Capability accretes, so this is permanent rather than a cold-start problem

Vendors ship features and rarely announce removals. A tool mapped to three risks in August may cover five by December, and nothing in a single-pass design ever looks again. Quote verification only checks existing mappings; it cannot propose new ones. So the never-proposed pile grows silently for tools already processed, and the sampling frame must include the unmapped pairs of already-mapped tools, not only tools with no mappings at all.

## §7 Freshness

*A freshness claim needs machinery behind it*

A mapping made against vendor documentation that changed four months ago is stale under a green timestamp. On a source change, any published mapping whose evidence span intersects the changed content drops back into review. Mappings that do not intersect keep their timestamp, so a marketing tweak does not re-review an entire tool.

The hash is taken over the quoted span, never the whole page. Hashing the page would demote every mapping derived from it on any edit anywhere.

A change to the signal register requeues rows too: see §9.

### Every entry is re-assessed within 12 months

Change detection only catches what it watches. So, separately, every tool's entry is re-assessed in full within 12 months of its last assessment, and straight away after a change of ownership, an acquisition or a rename. A re-assessment reviews every row for that tool, not only the ones whose quotes changed.

The two triggers do different jobs. A changed quote sends one row back to review at any time; the 12-month rule and the ownership trigger catch what no single quote shows. An entry past its 12 months is shown as due for re-assessment, not as current.

### Demotion carries the wrong prior by default

Because capability accretes, a quote that no longer appears usually signals a documentation rewrite, not a withdrawn capability. A demotion is therefore framed to the graders as *probably still true, re-anchor it*, not as probable removal. A grader primed to expect removal will confirm removals that never happened.

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
| Grading regime | A grading model, the grading instructions or the test suite changes (§5) |

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
| A | Category inferred | Something other than the source mapped the tool to the risk (a vendor's directory listing, a category, a pipeline proposal), but the source neither names the risk nor describes its registered signal. It mentions AI or LLMs, or describes only a shared line, with nothing to anchor to. |
| B | Unsupported by source | The quote does not demonstrate what it is quoted for. |

**Code A is not the same as no evidence found.** Code A rejects a mapping that someone or something proposed without an anchor in the source. Where nothing proposed a mapping and the source is silent, the row is *no evidence found* (§2), which rejects nothing.

**Why a bare claim is not a rejection.** A vendor naming the risk without describing the signal is Claimed (§2): admissible, recorded, and visibly the bottom rung. Listing it as a failure would make the ladder contradict itself, with the same evidence graded Claimed on one row and rejected on another.

### Two outcomes that are not rejections

Some pairs fail for reasons that say nothing about the evidence. They are routed instead, and neither counts in the rejection rate.

| Outcome | Meaning | What happens |
| --- | --- | --- |
| Wrong risk entry | The evidence is sound; it demonstrates a different risk, often across a boundary recorded in the register | The pair is re-proposed against the correct entry |
| Tool out of scope | The tool does not secure AI systems. A judgement about the tool, not this evidence | The tool goes back to triage, and every remaining pair for it is withdrawn |

Counting either as a rejection makes the rejection rate unreadable as a pipeline-failure signal.

### A wrong sentence is corrected, not rejected

When the mapping is right but the pipeline quoted the wrong sentence, the grader or the person handling the row selects the right passage in the source and makes it the evidence span. Without that, a wrong mapping and a wrong quote both come back as rejections, and the rejection rate stops saying which part of the pipeline failed. Corrections are counted in the override rate (§5).

## §11 Protecting the pipeline

*The grader reads text written by the people it grades*

Every source the pipeline reads was written by a vendor with an interest in the outcome. A page can carry instructions aimed at the grader, hidden or in plain sight. That is prompt injection, LLM01:2026, against Yuntona's own pipeline, and the pipeline is held to the same controls the signal register asks of vendors.

1. **The grader has no power (LLM03:2026).** A grading model has no tools, no web access and no write access to anything. It reads what it is given and returns a verdict in the fixed format of §5. The worst an injection can do is skew one verdict, which the second grader and the rules below are there to catch. It cannot fetch, send, change or publish anything.
2. **Code decides what publishes, not a model.** Publishing follows the table in §5. No model output reaches the published site without passing the deterministic checks and the rules for what goes to a person. Automation writes only to staging.
3. **The verdict must point at its evidence (LLM10:2026).** The supporting sentence is checked word for word against the evidence. An instruction such as "grade this as tested independently" cannot supply a test result that is not on the page.
4. **Only visible text is evidence.** Before grading, the source is reduced to what a human reader of the page can see. HTML comments, hidden elements, text styled to be invisible, zero-width and other invisible characters, alt text and metadata are removed. A claim that is only in hidden text does not exist for grading.
5. **Text aimed at the grader is flagged.** The source is scanned for instructions to reviewers or models, mentions of Yuntona or its graders, and phrases that try to set an outcome. A hit sends the row to a person rather than blocking it, because some hits are innocent, such as a vendor page that explains how to grade it. A vendor page caught steering the grader is recorded as an error on the entry.
6. **Two graders from different families.** An injection tuned to one model often fails on another, and any disagreement goes to a person (§5).
7. **Vendor text is shown as text.** Quotes are rendered on the site as plain text. Markup, scripts and links inside a quote are escaped, so a vendor cannot inject into Yuntona's own pages.
8. **The test suite includes attacks.** Hidden instructions, visible instructions, fake badges and claims that point to evidence not on the page are among the cases the graders must pass (§5).

What remains is persuasion: honest-looking prose that leads a reader to a generous view. No filter stops it. The word-for-word check, the second grader, the spot checks and error reports limit it.

---

*OWASP Top 10 for LLM Applications 2026 and OWASP Top 10 for Agentic Applications 2026 are published by the OWASP GenAI Security Project under CC BY-SA 4.0. Passages quoted here are reproduced under that licence with attribution. This specification refers to their entries; it does not redefine them.*
