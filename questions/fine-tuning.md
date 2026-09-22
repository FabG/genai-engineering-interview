# Fine-Tuning Questions and Answers

[Back to the README](../README.md) · [GenAI foundations](genai-foundations.md) · [RAG](rag.md) · [Agents](agents.md) · [Evaluation](evaluation.md)

These questions cover adapting pretrained language models, from choosing an objective to evaluating and deploying the result. Examples are illustrative. Training formats, supported methods, and deployment behavior depend on the model and framework; avoid treating example settings as universal defaults.

## Contents

- [Goals and training data](#goals-and-training-data): when to fine-tune, objectives, curation, and loss masking.
- [Adaptation methods](#adaptation-methods): full fine-tuning, PEFT, LoRA, and QLoRA.
- [Training and preferences](#training-and-preferences): configuration, generalization, and preference optimization.
- [Evaluation and delivery](#evaluation-and-delivery): comparisons, checkpoints, and deployment.

## Goals and training data

### Question: 1. When should you fine-tune instead of improving prompts or using RAG?

**Topic:** Adaptation choices
**Difficulty:** Beginner

**Short answer:**
Consider fine-tuning when a pretrained model has a repeatable task or behavior gap and representative training examples are available. First establish prompt and retrieval baselines.

**Explanation:**
Fine-tuning updates learned parameters; prompting supplies instructions and examples at inference, while RAG supplies external evidence. As a design guideline, use retrieval for changing facts and fine-tuning for durable task patterns or response behavior. They can work together. Training introduces data, compute, evaluation, and maintenance costs, so require measurable benefits.

**Example:**
Fine-tune consistent support-ticket extraction while retrieving the current product policy when answering factual questions.

**Follow-up questions:**

- What failure analysis would show that a problem comes from missing evidence rather than model behavior?

**References:**

- [Hugging Face: Fine-tuning pretrained models](https://huggingface.co/docs/transformers/training)

### Question: 2. How do continued pretraining, SFT, and preference optimization differ?

**Topic:** Training objectives
**Difficulty:** Intermediate

**Short answer:**
Continued pretraining learns from additional domain text, supervised fine-tuning (SFT) learns desired responses, and preference optimization learns from comparisons or reward signals.

**Explanation:**

| Approach | Typical signal | Intended adaptation |
| --- | --- | --- |
| Continued pretraining | Token prediction on domain text | Domain language and patterns |
| SFT | Demonstrations of desired outputs | Task execution and instruction following |
| Preference optimization | Preferred versus dispreferred responses, or rewards | Relative response quality |

These stages can be combined, but each requires evaluation. Domain exposure alone does not guarantee reliable instruction following or factual recall.

**Example:**
Adapt to a technical corpus, train on support answers, then refine responses using quality comparisons.

**Follow-up questions:**

- Why might training on raw manuals fail to teach the desired support-answer format?

**References:**

- [Gururangan et al.: Don't Stop Pretraining](https://arxiv.org/abs/2004.10964)
- [Hugging Face: SFT Trainer](https://huggingface.co/docs/trl/sft_trainer)
- [Rafailov et al.: Direct Preference Optimization](https://arxiv.org/abs/2305.18290)

### Question: 3. What makes a good fine-tuning dataset?

**Topic:** Data quality
**Difficulty:** Beginner

**Short answer:**
It should contain correct, consistent examples of the intended behavior across representative tasks and important edge cases.

**Explanation:**
Inspect examples before scaling data volume. Deduplicate related records, resolve conflicting demonstrations, and include realistic missing-information cases. Split related examples together to reduce leakage, and keep held-out evaluation separate from training and selection. Review sensitive content and provenance before use. Synthetic examples need validation because generated mistakes can become training targets.

**Example:**
A routing dataset includes ambiguous tickets with an escalation label instead of forcing every ticket into a confident but incorrect category.

**Follow-up questions:**

- Why might adding thousands of repetitive examples hurt coverage rather than improve it?

**References:**

- [Hugging Face: Supervised fine-tuning and data preparation](https://huggingface.co/learn/llm-course/en/chapter11/3)

### Question: 4. Why do chat formatting, loss masking, and truncation matter in SFT?

**Topic:** Training examples
**Difficulty:** Intermediate

**Short answer:**
Formatting defines the conversation structure, loss masking selects which tokens are training targets, and truncation determines which content survives preprocessing.

**Explanation:**
Use the model's expected chat template and inspect tokenized examples. Assistant-only loss can exclude user and system tokens as targets while retaining them as input context; it is different from attention masking. Check padding, end markers, and whether truncation removes answers. Packing can improve utilization, but inspect example boundaries and attention behavior in the chosen implementation.

**Example:**
A long prompt consumes the entire sequence limit, leaving no assistant target tokens and therefore no useful supervised response signal.

**Follow-up questions:**

- How would you verify that the loss is computed on the intended assistant tokens?

**References:**

- [Hugging Face: SFT formats, masking, and packing](https://huggingface.co/docs/trl/sft_trainer)

## Adaptation methods

### Question: 5. How does full fine-tuning compare with parameter-efficient fine-tuning?

**Topic:** PEFT
**Difficulty:** Beginner

**Short answer:**
Full fine-tuning updates all model parameters. Parameter-efficient fine-tuning (PEFT) updates a smaller subset or added parameters while freezing most of the pretrained model.

**Explanation:**
PEFT can reduce trainable-parameter memory, optimizer state, and the size of task-specific artifacts. It does not eliminate the cost of loading and computing through the base model. Quality depends on the task and adaptation capacity; full fine-tuning is not automatically better, and PEFT is not automatically sufficient.

**Example:**
Maintain separate small adapters for two extraction tasks while reusing one compatible base model.

**Follow-up questions:**

- Why can activation memory still be large even when very few parameters are trainable?

**References:**

- [Hugging Face: PEFT overview](https://huggingface.co/docs/peft/index)

### Question: 6. How does LoRA work, and what does its rank control?

**Topic:** Low-rank adaptation
**Difficulty:** Intermediate

**Short answer:**
LoRA freezes an original weight matrix and learns an additive update represented by two smaller matrices. The rank limits the update's capacity.

**Explanation:**
For a weight `W` of shape `d_out × d_in`, standard LoRA uses `W + (alpha / r)BA`, with `A` shaped `r × d_in` and `B` shaped `d_out × r`. The update has `r(d_in + d_out)` parameters. Rank, scaling, and target layers affect quality and cost; higher rank is not a guaranteed improvement.

**Example:**
For a `4096 × 4096` weight and rank 8, the two adapter matrices contain 65,536 parameters rather than 16,777,216 in the original weight.

**Follow-up questions:**

- Why might adapting more layers matter as much as increasing rank?

**References:**

- [Hu et al.: LoRA](https://arxiv.org/abs/2106.09685)

### Question: 7. How does QLoRA differ from LoRA and ordinary quantization?

**Topic:** Memory-efficient adaptation
**Difficulty:** Intermediate

**Short answer:**
QLoRA trains low-rank adapters through a frozen quantized base model. Quantization alone changes numerical representation; it does not teach new task behavior.

**Explanation:**
The original QLoRA method uses a 4-bit base representation, including NF4, with additional memory-saving techniques. Gradients flow through computations involving the frozen base into trainable adapters. This does not mean all arithmetic, activations, or trainable weights are 4-bit. Hardware and kernels affect speed, and reduced weight storage does not guarantee lower latency.

**Example:**
Use a quantized base to make adapter training fit in memory, then evaluate the actual serving configuration before deployment.

**Follow-up questions:**

- Why could a quantized training run still run out of memory on long examples?

**References:**

- [Dettmers et al.: QLoRA](https://arxiv.org/abs/2305.14314)

## Training and preferences

### Question: 8. Which training settings and memory tradeoffs should you understand?

**Topic:** Training configuration
**Difficulty:** Intermediate

**Short answer:**
Understand learning rate, training duration, effective batch size, sequence length, precision, and checkpointing, then tune them against validation results and hardware limits.

**Explanation:**
In ordinary data-parallel training, effective batch size is per-device batch size times device count times gradient-accumulation steps. Accumulation enables more examples per optimizer update without a larger microbatch. Activation checkpointing reduces stored activations by recomputing them during backward passes. These techniques trade memory against runtime; they do not replace data quality or validation.

**Example:**
A microbatch of 2 on 4 devices with 8 accumulation steps yields 64 examples per update, assuming full batches. Token counts can still vary.

**Follow-up questions:**

- Why might reducing sequence length fit memory but damage the target task?

**References:**

- [Hugging Face: Trainer configuration](https://huggingface.co/docs/transformers/main_classes/trainer)

### Question: 9. How do overfitting and catastrophic forgetting differ?

**Topic:** Generalization and regression
**Difficulty:** Intermediate

**Short answer:**
Overfitting means adapting too closely to training examples and generalizing poorly. Catastrophic forgetting means losing previously useful capabilities while learning new behavior.

**Explanation:**
A lower training loss can coexist with either problem. Track held-out task performance and regression tests for capabilities that must remain intact. As mitigation experiments, adjust training duration, learning rate, data diversity, or mixtures of old and new tasks. Neither freezing the base through adapters nor early stopping guarantees that the adapted system preserves every capability.

**Example:**
A model improves on a narrow extraction task but begins failing general instruction-following cases that the original model handled.

**Follow-up questions:**

- What evidence would distinguish dataset leakage from real improvement after fine-tuning?

**References:**

- [Luo et al.: Catastrophic forgetting during continual fine-tuning](https://arxiv.org/abs/2308.08747)

### Question: 10. How does DPO differ from a classic RLHF pipeline?

**Topic:** Preference optimization
**Difficulty:** Advanced

**Short answer:**
Direct Preference Optimization (DPO) trains on preferred and dispreferred responses directly. A classic RLHF pipeline trains a reward model and then optimizes a policy with reinforcement learning.

**Explanation:**
Standard DPO uses response likelihood ratios relative to a reference policy to learn from comparisons, without a separate reward model or an online rollout loop during that optimization. Preference labels can encode verbosity or other shortcuts instead of correctness. Check pair quality and evaluate whether the resulting behavior matches the intended criteria.

**Example:**
For the same support question, prefer a supported, concise answer over a confident answer that invents a policy exception.

**Follow-up questions:**

- Why would consistently preferring longer answers risk teaching the wrong behavior?

**References:**

- [Rafailov et al.: Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [Hugging Face: DPO Trainer and preference data](https://huggingface.co/docs/trl/dpo_trainer)

## Evaluation and delivery

### Question: 11. How do you know whether fine-tuning improved the application?

**Topic:** Model comparison
**Difficulty:** Intermediate

**Short answer:**
Compare the adapted model against meaningful baselines on held-out tasks, including target behavior, retained capabilities, reliability, and operational cost.

**Explanation:**
Keep prompts and evaluation conditions controlled when isolating the training effect. Separately compare complete application configurations when measuring product value. Evaluate important slices, output constraints, and unsupported claims; training loss alone is insufficient. Inspect uncertainty and regressions, and include a prompt-only or RAG baseline where relevant.

**Example:**
An extractor improves field accuracy but produces more invalid records; report both metrics before deciding whether the change is deployable.

**Follow-up questions:**

- How would you distinguish better memorization of common cases from improved handling of new cases?

**References:**

- [Liang et al.: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)

### Question: 12. What must be saved and verified when deploying a fine-tuned model?

**Topic:** Artifacts and deployment
**Difficulty:** Advanced

**Short answer:**
Preserve the exact base-model revision, adapted weights, tokenizer, chat template, configuration, and evaluation results needed to reproduce the deployed behavior.

**Explanation:**
An adapter checkpoint generally does not contain the entire base model. Record target modules and adapter settings, and verify compatibility when loading. Merging supported adapters into base weights changes the deployment artifact; evaluate the final precision and quantization configuration. For resumable training, preserve optimizer, scheduler, and random-state information as well. Keep a known-good version for rollback.

**Example:**
An adapter loads successfully but uses a different chat template at serving time, causing a regression despite unchanged adapter weights.

**Follow-up questions:**

- Why is saving only the adapter file insufficient to reproduce a training run or deployment?

**References:**

- [Hugging Face: PEFT checkpoint format](https://huggingface.co/docs/peft/developer_guides/checkpoint)
- [Hugging Face: Trainer checkpoints](https://huggingface.co/docs/transformers/main_classes/trainer)

Use the [evaluation question bank](evaluation.md) to design comparisons for these methods.
