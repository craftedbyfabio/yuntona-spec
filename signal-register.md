---
title: Signal register
register-version: "1 (draft)"
applies-to: Evidence-Graded Risk Mapping v0.2
licence: CC-BY-SA-4.0
taxonomies:
  - "OWASP Top 10 for Agentic Applications 2026 (Version 2026, December 2025)"
  - "OWASP Top 10 for LLM Applications 2026 (Version 2026, v1.0)"
---

# Signal register

This register names, for each risk entry, the one observable mechanism that evidence must describe before a mapping can reach **On-signal** under §2 of the specification. It is versioned separately from the specification: adding or changing a signal bumps the register version, not the specification version, and every mapping row carries both (§9).

> [!IMPORTANT]
> **Draft, first edition.** ASI06 was worked through in detail before this edition was written. The other nineteen entries are a first cut and need review before the register is tagged.

## How to read an entry

- **Citations.** `ASI06:2026 PM2` means Prevention and Mitigation Guideline 2 of ASI06 in the OWASP Top 10 for Agentic Applications 2026. `LLM03:2026 PM7` means Prevention and Mitigation Strategy 7 of LLM03 in the OWASP Top 10 for LLM Applications 2026. LLM02:2026 numbers its strategies by tier, so `LLM02:2026 PM T1.3` is Tier 1, item 3. `CE` means a numbered Common Example.
- **Primary signal.** The mechanism a quoted span must describe to reach On-signal. Each one is a *decision*: something that blocks, rejects, excludes, pauses or gates, not something that only records or alerts.
- **Does not clear.** Mechanisms that are in OWASP's guidance for this entry but do not reach On-signal on their own. They are not wrong controls; they are shared, generic, or detection-only.
- **Boundary.** Where OWASP draws the edge between this entry and its neighbours, in OWASP's terms. A mapping on the wrong side of a boundary is re-proposed against the right entry (§10), not rejected.
- **Considered, not chosen.** Other mechanisms that were candidates, and why they lost. Any of them can be proposed as a second primary signal under §3.
- **Measurement condition.** Where OWASP's own text sets a condition on what counts as a measurement, it binds rungs 3 and 4 for that entry.
- **Polarity.** Where a category of evidence is an exposure for this entry, not a mitigation.

## Shared lines

These appear across many entries, phrased generically. A quoted span that states only a shared line does not reach On-signal for any entry. Where an entry's primary signal names a *specific form* of a shared line (sandboxed execution of agent-generated code for ASI05, enforced spending caps for LLM06, signed and authenticated messages for ASI07), the quote must describe that specific form.

| Code | Shared line | Where it appears (examples) |
| --- | --- | --- |
| SL-LOG | Logging, monitoring, audit trails, alerting | ASI01:2026 PM7, ASI02:2026 PM8, ASI08:2026 PM10, ASI09:2026 PM2, ASI10:2026 PM1, LLM03:2026 PM8, LLM10:2026 PM7 |
| SL-PRIV | Least privilege and access control, in general | ASI01:2026 PM2, ASI06:2026 PM1, LLM05:2026 PM7, LLM07:2026 PM7 |
| SL-HITL | Human approval for high-impact actions | ASI01:2026 PM2, ASI02:2026 PM2, ASI03:2026 PM4, ASI05:2026 PM6, ASI09:2026 PM1, LLM01:2026 PM7, LLM03:2026 PM6 |
| SL-ISO | Sandboxing, isolation, segmentation, in general | ASI02:2026 PM3, ASI08:2026 PM2, ASI10:2026 PM2, LLM05:2026 PM4, LLM06:2026 PM4, LLM07:2026 PM7 |
| SL-ENC | Encryption in transit and at rest | ASI06:2026 PM1, LLM02:2026 PM T1.7, LLM09:2026 PM5 |
| SL-ZT | "Zero trust" as a design statement | ASI04:2026 PM9, ASI08:2026 PM1, LLM10:2026 PM1 |
| SL-RT | Red teaming and adversarial testing, in general | ASI01:2026 PM8, ASI06:2026 PM7, LLM05:2026 PM10, LLM07:2026 PM10 |
| SL-RATE | Rate limiting, in general | ASI08:2026 PM6, LLM03:2026 PM9, LLM07:2026 PM7 |

