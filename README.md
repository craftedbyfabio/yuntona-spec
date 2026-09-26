# Yuntona specifications

Open, versioned specifications for grading the evidence behind AI security claims.

| Specification | Version | Status |
| --- | --- | --- |
| [Evidence-Graded Risk Mapping](evidence-graded-risk-mapping.md) | 0.1 | Draft |

**Evidence-Graded Risk Mapping** maps graded evidence to the AI security risks it claims to
mitigate. It grades evidence on a four-class ladder, from bare assertion to currently verified,
and checks it against the OWASP LLM Top 10 (2026) and the OWASP Agentic (ASI) Top 10 (2026).

## Status

Version 0.1 is a draft, published before any results. No tool has been mapped against a named
risk under it yet, no gold labels exist, and no calibration has been fitted. Where the text refers
to something that does not exist yet, such as the certification allowlist, it says so.

## Versions

- Each release is a git tag (`v0.1`, `v0.2`, …). A tagged version never changes after release.
- [`CHANGELOG.md`](CHANGELOG.md) records what changed between versions and why.
- The rendered specification is published at [yuntona.ai](https://yuntona.ai). Every released
  version stays available at its own URL, so a citation to an older version keeps working.
- Work between releases happens on `main` and is not a published version until it is tagged.

## Citing

> Yuntona, *Evidence-Graded Risk Mapping*, version 0.1. https://yuntona.ai

Always cite a version. The specification changes between versions, and a citation without one
cannot be checked against the text it refers to.

## Corrections and contributions

Corrections are the fastest way to improve this specification. If something is wrong, open an
issue and cite the text you are disputing. Pull requests are welcome too.

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
