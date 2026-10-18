# Courses for Interview Preparation and Refreshers

[Back to the main README](../README.md) · [Terminology glossary](../GLOSSARY.md) · [Cheat sheet](../CHEAT_SHEET.md)

A growing collection of courses for preparing for AI and GenAI engineering interviews or refreshing key concepts. Each course identifies its origin, author, level, and best use, then goes straight into explanations and practical examples.

**11 courses available.** Start with [Prompt Engineering](llm-engineering/1-prompt-engineering.md), or use the [course template](COURSE_TEMPLATE.md) to add another course.

## Add a course

1. Copy [COURSE_TEMPLATE.md](COURSE_TEMPLATE.md) into this directory with a descriptive filename, such as `machine-learning-refresher.md`.
2. Fill in the origin, author, level, and what the course is best for. Follow the metadata with explanations, code examples, and useful exercises. When importing content, check its license and preserve attribution and required notices.
3. Add a link under the relevant category below.

Example index entry, to adapt after creating the course file:

```markdown
- [Course title](machine-learning-refresher.md) — Provider · Beginner · Refresher. Covers data splits, overfitting, and evaluation metrics.
```

## AI and Machine Learning Foundations

Courses on data preparation, supervised and unsupervised learning, traditional models, training, and evaluation.

**Practice alongside:** [AI foundations](../questions/ai-foundations.md) and [ML notebook exercises](../hands-on/README.md).

## GenAI and LLM Foundations

Courses on tokens, embeddings, Transformers, attention, language-model training, and generation.

**Practice alongside:** [GenAI and LLM foundations](../questions/genai-foundations.md).

## LLM Engineering

1. [Prompt Engineering — AI Engineering from Scratch](llm-engineering/1-prompt-engineering.md) — Intermediate (our assessment) · Interview preparation and refresher · Explanations, ten prompt patterns, and a Python testing-harness walkthrough.
2. [Structured Outputs — AI Engineering from Scratch](llm-engineering/2-structured-outputs.md) — Intermediate · JSON Schema, Pydantic, constrained decoding, validation, retries, and extraction evaluation.
3. [Embeddings](llm-engineering/3-embeddings.md) — Vector representations, similarity metrics, chunking, retrieval, reranking, and a NumPy walkthrough.
4. [Context Engineering](llm-engineering/4-context-engineering.md) — Context budgets, memory, retrieval, tool selection, and an offline Python assembly pipeline.
5. [RAG: Retrieval-Augmented Generation](llm-engineering/5-rag-retrieval-augmented-generation.md) — Document retrieval, grounded prompts, an offline pipeline, and retrieval/answer evaluation.
6. [Function Calling and Tool Use](llm-engineering/6-function-calling.md) — Tool schemas, validation, bounded execution loops, error handling, and MCP concepts.
7. [Evaluation and Testing](llm-engineering/7-evaluation.md) — Datasets, rubrics, judge calibration, confidence intervals, regression comparisons, and eval costs.
8. [Caching, Rate Limiting, and Cost Optimization](llm-engineering/8-caching-cost.md) — Prompt and response caches, model routing, token buckets, cost tracking, batching, and budget controls.
9. [Guardrails, Safety, and Content Filtering](llm-engineering/9-guardrails.md) — Input/output validation, prompt injection, privacy, tool boundaries, monitoring, and red-team evaluation.
10. [Building a Production LLM Application](llm-engineering/10-production-app.md) — Service architecture, prompt rollout, streaming, retries, observability, cost accounting, and deployment patterns.
11. [LLM Routing Layer — LiteLLM, OpenRouter, and Portkey](llm-engineering/11-llm-routing-layer.md) — Model aliases, routing strategies, bounded failover, gateway tradeoffs, usage attribution, and MCP sampling.

Courses on prompt design, structured outputs, embeddings, retrieval, and building reliable LLM applications.

**Practice alongside:** [RAG](../questions/rag.md), [prompt engineering](../questions/prompt-engineering.md), and [retrieval exercises](../hands-on/README.md).

## Agents and Orchestration

Courses on tool use, planning, state, memory, durable execution, permissions, and coordination.

**Practice alongside:** [Agents](../questions/agents.md), [agent orchestration](../questions/agent-orchestration.md), and [software factories](../questions/software-factory.md).

## Fine-Tuning and Evaluation

Courses on training data, supervised fine-tuning, adapters, preference optimization, quality metrics, and experiments.

**Practice alongside:** [Fine-tuning](../questions/fine-tuning.md) and [evaluation](../questions/evaluation.md).

## Production Engineering and System Design

Courses on model serving, reliability, latency, cost, observability, security, and architecture tradeoffs.

**Practice alongside:** [Production engineering](../questions/production-engineering.md) and [system design scenarios](../system-design/README.md).

## Turn a course into interview practice

- **Before studying:** Try the related questions aloud and identify the concepts you cannot explain yet.
- **For a refresher:** Focus on the modules addressing those gaps, then revisit the questions without notes.
- **For interview preparation:** Explain the concept simply, give an example, discuss a failure case, and name how you would measure success.
- **For practical reinforcement:** Complete a relevant notebook exercise or work through a design scenario. Record your own reasoning rather than only collecting a completion certificate.