LLM03:2026 says this outright for two of them: monitoring and rate limiting "will not prevent Excessive Agency but can limit the level of damage caused."

A red-teaming product is not a mitigation for any entry. Its output can be the *measurement* behind rung 3 or 4 for another product.

---

## OWASP Top 10 for Agentic Applications 2026

### ASI01:2026 Agent Goal Hijack

- **Primary signal.** Run-time validation of the agent's intended action against the declared goal, which pauses or blocks execution on an unexpected goal shift. This includes binding the declared goal and constraints to each execution cycle.
- **Cites.** ASI01:2026 PM4, PM5.
- **Does not clear.** Goal-state baselines and alerting without a pause or block (PM7, SL-LOG). Least privilege and human approval (PM2, SL-PRIV, SL-HITL). Locked system prompts (PM3) are configuration the deployer does, not a mechanism a product supplies.
- **Boundary.** ASI01 is direct alteration of the agent's goals, instructions or decision pathways, "regardless of whether the manipulation occurs interactively or through pre-positioned inputs such as documents." Persistent corruption of stored context or memory is ASI06. Misalignment without active attacker control is ASI10.
- **Considered, not chosen.** Prompt-carrier detection on connected data sources (PM6). It is the LLM01:2026 input-boundary control; a product that does only this reaches On-signal under LLM01:2026 and stays Claimed here unless its decision is tied to the active goal. *Judgement call; review.*
- **Changed from v0.1.** v0.1 named "goal-state and tool-use-pattern baselines" (PM7). That is monitoring; under v0.2 it clears only if the deviation pauses or blocks, which is PM4.

### ASI02:2026 Tool Misuse and Exploitation

- **Primary signal.** A pre-execution policy enforcement point that treats the planner's output as untrusted and validates each tool call's intent and arguments against policy before it runs.
- **Cites.** ASI02:2026 PM4.
- **Does not clear.** Tool-invocation logs and anomaly monitoring (PM8, SL-LOG). Least-privilege tool profiles that are not enforced per call (PM1). Sandboxes and egress allowlists in general (PM3, SL-ISO). Action-level human confirmation (PM2, SL-HITL).
- **Boundary.** ASI02 is a legitimate tool applied unsafely within the agent's authorised privileges. Privilege escalation or credential inheritance is ASI03; arbitrary or injected code execution is ASI05; a tool that is malicious at source is ASI04.
- **Considered, not chosen.** Semantic and identity validation of tool names and versions, failing closed on ambiguity (PM7). Narrower; a candidate second primary.
- **Overlap.** The same mechanism is LLM03:2026 PM7 (complete mediation). One product can reach On-signal under both; each mapping is graded on its own.

### ASI03:2026 Identity and Privilege Abuse

- **Primary signal.** Credentials issued per agent and per task, short-lived and narrowly scoped, and rejected when used outside the subject, purpose or intent they were bound to.
- **Cites.** ASI03:2026 PM1, PM5, PM7.
- **Does not clear.** Detection of delegated or transitive permissions without enforcement (PM8, PM9). Human approval for privileged actions (PM4, SL-HITL). Identity and SSO for human users in general.
- **Boundary.** "Unintended or unsafe use of already granted privilege" is ASI02.
- **Considered, not chosen.** Per-action re-authorisation through a central policy engine (PM3). Close to ASI02's signal; kept apart so the two entries stay distinguishable.

### ASI04:2026 Agentic Supply Chain Vulnerabilities

