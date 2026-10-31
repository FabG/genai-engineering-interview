# Courses for Interview Preparation and Refreshers

[Back to the main README](../README.md) · [Terminology glossary](../GLOSSARY.md) · [Cheat sheet](../CHEAT_SHEET.md)

A growing collection of courses for preparing for AI and GenAI engineering interviews or refreshing key concepts. Each course goes straight into explanations and practical examples, with its origin, author, level, and best use listed in a Resource section near the bottom.

**30 courses available.** Start with [Prompt Engineering](1-llm-engineering/1-prompt-engineering.md), or use the [course template](COURSE_TEMPLATE.md) to add another course.

## Add a course

1. Copy [COURSE_TEMPLATE.md](COURSE_TEMPLATE.md) into this directory with a descriptive filename, such as `machine-learning-refresher.md`.
2. Start with explanations, code examples, and useful exercises. Fill in the Resource section near the bottom with the origin, author, level, and what the course is best for. When importing content, check its license and preserve attribution and required notices in the Resource section.
3. Preserve useful source prose and diagrams, blending them into the explanations rather than rewriting everything. Use course-level attribution and license notices without repeating captions under every diagram, unless an asset requires separate credit. Avoid duplicate visuals; link interactive figures that cannot render in Markdown.
4. Add a link under the relevant category below.

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

1. [Prompt Engineering — AI Engineering from Scratch](1-llm-engineering/1-prompt-engineering.md) — Intermediate (our assessment) · Interview preparation and refresher · Explanations, ten prompt patterns, and a Python testing-harness walkthrough.
2. [Structured Outputs — AI Engineering from Scratch](1-llm-engineering/2-structured-outputs.md) — Intermediate · JSON Schema, Pydantic, constrained decoding, validation, retries, and extraction evaluation.
3. [Embeddings](1-llm-engineering/3-embeddings.md) — Vector representations, similarity metrics, chunking, retrieval, reranking, and a NumPy walkthrough.
4. [Context Engineering](1-llm-engineering/4-context-engineering.md) — Context budgets, memory, retrieval, tool selection, and an offline Python assembly pipeline.
5. [RAG: Retrieval-Augmented Generation](1-llm-engineering/5-rag-retrieval-augmented-generation.md) — Document retrieval, grounded prompts, an offline pipeline, and retrieval/answer evaluation.
6. [Function Calling and Tool Use](1-llm-engineering/6-function-calling.md) — Tool schemas, validation, bounded execution loops, error handling, and MCP concepts.
7. [Evaluation and Testing](1-llm-engineering/7-evaluation.md) — Datasets, rubrics, judge calibration, confidence intervals, regression comparisons, and eval costs.
8. [Caching, Rate Limiting, and Cost Optimization](1-llm-engineering/8-caching-cost.md) — Prompt and response caches, model routing, token buckets, cost tracking, batching, and budget controls.
9. [Guardrails, Safety, and Content Filtering](1-llm-engineering/9-guardrails.md) — Input/output validation, prompt injection, privacy, tool boundaries, monitoring, and red-team evaluation.
10. [Building a Production LLM Application](1-llm-engineering/10-production-app.md) — Service architecture, prompt rollout, streaming, retries, observability, cost accounting, and deployment patterns.
11. [LLM Routing Layer — LiteLLM, OpenRouter, and Portkey](1-llm-engineering/11-llm-routing-layer.md) — Model aliases, routing strategies, bounded failover, gateway tradeoffs, usage attribution, and MCP sampling.
12. [Shadow Traffic, Canary Rollouts, and Progressive Deployment](1-llm-engineering/12-shadow-canary-progressive.md) — Shadow comparisons, rollout gates, sample sizes, cost tradeoffs, and tested rollback plans.
13. [Agent Framework Tradeoffs](1-llm-engineering/13-agent-framework-tradeoffs.md) — LangGraph, CrewAI, AutoGen, Agno, Google ADK, Microsoft Agent Framework, and Pydantic AI; state, branching, recovery, and cost comparisons.

