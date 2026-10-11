# AI and GenAI Interview Cheat Sheet

[Back to the README](README.md) · [Definitions and terminology](GLOSSARY.md)

Use this page for recall, then open the linked question banks for assumptions, worked examples, diagrams, and references. Every question also has its own **Quick Cheat Sheet**. Numerical examples below are illustrative; targets depend on the application.

## AI and machine learning

**“V” for o“V”erfitting.** High variance means predictions are sensitive to the training sample; excessive model flexibility is one common cause.

| Concept | What it is | Too much of it causes… | Example |
| --- | --- | --- | --- |
| **Bias** | Systematic error; often rigid assumptions or insufficient model flexibility | **Underfitting**: poor train and test performance | A straight line for a curved trend |
| **Variance** | Sensitivity to the sampled training data | **Overfitting**: great train performance, poor test performance | A zigzag curve chasing every noisy point |
| **Irreducible noise** | Unpredictable variation given the available inputs | A floor on achievable error | Different outcomes from indistinguishable inputs |

For squared-error regression at a fixed input, expected error decomposes into **bias² + variance + noise**, averaging over training samples and outcome noise. Train/test gaps can also come from distribution shift, so the mnemonic is a diagnostic aid, not a proof.

| Remember | Practical check |
| --- | --- |
| **Train → validate → test** | Fit parameters → select settings → assess the finalized procedure. Split by time or entity when needed. |
| **Precision: trust the positives** | TP / (TP + FP). Of positive predictions, how many were right? |
| **Recall: recover the positives** | TP / (TP + FN). Of actual positives, how many were found? |
| **F1** | 2TP / (2TP + FP + FN); balances precision and recall, but ignores true negatives. |
| **MAE versus RMSE** | Both have target units; RMSE emphasizes large residuals. |
| **Calibration versus ranking** | Probabilities should match observed frequencies; ranking only orders cases. |
| **Leakage** | Was every feature and fitted transformation available at prediction time? |

With TP=80, FP=20, FN=40, TN=860: accuracy=94%, precision=80%, recall≈66.7%, F1≈72.7%. State the positive class, threshold, and prevalence.

[Study AI foundations](questions/ai-foundations.md).

## GenAI and LLM foundations

| Cue | Remember |
| --- | --- |
| **Tokens ≠ words** | Count with the actual tokenizer, especially for code and multilingual inputs. |
| **Q / K / V** | Queries seek matches, keys provide matching signals, values supply the combined information. |
| **Pretrain / tune / infer** | Learn broad patterns / update for a target objective / use the model. |
| **Context ≠ memory** | Current request capacity differs from externally persisted and retrieved state. |
| **Prefill / decode** | Process the prompt / generate incrementally. Diagnose their latency separately. |
| **Perplexity** | exp(mean negative log likelihood in nats); compare only compatible tokenization and evaluation data. |
| **Sampling ≠ verification** | Temperature and top-p alter sampling, not factual support. |

Approximate KV-cache bytes: **2 × layers × batch × sequence length × KV heads × head dimension × bytes per element**, before overhead. Use the number of KV heads, which may differ from query heads.

[Study LLM foundations](questions/genai-foundations.md).

## RAG

**Find → select → support.** First retrieve the evidence, then fit useful evidence into context, then verify the answer's claims.

| Cue | Remember |
| --- | --- |
| **Lexical / dense / hybrid** | Exact terms / semantic similarity / complementary signals. |
| **Retriever / reranker** | Find candidates / improve their order. Reranking cannot rescue absent evidence. |
| **Small child / larger parent** | Precise matching / enough context to retain conditions and exceptions. |
| **Gold-context test** | Give the generator the correct evidence to isolate generation from retrieval failure. |
| **ACLs everywhere** | Retrieval, expansion, reranking, citations, and caches must preserve effective access. |
| **Freshness is end-to-end** | Source updates, derived chunks, indexes, and cached answers can all become stale. |

Do not confuse evidence recall with answer correctness. A system may retrieve the right policy and still ignore its exception.

[Study RAG](questions/rag.md).

## Prompt engineering

| Cue | Remember |
| --- | --- |
| **Task + inputs + contract + unknowns** | Specify what to do, what to use, what to return, and when to clarify or abstain. |
| **Examples teach boundaries** | Include exceptions and negative cases; keep test examples separate. |
| **Parse → schema → semantics** | Valid JSON can still contain incorrect dates, totals, or identifiers. |
| **Propose ≠ execute** | Tool calls need runtime validation and authorization. |
| **Delimiters ≠ permissions** | Structure helps interpretation; external controls enforce authority. |
| **Version the whole prompt setup** | Include examples, templates, schemas, and relevant model settings. |

Evaluate task success and total cost, including repair calls. A shorter prompt that causes retries may cost more.

[Study prompt engineering](questions/prompt-engineering.md).

## Agents and tool use

**Observe → act → verify → stop.** Completion comes from authoritative results, not the agent's claim that it finished.

