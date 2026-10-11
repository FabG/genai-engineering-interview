# Interview Resources and Coverage

[Back to the main README](../README.md)

The resources below helped identify interview topics to supplement. The repository contains original answers and teaching illustrations; primary documentation and research papers support the technical explanations beside each question. Interview collections are reading context, not evidence that an answer is universal or that a topic occurs with a particular frequency.

Access and coverage reviewed on **2026-10-11**. Question numbers below refer to this repository.

## Supplied reading

| Resource | Accessible material and use here | Related questions |
| --- | --- | --- |
| [GeeksforGeeks: Machine Learning Interview Questions and Answers](https://www.geeksforgeeks.org/machine-learning/machine-learning-interview-questions/) | Public article used to identify additional ML topics, including feature selection, missing data, oversampling, and density clustering. | [AI foundations Q24, Q28–30, Q33](../questions/ai-foundations.md#additional-ml-interview-topics) |
| [DataCamp: Top Machine Learning Interview Questions](https://www.datacamp.com/blog/top-machine-learning-interview-questions) | Public article used for coverage of time-based validation, feature importance, ROC analysis, regression checks, and transfer learning. Calibration and selective prediction provide related extensions. | [AI foundations Q23, Q25–27, Q31–32](../questions/ai-foundations.md#additional-ml-interview-topics); [evaluation Q13](../questions/evaluation.md#abstention-and-coverage) |
| [Towards AI: 40 Generative AI Interview Questions That Actually Get Asked in 2026](https://towardsai.com/p/machine-learning/40-generative-ai-interview-questions-that-actually-get-asked-in-2026-with-answers) | Public article used for coverage of checkpoint choice, hierarchical retrieval, graph retrieval, SQL, planning patterns, and speculative decoding. Rank fusion and embedding migration deepen the retrieval discussion. | [GenAI Q23](../questions/genai-foundations.md#model-families-and-checkpoint-choices); [RAG Q13–17](../questions/rag.md#advanced-retrieval-and-structured-data); [agents Q13](../questions/agents.md#planning-patterns); [production Q13](../questions/production-engineering.md#inference-optimization-scenarios) |
| [Sanjay Kumar PhD: Top 40 Generative AI Scenario-Based Interview Questions and Answers](https://skphd.medium.com/top-40-generative-ai-scenario-based-interview-questions-and-answers-2026-8626d946cf52) | **Public preview only:** the first context-limit/latency scenario was accessible. The remaining member-only questions were not reviewed or used. | [Production Q14](../questions/production-engineering.md#inference-optimization-scenarios) |
| [Simplilearn: Most Asked 30 Generative AI Interview Questions 2026](https://www.youtube.com/watch?v=j5FU7kOGrsU) | Public title, description, and selected preview frames were inspected. The automatic caption track did not return content; no full-transcript review is claimed. Two selected frames illustrate existing RAG and LoRA answers. | [RAG Q2](../questions/rag.md#architecture-and-data); [fine-tuning Q6](../questions/fine-tuning.md#adaptation-methods) |

## Video study prompts

The timestamps are approximate positions derived from the video’s public preview-frame interval. Open the video to inspect the full-resolution explanation.

| Position | What to inspect | Interview exercise |
| --- | --- | --- |
| [Near 20:00: RAG architecture](https://www.youtube.com/watch?v=j5FU7kOGrsU&t=1200s) | The distinction between indexing documents and answering a query. | Redraw both paths, then place permission checks, source versions, and citation validation. |
| [Near 26:00: LoRA](https://www.youtube.com/watch?v=j5FU7kOGrsU&t=1560s) | Full fine-tuning versus a small trainable update. | Derive the adapter parameter count and explain why training-memory savings do not imply the entire frozen base disappears. |

The broader model-family, MoE, distillation, and calibration questions are original extensions supported by their cited papers or documentation, rather than claims about unreviewed portions of these resources.

## Visual provenance

- [Original illustrations and editable sources](../assets/diagrams/README.md): synthetic data and schematic designs are explicitly labeled.
- [Third-party video frames](../assets/third-party/README.md): source, approximate timestamp, extraction details, and separate rights notice.

Use the external articles and video as additional practice. Compare their explanations with primary sources, especially for framework behavior, implementation-specific performance, and claims of guaranteed reliability.