Courses on prompt design, structured outputs, embeddings, retrieval, and building reliable LLM applications.

**Practice alongside:** [RAG](../questions/rag.md), [prompt engineering](../questions/prompt-engineering.md), and [retrieval exercises](../hands-on/README.md).

## Agent Engineering

1. [The Agent Loop: Observe, Think, Act](2-agent-engineering/1-agent-loop.md) — ReAct, tool dispatch, observations, call IDs, stopping conditions, and a bounded offline Python loop.
2. [ReWOO and Plan-and-Execute](2-agent-engineering/2-rewoo-plan-execute.md) — Decoupled planning, evidence dependencies, validated DAG execution, failure handling, and bounded replanning.
3. [Reflexion: Verbal Reinforcement Learning](2-agent-engineering/3-reflexion-verbal-rl.md) — Actor, evaluator, self-reflector, episodic memory, bounded retries, and an offline Python demonstration.
4. [Tree of Thoughts and LATS](2-agent-engineering/4-tree-of-thoughts-lats.md) — Branching search, MCTS, UCT, evaluation tradeoffs, and runnable offline BFS and MCTS examples.
5. [Self-Refine and CRITIC](2-agent-engineering/5-self-refine-and-critic.md) — Iterative revision, tool-grounded critique, stopping policies, evaluation metrics, and an offline Python example.
6. [Anthropic Workflow Patterns](2-agent-engineering/6-anthropic-workflow-patterns.md) — Chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, and runnable offline examples.
7. [LangGraph Stateful Graphs](2-agent-engineering/7-langgraph-stateful-graphs.md) — Typed state, reducers, checkpoints, approval interrupts, recovery, and a runnable SQLite example.
8. [AutoGen and the Actor Model](2-agent-engineering/8-autogen-actor-model.md) — Async messages, typed runtimes, bounded mailboxes, failure isolation, and an offline two-actor demonstration.
9. [CrewAI Role-Based Crews](2-agent-engineering/9-crewai-role-based-crews.md) — Agents, tasks, sequential and hierarchical processes, Flows, structured handoffs, memory, and an offline three-role crew.
10. [OpenAI Agents SDK](2-agent-engineering/10-openai-agents-sdk.md) — Handoffs, guardrails, sessions, tracing, ownership boundaries, and a bounded offline runtime.
11. [Claude Agent SDK](2-agent-engineering/11-claude-agent-sdk.md) — Harness design, isolated worker contexts, hooks, session persistence, tracing, and an offline SQLite example.
12. [Agno and Mastra Runtimes](2-agent-engineering/12-agno-and-mastra-runtimes.md) — Python and TypeScript runtime tradeoffs, typed workflows, streaming, persistence, and performance measurement.

Courses on tool use, planning, state, memory, durable execution, permissions, and coordination.

**Practice alongside:** [Agents](../questions/agents.md), [agent orchestration](../questions/agent-orchestration.md), and [software factories](../questions/software-factory.md).

## Multi-Agent and Swarms

1. [Why Multi-Agent?](3-multi-agent-and-swarms/1-why-multi-agent.md) — Decomposition, context boundaries, coordination patterns, message contracts, and when a single agent is enough.
2. [Communication Protocols](3-multi-agent-and-swarms/2-communication-protocols.md) — MCP, A2A, agent discovery, task lifecycles, identity, audit trails, and reliable handoffs.
3. [The Multi-Agent Primitive Model](3-multi-agent-and-swarms/3-primitive-model.md) — Agents, handoffs, shared state, orchestrators, and framework tradeoffs with a runnable Python example.
4. [Supervisor / Orchestrator-Worker Pattern](3-multi-agent-and-swarms/4-supervisor-orchestrator-pattern.md) — Scoped delegation, parallel workers, synthesis, deadlines, partial failures, and production tradeoffs.
5. [Role Specialization](3-multi-agent-and-swarms/5-role-specialization.md) — Planner, executor, critic, and verifier contracts; independent checks, bounded revisions, and quality metrics.

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
