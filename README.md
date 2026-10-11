# GenAI and AI Engineering Interview Questions and Answers

![AI and GenAI: data points, a decision tree, and a neural network connected to generated text, code, and imagery.](assets/ai-genai-banner.png)

A growing collection of questions and answers for conducting and preparing for Generative AI (GenAI) and AI engineering interviews. This repository covers core concepts, implementation decisions, and the tradeoffs involved in building production AI systems.

## Target Audiences

- **Interviewers interviewing GenAI and AI engineers:** Use the question bank to plan interviews, assess technical understanding, and explore candidates' reasoning through practical examples and follow-up questions.
- **Engineers preparing for GenAI and AI interviews:** Use the answers and explanations to strengthen your knowledge, practice discussing engineering tradeoffs, and identify areas for further study.

## Question Bank

- [Foundational AI and machine learning questions](questions/ai-foundations.md): 33 questions covering traditional ML concepts, data preparation, training, common algorithms, evaluation, and production monitoring, with short answers, explanations, examples, follow-ups, and references.
- [Foundational GenAI and LLM questions](questions/genai-foundations.md): 23 questions covering core concepts, transformer architecture, training, inference, and limitations, with short answers, explanations, examples, follow-ups, and references.
- [Retrieval-augmented generation questions](questions/rag.md): 17 questions covering ingestion, chunking, search, reranking, grounding, access control, and troubleshooting.
- [Prompt engineering questions](questions/prompt-engineering.md): 12 questions covering instructions, examples, structured outputs, tool use, context, prompt injection, and iteration.
- [Agents and tool use questions](questions/agents.md): 13 questions covering execution loops, tool design, memory, retries, persistence, permissions, coordination, and evaluation.
- [Agent Orchestration questions](questions/agent-orchestration.md): 12 questions covering task decomposition, coordination patterns, scheduling, handoffs, shared state, recovery, budgets, and fleet evaluation.
- [Software Factory questions](questions/software-factory.md): 12 questions covering business intent, agent planning and coding, independent testing, integration, human review, deployment, monitoring, and delivery outcomes.
- [Fine-tuning questions](questions/fine-tuning.md): 13 questions covering training objectives, data preparation, PEFT, LoRA, QLoRA, preference optimization, evaluation, and deployment.
- [GenAI evaluation questions](questions/evaluation.md): 13 questions covering datasets, retrieval and answer metrics, model judges, human review, experiments, robustness, and production monitoring.
- [Production engineering questions](questions/production-engineering.md): 14 questions covering deployment, service objectives, inference performance, caching, overload, retries, releases, observability, security, and cost.

All question banks include short answers, explanations, practical examples, follow-up questions, and references. There are **162 questions** across ten banks. Selected answers also include original diagrams, plotted examples, and two attributed video snapshots, with supporting sources linked beside them.

## Visual Study Guide

Use these visuals to practice explaining a system or concept before reading the full answer:

