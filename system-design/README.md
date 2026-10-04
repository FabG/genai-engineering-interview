# System Design Scenarios

[Back to the main README](../README.md) · [Hands-on Python exercises](../hands-on/README.md)

Use these six scenarios for a 45–60 minute interview or a self-guided design session. All workloads, budgets, and targets below are hypothetical interview constraints, not product guarantees. Clarify requirements, estimate capacity, sketch the data flow, and discuss failures before selecting specific products.

Reference designs are expandable so candidates can attempt each problem first. They illustrate defensible approaches rather than a single correct architecture. Interviewers should assess assumptions, tradeoffs, and verification, and adjust depth to the role.

## Scenarios

1. [Permission-aware knowledge assistant](#1-permission-aware-knowledge-assistant)
2. [Support agent with controlled actions](#2-support-agent-with-controlled-actions)
3. [Document extraction and review pipeline](#3-document-extraction-and-review-pipeline)
4. [Multi-tenant inference gateway](#4-multi-tenant-inference-gateway)
5. [Evaluation and release platform](#5-evaluation-and-release-platform)
6. [Autonomous software factory](#6-autonomous-software-factory)

## Interview structure

| Stage | Suggested time | Expected discussion |
| --- | --- | --- |
| Requirements | 5–10 minutes | Users, authorization, correctness, exclusions, and success criteria |
| Capacity and data | 5–10 minutes | Peak demand, storage, token volume, freshness, and retention |
| Architecture | 15–20 minutes | Components, state, interfaces, and a complete request flow |
| Failures and tradeoffs | 10–15 minutes | Recovery, scaling, security boundaries, cost, and alternatives |
| Evaluation | 5 minutes | Evidence that the proposed system meets its requirements |

For each scenario, produce a component diagram, a data model or API sketch, one capacity estimate with units, and a rollout and failure-recovery plan. Strong answers connect choices to the stated workload and acknowledge what still needs measurement.

## 1. Permission-aware knowledge assistant

**Difficulty:** Intermediate to Advanced

**Prompt:** Design an internal assistant that answers employee questions using company documents and provides citations.

**Starting constraints:**

- 10,000 employees, 200,000 source documents, and an assumed average of 10 chunks per document.
- Peak demand of 20 questions per second; target p95 time to first answer token below 3 seconds.
- Searchable updates within 15 minutes. Revoked access must be enforced at request time even if indexing is delayed.
- Documents have group-based permissions, multiple versions, and occasional conflicting policies.

**Clarify first:** What counts as an authoritative source? Can the system answer partially? Which requests require current policy dates? Does the latency target include identity lookup and retrieval?

**Design tasks:** Describe ingestion and deletion handling, permission enforcement, retrieval and reranking, context assembly, citation checking, and abstention. Explain how you would investigate a correct document that produces an incorrect answer.

<details>
<summary>Reference design and interviewer notes</summary>

Use two paths: ingestion produces versioned chunks with source identifiers and access metadata; online requests authenticate the user, retrieve eligible evidence, and generate a supported answer. Apply current authorization before restricted content reaches generation; stale indexed permissions alone cannot satisfy immediate revocation. Keep document-to-chunk mappings for updates and deletions.

```mermaid
flowchart LR
    Sources[Versioned documents] --> Ingest[Parse and chunk]
    Ingest --> Index[Lexical and vector indexes]
    User[Employee request] --> Auth[Authenticate and resolve permissions]
    Auth --> Retrieve[Retrieve authorized evidence]
    Index --> Retrieve
    Retrieve --> Rank[Rerank and select context]
    Rank --> Generate[Generate answer with source IDs]
    Generate --> Check[Check citations and missing evidence]
    Check --> Answer[Answer or abstention]
```

An illustrative vector-storage lower bound is `200,000 × 10 × 768 × 4 = 6.144 GB` for 768-dimensional float32 vectors in decimal units. Text, index structures, replicas, and metadata add overhead. Estimate query-side token load separately; measure whether retrieval, reranking, and prefill can meet the latency budget.

Compare lexical, dense, and hybrid retrieval on labeled questions. Track evidence recall, answer correctness, citation support, access-control failures, and freshness. A vector similarity threshold alone is not a reliable answerability test. Scope caches to identity and permission state, and invalidate them when relevant data or permissions change.

**Strong signals:** Separates retrieval errors from generation errors, preserves version provenance, and addresses permission revocation and cache isolation explicitly.

**Failure injection:** A deleted document remains in the index; an access grant is revoked during a conversation; two sources disagree.

**Follow-up:** How would the design change for scanned PDFs or a tenfold increase in document count?

</details>

**Related study:** [RAG](../questions/rag.md), [production engineering](../questions/production-engineering.md). [Microsoft's security-filter pattern](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search) illustrates query-time filtering; the immediate-revocation requirement here is an additional design constraint.

## 2. Support agent with controlled actions

**Difficulty:** Advanced

**Prompt:** Design a customer-support agent that retrieves order information, proposes resolutions, and can create replacement requests after the required approval.

**Starting constraints:**

- 50,000 conversations per day, averaging 6 model decisions per conversation, with a peak 8 times the daily average decision rate.
- Order lookups are read-only. Replacement creation changes external state and requires approval of the specific order and replacement details.
- The order service occasionally times out after accepting a write. Sessions must survive worker restarts.
- A task may run for at most 2 minutes before returning a verified result, escalation, or an explicit pending status.

**Clarify first:** Who can approve a replacement? Which policy checks are deterministic? What is the authoritative completion record? How should cancellation affect a pending action?

**Design tasks:** Specify tools, task state, approval records, retry semantics, stopping conditions, and an audit trail. Walk through a crash between an external write and a local checkpoint.

<details>
<summary>Reference design and interviewer notes</summary>

Use a model for interpretation and action selection within an application-controlled state machine. Enforce user authorization and replacement policy outside the model. Read tools return typed outcomes; write tools accept stable operation identifiers and concrete approved arguments.

Store task ID, actor, observed order version, proposed action, approval binding, operation ID, and status. One possible progression is `proposed → awaiting_approval → approved → executing → confirmed`, with explicit failed, cancelled, and unresolved states. Revalidate stale order state and material action changes before execution. Do not turn a model's claim of completion into a confirmed state.

The mean decision rate is `50,000 × 6 / 86,400 ≈ 3.47 per second`; the assumed peak is about `27.8 per second`. This is not concurrent-request capacity: estimate that from decision duration and tool wait time. Count retries and independent tool traffic as additional load.

Persist the operation ID before attempting a write. After an ambiguous timeout or crash, reconcile with the external service or retry using its supported idempotency contract. A checkpoint alone cannot guarantee exactly-once effects. Apply bounded retries, a global deadline, and a pending/escalation path when the outcome is unknown.

Evaluate final external state, unauthorized actions, duplicate replacements, successful escalations, and latency. Test retrieved instructions that attempt to bypass policy. Traces should support diagnosis while limiting unnecessary customer-data retention.

**Strong signals:** Binds approval to exact arguments, handles ambiguous write outcomes, and distinguishes persistent execution from transactionality.

**Failure injection:** The service accepts a replacement but its response is lost; approval arrives after cancellation; a support article contains an injected instruction.

**Follow-up:** Which steps should remain fixed code even if the language model becomes more capable?

</details>

**Related study:** [Agents](../questions/agents.md), [prompt engineering](../questions/prompt-engineering.md). [AWS's discussion of idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) explains why retries need explicit side-effect semantics.

## 3. Document extraction and review pipeline

**Difficulty:** Intermediate to Advanced

**Prompt:** Design a service that extracts invoice fields from uploaded PDFs and produces validated records, routing uncertain or inconsistent cases to reviewers.

**Starting constraints:**

- 100,000 documents per day, averaging 5 pages; a burst can be 10 times average arrival rate.
- Documents must finish within 30 minutes or be reported as pending/failed. The workflow is asynchronous.
- Required fields include vendor ID, currency, line items, and total. Duplicate uploads must not create duplicate exported records.
- Some PDFs are scanned, unreadable, or contain instructions unrelated to extraction. Human review capacity is limited.

**Clarify first:** What is the ground truth? Which fields are critical? How do invoice corrections and duplicates differ? What happens when human review cannot meet the deadline?

**Design tasks:** Design upload, storage, queueing, parsing/OCR, extraction, validation, review, and export. Specify task states and the provenance retained for each field.

<details>
<summary>Reference design and interviewer notes</summary>

Accept uploads into tenant-scoped object storage and assign a durable job ID. Validate file limits, record a content hash, and queue work. Workers parse or OCR pages, extract a typed record, and run deterministic checks before any export. Preserve page references or evidence spans so reviewers can inspect the source.

Average throughput is `100,000 × 5 / 86,400 ≈ 5.79 pages per second`, or roughly `57.9 pages per second` at the assumed peak. If a worker processes 2 pages per second in a benchmark, 29 workers is only a peak-throughput lower bound; headroom, retries, queue drain, and other stages require additional capacity. Measure the slowest stage and oldest-job age.

Use schema checks plus domain checks: allowed currencies, line-item arithmetic, vendor matching, and missing fields. Schema validity does not establish correctness, and self-reported confidence should not be treated as calibrated. Set review thresholds from labeled data and reviewer capacity. Define terminal failure and review-pending states instead of retrying unreadable files forever.

Deduplicate per tenant using appropriate business keys and content identity; a revised invoice may legitimately have a new version. Make exports idempotent and retain an audit history. Evaluate field precision/recall, critical-field accuracy, review rate, reviewer agreement, duplicate exports, and end-to-end completion latency. Compare a simpler extraction baseline before introducing fine-tuning.

**Strong signals:** Separates extraction from validation, models backpressure and review queues, and distinguishes duplicates from corrections.

**Failure injection:** OCR returns empty text; a total contradicts its line items; the export succeeds but acknowledgment is lost.

**Follow-up:** How would reviewer corrections become training examples without leaking into held-out evaluation?

</details>

**Related study:** [Fine-tuning](../questions/fine-tuning.md), [evaluation](../questions/evaluation.md), and exercises 6–7 in the [hands-on notebooks](../hands-on/README.md).

## 4. Multi-tenant inference gateway

**Difficulty:** Advanced

**Prompt:** Design a gateway that serves interactive chat and asynchronous summarization across multiple model backends while enforcing tenant budgets and reliability targets.

**Starting constraints:**

- Peak chat load is 40 requests per second, averaging 2,000 input tokens and 300 output tokens per request.
- Batch summarization can wait up to 1 hour; interactive chat targets p95 time to first token below 2 seconds.
- Each tenant has an independent spend budget and permissions. One backend may be unavailable or rate-limited.
- Backends differ in context limits, tool support, latency, and response quality.

**Clarify first:** Which tasks can use a smaller model? Are fallbacks equivalent for required features and data policy? How are tokens reserved versus actually billed? What constitutes a completed streaming request?

**Design tasks:** Cover routing, admission control, queues, caching, deadlines, fallbacks, metering, cancellation, and capacity measurement.

<details>
<summary>Reference design and interviewer notes</summary>

Authenticate tenants, validate request size, reserve an estimated budget, and route according to evaluated task policies. Use separate interactive and batch queues so long jobs do not dominate latency. Limit concurrency and queue length; scale capacity using observed token workload and queue age rather than request count alone.

The assumed peak represents `80,000 input tokens/second` and `12,000 output tokens/second`. These are distinct serving demands, not interchangeable accelerator-capacity units. Benchmark the actual prompt/output distribution, cache behavior, concurrency, and batching policy to estimate replicas. Include startup and warmup time in scaling plans.

Set an overall deadline and coordinated retry budget. Route to a fallback only if it satisfies the task's feature and data requirements. Define client-visible behavior for interrupted streams; silently appending a second model's output to the first is unsafe. Cancel abandoned work where supported and reconcile reserved against actual cost.

Distinguish prefix caching from answer caching. Scope reused answers to trusted authorization context, model/prompt versions, and data freshness. Semantic similarity is insufficient for cache correctness. Track availability, first-token and completion latency, rejection rate, quality by route, and cost per successful task. Roll out routing changes with controlled traffic and rollback criteria.

**Strong signals:** Converts requests into token load, protects tenant isolation, and treats fallback quality and partial streaming as product contracts.

**Failure injection:** One tenant submits huge prompts; a primary backend fails mid-stream; a shared cache contains a response generated under different permissions.

**Follow-up:** How would the gateway behave during a sudden traffic spike while new accelerator replicas are still loading?

</details>

**Related study:** [Production engineering](../questions/production-engineering.md), [evaluation](../questions/evaluation.md), and exercise 8 in the [hands-on notebooks](../hands-on/README.md).

## 5. Evaluation and release platform

**Difficulty:** Intermediate to Advanced

**Prompt:** Design a platform that compares prompt, model, and retrieval changes before release and detects regressions after rollout.

**Starting constraints:**

- 20 candidate configurations per week, a 2,000-case evaluation suite, and 3 generation trials per case.
- Tasks include extraction, cited answers, and tool-using agents. Some graders call another model; others run deterministic checks.
- Runs must be reproducible enough to investigate regressions, with explicit data and configuration versions.
- A failing authorization test blocks release even when average answer quality improves.

**Clarify first:** Who owns the rubric? Which cases are tuning versus held-out? How are costly or state-changing tools simulated? What minimum difference is meaningful enough to justify release?

**Design tasks:** Describe dataset versioning, run orchestration, artifact storage, graders, comparisons, release gates, and post-release monitoring. Explain how to assess a small improvement with high output variability.

<details>
<summary>Reference design and interviewer notes</summary>

Register immutable dataset versions, candidate configurations, grader versions, and corpus snapshots. Schedule tasks through a bounded queue; persist case-level inputs, outputs, trace references, scores, errors, and resource usage. Keep sensitive content access-controlled. Isolate agent test environments and reset them between trials so one run cannot change another's starting state.

The workload is `20 × 2,000 × 3 = 120,000 candidate trials per week`, before baselines, retries, grader calls, or multi-step agent execution. If two model graders run once per trial, that adds 240,000 grader calls. Estimate token volume and rate limits separately, and use cheap deterministic checks where they answer the grading question.

Compare candidates on matched cases and inspect important slices. Track uncertainty at the independent case or conversation level; three generations are not three independent user tasks. Calibrate model judges against human review, test order bias, and keep formatting, correctness, citations, and action policy as distinct dimensions. Do not optimize prompts on the final held-out set.

A release gate combines hard constraints with quality and operational targets. After passing offline checks, use a canary rollout with specified stop conditions and a compatible rollback path. Online feedback can reveal distribution changes but is not automatically ground truth. Add verified incidents to regression coverage without silently converting every assessment case into tuning data.

**Strong signals:** Versions graders as well as models, accounts for evaluation cost, and separates outcome checks from persuasive final responses.

**Failure injection:** A judge upgrade inflates all scores; an agent test reuses mutated state; a candidate improves averages but fails one tenant's permission checks.

**Follow-up:** How would you prioritize the evaluation suite when cost or release time is cut in half?

</details>

**Related study:** [Evaluation](../questions/evaluation.md), [agents](../questions/agents.md). [Google SRE's canary-release guidance](https://sre.google/workbook/canarying-releases/) describes staged comparison and release risk.

## 6. Autonomous software factory

**Difficulty:** Advanced

**Prompt:** Design an end-to-end software development system where fleets of autonomous AI agents handle planning, coding, testing, and monitoring, while human engineers focus on defining business intent and reviewing results. Follow a request from its initial specification to a deployed, observed outcome, including rejected changes and production incidents.

**Starting constraints:**

- 200 engineers across 100 repositories submit 300 change requests per working day over an 8-hour arrival window. Peak arrivals are 3 times the window average.
- Each request averages 6 agent tasks, each occupying a sandbox for 12 minutes, excluding queue time and human review. Initial capacity is 200 concurrent sandboxes.
- Each task averages 15 model calls with 4,000 input tokens and 800 output tokens per call. Treat these as sizing assumptions; retries and independent evaluation add load.
- Target p95 time from accepted specification to a review-ready candidate below 90 minutes for a defined class of small changes. Human review and production observation have separate clocks.
- Multiple agents may modify the same service. Workers may crash, model providers may be rate-limited, and external actions may succeed before their acknowledgments arrive.
- Humans own intent and review results. For this scenario, production deployment requires an authorized engineer's approval bound to a verified candidate. Coding agents cannot modify protected release checks or access production credentials.
- Every release must be traceable to its intent, source revision, verification evidence, and deployed artifact. Production regressions must support bounded mitigation and escalation.

**Clarify first:** Which changes qualify for autonomous execution? Who resolves conflicting requirements? What counts as an accepted result? Which actions are preauthorized? What repositories, data, and environments may each worker access? How are migrations, cross-repository changes, review delays, and emergency fixes handled?

**Design tasks:** Define intent intake, planning, fleet scheduling, sandbox execution, independent testing, integration, human review, release, and monitoring. Include a task and artifact model, one capacity estimate, permission boundaries, budget enforcement, and recovery after a crash between an external action and its local checkpoint. Explain how production feedback creates new work without allowing an uncontrolled repair loop.

<details>
<summary>Reference design and interviewer notes</summary>

Use a durable orchestration service as the authoritative owner of runs and tasks. Models propose plans and actions; application services validate permissions, dispatch work, record evidence, and enforce state transitions. Keep worker execution separate from trusted verification and release services.

```mermaid
flowchart TD
    Human[Engineers define business intent] --> Spec[Versioned specification and acceptance criteria]
    Spec --> Planner[Planning agents propose task graph]
    Planner --> Control[Durable orchestration and policy service]
    Control <--> State[(Task state and artifact records)]
    Control --> Queue[Bounded queues and worker leases]
    Queue --> Workers[Coding and test agents in isolated sandboxes]
    Workers --> Verify[Independent verification and integration queue]
    Verify --> Review[Engineer reviews candidate and evidence]
    Review --> Release[Authorized release service and canary]
    Release --> Prod[Production]
    Prod --> Monitor[Telemetry and monitoring agents]
    Monitor --> Outcome[Outcome evidence for engineers]
    Outcome --> Human
    Monitor --> Incident[Incident record and bounded remediation proposal]
    Incident --> Control
```

**Request flow:** An engineer supplies the desired outcome and constraints. Planning agents inspect a pinned repository revision and propose a specification and task graph; unresolved material product choices return to the owner. Coding agents receive ready tasks with explicit scope and acceptance criteria. Test agents can propose additional checks, while an independent service executes protected checks against the integrated candidate. The review packet includes a demonstration where appropriate, requirement coverage, diff, test reports, limitations, cost, and a rollout plan. An authorized review permits deployment of the verified artifact. Monitoring collects reliability and business-outcome evidence for engineers and links any remediation to the original release.

**State and contracts:** One possible run progression is `intake → specified → planned → executing → verifying → awaiting_review → approved → deploying → observing → accepted`. Include explicit `blocked`, `failed`, `cancelled`, and `rolled_back` outcomes. Keep bounded repair attempts under the run rather than silently restarting its budget. Define acceptance over an agreed observation window, distinguishing software conformance from longer-term business impact.

| Record | Essential fields |
| --- | --- |
| Intent | ID, owner, version, outcome, acceptance criteria, constraints, authorization scope |
| Run | ID, intent version, plan version, repository revisions, configuration versions, state, deadline, reserved and actual cost |
| Task | ID, run ID, dependency IDs, input artifact hashes, output contract, status, lease generation, attempt count |
| Artifact | Digest, source revision, build inputs, producer attempt, protected verification reports, retention policy |
| Review | Reviewer, decision, candidate digest, relevant intent and policy versions, target environment, permitted action |
| Release | Operation ID, artifact digest, environment, rollout state, observation window, rollback or recovery reference |
| Incident | Affected release, telemetry evidence, owner, mitigation status, linked remediation run |

The scheduler accepts a task result only when its attempt and input versions remain current. Changing intent or shared interfaces invalidates dependent work. An approval applies to its recorded candidate; rebase, rebuild, or behavior changes require revalidation and renewed approval when the approved artifact changes.

**Capacity:** Average arrival rate during the working window is `300 / 8 = 37.5 requests/hour`. Task demand is `37.5 × 6 = 225 tasks/hour`. At `12 / 60 = 0.2 sandbox-hours/task`, average offered load is `225 × 0.2 = 45 occupied sandboxes`, rising to `135` at the assumed peak. This is a workload estimate, not a latency guarantee: dependency chains, retries, uneven task duration, and verification queues affect completion time. The initial 200 slots provide nominal headroom; validate the 90-minute target with measured task distributions and queue simulations.

The baseline workload is `300 × 6 × 15 = 27,000 model calls/day`, or `108 million input tokens/day` and `21.6 million output tokens/day`. Over the 8-hour window, those average `3,750 input tokens/second` and `750 output tokens/second`; the assumed peak is three times those rates. Provider quotas, model response times, and build infrastructure impose separate limits. Human review is another capacity constraint: at an illustrative 10 minutes per request, 300 requests require 50 reviewer-hours/day. Bound work in progress when review cannot keep pace.

**Isolation and integration:** Run workers in disposable environments with task-scoped credentials, network controls, and no production secrets. Separate workspaces avoid edit collisions, while a merge queue validates behavioral compatibility against the current target branch. Keep protected acceptance checks and release policy outside coding-worker write scope. Tests generated by the same agents are useful additions but cannot replace independent criteria. Verify the exact artifact to be deployed and bind source, build, and test evidence to its digest.

**Recovery and budgets:** Persist accepted outputs and operation IDs before issuing external writes. When a lease expires, reassign work with a new generation and reject stale results. After an ambiguous deployment response, query the release service using the operation ID instead of assuming failure. Checkpoints do not make external effects exactly once. Cancel descendants and reconcile in-flight actions when a run stops. Enforce per-run time, token, sandbox, and repair limits with atomic reservations; preserve an incomplete result when a limit is reached.

**Release and monitoring:** Roll out gradually using predeclared health criteria and a compatible rollback or forward-recovery plan. Application rollback alone may not reverse a database migration. Monitoring agents correlate telemetry with release versions and propose fixes; a trusted controller may execute an explicitly preauthorized mitigation. Novel patches go through verification and review. Deduplicate incident-triggered work, cap repair loops, and provide an emergency stop. Missing or stale monitoring data blocks further rollout rather than being interpreted as healthy behavior.

**Evaluation and rollout:** Start with a held-out set of representative repository tasks and a single-agent or existing delivery-process baseline. Measure requirement satisfaction, accepted changes, escaped defects, reviewer effort, end-to-end latency, total cost, and unauthorized actions. Include abandoned requests and failed attempts. Pilot on bounded changes, then expand scope only after measured outcomes justify it. Version factory configurations separately from produced software, and define how active runs finish when the factory itself is upgraded.

**Strong signals:** Connects human intent to independently verified outcomes, models integration and review as bottlenecks, limits authority outside the model, and distinguishes deployment success from business success.

**Failure injection:** Two agents produce incompatible API changes; a worker weakens tests to make its patch pass; a crash occurs after deployment but before checkpointing; approval refers to an older candidate; monitoring repeatedly proposes fixes that cause new incidents.

**Follow-ups:** How would you support a coordinated release across ten repositories? What changes if only 20% of requests have clear acceptance tests? How would you drain active runs after discovering a compromised worker image?

</details>

**Related study:** [Software Factory](../questions/software-factory.md), [Agent Orchestration](../questions/agent-orchestration.md), [evaluation](../questions/evaluation.md), and [production engineering](../questions/production-engineering.md). [GitHub's merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) explains integration checks; [SLSA provenance](https://slsa.dev/spec/v1.2/provenance) describes build evidence. The factory architecture above is an illustrative synthesis, not a guarantee supplied by either mechanism.
