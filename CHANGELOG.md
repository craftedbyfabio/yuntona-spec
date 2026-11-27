# Changelog

Each entry corresponds to a git tag. Dates are the date the tag was created.

## Evidence-Graded Risk Mapping

### v0.3 — unreleased (draft)

Version 0.2 had a person review every row, blind to the proposed rung. Grading one tool took
35 decisions, which does not scale. Version 0.3 lets rules and two independent graders decide, sends
the hard cases to a person, and measures the graders instead of assuming a person is always right.

**Changed**

- **§5 Review → Grading.** Rows are machine-graded and published without a person unless the two
  graders disagree, either reaches *tested by vendor* or higher, either marks *aggravates*, or the
  source tried to steer them. Published rows say *machine-graded* or *reviewed*. *Why:* a person on
  every row does not scale, and the error rate of the graders can be measured.
- **Grading regime replaces review question regime.** The models, the grading instructions and the
  test suite together are versioned and stamped on every row. Regime 3 starts with v0.3.
- **Quality series** now track grader agreement, person overrides, spot-check agreement and the
  test-suite record.

**Added**

- **Not covered (vendor states).** A vendor's statement that its tool does not address a risk is
  recorded as such, without grading. *Why:* v0.2 had no outcome for it; graders were forcing it into
  Code A, which is for evidence mapped on category alone.
- **No evidence found.** Every tool is checked against every risk, and a risk with nothing in the
  sources is recorded as *no evidence found*, with the date and the sources searched. It is never
  shown as *not covered*. *Why:* silence is not a statement, and recording it makes the pairs the
  pipeline missed visible to the §6 sample. Code A now applies only where something other than the
  source proposed the mapping.
- **§11 Protecting the pipeline.** Controls against prompt injection by vendor pages: graders with
  no tools or write access, code decides publishing, word-for-word evidence checks, visible text
  only, flags for text aimed at graders, two model families, vendor text escaped on the site.
  *Why:* the grader reads text written by the people it grades.
- **Grader test suite** (`grader-tests.yaml`, suite 1): 47 known-answer cases, 3 of them pages with nothing to find and 7 of them attempts to
  manipulate the grader. Both graders must pass every case before a regime goes live.
- **Monthly spot check** of ten machine-graded rows by a person, with the agreement published.
- **Off by default mark** (§2). A mechanism that does nothing until the deployer sets it up, such
  as a policy engine that allows everything with no rules or a budget unset until configured, is
  marked *off by default*. Added only when the evidence states the default. *Why:* grading Preloop
  showed four rows reading *explained by vendor* for controls that do nothing out of the box, and
  readers could not tell.
- **How code-confirmed is awarded** (§2, §5). Both graders must say the cited code shows the
  mechanism and quote the executable line that does; comments, docstrings, configuration fields and
  names do not count. Code checks the quoted line is inside a cited code source. Where the graders
  do not both say so, the mark is left off without sending the row to a person. *Why:* v0.2 defined
  the mark but nothing in the pipeline awarded it.
- **Who put the quote under the risk** (§2, §10). A vendor that files another entry's mechanism
  under a risk has made a claim, recorded as *claimed only*. *Wrong risk entry* and Code A apply
  only when Yuntona made the mapping: a directory category, a third party, or the pipeline's own
  matching. A quote beneath the vendor's own heading for a risk counts as the vendor's mapping, and
  evidence labels now carry that heading. *Why:* three of four grader disagreements on Preloop came
  from this one ambiguity.
- **Marks must match.** Graders must now agree on marks as well as outcome and polarity before a row
  publishes, because marks are shown to readers.

**Removed**

- **Blind human review on every row**, the anchoring measurement and the reviewer self-report field.
  *Why:* no person reviews most rows; the two graders are kept blind to each other instead.

### v0.2 — 2026-11-26

Version 0.1 asked one question and answered three: who wrote the sentence, how directly the
capability was described, and whether anyone was still checking. It then treated the answer as
support for the claim. Version 0.2 asks only what the evidence shows about one registered
mechanism per risk. Nothing was graded under v0.1, so no published grade changes.

**Changed**

- **§2 Evidence classes → evidence rungs.** Assertion, Mechanism, Third-party and Currently verified
  are replaced by Claimed, On-signal, Self-measured and Externally measured. *Why:* v0.1's classes
  ranked who looked and whether they kept looking, not what was tested. A one-off independent
  benchmark sat below an open repository that someone was still watching, although code
  availability says nothing about whether the code works.
- **Rechecked is a modifier on Externally measured, not a rung.** *Why:* as a top rung, a vendor
  rerunning its own test could rank above a fresh independent test.
- **Measured rungs require corpus, operating point, outcome and product version.** A number without
  them stays On-signal. Vendor-commissioned tests count as Self-measured. *Why:* a bare percentage
  cannot be checked or compared.