| Topic | Visuals to study |
| --- | --- |
| [AI foundations](questions/ai-foundations.md#data-and-validation) | Preprocessing (Q6); generalization (Q8); ensembles (Q14); PCA (Q18); confusion matrix (Q19); visual examples for Q23–33 |
| [LLM foundations](questions/genai-foundations.md#transformer-architecture) | Attention and causal mask (Q6); shifted targets (Q9); sampling (Q16); caching (Q17); model families and checkpoints (Q21–23) |
| [RAG](questions/rag.md#architecture-and-data) | Architecture and video snapshot (Q2); chunking (Q3); hybrid retrieval (Q5); hierarchical, graph, SQL, and migration examples (Q13–17) |
| [Prompt engineering](questions/prompt-engineering.md#outputs-and-workflows) | Output validation (Q4); data and authority boundaries (Q10) |
| [Agents](questions/agents.md#architecture-and-tools) | Tool-use loop (Q2); recovery after an ambiguous write (Q7) |
| [Agent orchestration](questions/agent-orchestration.md#architecture-and-decomposition) | Parallel task graph (Q3); durable state (Q7) |
| [Software factory](questions/software-factory.md#implementation-and-verification) | Integration queue (Q6); release provenance (Q8) |
| [Fine-tuning](questions/fine-tuning.md#goals-and-training-data) | Training objectives (Q2); LoRA diagram and video snapshot (Q6); distillation (Q13) |
| [Evaluation](questions/evaluation.md#component-and-answer-quality) | Ranked retrieval (Q4); correctness and grounding (Q5); judges (Q7); online checks (Q12); risk–coverage plot (Q13) |
| [Production engineering](questions/production-engineering.md#reliability-and-releases) | Overload control (Q7); releases (Q9); speculative decoding (Q13); latency diagnosis (Q14) |

Diagrams use [Mermaid, which GitHub renders directly](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams). In other Markdown viewers, enable Mermaid support to see the diagrams. The [SVG illustrations](assets/diagrams/README.md) also open independently. Visuals simplify the concepts; the surrounding answers describe assumptions and limitations. The new visual supplement adds 32 original SVG illustrations across 32 answers, plus two attributed video preview frames. See the [resource and coverage guide](resources/README.md) for the supplied reading, primary-source approach, and video study prompts.

## System Design Scenarios

[Practice six system design scenarios](system-design/README.md), each with a problem brief, workload assumptions, design tasks, an expandable reference design, and interviewer follow-ups:

1. Permission-aware knowledge assistant.
2. Support agent with controlled actions.
3. Document extraction and review pipeline.
4. Multi-tenant inference gateway.
5. Evaluation and release platform.
6. Autonomous software factory.

## Hands-on Python Exercises

[Start the hands-on section](hands-on/README.md) for eight notebook exercises across four areas: ML data and metrics, retrieval and RAG, evaluation and validation, and production utilities.

- [Questions notebook](hands-on/questions.ipynb): exercise contracts, implementation stubs, sample data, and checks.
- [Answers notebook](hands-on/answers.ipynb): matching reference implementations, checks, and explanations.

The exercises use Python 3.10+ and the standard library, with embedded data and no API keys or model downloads. The hands-on guide explains notebook setup and how to work through the exercises.

## Topics to Cover

- **AI and machine learning foundations:** Learning paradigms, data preparation, generalization, traditional algorithms, evaluation metrics, and production monitoring.
- **GenAI foundations:** Generative models, neural networks, transformers, tokenization, and attention.
- **Large language models:** Pretraining, inference, context windows, sampling, and model selection.
- **Prompt engineering:** Instruction design, few-shot examples, structured outputs, and prompt testing.
- **Retrieval-augmented generation (RAG):** Embeddings, chunking, vector search, reranking, and grounding.
- **Fine-tuning:** Supervised fine-tuning, parameter-efficient methods, and preference optimization.
- **Agents and tool use:** Function calling, workflow orchestration, memory, and failure handling.
- **Agent Orchestration:** Task graphs, worker fleets, coordination, durable execution, resource budgets, and evaluation.
- **Software Factory:** End-to-end software development by autonomous agents, with engineers defining business intent and reviewing results across planning, coding, testing, release, and monitoring.
- **Evaluation and safety:** Quality metrics, hallucinations, prompt injection, privacy, and guardrails.
- **Production engineering:** Deployment, service objectives, batching, quantization, caching, overload handling, releases, observability, security, and cost.
- **Multimodal AI:** Working with text, images, audio, and video.
- **System design:** Architecture scenarios, capacity estimates, failure handling, and design tradeoffs.
- **Hands-on Python:** Notebook exercises for data preparation, retrieval, evaluation, validation, retries, and caching.

## Question and Answer Format

Use this template when adding a question:

```markdown
### Question: [Interview question]

**Topic:** [Topic]
**Difficulty:** [Beginner / Intermediate / Advanced]

**Short answer:**
[A concise answer suitable for an interview.]

**Explanation:**
[How it works, when to use it, and key tradeoffs or limitations.]

**Example:**
[A practical scenario, code snippet, or design sketch, where helpful.]

**Visual (optional):**
[An original Mermaid diagram or accessible local image, with a caption and concept reference.]

**Follow-up questions:**
- [A question that explores the topic more deeply.]

**References:**
- [Link to relevant documentation, a paper, or another reliable source.]
```

## How to Use This Repository

### For Interviewers

1. Select topics and difficulty levels relevant to the role.
2. Use the questions to assess understanding and practical experience.
3. Ask follow-up questions to explore assumptions, design choices, and tradeoffs.
4. Treat the answers as reference points, allowing for alternative approaches supported by sound reasoning.
5. Use the [system design scenarios](system-design/README.md) for architecture discussions and the [questions notebook](hands-on/questions.ipynb) for coding exercises; the [answers notebook](hands-on/answers.ipynb) provides reference solutions.

### For Engineers Preparing for Interviews

1. Study one topic at a time, starting with [AI and machine learning foundations](questions/ai-foundations.md), then [GenAI and LLM foundations](questions/genai-foundations.md).
2. Continue with [RAG](questions/rag.md) and [prompt engineering](questions/prompt-engineering.md) to practice application design.
3. Explore [agents](questions/agents.md), [Agent Orchestration](questions/agent-orchestration.md), and [fine-tuning](questions/fine-tuning.md), using [evaluation](questions/evaluation.md) to assess the resulting systems.
4. Study [production engineering](questions/production-engineering.md) to connect model behavior with deployment, reliability, and operational constraints.
5. Study the [Software Factory questions](questions/software-factory.md), then attempt the [system design scenarios](system-design/README.md) before expanding their reference designs. Implement exercises in the [questions notebook](hands-on/questions.ipynb) before opening the answers.
6. Try answering each question aloud before reading the answer.
7. Practice explaining both the concept and its engineering tradeoffs.
8. Revisit weak areas and add questions from mock or real interviews.
9. Update answers and references as tools and practices evolve.

## Initial Roadmap

- [x] Add foundational AI and traditional machine learning questions and answers.
- [x] Add foundational GenAI and LLM questions and answers.
- [x] Expand into RAG, prompt engineering, and evaluation.
- [x] Add agents and fine-tuning topics.
- [x] Add production engineering topics.
- [x] Add Agent Orchestration and Software Factory questions and answers.
- **− In progress:** Expand system design scenarios (6 available; more planned).
- **− In progress:** Expand hands-on Python coding exercises with question and answer notebooks (8 available; more planned).
- [x] Organize the question bank into topic-specific Markdown files as it grows.

## Contributing

Add new questions, improve existing explanations, or suggest missing topics. Keep answers clear, technically accurate, and supported by reliable references. Call out assumptions and distinguish general principles from behavior specific to a model or tool. For diagrams, include descriptive labels, a short explanation, and a primary source for the concept; label illustrative architectures as examples. Add alt text to images and `accTitle` / `accDescr` to Mermaid diagrams.

## License

Original repository content is licensed under the [MIT License](LICENSE). The [identified third-party video frames](assets/third-party/README.md) are excluded from that license. You may use, copy, modify, and redistribute the original content for personal or commercial purposes, provided you retain the copyright and license notices. The content is provided without warranty. Linked third-party resources remain subject to their own licenses.