- **Primary signal.** A gate that verifies provenance (signature, attestation or pinned content hash) of a third-party agent component (tool, MCP server, prompt template, agent card, plug-in) before it is installed or activated, and rejects what fails.
- **Cites.** ASI04:2026 PM2, PM7.
- **Does not clear.** An inventory, SBOM or AIBOM without a gate (PM1). Runtime monitoring (PM6, SL-LOG). Zero-trust design statements (PM9, SL-ZT).
- **Boundary.** Manipulation of an otherwise legitimate tool's interface at runtime is ASI02 (ASI02:2026, Example Attack Scenario 1). The non-agentic model, dataset and artefact supply chain is LLM04:2026.
- **Considered, not chosen.** An emergency kill switch that revokes a compromised component everywhere (PM8). Response, not prevention; a candidate second primary.

### ASI05:2026 Unexpected Code Execution (RCE)

- **Primary signal.** Agent-generated or agent-invoked code runs only inside an isolated execution environment with restricted network and filesystem access, behind a validation gate that separates generation from execution.
- **Cites.** ASI05:2026 PM4, PM5.
- **Does not clear.** Sandboxing claims that do not say agent-generated code runs inside them (SL-ISO). Logging and auditing of runs (PM7, SL-LOG). Human approval for elevated runs (PM6, SL-HITL).
- **Boundary.** Unsafe use of a tool short of code execution is ASI02. Hostile code that runs during package install or import is ASI05 (ASI05:2026 CE6), even though the package arrived through the supply chain.
- **Considered, not chosen.** Banning `eval` and taint-tracking generated code (PM3). Narrower; a candidate second primary.

### ASI06:2026 Memory & Context Poisoning

- **Primary signal.** A decision on the memory write or on the later read: content is scanned before it is committed to memory, or provenance attached to each entry lets a poisoned or low-trust entry be excluded at retrieval.
- **Cites.** ASI06:2026 PM2 ("Scan all new memory writes and model outputs... before commit"), PM5 (source attribution), PM9 (weight retrieval by trust and tenancy).
- **Does not clear.** Encryption and least-privilege access (PM1, SL-ENC, SL-PRIV). Generic logs. A classifier on the current turn's prompt: that is one-time input, which ASI06 excludes. Detection of "suspicious updates or frequencies" (the second half of PM5) without the ability to exclude the entry.
- **Boundary.** ASI06 context "excludes one-time input prompts covered under LLM01:2025 Prompt Injection" (unchanged as LLM01:2026). ASI06 is "persistent corruption of agent memory and retrievable context that propagates across sessions." Direct goal manipulation is ASI01; degradation after poisoning spreads is ASI08. **Worked example:** a chat turn that is later summarised into memory is ASI06, because the harm is the later read. OWASP names this case as ASI06:2026 CE3 ("context-window manipulation").
- **Proposed second primary (pending, §3).** Quarantine, expiry or decay of unverified memory, so an entry that has not been verified stops being served. Cites ASI06:2026 PM7 (trust scores, "decaying or expiring unverified memory," "rollback/quarantine") and PM8 ("Expire unverified memory"). This is the worked example of the proposal path: accepting it bumps the register version and requeues ASI06 rows at Claimed.
- **Considered, not chosen.** Memory segmentation per session and domain (PM3). It stops cross-tenant bleed (ASI06:2026 Example Attack Scenario 5) but is SL-ISO in general form.
- **Changed from v0.1.** v0.1 named "source attribution and write-frequency anomalies." Attribution stays, but only where it can exclude an entry at retrieval; frequency anomaly detection alone no longer clears.

### ASI07:2026 Insecure Inter-Agent Communication

- **Primary signal.** Each inter-agent message is authenticated to an agent identity and integrity-checked (signed, payload and context hashed), and replays are rejected.
- **Cites.** ASI07:2026 PM1 (mutual authentication with per-agent credentials), PM2, PM3.
- **Does not clear.** Transport encryption alone, such as generic TLS without per-agent identity (SL-ENC). Monitoring routing flows (PM7, SL-LOG).
- **Boundary.** Credential and permission misuse is ASI03; stored knowledge corruption is ASI06. ASI07 is "compromising real-time messages between agents."
- **Considered, not chosen.** Protocol pinning and downgrade rejection (PM6); attested registries and signed agent cards (PM8). Candidates for a second primary.

