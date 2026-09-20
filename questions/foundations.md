# Foundational GenAI and LLM Questions and Answers

[Back to the README](../README.md)

Start with the short answers, then use the explanations and follow-ups to practice deeper interview discussions. Examples are illustrative unless explicitly attributed to a source. Generation details below assume an autoregressive, decoder-only language model unless stated otherwise.

## Contents

- [Core concepts](#core-concepts): GenAI, LLMs, tokens, and embeddings.
- [Transformer architecture](#transformer-architecture): transformer blocks, attention, position, and model families.
- [Training and adaptation](#training-and-adaptation): objectives, fine-tuning, human feedback, parameters, and in-context learning.
- [Inference and context](#inference-and-context): generation, context windows, sampling, and caching.
- [Evaluation and limitations](#evaluation-and-limitations): perplexity, hallucinations, and model scale.

## Core concepts

### Question: 1. What is generative AI, and how does it differ from discriminative AI?

**Topic:** GenAI basics
**Difficulty:** Beginner

**Short answer:**
Generative AI learns patterns in data to produce content such as text, images, or audio. Discriminative models learn to predict a target, such as a class label, from an input.

**Explanation:**
The distinction concerns the modeling objective. Generative models can also perform classification by generating labels, so the categories do not define exclusive application types. GenAI extends beyond language models.

**Example:**
A spam classifier predicts whether an email is spam. A generative model can draft an email or output a spam label when prompted.

**Follow-up questions:**

- When would a dedicated classifier be preferable to a generative model?

**References:**

- [Google: What is machine learning?](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml)

### Question: 2. What is a large language model?

**Topic:** LLM basics
**Difficulty:** Beginner

**Short answer:**
An LLM is a neural language model trained at substantial scale to learn patterns in token sequences. Generative LLMs use those patterns to produce text conditioned on context.

**Explanation:**
Many LLMs use transformers. Their training supports multiple language tasks, but fluent output does not establish correctness. A language model is one component of a chat application, which may additionally provide retrieval, tools, and conversation storage. There is no universal parameter threshold for “large.”

**Example:**
The same generative LLM can summarize a paragraph or draft code when given different instructions.

**Follow-up questions:**

- How does a base language model differ from an instruction-tuned model?

**References:**

- [Hugging Face: How do transformers work?](https://huggingface.co/learn/llm-course/en/chapter1/4)

### Question: 3. What are tokens, and why does tokenization matter?

**Topic:** Tokenization
**Difficulty:** Beginner

**Short answer:**
Tokens are units that a tokenizer maps to integer IDs for a model. They may represent whole words, word fragments, punctuation, or bytes.

**Explanation:**
Subword methods such as byte-pair encoding balance vocabulary size against sequence length. Token counts depend on the tokenizer, language, and text; one word does not necessarily equal one token. Tokenization affects context usage and computational cost. Use the tokenizer associated with the model.

**Example:**
A rare identifier may require several tokens even though a programmer sees it as one word.

**Follow-up questions:**

- What tradeoff arises when increasing a tokenizer's vocabulary size?

**References:**

- [Hugging Face: Tokenization algorithms](https://huggingface.co/docs/transformers/tokenizer_summary)

### Question: 4. What is an embedding?

**Topic:** Representations
**Difficulty:** Beginner

**Short answer:**
An embedding is a learned vector representation of an item, such as a token, sentence, or document.

**Explanation:**
Embeddings encode relationships useful for their training objective. An LLM's input embedding maps a token ID to a vector; transformer layers then produce contextual representations. A sentence embedding used for retrieval is a different representation, designed or trained to support comparisons between texts. Similarity does not prove factual equivalence.

**Example:**
A retrieval model may place “reset my password” near “recover account access,” helping match a query to relevant documentation.

**Follow-up questions:**

- Why might averaging token embeddings perform worse than a trained sentence embedding model?

**References:**

- [Google: Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings)

## Transformer architecture

### Question: 5. What is a transformer?

**Topic:** Architecture
**Difficulty:** Beginner

**Short answer:**
A transformer processes sequences using attention and feed-forward layers, with residual connections and normalization.

**Explanation:**
Attention mixes information across positions; feed-forward layers transform each position's representation. During training, many token positions can be processed in parallel. Ordinary autoregressive generation still depends on previously generated tokens.

**Example:**
Training can evaluate predictions at many positions in a sentence in one forward pass, while basic decoding selects the next token before continuing.

**Follow-up questions:**

- Why do residual connections help train deep networks?

**References:**

- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/html/1706.03762v7)

### Question: 6. How does self-attention work?

**Topic:** Attention
**Difficulty:** Intermediate

**Short answer:**
Self-attention uses learned query, key, and value projections to combine information from positions in the same sequence.

**Explanation:**
Scaled dot-product attention is `softmax(QKᵀ / √d_k + M)V`, where `d_k` is the key dimension and `M` masks disallowed positions with negative infinity. Query-key similarity determines weights over values. Multiple heads learn different projections. Causal masking prevents access to future tokens.

**Example:**
When predicting a continuation after “The cat slept because it,” attention can incorporate earlier words such as “cat.”

**Follow-up questions:**

- Why divide attention scores by the square root of the key dimension?

**References:**

- [Vaswani et al.: Scaled dot-product and multi-head attention](https://arxiv.org/html/1706.03762v7)

### Question: 7. Why do transformers need positional information?

**Topic:** Position encoding
**Difficulty:** Intermediate

**Short answer:**
Attention needs a way to represent token positions and their relationships so that sequence order can influence processing.

**Explanation:**
Approaches include absolute position embeddings and rotary position embeddings (RoPE). RoPE rotates query and key vectors according to position, allowing their dot products to incorporate relative position. A position encoding scheme alone does not guarantee reliable performance at arbitrary sequence lengths.

**Example:**
“The dog chased the cat” and “The cat chased the dog” contain the same words but express different events.

**Follow-up questions:**

- What can go wrong when using a model beyond the sequence lengths seen during training?

**References:**

- [Su et al.: RoFormer](https://arxiv.org/abs/2104.09864)

### Question: 8. How do encoder-only, decoder-only, and encoder-decoder models differ?

**Topic:** Model families
**Difficulty:** Intermediate

**Short answer:**
Encoders build representations of input text, causal decoders generate continuations, and encoder-decoder models generate output conditioned on an encoded input.

**Explanation:**

| Architecture | Typical attention pattern | Example family | Common use |
| --- | --- | --- | --- |
| Encoder-only | Bidirectional across the input | BERT | Classification and representation learning |
| Decoder-only | Causal within the sequence | GPT | Text continuation and chat |
| Encoder-decoder | Bidirectional encoder; causal decoder with cross-attention to encoder outputs | T5 | Translation and summarization |

These are typical uses, not strict task boundaries.

**Example:**
For translation, an encoder-decoder model reads the source sentence and generates a target sentence token by token.

**Follow-up questions:**

- How does cross-attention differ from self-attention?

**References:**

- [Hugging Face: Transformer architectures](https://huggingface.co/learn/llm-course/en/chapter1/6)

## Training and adaptation

### Question: 9. What is next-token prediction, and why is it self-supervised?

**Topic:** Pretraining objectives
**Difficulty:** Beginner

**Short answer:**
Next-token prediction trains a model to predict each token from the preceding tokens. The text supplies its own targets, so separate human labels are unnecessary.

**Explanation:**
Training commonly minimizes cross-entropy: the negative log probability assigned to the actual next token, averaged over target positions. Causal masking prevents future-token leakage. This objective rewards prediction of training text; it does not directly certify truth. Masked language modeling is a different objective that predicts hidden tokens from surrounding context.

**Example:**
For “Birds can fly,” the token sequence corresponding to “Birds can” provides context for predicting the next token.

**Follow-up questions:**

- Why would access to future tokens invalidate causal language-model training?

**References:**

- [Hugging Face: Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)

### Question: 10. How do pretraining, fine-tuning, and inference differ?

**Topic:** Model lifecycle
**Difficulty:** Beginner

**Short answer:**
Pretraining learns broad patterns from data. Fine-tuning further trains an existing model for a domain, task, or behavior. Inference uses a trained model to produce outputs.

**Explanation:**
Both pretraining and fine-tuning update learned parameters, although some methods update only a subset or added adapters. Ordinary inference keeps those parameters fixed. Instructions or examples in a prompt change the context, not the model weights.

**Example:**
Training on a broad text corpus, adapting to support conversations, and answering a customer question illustrate the three stages.

**Follow-up questions:**

- What evidence would justify fine-tuning instead of improving the prompt?

**References:**

- [Hugging Face: Pretraining and fine-tuning](https://huggingface.co/learn/llm-course/en/chapter1/4)

### Question: 11. What are instruction tuning and RLHF?

**Topic:** Post-training
**Difficulty:** Intermediate

**Short answer:**
Instruction tuning trains on examples of requested behavior. Reinforcement learning from human feedback (RLHF) uses human feedback to guide optimization toward preferred outputs.

**Explanation:**
In a classic RLHF pipeline, supervised fine-tuning teaches responses, human comparisons train a reward model, and reinforcement learning optimizes the language model against that reward. This can improve helpfulness and instruction following, but preference rewards are imperfect proxies for correctness and safety. Post-training pipelines vary.

**Example:**
Annotators prefer a clear, relevant answer over a rambling one; those comparisons provide a training signal.

**Follow-up questions:**

- What happens if a model learns to exploit weaknesses in the reward model?

**References:**

- [Ouyang et al.: Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

### Question: 12. What is the difference between parameters and hyperparameters?

**Topic:** Machine learning basics
**Difficulty:** Beginner

**Short answer:**
Parameters are values learned during training, such as weight matrices. Hyperparameters are configuration choices that govern the model or training process, such as learning rate and layer count.

**Explanation:**
An optimizer updates parameters using gradients. Engineers choose or search over hyperparameters. Generation controls such as temperature are inference settings; changing them does not retrain the model. Parameter count describes model size, not a count of stored facts.

**Example:**
Changing the learning rate affects training updates; changing temperature affects how tokens are selected from the trained model's outputs.

**Follow-up questions:**

- Why can an excessively large learning rate prevent training from converging?

**References:**

- [Google: Machine learning glossary](https://developers.google.com/machine-learning/glossary#hyperparameter)

### Question: 13. What are zero-shot, few-shot, and in-context learning?

**Topic:** Adaptation through prompts
**Difficulty:** Beginner

**Short answer:**
Zero-shot prompting supplies a task without demonstrations. Few-shot prompting includes a small number of examples. In-context learning adapts behavior using the supplied context without updating model weights.

**Explanation:**
Demonstrations communicate patterns such as output format or label meanings. Their quality, relevance, and order can affect results. This adaptation is not persistent training: later requests need the relevant context supplied again unless the application retains it.

**Example:**
Provide “excellent → positive” and “awful → negative,” then ask the model to label “wonderful.”

**Follow-up questions:**

- How would you test whether few-shot examples actually improve performance?

**References:**

- [Brown et al.: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

## Inference and context

### Question: 14. How does an autoregressive LLM generate an answer?

**Topic:** Inference
**Difficulty:** Beginner

**Short answer:**
It processes the prompt, computes scores for possible next tokens, selects one using a decoding strategy, and repeats with the selected token added to the context.

**Explanation:**
The scores are called logits; softmax converts them into probabilities. Greedy decoding selects the highest-scoring token, while sampling draws from a distribution. Generation stops at an end token, a configured stop condition, or an output limit. Greedy local choices do not guarantee the most probable complete sequence.

**Example:**
Different first-token selections can lead the same prompt toward different complete answers.

**Follow-up questions:**

- Why does generating a longer answer usually increase latency?

**References:**

- [Hugging Face: Generation strategies](https://huggingface.co/docs/transformers/generation_strategies)

### Question: 15. What is a context window, and is it the same as memory?

**Topic:** Context limits
**Difficulty:** Beginner

**Short answer:**
A context window bounds the token sequence a model can process. It is different from information learned in weights or stored by an application.

**Explanation:**
For a typical decoder-only request, prompt tokens and generated tokens share a context budget; serving systems may impose additional limits. A larger window does not guarantee reliable use of every detail. The Lost in the Middle study found sensitivity to information position in the models it evaluated.

**Example:**
With an illustrative 8,000-token total budget and a 6,000-token prompt, at most 2,000 tokens remain for generation before other constraints.

**Follow-up questions:**

- How would you preserve useful conversation information when the history exceeds the context limit?

**References:**

- [Google: Context window](https://developers.google.com/machine-learning/glossary#context-window)
- [Liu et al.: Lost in the Middle](https://arxiv.org/abs/2307.03172)

### Question: 16. What do temperature, top-k, and top-p control?

**Topic:** Sampling
**Difficulty:** Intermediate

**Short answer:**
Temperature reshapes token probabilities. Top-k limits sampling to the k highest-scoring tokens. Top-p limits sampling to the smallest highest-probability set whose cumulative probability reaches a threshold.

**Explanation:**
For positive temperature `T`, probabilities are proportional to `exp(logit / T)`. Lower values sharpen the distribution; higher values flatten it. Top-k and top-p filter candidates before sampling. Greedy decoding is commonly exposed separately or through a zero-temperature convention; implementations vary. Lower randomness does not guarantee factual accuracy or reproducibility across execution environments.

**Example:**
With probabilities `[0.60, 0.25, 0.10, 0.05]`, top-p at `0.80` retains the first two candidates and renormalizes their probabilities.

**Follow-up questions:**

- How can changing both temperature and top-p complicate an experiment?

**References:**

- [Hugging Face: Generation configuration](https://huggingface.co/docs/transformers/main_classes/text_generation)

### Question: 17. What are prefill, decoding, and the KV cache?

**Topic:** Inference efficiency
**Difficulty:** Intermediate

**Short answer:**
Prefill processes the prompt. Decoding generates subsequent tokens. A key-value (KV) cache stores earlier attention keys and values so decoding can reuse them.

**Explanation:**
For a causal transformer, later tokens do not change earlier tokens' representations, enabling reuse. Caching reduces repeated computation but consumes memory, typically increasing with retained sequence length and batch size. It stores intermediate tensors, not finished answers, and does not remove the need to attend to relevant prior positions.

**Example:**
After processing a long prompt, the model reuses its cached keys and values when generating each answer token.

**Follow-up questions:**

- Why can long concurrent requests exhaust memory even when the model weights fit on the device?

**References:**

- [Hugging Face: How caching works](https://huggingface.co/docs/transformers/cache_explanation)

## Evaluation and limitations

### Question: 18. What is perplexity, and what does it tell us?

**Topic:** Language-model evaluation
**Difficulty:** Intermediate

**Short answer:**
Perplexity is the exponential of average negative log-likelihood per token. Lower values indicate that a model assigns higher probability to the observed evaluation text.

**Explanation:**
Using natural logarithms, `perplexity = exp(cross-entropy)`. Compare results only under compatible tokenization, data, and context-evaluation protocols. Perplexity measures predictive fit, not directly factual accuracy, helpfulness, or application success. It is not directly defined in the same way for masked language models.

**Example:**
An average loss of approximately `0.693` nats per token corresponds to perplexity `2`.

**Follow-up questions:**

- Why should a chatbot evaluation include measures beyond perplexity?

**References:**

- [Hugging Face: Perplexity of fixed-length models](https://huggingface.co/docs/transformers/perplexity)

### Question: 19. What is an LLM hallucination, and why can it happen?

**Topic:** Reliability
**Difficulty:** Beginner

**Short answer:**
A hallucination is generated content that is false or unsupported by the relevant evidence or input, even when it sounds plausible.

**Explanation:**
Learning to predict text does not ensure truth: training data can contain misconceptions, and plausible continuations can fill gaps without evidence. Confident language is not a calibrated correctness score. As an engineering practice, verify important claims against trusted evidence and test whether a system can acknowledge missing information.

**Example:**
A model supplies a convincing paper title and citation, but the paper does not exist.

**Follow-up questions:**

- How would you detect an answer that contradicts a supplied document?

**References:**

- [Lin et al.: TruthfulQA](https://arxiv.org/abs/2109.07958)

### Question: 20. Does a larger model always perform better?

**Topic:** Scaling and model selection
**Difficulty:** Intermediate

**Short answer:**
No. Performance depends on training data, compute allocation, architecture, adaptation, and the task, as well as parameter count.

**Explanation:**
The Chinchilla study demonstrated that a smaller model trained on more tokens could outperform larger models under a comparable training-compute budget. That result is not a universal model-selection rule. In practice, compare candidate models on representative tasks and measure quality, latency, and resource requirements together.

**Example:**
For a narrow support-labeling task, evaluate whether a smaller adapted model meets accuracy requirements before accepting the cost of a larger one.

**Follow-up questions:**

- How would you design a fair comparison between two models for your application?

**References:**

- [Hoffmann et al.: Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
