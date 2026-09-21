# GenAI Evaluation Questions and Answers

[Back to the README](../README.md) · [AI foundations](ai-foundations.md) · [RAG](rag.md) · [Prompt engineering](prompt-engineering.md)

These questions cover how to evaluate an entire application as well as its individual components. Use the examples to discuss experimental design and operational tradeoffs. Examples and proposed workflows are illustrative; metric definitions and grading conventions should be recorded explicitly for each project.

## Contents

- [Evaluation design](#evaluation-design): success criteria, datasets, and leakage.
- [Component and answer quality](#component-and-answer-quality): retrieval, grounding, and automated checks.
- [Judgment and experiments](#judgment-and-experiments): model judges, human review, and uncertainty.
- [Robustness and operations](#robustness-and-operations): adversarial tests, efficiency, and production monitoring.

## Evaluation design

### Question: 1. Why is a single benchmark score insufficient for a GenAI application?

**Topic:** Success criteria
**Difficulty:** Beginner

**Short answer:**
A benchmark captures particular tasks and conditions, while an application must meet several requirements on its own users, data, and workflows.

**Explanation:**
Measure task success alongside relevant constraints such as groundedness, format validity, safety, latency, and cost. Report important slices rather than only an average. As a release practice, define acceptance criteria before comparing systems so that gains on one dimension do not silently conceal unacceptable regressions elsewhere.

**Example:**
A support assistant may improve answer ratings while producing more invalid account actions; those outcomes need separate checks.

**Follow-up questions:**

- Which failures should block a release even when the average quality score improves?

**References:**

- [Liang et al.: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)

### Question: 2. What belongs in a useful evaluation dataset?

**Topic:** Test coverage
**Difficulty:** Intermediate

**Short answer:**
Include representative tasks, important edge cases, and known failure patterns, together with the evidence and grading criteria needed to judge each result.

**Explanation:**
Cover variations in language, input length, ambiguity, and answerability. For RAG, retain relevant evidence and corpus versions. Synthetic examples can fill gaps, but review them and compare with real usage. Keep targeted stress tests distinguishable from representative samples so their scores are not mistaken for production error rates.

**Example:**
A policy-assistant dataset includes routine questions, missing information, conflicting versions, and questions requiring an exception clause.

**Follow-up questions:**

- How would you identify coverage gaps when production traffic is still limited?

**References:**

- [Anthropic: Defining success criteria and evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)
- [Ribeiro et al.: Behavioral testing with CheckList](https://arxiv.org/abs/2005.04118)

### Question: 3. How do you prevent evaluation leakage while improving prompts and retrieval?

**Topic:** Experimental integrity
**Difficulty:** Intermediate

**Short answer:**
Separate development cases from held-out evaluation cases, and avoid choosing prompts, examples, or retrieval settings using the held-out answers.

**Explanation:**
Repeated tuning against the same test set makes it a development set. Split related questions or document families together when appropriate, and audit duplicates. In RAG, access to legitimate source documents is expected; exposing evaluation answer keys is different. Public benchmark results may also be affected by unknown pretraining contamination.

**Example:**
Paraphrases of the same question should not appear as few-shot demonstrations in development and as supposedly independent held-out tests.

**Follow-up questions:**

- What would you do with a test case after using its failure to redesign the prompt?

**References:**

- [scikit-learn: Leakage and evaluation pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)

## Component and answer quality

### Question: 4. How do precision@k, recall@k, MRR, and nDCG measure retrieval?

**Topic:** Retrieval metrics
**Difficulty:** Intermediate

**Short answer:**
They measure different properties of a ranked result list: relevance density, relevant-item coverage, the first relevant result's rank, and graded ranking quality.

**Explanation:**

| Metric | Meaning |
| --- | --- |
| Precision@k | Relevant items in the top k divided by k |
| Recall@k | Relevant items in the top k divided by all relevant items for the query |
| MRR | Mean reciprocal rank of the first relevant result; zero when none is found under the evaluation cutoff |
| nDCG@k | Discounted relevance gain through rank k, normalized by an ideal ranking |

Define document versus passage relevance, cutoffs, and conventions for queries with no relevant items. Incomplete relevance labels can distort scores. Retrieval metrics do not establish answer correctness.

**Example:**
With four relevant passages overall and relevant hits at ranks 2 and 5, precision@5 is 0.4, recall@5 is 0.5, and reciprocal rank is 0.5.

**Follow-up questions:**

- Why might recall matter more than the first relevant rank for a question requiring multiple sources?

**References:**

- [Manning, Raghavan, and Schütze: Ranked retrieval evaluation](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html)
- [TorchMetrics: Mean reciprocal rank implementation and documentation](https://github.com/Lightning-AI/torchmetrics/blob/master/src/torchmetrics/retrieval/reciprocal_rank.py)

### Question: 5. How do correctness, faithfulness, and citation quality differ?

**Topic:** Answer quality
**Difficulty:** Intermediate

**Short answer:**
Correctness asks whether the answer is right; faithfulness asks whether its claims are supported by the supplied context; citation quality asks whether the cited evidence supports and covers those claims.

**Explanation:**
A response can accurately repeat an outdated source and still be wrong today. Conversely, a correct answer may introduce claims absent from its context. Assess citation support separately from coverage of claims needing evidence. Define how partially supported claims and missing answers are scored.

**Example:**
An answer citing an old return policy is traceable, but may fail correctness against the policy effective on the user's purchase date.

**Follow-up questions:**

- How would you grade an answer that contains one correct claim and one unsupported qualification?

**References:**

- [Es et al.: Ragas](https://arxiv.org/abs/2309.15217)
- [Gao et al.: Evaluating text with citations](https://arxiv.org/abs/2305.14627)

### Question: 6. When should you use deterministic checks instead of semantic grading?

**Topic:** Automated evaluation
**Difficulty:** Beginner

**Short answer:**
Use deterministic checks for objectively testable requirements, and semantic or human judgment when acceptable answers vary in wording or require interpretation.

**Explanation:**
Schema validation, exact class labels, executable tests, and numeric tolerances provide reproducible checks. Exact string matching is often too strict for free-form answers; keyword matching can accept negated or irrelevant statements. Combine checks instead of equating valid formatting with successful completion.

**Example:**
For extracted invoice data, validate the schema, compare amounts within an explicit tolerance, and verify totals independently.

**Follow-up questions:**

- Why could an answer containing every reference keyword still be incorrect?

**References:**

- [Anthropic: Code-based, human, and model-based grading](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)

## Judgment and experiments

### Question: 7. What are the strengths and limitations of an LLM judge?

**Topic:** Model-based grading
**Difficulty:** Intermediate

**Short answer:**
An LLM judge can scale nuanced comparisons, but its judgments can be wrong, biased, or sensitive to presentation.

**Explanation:**
Use an explicit rubric, relevant evidence, and a fixed judge configuration. Validate agreement with human judgments on representative cases. Test answer-order effects in pairwise comparisons and avoid rewarding verbosity by accident. Treat candidate responses as untrusted input to the judge; a judge score is a measurement, not ground truth.

**Example:**
Grade the same answer pair in both orders and investigate inconsistent preferences.

**Follow-up questions:**

- Why might a judge favor an eloquent but unsupported answer?

**References:**

- [Zheng et al.: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685)

### Question: 8. How would you make human evaluation more consistent?

**Topic:** Human review
**Difficulty:** Intermediate

**Short answer:**
Give reviewers a clear rubric, examples, and the evidence needed to judge, then measure and investigate disagreement.

**Explanation:**
A practical review design hides system identity, randomizes answer order, and uses independent reviewers on an overlapping subset. Define partial credit and failure severity. Adjudicate disagreements and revise ambiguous criteria before treating aggregate ratings as reliable. Human judgment also has variability.

**Example:**
Reviewers disagree whether an omitted exception is minor; add an explicit criterion for omissions that change the answer.

**Follow-up questions:**

- When should a domain expert review cases rather than a general annotator?

**References:**

- [Zheng et al.: Human preferences and model-judge comparisons](https://arxiv.org/abs/2306.05685)

### Question: 9. How do you compare two systems when outputs and test scores vary?

**Topic:** Uncertainty and experiments
**Difficulty:** Advanced

**Short answer:**
Evaluate both systems on matched cases, repeat generation where needed, and report the size and uncertainty of the difference rather than only two averages.

**Explanation:**
Keep data, rubrics, and other settings fixed. A paired bootstrap can estimate uncertainty in score differences; resample at the independent unit, such as a conversation, instead of treating correlated turns as separate samples. Repeated generations reveal output variability, but are not new independent user cases. Review practical impact and important slices before declaring a winner.

**Example:**
A one-point average improvement with a wide interval spanning zero is inconclusive evidence of a reliable gain.

**Follow-up questions:**

- Why can repeatedly checking results and stopping when they look favorable bias a comparison?

**References:**

- [SciPy: Bootstrap confidence intervals and paired resampling](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html)

## Robustness and operations

### Question: 10. What should robustness and adversarial evaluations test?

**Topic:** Failure-oriented testing
**Difficulty:** Intermediate

**Short answer:**
Test benign variations and malicious inputs against explicit behavioral requirements, including the application's permissions and tool boundaries.

**Explanation:**
Include paraphrases, distractors, missing evidence, conflicting documents, and injections in retrieved text or tool results. Check unauthorized actions and data disclosure separately from answer quality. Test that valid requests still succeed so blanket refusal does not masquerade as robustness. Maintain known-failure regression cases alongside newly designed attacks.

**Example:**
Insert an instruction to reveal unrelated records into a retrieved document and verify that access controls still prevent disclosure.

**Follow-up questions:**

- Why does passing a fixed attack suite not prove that a system is secure?

**References:**

- [Ribeiro et al.: CheckList](https://arxiv.org/abs/2005.04118)
- [Greshake et al.: Indirect prompt injection](https://arxiv.org/abs/2302.12173)

### Question: 11. How should latency and cost be evaluated alongside quality?

**Topic:** Operational metrics
**Difficulty:** Intermediate

**Short answer:**
Measure complete task performance under representative load, including latency distributions, failures, and total cost per successful task.

**Explanation:**
Separate time to first token from completion time. Include retrieval, reranking, tool calls, retries, and validation; report median and tail latency. Compare cold and warm cache conditions deliberately. Efficiency improvements are useful only if the resulting system still meets quality requirements.

**Example:**
A faster model that requires frequent retries can have worse end-to-end latency and cost than a slower model that succeeds immediately.

**Follow-up questions:**

- Why can streaming improve the user experience without improving total completion time?

**References:**

- [Anthropic: Latency considerations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)
- [Liang et al.: Multi-metric evaluation with HELM](https://arxiv.org/abs/2211.09110)

### Question: 12. How do offline evaluation and production monitoring complement each other?

**Topic:** Continuous evaluation
**Difficulty:** Intermediate

**Short answer:**
Offline tests provide controlled comparisons before release. Production monitoring reveals real traffic patterns, operational failures, and changes that the test set may miss.

**Explanation:**
Track task outcomes, sampled quality judgments, errors, latency, and relevant input shifts. As a rollout design, compare versions on a limited traffic allocation with predefined stopping criteria. Feedback such as clicks or thumbs-up is a noisy proxy for correctness. Turn verified incidents into development and regression cases while maintaining a separate held-out assessment.

**Example:**
A corpus update introduces documents in a new format; monitoring detects missing citations even though the previous offline suite still passes.

**Follow-up questions:**

- What evidence would trigger rollback rather than another prompt change?

**References:**

- [Google: Monitoring production ML systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring)