### ASI08:2026 Cascading Failures

- **Primary signal.** Blast-radius guardrails between agents or between planner and executor (quotas, progress caps, circuit breakers) that throttle or pause propagation when a fault fans out.
- **Cites.** ASI08:2026 PM7, PM6.
- **Does not clear.** Lineage metadata and tamper-evident logs (PM10, SL-LOG). Drift detection without a pause (PM8). Zero-trust design (PM1, SL-ZT). Isolation in general (PM2, SL-ISO).
- **Boundary.** OWASP: "Use the initial defect under ASI04, ASI06, or ASI07 when it represents a direct compromise... and apply ASI08 only when that defect spreads across agents, sessions, or workflows, causing measurable fan-out."
- **Considered, not chosen.** Digital-twin replay that gates policy expansion (PM9). Pre-deployment testing rather than a runtime decision.
- **Changed from v0.1.** v0.1 named "blast-radius fan-out and lineage metadata." Lineage is logging; fan-out counts only where something pauses it.

### ASI09:2026 Human-Agent Trust Exploitation

- **Primary signal.** Preview is separated from effect, so state-changing calls are blocked while a human reviews; or actions that lack trusted provenance are blocked before they reach the human for approval.
- **Cites.** ASI09:2026 PM7, PM6.
- **Does not clear.** Confirmation prompts as such (PM1, SL-HITL): the approval step is what this entry's attacker exploits. Immutable logs (PM2, SL-LOG). UI cues and training (PM8).
- **Boundary.** "This entry is about human misperception or over-reliance whereas ASI10 is agent intent deviation."
- **Considered, not chosen.** Plan-divergence detection against approved workflows (PM9). Detection, not a decision, unless it blocks.

### ASI10:2026 Rogue Agents

- **Primary signal.** A signed behavioural manifest declaring an agent's expected capabilities, tools and goals, validated before each action, with deviation triggering containment (kill switch, credential revocation, quarantine).
- **Cites.** ASI10:2026 PM5, PM4.
- **Does not clear.** Immutable, signed audit logs (PM1, SL-LOG). Watchdog detection that does not trigger containment (PM3). Trust zones and sandboxes in general (PM2, SL-ISO).
- **Boundary.** The initial intrusion (LLM01, ASI01, ASI04) is mapped there. ASI10 is "the loss of behavioral integrity and governance once the drift begins."

---

## OWASP Top 10 for LLM Applications 2026

### LLM01:2026 Prompt Injection

