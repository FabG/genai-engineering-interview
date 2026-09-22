# Agents and Tool Use Questions and Answers

[Back to the README](../README.md) · [Prompt engineering](prompt-engineering.md) · [RAG](rag.md) · [Fine-tuning](fine-tuning.md) · [Evaluation](evaluation.md)

These questions cover systems that use language models to select actions, interact with tools, and adapt to results. Engineers can practice the short answers; interviewers can explore design choices with the follow-ups. Examples and proposed designs are illustrative. Framework references demonstrate particular implementations, not universal agent behavior.

## Contents

- [Architecture and tools](#architecture-and-tools): agents versus workflows, execution loops, and tool interfaces.
- [State and execution](#state-and-execution): memory, stopping conditions, retries, and persistence.
- [Control and coordination](#control-and-coordination): approvals, prompt injection, and multiple agents.
- [Evaluation and observability](#evaluation-and-observability): outcomes, traces, and operational metrics.

## Architecture and tools

### Question: 1. How does an agent differ from a fixed workflow?

**Topic:** Architecture choices
**Difficulty:** Beginner

**Short answer:**
In a fixed workflow, code determines the main sequence of steps. In an agent, a model chooses some next steps dynamically using the task and observed results.

**Explanation:**
The boundary is a design spectrum, not a universal naming rule. Workflows suit predictable procedures; agents help when the required path is uncertain. Dynamic decisions introduce variability, latency, and failure modes. Start with the simplest approach that meets the task requirements.

**Example:**
Extracting invoice fields and checking totals can follow a fixed workflow; investigating an unfamiliar software failure may require adaptive tool choices.

**Follow-up questions:**

- What evidence would justify replacing a fixed workflow with an agent?

**References:**

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 2. What happens in an agent's tool-use loop?

**Topic:** Execution model
**Difficulty:** Beginner

**Short answer:**
The model selects an action, the application validates and executes it, and the resulting observation informs the next decision or final response.

**Explanation:**
ReAct is a research pattern that interleaves reasoning and actions with observations. In an application, distinguish proposed tool calls from actual execution and verified outcomes. Preserve relevant results in state, handle errors explicitly, and terminate when the task is complete or a control condition is reached. A narrated action is not evidence that the action happened.

**Example:**
An assistant requests an order lookup, receives the record from the application, and then reports the observed shipment status.

**Follow-up questions:**

- How would you prevent the agent from claiming success after a failed tool call?

**References:**

- [Yao et al.: ReAct](https://arxiv.org/abs/2210.03629)

### Question: 3. What makes a tool interface reliable for an agent?

**Topic:** Tool design
**Difficulty:** Intermediate

**Short answer:**
A reliable tool has a clear purpose, precise argument definitions, bounded behavior, and results that distinguish success, failure, and missing data.

**Explanation:**
Avoid overlapping tool descriptions that make selection ambiguous. Validate schemas and domain constraints in code, return useful identifiers and errors, and limit unnecessary output. Separate read operations from state-changing operations where useful. The application's permissions determine whether execution is allowed, regardless of the model's requested arguments.

**Example:**
A lookup returns an explicit `not_found` status for an unknown order rather than a blank string that could be mistaken for success.

**Follow-up questions:**

- When would a focused business operation be easier to use safely than a generic execution tool?

**References:**

- [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)

## State and execution

### Question: 4. How do context, working state, and long-term memory differ?

**Topic:** Memory
**Difficulty:** Intermediate

**Short answer:**
Context is the information supplied to a model call. Working state tracks the current task. Long-term memory stores information for later tasks or conversations.

**Explanation:**
Persisted state does not automatically fit into the model's context; the application selects or summarizes what to include. Treat memory as data with provenance, scope, and update rules. Summaries can lose qualifications, and stored mistakes can contaminate later decisions. Reading or writing memory does not by itself update model weights.

**Example:**
Store completed task steps in a run record and retrieve a user's verified preferences separately, rather than replaying every past conversation.

**Follow-up questions:**

- How would you correct a false memory and prevent it from being reused?

**References:**

- [LangChain: Memory concepts](https://docs.langchain.com/oss/python/concepts/memory)

### Question: 5. How should an agent plan and decide when to stop?

**Topic:** Planning and budgets
**Difficulty:** Intermediate

**Short answer:**
Use a revisable plan and explicit completion criteria, with application-enforced limits on steps, time, tool calls, or spending.

**Explanation:**
Plans should change when observations invalidate assumptions. A practical design checks for progress, repeated failures, and blocked dependencies. Hitting a budget is not successful completion; return the verified partial result and unresolved issue. Application controls should enforce limits even if the model requests another step.

**Example:**
After repeated searches produce no new evidence, stop and report the missing information instead of repeating the same query indefinitely.

**Follow-up questions:**

- What signals would distinguish useful exploration from a loop?

**References:**

- [Anthropic: Agent loops and stopping conditions](https://www.anthropic.com/engineering/building-effective-agents)

### Question: 6. How should an agent handle tool failures and retries?

**Topic:** Failure recovery
**Difficulty:** Intermediate

**Short answer:**
Classify the failure, retry transient problems within limits, and avoid repeating state-changing actions unless their effects can be deduplicated or verified.

**Explanation:**
A timeout can occur after a remote action succeeds, so it does not prove that nothing happened. Use idempotency keys where supported, query operation status, and preserve action identifiers. Apply bounded backoff for transient failures; invalid arguments or permission denials usually need a different response. Do not let model retries bypass these controls.

**Example:**
If ticket creation times out, check the request's operation identifier before submitting another creation request.

**Follow-up questions:**

- Why is retrying a read usually simpler than retrying a purchase or record creation?

**References:**

- [AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

### Question: 7. What does durable execution add to an agent?

**Topic:** Persistence and resumption
**Difficulty:** Advanced

**Short answer:**
Durable execution persists enough state and completed work to resume after interruption instead of starting the whole task again.

**Explanation:**
Checkpoint task state, tool outcomes, and pending decisions. Resumption semantics depend on the runtime: some work may replay. Protect side effects with idempotency or explicit reconciliation. A checkpoint is not a distributed transaction and does not guarantee exactly-once execution across external services. Recheck assumptions that may have changed while paused.

**Example:**
After a worker restarts, resume from a saved document-analysis result while verifying whether a previously requested external update completed.

**Follow-up questions:**

- What happens if the process crashes after an external write but before saving its success locally?

**References:**

- [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [AWS Builders' Library: Idempotent retries](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

## Control and coordination

### Question: 8. Where should human review and authorization fit into an agent?

**Topic:** Action control
**Difficulty:** Intermediate

**Short answer:**
Enforce authorization in the application, and request human review where an action's impact or unresolved ambiguity requires it under the product's policy.

**Explanation:**
An approval should identify a concrete action and its material arguments. A practical design binds approval to that proposal, preserves it across a pause, and reassesses material changes before execution. Do not treat model confidence or a generic “approved” message as authority. Routine authorized actions can proceed without adding unnecessary review steps.

**Example:**
Present the exact recipients and draft before a workflow's required publishing approval, then execute only the approved version.

**Follow-up questions:**

- How would you prevent stale approval from authorizing a changed action after resumption?

**References:**

- [LangGraph: Interrupts and human review](https://docs.langchain.com/oss/python/langgraph/interrupts)

### Question: 9. Why is prompt injection especially important for agents?

**Topic:** Untrusted inputs
**Difficulty:** Intermediate

**Short answer:**
An injected instruction can influence tool selection and external actions, not only the wording of an answer.

**Explanation:**
Retrieved pages, files, and tool responses can contain instructions from untrusted sources. Treat them as data and enforce least privilege, argument validation, and action policy outside the model. Delimiters and defensive prompts help interpretation but do not establish a security boundary. Test actual tool behavior and information exposure, not merely whether the final response looks safe.

**Example:**
A retrieved support article instructs the assistant to upload private records elsewhere; that text cannot grant permission to access or transmit them.

**Follow-up questions:**

- Which restrictions would still protect the system if the model followed the injected text?

**References:**

- [Greshake et al.: Indirect prompt injection in LLM applications](https://arxiv.org/abs/2302.12173)

### Question: 10. When is a multi-agent design worth the complexity?

**Topic:** Coordination
**Difficulty:** Advanced

**Short answer:**
Use multiple agents when tasks can benefit from separate contexts, specializations, or independent work, and evaluation shows that the gains justify coordination costs.

**Explanation:**
Define ownership, handoff formats, shared-state rules, and a coordinator responsible for synthesis. Additional agents can duplicate effort, propagate mistakes, or conflict over state. Agreement among similar models is not independent verification. Compare against a single-agent baseline under comparable resource limits.

**Example:**
Separate workers investigate independent source collections, while a coordinator resolves contradictions and produces a cited synthesis.

**Follow-up questions:**

- Why might parallel workers help research but complicate edits to the same shared record?

**References:**

- [Anthropic: Building a multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

## Evaluation and observability

### Question: 11. How do you evaluate an agent beyond its final response?

**Topic:** Agent evaluation
**Difficulty:** Intermediate

**Short answer:**
Evaluate the verified environment outcome, compliance with action constraints, and the resources used to complete the task.

**Explanation:**
Run representative tasks in resettable environments and inspect resulting state, tool arguments, failures, and unauthorized effects. Allow valid alternative action sequences rather than requiring one exact trace. Repeat trials to estimate reliability, and distinguish eventual success after retries from success on the first attempt. Use human or model graders where deterministic checks are insufficient.

**Example:**
For an issue-resolution task, check the resulting code and tests, not merely whether the assistant says the bug is fixed.

**Follow-up questions:**

- How would you score an agent that completes the task but changes an unrelated record?

**References:**

- [Anthropic: Demystifying evaluations for agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### Question: 12. What should you trace and monitor in an agent system?

**Topic:** Observability
**Difficulty:** Intermediate

**Short answer:**
Link model calls, tool executions, state transitions, and final outcomes into a trace, then monitor success, failure, latency, and cost by task type.

**Explanation:**
Record model and prompt versions, tool identifiers, durations, retry counts, and termination reasons. As an operational design, retain enough input and output detail to diagnose failures while controlling sensitive content and access. Distinguish time spent in models, tools, queues, and human review. Tracing application events does not require access to private model reasoning.

**Example:**
A trace reveals that a slow run spent most of its time retrying a search timeout rather than generating tokens.

**Follow-up questions:**

- What would you record to distinguish a model regression from a failing downstream API?

**References:**

- [LangSmith: Observability concepts](https://docs.langchain.com/langsmith/observability-concepts)

Continue with [fine-tuning](fine-tuning.md) or [evaluation](evaluation.md).