- **§3 Risk signal → signal register.** One primary signal per risk entry, cited to the entry's
  numbered OWASP guidance, closed against shared lines, with OWASP's boundary notes quoted beside
  it. The signals move to a separately versioned file, `signal-register.md`, covering all twenty
  entries. *Why:* v0.1's three example signals were uncited, and two of them (goal-state baselines,
  lineage metadata) were monitoring, which every entry already lists.
- **Second-signal proposal path.** A public issue citing the guideline; accepted proposals bump the
  register version and requeue rows. *Why:* one signal per entry is deliberately narrow and needs a
  way to admit other mechanisms that does not reopen the generic-control loophole.
- **Rungs are never counted.** No tool-level "covers N risks" figure. *Why:* a count turns Claimed
  rows into something that reads as coverage.
- **Plain-word labels for readers.** Each rung has one published label: claimed only, explained by
  vendor, tested by vendor, tested independently. *Why:* readers should not need the
  specification's terms, and no two rungs may share a label.
- **Code-confirmed modifier** for open-source tools: the mechanism was found in the cited code at a
  named release. It does not raise the rung. *Why:* it is real information, but code shows a
  mechanism exists, not that it works.
- **Measurement conditions mark a rung instead of lowering it.** A prompt-injection number from a
  fixed attack set keeps its rung and is marked *fixed attacks only* (LLM01:2026 PM11). *Why:* a
  cap would put almost every published result level with vendors who publish nothing.
- **§7 Freshness adds a 12-month re-assessment**, and an immediate one after an ownership change,
  acquisition or rename, alongside quote-level change detection. *Why:* change detection only
  catches what it watches.
- **LLM09 has two primary signals** from the first edition: tenant scoping inside the index query
  (PM1), or per-embedding provenance used to invalidate a compromised batch (PM2). *Why:* one
  signal covered access-control failure only, not poisoning.
- **ASI06 has two primary signals** from the first edition: a decision on the write or read, or
  quarantine and expiry of unverified memory (PM7, PM8).
- **Review question reworded** to "which rung does the selected evidence reach for this risk's
  registered signal?" This is review regime 2.
- **§11 → §9 Taxonomy and register versioning.** Each row carries taxonomy, register and review
  regime versions. Adds the requeue rule for register changes and the live example of the Agentic
  Top 10 citing LLM Top 10 *2025* numbers.

**Removed**

- **Certification as evidence** (v0.1 Class 4 certification path, AIUC-1 reference, allowlist).
  Certificates are now a separate attribute, *vendor's own system independently assured*, with no
  rung (§4), labelled *checked with issuer* or *vendor states*. *Why:* a certificate such as AIUC-1 assures how a vendor runs its own AI systems. It
  does not test whether the product mitigates a named risk for the buyer.
- **The open-repository path to Class 4.** *Why:* being able to read code is not evidence that it
  mitigates the risk, and an open core does not show what the hosted product does.
- **Derived confidence, calibration and thresholds** (v0.1 §4 signals S1, S2, S4; §5; §6),
  including automatic promotion and the audit floor. Every row is reviewed by a person (§5).
  *Why:* calibration needed hundreds of labels before a score meant anything, every row is reviewed
  anyway, and a score published beside a rung would read as a grade. This also removes the
  unexplained gap where S5 was missing.
- **Freshness checks on gold labels** (v0.1 §9). *Why:* gold labels existed only to fit the
  calibrator.

**Copyright**

- The copyright holder changes from Yuntona Ltd to Fabio Baumeler. The v0.1 tag still names
  Yuntona Ltd, because tagged versions never change; its rights are assigned separately.

**Kept**

- Scope boundary (§1), with a note that selecting a signal from OWASP's own guidance is in scope.
- Polarity, screenshots as discovery, queryable rungs, blind review, self-report, the
  review-quality series (v0.1's S6, no longer a confidence input), elusion testing, span-hash
  freshness, entity resolution, the asymmetric requeue rule, and rejection codes A and B.

**Corrected**

- v0.1 §3 said every one of the ten Agentic entries lists logging and monitoring. Nine do in so many
  words; ASI06 lists anomaly detection instead.
- v0.1 §3 attributed "excessive telemetry and monitoring leakage" to the LLM Top 10 2026 as its own
  weakness. The phrase is the name of DSGAI14 (OWASP GenAI Data Security), which the LLM Top 10's
  Appendix A maps to LLM02. LLM02:2026 itself names observability platforms as a disclosure
  surface in Common Example 7. v0.2 cites both precisely.

### v0.1 — 2026-09-26

First public draft, published before any results.

- §1 Scope boundary: map against the published risk description; do not extend it.
- §2 Evidence classes: a four-class ladder (Assertion, Mechanism, Third-party, Currently verified).
- §3–§12: risk signal and polarity, derived confidence, calibration, published tolerance, blind
  review, elusion testing, staleness, entity resolution, taxonomy versioning, review codes.