- **Primary signal.** A decision on untrusted input at the boundary before it reaches the model: classified and blocked at every modality, stripped of smuggling characters, or carried in a structurally separate, provenance-labelled channel.
- **Cites.** LLM01:2026 PM3, PM5, PM6.
- **Measurement condition.** LLM01:2026 PM11: "Test against adaptive attackers who have read the deployed defense, and reject static-only attack-success claims." A measurement from a static attack set only does not reach rung 3 or 4 for this entry; the row stays On-signal and is marked *static-only*.
- **Does not clear.** Role constraints in the system prompt, which OWASP calls "a partial control only" (PM1). Output schema validation (PM2), which is LLM10:2026 territory. Human confirmation (PM7, SL-HITL).
- **Read with this.** OWASP states that "no reliable prevention mechanism exists today" and that the input-side controls "are expected to degrade against adaptive attackers." The controls it calls load-bearing, least privilege and capability budgeting (PM4, PM8), belong to LLM03:2026. An On-signal LLM01 row is a narrower claim than it looks.
- **Boundary.** Memory writes are covered here as PM9 but owned by ASI06:2026 once the model is an actor with memory (the LLM list's own boundary note: "the moment that model becomes an actor... the risk moves to the OWASP Agentic Top 10"). Output sanitisation is LLM10:2026; consequences of output reaching privileged actions are LLM03:2026.

### LLM02:2026 Sensitive Information Disclosure

- **Primary signal.** A decision that stops sensitive data crossing a disclosure channel: chunk-level authorisation enforced inside the retrieval query, or classifier-based detection and redaction applied to outputs, tool-call arguments and reasoning traces.
- **Cites.** LLM02:2026 PM T1.3, PM T1.5, PM T2.4.
- **Does not clear.** Regex-only pattern matching (PM T1.5 says "classifiers, not regex alone"). Encryption (PM T1.7, SL-ENC). Policy text promising no training or retention, as opposed to technical enforcement (PM T1.7).
- **Polarity.** Logging full prompts, completions, retrieved chunks and traces to observability platforms is an **exposure** for this entry. LLM02:2026 CE7 names Langfuse, LangSmith and Datadog LLM Observability as logging these by default; PM T1.7 and T2.4 say to scrub before ingestion and never log raw traces to unrestricted observability. Evidence of comprehensive prompt logging is recorded with negative polarity here.
- **Boundary.** Agentic cross-session disclosure is "owned by ASI." Hidden system context is LLM08:2026, but regulated data inside it is LLM02.

### LLM03:2026 Excessive Agency

- **Primary signal.** Complete mediation: authorisation enforced in logic, by an independent pre-execution policy decision point between the tool and the downstream system, not by the model.
- **Cites.** LLM03:2026 PM7.
- **Does not clear.** Monitoring (PM8) and rate limiting (PM9): OWASP says these "will not prevent Excessive Agency." Input or output sanitisation: "not a root control for Excessive Agency" (LLM03:2026 description). Human approval (PM6, SL-HITL).
- **Overlap.** Same mechanism as ASI02:2026 PM4.
- **Considered, not chosen.** Minimising tools, functionality and permissions (PM1–PM4). These are deployment choices, not a product mechanism.

### LLM04:2026 Supply Chain

- **Primary signal.** Verification of a model, adapter or dataset artefact's integrity and origin (signature, hash, transparency log) before use, combined with a policy-based release gate.
- **Cites.** LLM04:2026 PM5. OWASP's own caveat: "Signing proves integrity and origin, not safety."
- **Does not clear.** Supplier vetting and terms review (PM1). Generic vulnerability management (PM2). An inventory, SBOM or AIBOM without a gate (PM4).
- **Boundary.** MCP servers and tool registries are ASI04:2026. Poisoned content inside a genuine artefact is LLM05:2026.

### LLM05:2026 Data and Model Poisoning

- **Primary signal.** A gate that validates data or model artefacts before they are trained on, embedded or deployed (content validation, signing, hash verification, static analysis of inference artefacts) and blocks what fails.
- **Cites.** LLM05:2026 PM2, PM12.
- **Does not clear.** Drift and anomaly monitoring after the fact (PM5, SL-LOG). Data version control alone (PM8). Least privilege (PM7, SL-PRIV). Isolation (PM4, SL-ISO).
- **Boundary.** "Prompt instructions delivered through retrieved content at inference time are covered by LLM01:2026... and attacks that exploit embedding geometry by LLM09:2026." Persistent agent memory is ASI06:2026.
- **Considered, not chosen.** Trigger-probing for backdoors after every alignment cycle (PM10). A test, so it is measurement evidence rather than a mechanism; a scanner that runs it as a deployment gate falls under PM12.

### LLM06:2026 Unbounded Consumption

- **Primary signal.** Enforced ceilings that halt inference or agent execution when exceeded: hard spending caps, and step, recursion, time and cost limits per agent run.
- **Cites.** LLM06:2026 PM2 ("enforcement mechanisms that halt inference when exceeded, rather than alerting thresholds"), PM9.
- **Does not clear.** Request-rate limiting alone: "Traditional request-rate limiting alone is no longer sufficient" (LLM06:2026 description). Cost dashboards and alerts. Resource monitoring (PM3, PM8) without a halt.

### LLM07:2026 Misinformation

- **Primary signal.** A claim-check-act gate: generation is separated from execution, and claims are verified for groundedness and consistency before an action or decision depends on them.
- **Cites.** LLM07:2026 PM2, PM4 ("Use Verification Signals (Not Just Confidence)").
- **Does not clear.** The model's own confidence score (PM4 says "not just confidence"). Logging claims and outcomes (PM8, SL-LOG). Blast-radius limits in general (PM7).
- **Boundary.** Where the root cause is prompt injection, poisoning or supply chain, "those risks should be referenced separately." Execution of unsafe generated code is LLM10:2026; hallucinated package names are LLM04:2026.

### LLM08:2026 Hidden Context Exposure

- **Primary signal.** A check that finds credentials, secrets or security-critical configuration placed in system prompts or other hidden context, and blocks it before deployment or at runtime.
- **Cites.** LLM08:2026 PM1.
- **Does not clear.** Output filters that try to stop the system prompt being extracted. LLM08:2026 tells practitioners to "design under the assumption that hidden context is discoverable," so preventing extraction is not the mitigation OWASP names. Such evidence is Claimed at most.
- **Boundary.** Leakage of regulated user or training data is LLM02:2026. Agentic amplifications (persistent memory, inter-agent channels) belong to the Agentic list. Generic application-security leaks are out of scope.
- **Considered, not chosen.** Enforcing authorisation and behaviour outside the model (PM2, PM3). That is the architecture OWASP wants, but it is the deployer's design, and the product mechanism for it is already LLM03:2026's signal.

### LLM09:2026 Vector and Embedding Weaknesses

- **Primary signal.** Tenant and permission scoping enforced inside the index query, server-side and at chunk level, not as a post-retrieval filter.
- **Cites.** LLM09:2026 PM1.
- **Does not clear.** Encryption of embeddings at rest (PM5, SL-ENC). Retrieval logs (PM6, SL-LOG).
- **Boundary.** "Indirect prompt injection through retrieved content is covered in LLM01:2026... training-time poisoning of the embedding model in LLM05:2026... and agent-memory attacks that do not rely on embedding geometry in ASI06:2026."
- **Considered, not chosen.** Provenance per embedding so compromised batches can be invalidated (PM2), and anomaly detection at ingest and retrieval (PM4). This entry covers four failure modes ("poisoning makes the system wrong, inversion makes it leak, jamming makes it silent, and access-control failure makes it indiscriminate"); one primary signal covers only the last. PM2 is the strongest candidate for a second primary. *This is where the one-signal rule is weakest; review.*

### LLM10:2026 Improper Output Handling

- **Primary signal.** Model output is encoded, sanitised or stripped for its specific sink (HTML, SQL, shell, terminal, renderer) before the downstream component consumes it, including blocking auto-fetch of external resources in renderers.
- **Cites.** LLM10:2026 PM4, PM8, PM9.
- **Does not clear.** Logging and monitoring of outputs (PM7, SL-LOG). "Treat the model as any other user" as a statement (PM1, SL-ZT).
- **Boundary.** Incorrect or misleading output is LLM07:2026; input validation is LLM01:2026.
- **Considered, not chosen.** Parameterised queries (PM5) and content security policies (PM6). Standard application-security controls that are specific to one sink each.

---

## Sources

- OWASP GenAI Security Project, *OWASP Top 10 for Agentic Applications 2026*, Version 2026, December 2025. CC BY-SA 4.0.
- OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*, Version 2026 (v1.0 PDF). CC BY-SA 4.0.

Quoted passages are reproduced from those documents under CC BY-SA 4.0, with attribution as above. This register refers to their entries; it does not redefine them.
