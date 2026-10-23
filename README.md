# GenAI and AI Engineering Interview Questions and Answers

![AI and GenAI: data points, a decision tree, and a neural network connected to generated text, code, and imagery.](assets/ai-genai-banner.png)

A growing collection of questions and answers for conducting and preparing for Generative AI (GenAI) and AI engineering interviews. This repository covers core concepts, implementation decisions, and the tradeoffs involved in building production AI systems.

## Target Audiences

- **Interviewers interviewing GenAI and AI engineers:** Use the question bank to plan interviews, assess technical understanding, and explore candidates' reasoning through practical examples and follow-up questions.
- **Engineers preparing for GenAI and AI interviews:** Use the answers and explanations to strengthen your knowledge, practice discussing engineering tradeoffs, and identify areas for further study.

## Question Bank

- [Foundational AI and machine learning questions](questions/ai-foundations.md): 33 questions covering traditional ML concepts, data preparation, training, common algorithms, evaluation, and production monitoring, with short answers, simple explanations and analogies, advanced technical answers, multiple examples, cheat sheets, follow-ups, and references.
- [Foundational GenAI and LLM questions](questions/genai-foundations.md): 23 questions covering core concepts, transformer architecture, training, inference, and limitations, with short answers, simple explanations and analogies, advanced technical answers, multiple examples, cheat sheets, follow-ups, and references.
- [Retrieval-augmented generation questions](questions/rag.md): 18 questions covering ingestion, chunking, search, reranking, grounding, access control, troubleshooting, and RAG architecture types.
- [Prompt engineering questions](questions/prompt-engineering.md): 12 questions covering instructions, examples, structured outputs, tool use, context, prompt injection, and iteration.
- [Agents and tool use questions](questions/agents.md): 13 questions covering execution loops, tool design, memory, retries, persistence, permissions, coordination, and evaluation.
- [Agent Orchestration questions](questions/agent-orchestration.md): 12 questions covering task decomposition, coordination patterns, scheduling, handoffs, shared state, recovery, budgets, and fleet evaluation.
- [Software Factory questions](questions/software-factory.md): 12 questions covering business intent, agent planning and coding, independent testing, integration, human review, deployment, monitoring, and delivery outcomes.
- [Fine-tuning questions](questions/fine-tuning.md): 13 questions covering training objectives, data preparation, PEFT, LoRA, QLoRA, preference optimization, evaluation, and deployment.
- [GenAI evaluation questions](questions/evaluation.md): 13 questions covering datasets, retrieval and answer metrics, model judges, human review, experiments, robustness, and production monitoring.
- [Production engineering questions](questions/production-engineering.md): 14 questions covering deployment, service objectives, inference performance, caching, overload, retries, releases, observability, security, and cost.

All question banks include **Short answers**, **Simple answer and analogy** sections, detailed **Advanced answer and AI/maths** sections, relevant **metrics and checks**, at least **two examples per question**, **Quick Cheat Sheets**, follow-up questions, and references. Numerical examples are illustrative, not benchmark results or universal targets. There are **163 questions** across ten banks. Selected answers also include original diagrams, plotted examples, two attributed video snapshots, and a user-supplied RAG types infographic, with supporting sources linked beside them.

## Definitions and Terminology

Use the [AI and GenAI Terminology Glossary](GLOSSARY.md) for **275 concise definitions and explanations** covering foundational ML, LLMs, RAG, prompting, fine-tuning, evaluation, agents, and production engineering. It expands acronyms and distinguishes terms with multiple meanings, such as bias, precision, rank, and checkpoint. Every question, design scenario, and notebook exercise includes **Key terms** links for quick lookup.

