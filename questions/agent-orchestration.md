# Agent Orchestration Questions and Answers

[Back to the README](../README.md) · [Agents and tool use](agents.md) · [Software Factory](software-factory.md) · [Evaluation](evaluation.md)

These questions extend the single-agent foundations into coordinating fleets of agents. They cover how work is divided, scheduled, verified, and recovered. The architectures and examples are illustrative design proposals; cited systems demonstrate particular techniques rather than universal guarantees.

## Contents

- [Architecture and decomposition](#architecture-and-decomposition): orchestration, coordination patterns, and task graphs.
- [Scheduling and collaboration](#scheduling-and-collaboration): worker assignment, handoffs, and shared state.
- [Recovery and control](#recovery-and-control): durable execution, retries, cancellation, and budgets.
- [Verification and evaluation](#verification-and-evaluation): disagreement, traces, and measured value.

## Architecture and decomposition

### Question: 1. What does agent orchestration add beyond an individual agent's execution loop?

**Topic:** Orchestration responsibilities
**Difficulty:** Beginner

**Short answer:**
Orchestration coordinates tasks, dependencies, workers, and resources across a larger objective, while an individual agent chooses actions within its assigned task.

**Explanation:**
A planner can propose work, but trusted application logic should own scheduling, permissions, and completion records. Separate the model's proposed plan from the system's authoritative execution state. A fleet needs a shared definition of completion; collecting successful worker messages does not establish that the overall objective succeeded.

**Example:**
For a feature request, an orchestrator waits for a versioned API contract before assigning compatible backend and frontend work, then schedules integration checks.

**Follow-up questions:**

- Which orchestration decisions should use deterministic code?

**References:**

- [Anthropic: Orchestrator-worker patterns](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 2. When should you use a fixed workflow, a supervisor, or peer-to-peer coordination?

**Topic:** Coordination patterns
**Difficulty:** Intermediate

**Short answer:**
Use a fixed workflow for known dependencies, a supervisor for dynamic decomposition, and peer coordination when local decisions justify the added reconciliation complexity.

**Explanation:**
Central coordination gives a clear owner but can become a bottleneck. Peer communication allows flexible collaboration but needs explicit ownership, termination, and conflict rules. A useful hybrid lets a model suggest subtasks inside a workflow whose release and validation steps remain fixed.

**Example:**
A supervisor discovers which modules need changes, while the application always requires integration checks before presenting the result for review.

**Follow-up questions:**

- How would you detect circular delegation between peers?

**References:**

- [Anthropic: Workflow and agent architecture patterns](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 3. How should an orchestrator decompose work into tasks that can run in parallel?

**Topic:** Task graphs and dependencies
**Difficulty:** Intermediate

**Short answer:**
Define bounded deliverables, interfaces, dependencies, and acceptance criteria; parallelize tasks whose inputs and ownership are sufficiently independent.

**Explanation:**
Represent a plan as a versioned dependency graph. Each task needs an owner, input revisions, output contract, and verification step. Reject dependency cycles and revise the graph when discoveries invalidate assumptions. Tiny tasks increase coordination overhead; broad tasks create overlap and make failures difficult to isolate.

**Example:**
After agreeing on a response schema, assign implementation and client updates separately. A schema revision invalidates dependent work until compatibility is checked.

**Follow-up questions:**

- How would you identify the critical path before adding workers?

**References:**

- [Anthropic: Delegation and task boundaries in a multi-agent system](https://www.anthropic.com/engineering/multi-agent-research-system)

## Scheduling and collaboration

### Question: 4. How should a scheduler assign work across an agent fleet?

**Topic:** Admission control and scheduling
**Difficulty:** Advanced

**Short answer:**
Schedule ready tasks according to capabilities, authorization, priority, and available resources, with limits that prevent one run from exhausting the fleet.

**Explanation:**
Track model quotas, sandbox capacity, tool limits, and per-run concurrency separately. Use bounded queues, fairness across projects, and aging to avoid starving older work. Worker leases need expiry and renewal. A reassigned task must reject stale workers' results using an attempt or lease generation checked by the state store.

**Example:**
A run may occupy four coding sandboxes, while integration checks use a reserved pool so a coding surge cannot block completed changes from verification.

**Follow-up questions:**

- How do you distinguish a resource-starved task from a failed worker?

**References:**

- [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/)

### Question: 5. What should an agent handoff contain?

**Topic:** Task and result contracts
**Difficulty:** Intermediate

**Short answer:**
A handoff should include the objective, input versions, constraints, expected output, evidence, and unresolved issues in a structured record.

**Explanation:**
Pass durable artifact references rather than relying on an expanding conversation transcript. Record task and attempt IDs so late or duplicate responses can be recognized. Distinguish facts, assumptions, and proposed next steps. A receiving worker should validate that the artifact exists and matches the expected revision before using it.

**Example:**
A coding agent returns a commit identifier, test report references, and a known limitation. The next stage retrieves those artifacts rather than interpreting “all done” as a sufficient result.

**Follow-up questions:**

- What happens when the referenced artifact has expired or changed?

**References:**

- [Anthropic: Agent communication and artifact handling](https://www.anthropic.com/engineering/multi-agent-research-system)

### Question: 6. How should agents share state without overwriting one another's work?

**Topic:** State ownership and concurrency
**Difficulty:** Advanced

**Short answer:**
Give each task an isolated workspace, publish immutable outputs, and use explicit version checks when updating shared records or integrating changes.

**Explanation:**
A shared chat history is not a transaction mechanism. An illustrative design stores accepted task results with compare-and-set updates and records conflicting proposals separately. For code, separate branches or worktrees reduce filesystem collisions, but they do not resolve semantic conflicts. Git worktrees also share repository metadata and are not a security boundary.

**Example:**
Two workers change different callers of a common API in separate workspaces. Integration checks expose incompatible assumptions even though the patches merge cleanly.

**Follow-up questions:**

- Which shared state needs strong consistency, and which can be eventually consistent?

**References:**

- [Git: Worktree behavior and shared repository state](https://git-scm.com/docs/git-worktree)

## Recovery and control

### Question: 7. How can an orchestration run survive process crashes or long pauses?

**Topic:** Durable execution
**Difficulty:** Advanced

**Short answer:**
Persist the plan, task states, accepted outputs, and pending operations so the system can resume and reconcile incomplete work.

**Explanation:**
Checkpoint at meaningful boundaries and retain the configuration needed to interpret state. Resumption may replay part of a task, so separate repeatable computations from external effects. Revalidate permissions, deadlines, and input revisions after a pause. If a required artifact is missing, explicitly recompute or block its dependents instead of pretending the step is complete.

**Example:**
After a scheduler restart, completed build artifacts remain accepted, an expired coding lease is reassigned, and a pending deployment is reconciled with the deployment service.

**Follow-up questions:**

- How would you migrate persisted runs when the workflow definition changes?

**References:**

- [LangGraph: Persistence and checkpoints](https://docs.langchain.com/oss/python/langgraph/persistence)

### Question: 8. How should retries and cancellation work across delegated tasks?

**Topic:** Failure and side-effect semantics
**Difficulty:** Advanced

**Short answer:**
Bound retries at the run level, deduplicate repeated operations, propagate cancellation, and reconcile effects that may already have happened.

**Explanation:**
Assign a stable operation ID before a state-changing request. A lost acknowledgment leaves the outcome unknown; retry only under a suitable idempotency contract or after checking status. Cancellation prevents new authorized work but does not undo a completed external action. Record compensation or manual intervention as separate outcomes.

**Example:**
A cancelled parent stops scheduling children, revokes tool access where possible, rejects late results, and checks whether an already-requested release was deployed.

**Follow-up questions:**

- How would you prevent retries in the supervisor, worker, and SDK from multiplying?

**References:**

- [AWS Builders' Library: Idempotent APIs and ambiguous outcomes](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

### Question: 9. How do you keep delegation and repair loops within a budget?

**Topic:** Resource limits and stopping conditions
**Difficulty:** Intermediate

**Short answer:**
Enforce shared limits on spending, elapsed time, active workers, delegation depth, and repair attempts, then stop or escalate when progress stalls.

**Explanation:**
Reserve resources before dispatch so concurrent workers cannot each spend the same remaining budget. Include failed attempts and evaluation in accounting. Reconcile reservations when usage becomes known. Progress should mean new evidence or verified outputs, not additional messages. Budget exhaustion produces an incomplete outcome with preserved artifacts.

**Example:**
A run reserves part of its budget for final integration checks and stops generating new candidate patches when the remaining allowance cannot cover verification.

**Follow-up questions:**

- What should happen if billing information arrives after a worker finishes?

**References:**

- [Google SRE: Limiting admitted work and overload propagation](https://sre.google/sre-book/handling-overload/)

## Verification and evaluation

### Question: 10. How should an orchestrator resolve conflicting agent outputs?

**Topic:** Evidence and disagreement
**Difficulty:** Intermediate

**Short answer:**
Compare outputs against explicit requirements and executable evidence; seek more evidence or human judgment when the disagreement cannot be resolved mechanically.

**Explanation:**
Majority agreement is weak evidence when agents share models, context, or faulty assumptions. Preserve competing artifacts and reasons for rejection. A verifier can identify problems without having authority to redefine acceptance criteria. Useful escalation explains the decision, evidence, and unresolved tradeoff.

**Example:**
Two agents propose different timeout behavior. Contract tests settle protocol compliance, while a product owner decides the acceptable user experience under slow responses.

**Follow-up questions:**

- How would you reduce correlated errors between generation and review?

**References:**

- [Anthropic: Evaluator-optimizer workflows](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 11. What observability is needed for a fleet of agents?

**Topic:** Distributed tracing and auditability
**Difficulty:** Intermediate

**Short answer:**
Correlate the overall run with tasks, attempts, model calls, tools, artifacts, and external operations so failures can be traced across delegation boundaries.

**Explanation:**
Record queue time, execution time, retries, resource use, accepted outputs, and terminal reasons. Use parent-child relationships or trace links for asynchronous work. Keep permissions and retention controls on sensitive trace content. Operational events and artifact evidence are sufficient for audit; private model reasoning is not required.

**Example:**
A delayed feature is traced to repeated integration failures after a contract revision, rather than misclassified as slow model inference.

**Follow-up questions:**

- Which metrics would reveal a supervisor bottleneck or excessive task fragmentation?

**References:**

- [OpenTelemetry: Traces, spans, and links](https://opentelemetry.io/docs/concepts/signals/traces/)

### Question: 12. How do you determine whether multiple agents improve the system?

**Topic:** Fleet evaluation
**Difficulty:** Advanced

**Short answer:**
Compare the fleet with a simpler baseline on matched tasks using verified outcomes, latency, cost, and human effort under comparable resource limits.

**Explanation:**
Use held-out tasks and repeat variable runs. Inspect failures by task complexity, dependency structure, and shared-state contention. Measure the cost of coordination and verification, including unsuccessful attempts. More parallel work may shorten independent tasks while leaving the critical path unchanged. An improvement on one workload does not establish general superiority.

**Example:**
Compare a single coding agent with a planner and three workers on the same repository snapshots, scoring accepted changes and reviewer minutes as well as test results.

**Follow-up questions:**

- How would you separate the benefit of more compute from the benefit of orchestration?

**References:**

- [SWE-bench: Reproducible software-task evaluation](https://www.swebench.com/SWE-bench/)

Continue with [Software Factory](software-factory.md) and the [autonomous software factory design scenario](../system-design/README.md#6-autonomous-software-factory).
