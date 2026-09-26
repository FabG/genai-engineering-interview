# Production Engineering Questions and Answers

[Back to the README](../README.md) · [Agents](agents.md) · [Fine-tuning](fine-tuning.md) · [RAG](rag.md) · [Evaluation](evaluation.md)

These questions cover deploying and operating reliable GenAI applications. Engineers can practice the short answers; interviewers can use the examples and follow-ups to explore operational judgment. Designs, numerical examples, and targets are illustrative. Serving behavior and supported optimizations depend on the model, runtime, hardware, and provider.

## Contents

- [Deployment and service goals](#deployment-and-service-goals): hosting choices, service objectives, and latency.
- [Serving performance](#serving-performance): batching, memory, quantization, and caching.
- [Reliability and releases](#reliability-and-releases): overload, retries, fallbacks, and rollout safety.
- [Operations and cost](#operations-and-cost): observability, security, and efficiency.

## Deployment and service goals

### Question: 1. How do you choose between a hosted model API and self-managed inference?

**Topic:** Deployment architecture
**Difficulty:** Intermediate

**Short answer:**
Compare task quality, data-handling requirements, control over the serving stack, operational capacity, and total cost under realistic traffic.

**Explanation:**
A hosted API reduces infrastructure work but introduces provider quotas, dependencies, and configuration constraints. Self-managed inference offers more control while requiring capacity planning, upgrades, security, and incident response. Managed dedicated endpoints offer another option between these extremes. Benchmark the complete application; self-hosting is not automatically cheaper, and a managed service does not remove application-level responsibilities.

**Example:**
A team compares a shared API with a dedicated endpoint using the same workload, including idle periods, peak traffic, and failure handling.

**Follow-up questions:**

- Which costs would you include beyond the model's token price or accelerator rental?

**References:**

- [Hugging Face: Managed inference endpoints](https://huggingface.co/docs/inference-endpoints/index)

### Question: 2. What are SLIs, SLOs, and error budgets for a GenAI service?

**Topic:** Service reliability
**Difficulty:** Intermediate

**Short answer:**
A service-level indicator (SLI) measures behavior, a service-level objective (SLO) sets a target over a window, and an error budget describes the allowed deviation.

**Explanation:**
Define the eligible request population, success criteria, and measurement point. Track availability and latency separately from answer quality: an HTTP success can contain an unusable answer. Quality may require delayed or sampled evaluation. Use budget consumption to guide release and reliability work rather than treating every service as requiring perfect availability.

**Example:**
For a request-based 99.9% success SLO over 100,000 eligible requests, the budget permits 100 unsuccessful requests in that window.

**Follow-up questions:**

- How should a response that starts streaming but fails before completion affect the success SLI?

**References:**

- [Google SRE: Service-level objectives](https://sre.google/sre-book/service-level-objectives/)

### Question: 3. How do you diagnose latency in a streaming LLM application?

**Topic:** Latency analysis
**Difficulty:** Intermediate

**Short answer:**
Separate queueing, retrieval, prompt processing, token generation, and downstream work; measure time to first token and total completion time.

**Explanation:**
Prefill processes the prompt, while decoding generates subsequent tokens. Record where timing begins, because client-observed latency includes work that model-server metrics may exclude. Inspect median and tail latency across realistic input and output lengths. Streaming can improve responsiveness without shortening completion time, and a fast first token can hide slow later generation.

**Example:**
With a 1-second time to first token and 99 further tokens arriving 20 milliseconds apart, the 100-token response completes in approximately 2.98 seconds, ignoring finalization overhead.

**Follow-up questions:**

- What would you investigate if time to first token rises while token-generation speed remains stable?

**References:**

- [vLLM: Serving metrics](https://docs.vllm.ai/en/latest/design/metrics/)

## Serving performance

### Question: 4. How do batching and memory affect inference capacity?

**Topic:** Throughput and scaling
**Difficulty:** Intermediate

**Short answer:**
Batching shares computation across requests, while available memory limits the model, active sequences, and their key-value caches. Capacity depends on token workload, not just request count.

**Explanation:**
Continuous batching lets new requests join as others finish rather than waiting for an entire fixed batch. Higher concurrency can improve throughput but increase queueing and per-request latency. Account for prompt length, output length, KV-cache growth, and startup time when sizing or scaling replicas. Paged KV-cache management improves utilization but does not create unlimited capacity.

**Example:**
Ten requests with long histories and long outputs can consume more serving capacity than many short classification requests.

**Follow-up questions:**

- Why might queue depth and active token counts be more useful scaling signals than CPU utilization alone?

**References:**

- [Hugging Face: Continuous batching](https://huggingface.co/docs/transformers/continuous_batching)
- [Kwon et al.: PagedAttention and LLM serving](https://arxiv.org/abs/2309.06180)

### Question: 5. What does inference quantization save, and what must you verify?

**Topic:** Model optimization
**Difficulty:** Intermediate

**Short answer:**
Quantization stores selected tensors at lower precision, reducing their memory footprint. Validate both task quality and performance on the actual serving hardware.

**Explanation:**
Weight-only quantization does not automatically reduce activations or the KV cache. Metadata, temporary buffers, and runtime overhead also consume memory. Speed depends on supported kernels and workload; a smaller model representation can still run slower. Test difficult task slices and the final deployed artifact rather than assuming compression preserves behavior.

**Example:**
Eight billion weights require approximately 16 GB at 16 bits each or 4 GB at 4 bits each, using decimal units and excluding all other memory costs.

**Follow-up questions:**

- Why can a model's weights fit on a device while production requests still exhaust memory?

**References:**

- [Hugging Face: Quantization overview](https://huggingface.co/docs/transformers/quantization/overview)

### Question: 6. How do response caching, semantic caching, and prefix caching differ?

**Topic:** Cache design
**Difficulty:** Intermediate

**Short answer:**
Response caching reuses a completed result, semantic caching reuses a result for a sufficiently similar request, and prefix caching reuses computation for an identical prompt prefix.

**Explanation:**
Prefix caching reduces repeated prefill work; it does not reuse a finished answer or eliminate decoding. As an application design, include relevant model, prompt, data-version, and authorization scope in response-cache decisions. Similar wording does not prove equivalent meaning. Define invalidation rules for source changes and permission revocations, and measure cold-cache as well as warm-cache behavior.

**Example:**
Reusing an answer about one customer's order for another customer is incorrect even if their questions are nearly identical.

**Follow-up questions:**

- When could a semantic cache return a plausible answer that violates freshness or access requirements?

**References:**

- [vLLM: Automatic prefix caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)

## Reliability and releases

### Question: 7. How do you protect a GenAI service from overload?

**Topic:** Admission control
**Difficulty:** Intermediate

**Short answer:**
Limit admitted work, bound queues and concurrency, and reject or defer excess demand before it causes widespread timeouts or memory exhaustion.

**Explanation:**
Requests have different costs, so consider token limits and per-tenant budgets as well as request rate. Backpressure slows upstream producers; load shedding rejects work the service cannot safely handle. Autoscaling helps only after capacity becomes ready. Propagate cancellations where possible, and prevent a backlog of expired requests from consuming scarce inference capacity.

**Example:**
During a traffic spike, enforce bounded queues and explicit overload responses rather than accepting every request into an indefinitely growing queue.

**Follow-up questions:**

- How would you keep one tenant's long-running requests from starving everyone else?

**References:**

- [Google SRE: Handling overload](https://sre.google/sre-book/handling-overload/)

### Question: 8. How should retries, deadlines, and fallbacks work together?

**Topic:** Dependency failures
**Difficulty:** Advanced

**Short answer:**
Set an overall request deadline, retry only appropriate failures within a bounded budget, and use fallbacks whose behavior has been evaluated in advance.

**Explanation:**
Exponential backoff with jitter helps avoid synchronized retry bursts. Avoid multiplying retries across application and SDK layers. Do not blindly retry invalid requests, permission failures, or ambiguous side-effecting actions. A circuit breaker can temporarily stop calls to a failing dependency. Fallback models must still satisfy output, privacy, and task requirements; restarting after partial streaming also needs explicit client handling.

**Example:**
If the primary model times out, use the remaining deadline for one validated fallback rather than starting another full timeout window.

**Follow-up questions:**

- How could a fallback improve availability while silently reducing application correctness?

**References:**

- [AWS: Retry behavior, backoff, and retry budgets](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html)
- [Google SRE: Handling overload and limiting dependency pressure](https://sre.google/sre-book/handling-overload/)

### Question: 9. How do you release and roll back a GenAI application safely?

**Topic:** Deployment lifecycle
**Difficulty:** Intermediate

**Short answer:**
Version the complete application configuration, validate a candidate, expose limited traffic, and retain a tested path back to a compatible known-good release.

**Explanation:**
The release includes model revision, tokenizer, prompt, tool schemas, retrieval configuration, and relevant data versions. A practical rollout uses readiness checks, warmup, and canary monitoring for quality and reliability. Shadow requests must not duplicate external side effects. Infrastructure rollback alone may not restore changed indexes, prompts, or database state, so plan compatibility explicitly.

**Example:**
A new embedding model uses a separately built index; switching back restores the previous compatible model-index pair.

**Follow-up questions:**

- Why might rolling back only the application container fail to restore previous behavior?

**References:**

- [Kubernetes: Deployment updates and rollbacks](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

## Operations and cost

### Question: 10. What observability helps diagnose and manage production incidents?

**Topic:** Monitoring and incident response
**Difficulty:** Intermediate

**Short answer:**
Combine user-facing metrics with correlated traces and structured logs so you can identify the failing stage, mitigate impact, and verify recovery.

**Explanation:**
Trace retrieval, model calls, tools, and retries using shared request identifiers. Record versions, durations, errors, token usage, and cache behavior without indiscriminately retaining sensitive content. Alert on meaningful user impact. During incidents, establish ownership, communicate status, and prioritize mitigation; preserve evidence for root-cause analysis and follow-up regression tests.

**Example:**
A latency alert leads to traces showing slow reranking. Reverting that component restores the service while the team investigates its resource contention.

**Follow-up questions:**

- Which measurements would distinguish a provider outage from a bad prompt release or a slow retrieval index?

**References:**

- [OpenTelemetry: Distributed traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- [Google SRE: Managing incidents](https://sre.google/sre-book/managing-incidents/)

### Question: 11. Where should security boundaries sit in a production GenAI application?

**Topic:** Application security
**Difficulty:** Intermediate

**Short answer:**
Enforce identity, authorization, secret handling, and action policy in trusted application components rather than relying on model instructions.

**Explanation:**
Treat user inputs, retrieved documents, tool results, and generated output as potentially untrusted. Scope data access and caches to the correct tenant, constrain tool permissions and network access, and validate generated commands or parameters before execution. Prompt injection defenses do not replace these controls. Give logs and traces explicit access and retention rules because they can contain sensitive content.

**Example:**
A generated query must execute under the authenticated user's permitted data scope, even when its syntax is valid.

**Follow-up questions:**

- How could a debugging trace or shared cache leak information even when normal retrieval is correctly authorized?

**References:**

- [OWASP: AI agent security guidance](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)

### Question: 12. How do you optimize cost without undermining task success?

**Topic:** Cost and utilization
**Difficulty:** Intermediate

**Short answer:**
Measure total cost per successfully completed task, then optimize the largest contributors while keeping quality and reliability requirements fixed.

**Explanation:**
Include model calls, failed attempts, retrieval, tools, storage, and provisioned capacity. Hosted token billing and dedicated hardware billing respond differently to idle time and utilization. Test shorter outputs, appropriate model routing, caching, batching, or asynchronous processing where the task permits. Compare equivalent workloads and cache conditions; a lower price per call can be offset by more failures and retries.

**Example:**
Spending 12 cost units for 800 successful tasks costs 0.015 per success; spending 10 for only 500 successes costs 0.02. The cheaper total is less efficient in this example.

**Follow-up questions:**

- How would bursty demand change the comparison between shared API usage and continuously provisioned accelerators?

**References:**

- [Hugging Face: Dedicated endpoint billing model](https://huggingface.co/docs/inference-endpoints/pricing)
- [Hugging Face: Continuous batching and utilization](https://huggingface.co/docs/transformers/continuous_batching)

Use the [evaluation question bank](evaluation.md) to define release criteria and assess these operational tradeoffs.
