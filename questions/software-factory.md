# Software Factory Questions and Answers

[Back to the README](../README.md) · [Agent Orchestration](agent-orchestration.md) · [Agents and tool use](agents.md) · [Production engineering](production-engineering.md) · [System design scenario](../system-design/README.md#6-autonomous-software-factory)

Here, a software factory means an end-to-end software development system in which fleets of autonomous AI agents handle planning, coding, testing, and monitoring, while human engineers define business intent and review results. Autonomy operates within explicit permissions and delivery policies. These questions describe illustrative architectures, not a claim that a particular product can reliably automate every development task. References support individual engineering techniques; the proposed factory combines them into a design for discussion.

## Contents

- [Intent and planning](#intent-and-planning): the factory model, acceptance criteria, and task decomposition.
- [Implementation and verification](#implementation-and-verification): execution environments, independent tests, and integration.
- [Review and release](#review-and-release): human judgment, provenance, deployment, and rollback.
- [Monitoring and improvement](#monitoring-and-improvement): production feedback, outcome metrics, and factory changes.

## Intent and planning

### Question: 1. What makes an autonomous software factory different from a coding assistant or a CI/CD pipeline?

**Topic:** End-to-end development lifecycle
**Difficulty:** Beginner

**Short answer:**
A software factory coordinates agents across the development lifecycle, turning business intent into verified changes and monitored releases. Coding assistance and CI/CD are components of that larger system.

**Explanation:**
The factory needs persistent work ownership and evidence connecting requirements to deployed behavior. Agents can investigate, propose plans, implement changes, and interpret failures; deterministic services execute builds and enforce policy. Humans remain responsible for business priorities and judging whether results satisfy intent. The architecture should also handle rejected, blocked, and partially completed requests.

**Example:**
An engineer requests invoice export. Agents identify affected services, propose a contract, implement it, assemble test evidence, and monitor the reviewed release against the agreed objectives.

**Follow-up questions:**

- Which lifecycle steps would you automate first, and what evidence would justify expanding autonomy?

**References:**

- [Anthropic: Agent workflows and coding applications](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 2. How should business intent become an executable development specification?

**Topic:** Requirements and acceptance criteria
**Difficulty:** Intermediate

**Short answer:**
Turn the requested outcome into versioned user scenarios, measurable acceptance criteria, constraints, and explicit non-goals, while recording ambiguities for human resolution.

**Explanation:**
Distinguish desired business impact from software behavior and operational targets. A specification should identify users, permissions, compatibility needs, and observable failure behavior. Agents may propose missing details, but material product decisions need an accountable owner. Tests cover parts of a specification; passing them does not prove business value.

**Example:**
“Make exports reliable” becomes “authorized users can export their own invoices; failures are recoverable without duplicate jobs; 99% of eligible jobs finish within five minutes over a defined window.” The team separately measures whether support requests fall.

**Follow-up questions:**

- How would you handle a request whose success depends on user behavior rather than a deterministic test?

**References:**

- [Google SRE: Defining measurable service objectives](https://sre.google/sre-book/service-level-objectives/)

### Question: 3. How should planning agents divide a feature across a fleet?

**Topic:** Planning and dependency management
**Difficulty:** Advanced

**Short answer:**
Inspect the repository and architecture, define interfaces and bounded tasks, then schedule independent work around explicit dependencies and integration milestones.

**Explanation:**
Each task should reference the intent version, repository revision, allowed scope, expected artifact, and acceptance criteria. Assign ownership for shared contracts and migrations. Replan when discoveries change the assumptions; mark affected downstream results stale. A larger fleet helps only when useful independent work exists and integration capacity can keep up.

**Example:**
An export feature has separate API, worker, and UI tasks after its job-state contract is agreed. A retention-policy discovery changes that contract and triggers targeted revalidation of dependent work.

**Follow-up questions:**

- When is one agent completing a vertical slice preferable to separate specialist agents?

**References:**

- [Anthropic: Task decomposition and delegation lessons](https://www.anthropic.com/engineering/multi-agent-research-system)

## Implementation and verification

### Question: 4. What execution environment should a coding agent receive?

**Topic:** Sandboxes and permissions
**Difficulty:** Intermediate

**Short answer:**
Provide an isolated, disposable environment with pinned inputs, scoped credentials, bounded compute, and only the network and tools needed for the task.

**Explanation:**
Treat repository scripts, dependencies, and generated code as untrusted execution inputs. A branch or worktree separates edits but does not isolate processes, secrets, or network access. Use an appropriate container or VM boundary for the threat model, and keep production credentials out of coding environments. Trusted services should mediate privileged actions and collect artifacts before cleanup.

**Example:**
A worker can fetch approved dependencies and test against disposable data, but a command embedded in a source comment cannot grant it access to release credentials.

**Follow-up questions:**

- How would you prevent one compromised build from affecting the next task on a reused runner?

**References:**

- [GitHub: Secure use of automation and runners](https://docs.github.com/en/actions/reference/security/secure-use)

### Question: 5. How can the factory verify code when agents also generate the tests?

**Topic:** Independent verification
**Difficulty:** Advanced

**Short answer:**
Combine agent-generated tests with protected acceptance checks, existing regression coverage, and independent review tied to the approved specification.

**Explanation:**
An implementation and its tests can share the same misunderstanding. Preserve trusted checks outside the coding worker's write scope, and scrutinize deleted or weakened assertions. Use contract, integration, property, security, or performance checks according to the change. Run them against the actual candidate artifact. Coverage and model approval are supporting signals, not proof of correctness.

**Example:**
An export patch passes its new unit tests but fails a protected cross-tenant access test. The factory rejects the patch even if a reviewing agent calls it correct.

**Follow-up questions:**

- What would you do when the existing test suite is weak or flaky?

**References:**

- [SWE-bench: Executable evaluation of generated software changes](https://www.swebench.com/SWE-bench/)

### Question: 6. How should the factory integrate concurrent changes from multiple agents?

**Topic:** Integration and merge coordination
**Difficulty:** Advanced

**Short answer:**
Keep changes isolated, coordinate shared interfaces, and validate the combined candidate against the current target branch before merging.

**Explanation:**
A clean text merge does not establish behavioral compatibility. Use a merge queue or equivalent serialization point that tests the proposed integration result. If the target branch or candidate changes, invalidate affected checks and approvals according to policy. Bound conflict-repair attempts and return unresolved architectural conflicts to an owner.

**Example:**
Two individually passing patches change a job-state enum and a UI switch statement. Their combined integration test fails, so the queue blocks the release until the contract is reconciled.

**Follow-up questions:**

- How would you coordinate a feature spanning multiple repositories that cannot merge atomically?

**References:**

- [GitHub: Managing a merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue)

## Review and release

### Question: 7. Where should human engineers participate in an autonomous software factory?

**Topic:** Human intent and review
**Difficulty:** Intermediate

**Short answer:**
Engineers define outcomes and constraints, resolve material ambiguities, and review concrete results at checkpoints determined by impact and organizational policy.

**Explanation:**
Prepare a review packet containing requirement coverage, the diff, a demonstration where useful, test evidence, limitations, and rollout options. Avoid requiring engineers to approve every internal tool call. Bind any required authorization to the candidate, environment, and permitted action; changed behavior may require renewed review. Agents cannot grant themselves authority by declaring a task low risk.

**Example:**
An engineer reviews a working export flow and its access-control evidence. A later change to export visibility invalidates the relevant review before release.

**Follow-up questions:**

- How would you prevent a large agent fleet from overwhelming the human review queue?

**References:**

- [LangGraph: Persisted workflow state and human-in-the-loop support](https://docs.langchain.com/oss/python/langgraph/persistence)

### Question: 8. What provenance should connect business intent to a production release?

**Topic:** Artifact identity and audit trails
**Difficulty:** Advanced

**Short answer:**
Maintain a versioned chain from intent and task records through source commits, build inputs, test reports, approvals, and the deployed artifact digest.

**Explanation:**
Record model and tool configurations for diagnosis, but do not promise identical model outputs on replay. Protect evidence from the workers whose work it verifies. Build provenance describes artifact origin and build execution; it does not prove functional correctness. The factory's requirements and review records extend beyond build provenance and need their own integrity and access controls.

**Example:**
An incident responder starts with a container digest and finds the exact source revision, checks, reviewer decision, and business request that produced it.

**Follow-up questions:**

- How would you detect a release artifact that differs from the one that passed verification?

**References:**

- [SLSA: Build provenance](https://slsa.dev/spec/v1.2/provenance)

### Question: 9. How should agents participate in deployment and rollback?

**Topic:** Controlled release execution
**Difficulty:** Advanced

**Short answer:**
Agents can propose rollout plans and analyze results, while a trusted release service enforces permissions, artifact identity, staged exposure, and stop conditions.

**Explanation:**
Deploy a verified immutable artifact and compare canary behavior with a suitable baseline. Persist release operation IDs and reconcile ambiguous outcomes before retrying. Rollback requires compatible data and dependencies; reversing an application image does not undo a destructive migration. Use staged schema evolution, feature flags, or a tested forward-recovery plan when needed.

**Example:**
A new export worker is enabled for limited traffic. A sustained error-rate increase stops rollout and restores the previous compatible worker while preserving queued jobs.

**Follow-up questions:**

- How would you evaluate a low-traffic canary that has insufficient observations?

**References:**

- [Google SRE: Canarying releases](https://sre.google/workbook/canarying-releases/)
- [AWS Builders' Library: Idempotent operations](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

## Monitoring and improvement

### Question: 10. How should monitoring agents close the loop after deployment?

**Topic:** Production feedback and incident response
**Difficulty:** Advanced

**Short answer:**
Connect telemetry and user outcomes to release versions, detect meaningful regressions, and turn verified incidents into bounded remediation work.

**Explanation:**
Separate detection from authority to act. Preauthorized mitigation can follow a tested runbook; a novel code fix should pass the development and verification process. Deduplicate incidents, limit repair attempts, and provide an emergency stop to prevent repeated fix-and-redeploy loops. Monitoring agents should report uncertainty and preserve evidence for an accountable incident owner.

**Example:**
An agent links a rise in failed exports to a release, triggers an allowed rollback, and proposes a regression test and patch through the normal review path.

**Follow-up questions:**

- How would the factory behave if the monitoring pipeline itself became unavailable?

**References:**

- [OpenTelemetry: Correlating distributed execution with traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [Google SRE: Service objectives and indicators](https://sre.google/sre-book/service-level-objectives/)

### Question: 11. Which metrics show whether the software factory is delivering value?

**Topic:** Delivery outcomes and economics
**Difficulty:** Intermediate

**Short answer:**
Measure accepted business outcomes, delivery time, escaped defects, operational reliability, human effort, and total cost per accepted change.

**Explanation:**
Lines of code, agent activity, and PR counts can increase without improving results. Compare similar task classes and include failed attempts, review, rework, infrastructure, and model costs. Define acceptance independently of the generating agents and track results after release. Report completion and abandonment rates alongside cost so difficult tasks cannot disappear from the denominator.

**Example:**
Factory A spends 600 illustrative cost units for 30 accepted changes: 20 per change. Factory B spends 500 for 20: 25 per change. Compare review effort and escaped defects before deciding which is better.

**Follow-up questions:**

- How would you avoid attributing an improvement to agents when the task mix became easier?

**References:**

- [SWE-bench: Task-level software evaluation](https://www.swebench.com/SWE-bench/)

### Question: 12. How should the factory improve its own prompts, tools, and orchestration?

**Topic:** Factory evaluation and controlled evolution
**Difficulty:** Advanced

**Short answer:**
Version factory configurations, evaluate candidates on held-out representative tasks, and expand deployment only after quality and operational evidence support the change.

**Explanation:**
Separate changes to customer software from changes to the machinery that builds it. An agent may propose a better planner or test policy, but cannot silently weaken its own release criteria. Evaluate task outcomes, permission violations, cost, and review effort. Shadow experiments need isolated environments to avoid duplicate external effects. Preserve a compatible way to finish or migrate runs started under an older configuration.

**Example:**
A revised planner reduces completion time in offline trials but increases integration failures. The team retains the existing planner while testing a narrower change to task decomposition.

**Follow-up questions:**

- How would you evaluate a factory change that only affects rare, long-running failures?

**References:**

- [Google SRE: Controlled comparison and staged releases](https://sre.google/workbook/canarying-releases/)

Apply these ideas in the [autonomous software factory system design scenario](../system-design/README.md#6-autonomous-software-factory).