| Cue | Remember |
| --- | --- |
| **Workflow / agent** | Predefined control / observation-driven action selection. |
| **Transient / permanent / ambiguous** | Retry boundedly / fix or stop / reconcile external state before repeating a write. |
| **Checkpoint ≠ exactly once** | A crash can occur after a successful side effect but before saving its result. |
| **Approval binds to a proposal** | Changed amount, target, or scope may invalidate the earlier approval. |
| **Memory needs provenance** | Stored model guesses do not become verified facts. |
| **Evaluate the trajectory** | Check unauthorized actions, duplicate writes, budgets, and real task completion. |

[Study agents](questions/agents.md).

## Agent orchestration

| Cue | Remember |
| --- | --- |
| **Parallelize independent work** | Agree on shared interfaces before workers implement them. |
| **Handoff = contract + evidence** | Include objective, versions, constraints, expected artifact, and definition of done. |
| **Lease + fencing** | Temporary ownership plus rejection of stale writers. |
| **One logical retry budget** | Independent retry layers can multiply downstream attempts. |
| **Consensus ≠ independent evidence** | Multiple agents can share the same wrong assumption. |
| **Measure complete tasks** | Include queueing, integration, review, and failed work. |

Three layers with three total attempts each can create **27 downstream attempts**. Bound retries across the full task tree.

[Study orchestration](questions/agent-orchestration.md).

## Software factories

| Cue | Remember |
| --- | --- |
| **Intent → specification → evidence → release** | Make user outcomes testable before delegating implementation. |
| **Independent acceptance checks** | Implementation and agent-written tests can share the same misunderstanding. |
| **Test the integrated revision** | Individually passing branches can fail when combined. |
| **Provenance links exact artifacts** | Requirements, commits, tests, approvals, and deployed digests must match. |
| **Rollback includes state** | Reverting code does not restore deleted data or undo external effects. |
| **Accepted changes, not generated code** | Include human review, rework, and incidents in value and cost measures. |

[Study software factories](questions/software-factory.md).

## Fine-tuning

| Cue | Remember |
| --- | --- |
| **CPT / SFT / preference** | Domain text distribution / desired demonstrations / relative response quality. |
| **LoRA** | Frozen base plus a trainable low-rank weight update. |
| **QLoRA** | Quantized base plus low-rank adapters; verify the final serving artifact separately. |
| **Overfitting / forgetting** | Worse unseen target performance / loss of previously useful capabilities. |
| **Template + mask + truncation** | Inspect the tokens that actually receive training loss. |
| **Distill / quantize** | Train a student / reduce numerical precision. These are different interventions. |

For one d_out × d_in weight matrix, LoRA adds **r(d_in + d_out)** parameters. A 4096 × 4096 matrix with rank 8 adds 65,536 parameters, about **0.39%** of that matrix's 16,777,216 weights. This is not the percentage of total training memory saved.

[Study fine-tuning](questions/fine-tuning.md).

## Evaluation

| Metric or distinction | Remember |
| --- | --- |
| **P@k / R@k** | Relevant returned items divided by k / relevant returned items divided by all known relevant items. |
| **MRR / nDCG** | First relevant hit / graded quality of the ranking normalized against the ideal. |
| **Correct / faithful / cited** | Right for the task / supported by context / linked to evidence that supports the claim. |
| **Judge ≠ ground truth** | Audit position bias, verbosity bias, false accepts, and false rejects. |
| **Paired evaluation** | Compare systems on the same tasks; resample independent units, not correlated turns. |
| **Coverage / selective risk** | Fraction answered / error fraction among answered cases. |

Answering 60 of 100 eligible questions with three wrong answers gives **60% coverage and 5% selective risk**. Compare risk at similar coverage, and include the cost of escalation.

[Study evaluation](questions/evaluation.md).

## Production engineering

| Cue | Remember |
| --- | --- |
| **SLI / SLO / error budget** | Measurement / target and window / permitted bad events. |
| **TTFT / inter-token / total** | First visible progress / streaming pace / full completion latency. |
| **Response / semantic / prefix cache** | Reuse an answer / reuse by similarity / reuse model computation. |
| **Throughput ≠ SLO capacity** | Maximum processing rate may come with unacceptable queueing. |
| **Quantization ≠ automatic speedup** | Kernels, workload, and quality determine the realized benefit. |
| **Cost per successful task** | Total included costs across all attempts divided by successful tasks. |

A request-based **99.9%** success SLO over **1,000,000** eligible requests allows **1,000** failures. It does not specify downtime minutes unless the SLI is time-based.

Under stable conditions, **Little's Law: average in-flight work = arrival rate × average time in the system**. Use averages with consistent units, not p95 latency.

[Study production engineering](questions/production-engineering.md).

## A reusable interview answer structure

1. Define the concept and distinguish its closest alternative.
2. Explain the mechanism and assumptions.
3. Give two contrasting examples, including a failure case.
4. Name metrics with units and denominators.
5. Explain how you would validate the choice and what would change your mind.

Use mnemonics to retrieve the explanation, then state the limitations. They are memory aids, not universal decision rules.
