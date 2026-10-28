# Yuntona specifications

Open, versioned specifications for grading the evidence behind AI security claims.

| Specification | Version | Status |
| --- | --- | --- |
| [Evidence-Graded Risk Mapping](evidence-graded-risk-mapping.md) | 0.2 | Draft |
| [Signal register](signal-register.md) | 1 | Draft |

**Evidence-Graded Risk Mapping** names what a tool's evidence shows against a named AI security
risk. It grades claims on four rungs (Claimed, On-signal, Self-measured, Externally measured)
against one registered mechanism per risk, for the OWASP Top 10 for LLM Applications 2026 and the
OWASP Top 10 for Agentic Applications 2026. It grades claims; it does not measure protection.

The **signal register** names that mechanism for each of the twenty entries, cited to OWASP's own
numbered mitigation guidance. It is versioned separately, so adding a signal does not change the
specification.

## Status

Version 0.2 is a draft, published before any results. No tool has been graded against a named
risk under it yet. Version 0.1 remains available at its tag; [`CHANGELOG.md`](CHANGELOG.md) explains
what changed and why.

## Versions

- Each release is a git tag (`v0.1`, `v0.2`, …). A tagged version never changes after release.
- [`CHANGELOG.md`](CHANGELOG.md) records what changed between versions and why.
- The rendered specification is published at [yuntona.ai](https://yuntona.ai). Every released
  version stays available at its own URL, so a citation to an older version keeps working.
- Work between releases happens on `main` and is not a published version until it is tagged.

## Citing

> Yuntona, *Evidence-Graded Risk Mapping*, version 0.2. https://yuntona.ai

Always cite a version. The specification changes between versions, and a citation without one
cannot be checked against the text it refers to. When citing a grade, cite the signal register
version too.

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

Copyright © 2026 Yuntona Ltd.

Licensed under the [Creative Commons Attribution-ShareAlike 4.0 International
licence](LICENSE) (CC BY-SA 4.0). You may share and adapt it, including commercially, provided you
give credit and release adaptations under the same licence.

Maintained by a CISSP-certified practitioner (MSc Information Security, Royal Holloway).