The glossary uses the supplied [Google ML Glossary](https://developers.google.com/machine-learning/glossary), [ML Cheatsheet glossary](https://ml-cheatsheet.readthedocs.io/en/latest/glossary.html), and [GeeksforGeeks terminology guide](https://www.geeksforgeeks.org/machine-learning/50-machine-learning-terms-explained/) as vocabulary references, with primary documentation and research papers for technical detail.

## Cheat Sheet

Use the [AI and GenAI Interview Cheat Sheet](CHEAT_SHEET.md) for cross-topic revision, key formulas, common pitfalls, and memory aids such as **“V” for o“V”erfitting**. Every question also includes a compact **Quick Cheat Sheet** beside its detailed answer. Start with recall, then use the advanced answer to explain assumptions, tradeoffs, and how to measure success.



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

## Courses

Use the [Courses section](courses/README.md) to collect useful courses for **interview preparation** and **refreshing key concepts**. Courses are organized by topic and can be linked to the question bank, coding exercises, and system design scenarios.

### LLM Engineering

1. [Prompt Engineering](courses/1-llm-engineering/1-prompt-engineering.md) — Prompt patterns, Python examples, and exercises.
2. [Structured Outputs](courses/1-llm-engineering/2-structured-outputs.md) — JSON Schema, validation, constrained decoding, and extraction pipelines.
3. [Embeddings](courses/1-llm-engineering/3-embeddings.md) — Vector representations, similarity metrics, chunking, retrieval, reranking, and a NumPy walkthrough.
4. [Context Engineering](courses/1-llm-engineering/4-context-engineering.md) — Context budgets, memory, retrieval, tool selection, and an offline Python assembly pipeline.
5. [RAG: Retrieval-Augmented Generation](courses/1-llm-engineering/5-rag-retrieval-augmented-generation.md) — Document retrieval, grounded prompts, an offline pipeline, and retrieval/answer evaluation.
6. [Function Calling and Tool Use](courses/1-llm-engineering/6-function-calling.md) — Tool schemas, validation, bounded execution loops, error handling, and MCP concepts.
7. [Evaluation and Testing](courses/1-llm-engineering/7-evaluation.md) — Datasets, rubrics, judge calibration, confidence intervals, regression comparisons, and eval costs.
8. [Caching, Rate Limiting, and Cost Optimization](courses/1-llm-engineering/8-caching-cost.md) — Prompt and response caches, model routing, token buckets, cost tracking, batching, and budget controls.
9. [Guardrails, Safety, and Content Filtering](courses/1-llm-engineering/9-guardrails.md) — Input/output validation, prompt injection, privacy, tool boundaries, monitoring, and red-team evaluation.
10. [Building a Production LLM Application](courses/1-llm-engineering/10-production-app.md) — Service architecture, prompt rollout, streaming, retries, observability, cost accounting, and deployment patterns.
11. [LLM Routing Layer — LiteLLM, OpenRouter, and Portkey](courses/1-llm-engineering/11-llm-routing-layer.md) — Model aliases, routing strategies, bounded failover, gateway tradeoffs, usage attribution, and MCP sampling.
12. [Shadow Traffic, Canary Rollouts, and Progressive Deployment](courses/1-llm-engineering/12-shadow-canary-progressive.md) — Shadow comparisons, rollout gates, sample sizes, cost tradeoffs, and tested rollback plans.
13. [Agent Framework Tradeoffs](courses/1-llm-engineering/13-agent-framework-tradeoffs.md) — LangGraph, CrewAI, AutoGen, Agno, Google ADK, Microsoft Agent Framework, and Pydantic AI; state, branching, recovery, and cost comparisons.

### Agent Engineering

1. [The Agent Loop: Observe, Think, Act](courses/2-agent-engineering/1-agent-loop.md) — ReAct, tool dispatch, observations, call IDs, stopping conditions, and a bounded offline Python loop.
2. [ReWOO and Plan-and-Execute](courses/2-agent-engineering/2-rewoo-plan-execute.md) — Decoupled planning, evidence dependencies, validated DAG execution, failure handling, and bounded replanning.
3. [Reflexion: Verbal Reinforcement Learning](courses/2-agent-engineering/3-reflexion-verbal-rl.md) — Actor, evaluator, self-reflector, episodic memory, bounded retries, and an offline Python demonstration.
4. [Tree of Thoughts and LATS](courses/2-agent-engineering/4-tree-of-thoughts-lats.md) — Branching search, MCTS, UCT, evaluation tradeoffs, and runnable offline BFS and MCTS examples.

To add a course, copy the [course template](courses/COURSE_TEMPLATE.md), record its origin, author, level, and what it is best for, then go straight into explanations and code examples. Add the course to the index.

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
## Question: [Interview question]

**Topic:** [Topic]
**Difficulty:** [Beginner / Intermediate / Advanced]

**Key terms:**
[Link the relevant entries in GLOSSARY.md; expand unfamiliar acronyms on first use.]

**Short answer:**
[Start with a crisp definition, then state the main distinction or use.]

**Simple answer and analogy:**

**In plain language:**
[Explain the answer for someone with no AI/ML background. Use familiar words and explain any essential technical term.]

**Analogy:**
[Use a concrete everyday situation, explicitly connect it to the concept, and note a limitation if the comparison could mislead.]

**Advanced answer and AI/maths:**
[Explain the mechanism, assumptions, practical decisions, and failure modes. Include relevant AI detail and mathematics with symbols defined; do not add formulas where they do not help.]

**Metrics and checks:**
[Define relevant metrics, formulas, units, denominators, and validation methods. Label numerical examples as illustrative; avoid universal targets.]

**Examples:**

**Example 1:**
[A practical scenario, calculation, code snippet, or design sketch.]

**Example 2:**
[A distinct scenario or failure case that reveals another tradeoff.]

**Visual (optional):**
[An original Mermaid diagram or accessible local image, with a caption and concept reference.]

**Quick Cheat Sheet:**

[Optional mnemonic that helps recall without replacing the technical definition.]

| Cue | Remember |
| --- | --- |
| [Key concept] | [Short definition, distinction, or useful check] |
| [Common pitfall] | [What to verify or avoid] |

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
7. Read the simple explanation and analogy for intuition, then the advanced answer for technical detail. Work through the examples and explain the metrics and engineering tradeoffs. Then use the [cheat sheet](CHEAT_SHEET.md) for recall practice.
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
- **− In progress:** Build the course collection for interview preparation and concept refreshers.
- [x] Organize the question bank into topic-specific Markdown files as it grows.

## Contributing

Add new questions, improve existing answers, or suggest missing topics. Follow the three layers: a crisp short answer, an accessible simple explanation with a concrete analogy, and an advanced answer with relevant technical detail or mathematics. Keep analogies accurate and do not assume prior AI/ML knowledge in the simple section. Include meaningful metrics or checks, at least two distinct examples where possible, and a quick cheat sheet. Define units and denominators, explain metric limitations, and distinguish illustrative numbers from measured results. Keep answers clear, technically accurate, and supported by reliable references. Define new technical terms in the [glossary](GLOSSARY.md), expand unfamiliar acronyms on first use, and add relevant Key terms links. Distinguish overloaded meanings rather than relying on context alone. Call out assumptions and distinguish general principles from behavior specific to a model or tool. For diagrams, include descriptive labels, a short explanation, and a primary source for the concept; label illustrative architectures as examples. Add alt text to images and `accTitle` / `accDescr` to Mermaid diagrams.

For course contributions, use the [course template](courses/COURSE_TEMPLATE.md) and link the most relevant interview practice.

## License

Original repository content is licensed under the [MIT License](LICENSE). The [identified third-party media](assets/third-party/README.md) are excluded from that license. You may use, copy, modify, and redistribute the original content for personal or commercial purposes, provided you retain the copyright and license notices. The content is provided without warranty. Linked third-party resources remain subject to their own licenses.

The imported [Prompt Engineering](courses/1-llm-engineering/1-prompt-engineering.md), [Structured Outputs](courses/1-llm-engineering/2-structured-outputs.md), [Embeddings](courses/1-llm-engineering/3-embeddings.md), [Context Engineering](courses/1-llm-engineering/4-context-engineering.md), [RAG](courses/1-llm-engineering/5-rag-retrieval-augmented-generation.md), [Function Calling](courses/1-llm-engineering/6-function-calling.md), [Evaluation](courses/1-llm-engineering/7-evaluation.md), [Caching and Cost](courses/1-llm-engineering/8-caching-cost.md), [Guardrails](courses/1-llm-engineering/9-guardrails.md), [Production App](courses/1-llm-engineering/10-production-app.md), [LLM Routing Layer](courses/1-llm-engineering/11-llm-routing-layer.md), [Shadow and Canary Deployment](courses/1-llm-engineering/12-shadow-canary-progressive.md), and [Agent Framework Tradeoffs](courses/1-llm-engineering/13-agent-framework-tradeoffs.md) lessons retain their upstream copyright and [MIT license notice](courses/licenses/ai-engineering-from-scratch-LICENSE).

The imported [Agent Loop](courses/2-agent-engineering/1-agent-loop.md), [ReWOO and Plan-and-Execute](courses/2-agent-engineering/2-rewoo-plan-execute.md), [Reflexion](courses/2-agent-engineering/3-reflexion-verbal-rl.md), and [Tree of Thoughts and LATS](courses/2-agent-engineering/4-tree-of-thoughts-lats.md) lessons also retain their upstream copyright and [MIT license notice](courses/licenses/ai-engineering-from-scratch-LICENSE).
