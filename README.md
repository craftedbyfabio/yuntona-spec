# Yuntona specifications

Open, versioned specifications for grading the evidence behind AI security claims.

| Specification | Version | Status |
| --- | --- | --- |
| [Evidence-Graded Risk Mapping](evidence-graded-risk-mapping.md) | 0.3 | Draft |
| [Signal register](signal-register.md) | 2 | Draft |
| [Grading instructions](grader-instructions.md) | Grading regime 3 | Draft |
| [Grader test suite](grader-tests.yaml) | Suite 1 | Draft |

**Evidence-Graded Risk Mapping** names what a tool's evidence shows against a named AI security
risk. It grades claims on four rungs (Claimed, On-signal, Self-measured, Externally measured)
against one registered mechanism per risk, for the OWASP Top 10 for LLM Applications 2026 and the
OWASP Top 10 for Agentic Applications 2026. It grades claims; it does not measure protection.

The **signal register** names that mechanism for each of the twenty entries, cited to OWASP's own
numbered mitigation guidance. It is versioned separately, so adding a signal does not change the
specification.

From v0.3, grades are produced by two model graders working from the same fixed **grading
instructions**, with code deciding what publishes and what goes to a person (specification §5).
The **grader test suite** holds known-answer cases the graders must pass before a grading regime
is used. [`tools/`](tools) holds the deterministic part of the pipeline and its checks, and
[`test-results/`](test-results) records each run of the suite.

## Status

Version 0.3 is a draft. One tool has been graded in testing; no grade has been published yet.
Grading regime 3 has so far been tested with two graders from the same model family; the
specification asks for different families where available, and the test results say which were
used. Earlier versions remain available at their tags; [`CHANGELOG.md`](CHANGELOG.md) explains
what changed and why.

## Versions

- Each release is a git tag (`v0.1`, `v0.2`, `v0.3`, …). A tagged version never changes after release.
- [`CHANGELOG.md`](CHANGELOG.md) records what changed between versions and why.
- The rendered specification is published at [yuntona.ai](https://yuntona.ai). Every released
  version stays available at its own URL, so a citation to an older version keeps working.
- Work between releases happens on `main` and is not a published version until it is tagged.

## Citing

> Yuntona, *Evidence-Graded Risk Mapping*, version 0.3. https://yuntona.ai

Always cite a version. The specification changes between versions, and a citation without one
cannot be checked against the text it refers to. When citing a grade, cite the signal register
version and the grading regime too.

## Corrections and contributions

Corrections are the fastest way to improve this specification. If something is wrong, open an
issue and cite the text you are disputing. Pull requests are welcome too.

To propose a second primary signal for a risk entry, open an issue citing the numbered OWASP
guideline in that entry that it comes from (specification §3). Declined proposals keep their
reason on the issue.

By contributing, you agree that your contribution is licensed under CC BY-SA 4.0, the same
licence as the rest of the specification.

## What is and is not in this repository

This repository contains the specification text only. The graded tool-to-risk mappings produced
under it are **not** part of this repository and are **not** covered by its licence.

The OWASP LLM Top 10 and OWASP Agentic Top 10 are published by the OWASP Foundation under their
own licence. This specification refers to their entries; it does not redefine them.

## Licence

Copyright © 2026 Fabio Baumeler.

Licensed under the [Creative Commons Attribution-ShareAlike 4.0 International
licence](LICENSE) (CC BY-SA 4.0). You may share and adapt it, including commercially, provided you
give credit and release adaptations under the same licence.

Maintained by a CISSP-certified practitioner (MSc Information Security, Royal Holloway).
