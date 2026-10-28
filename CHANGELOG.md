# Changelog

Each entry corresponds to a git tag. Dates are the date the tag was created.

## Evidence-Graded Risk Mapping

### v0.2 — unreleased (draft)

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
- **Review question reworded** to "which rung does the selected evidence reach for this risk's
  registered signal?" This is review regime 2.
- **§11 → §9 Taxonomy and register versioning.** Each row carries taxonomy, register and review
  regime versions. Adds the requeue rule for register changes and the live example of the Agentic
  Top 10 citing LLM Top 10 *2025* numbers.

**Removed**

- **Certification as evidence** (v0.1 Class 4 certification path, AIUC-1 reference, allowlist).
  Certificates are now a separate attribute, *vendor's own system independently assured*, with no
  rung (§4). *Why:* a certificate such as AIUC-1 assures how a vendor runs its own AI systems. It
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
