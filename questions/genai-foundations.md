# Foundational GenAI and LLM Questions and Answers

[Back to the README](../README.md) · [Terminology glossary](../GLOSSARY.md) · [Previous: AI and machine learning foundations](ai-foundations.md) · [Next: RAG](rag.md)

Start with the short answers, then use the explanations and follow-ups to practice deeper interview discussions. Examples are illustrative unless explicitly attributed to a source. Generation details below assume an autoregressive, decoder-only language model unless stated otherwise.

Each question includes a short answer, a plain-language explanation with an analogy, an advanced answer with technical detail, metrics or checks, at least two examples, and a quick cheat sheet. Numerical examples are illustrative, not benchmark results or universal targets. Use the [cross-topic cheat sheet](../CHEAT_SHEET.md) for quick revision.

## Contents

- [Core concepts](#core-concepts): GenAI, LLMs, tokens, and embeddings.
- [Transformer architecture](#transformer-architecture): transformer blocks, attention, position, and model families.
- [Training and adaptation](#training-and-adaptation): objectives, fine-tuning, human feedback, parameters, and in-context learning.
- [Inference and context](#inference-and-context): generation, context windows, sampling, and caching.
- [Evaluation and limitations](#evaluation-and-limitations): perplexity, hallucinations, and model scale.
- [Model families and checkpoint choices](#model-families-and-checkpoint-choices)

## Core concepts

## Question: 1. What is generative AI, and how does it differ from discriminative AI?

**Topic:** GenAI basics
**Difficulty:** Beginner

**Key terms:** [Generative AI (GenAI)](../GLOSSARY.md#generative-ai-genai) · [Generative model](../GLOSSARY.md#generative-model) · [Discriminative model](../GLOSSARY.md#discriminative-model)

**Short answer:**
Generative AI learns patterns in data to produce content such as text, images, or audio. Discriminative models learn to predict a target, such as a class label, from an input.

**Simple answer and analogy:**

**In plain language:** Generative AI creates content. A discriminative model makes a judgment about supplied content. Both learn from examples, and a generator can also be asked to produce a category label.

**Analogy:** One worker writes a new restaurant review; another sorts existing reviews into positive and negative piles. These illustrate different jobs. Being able to write convincingly does not guarantee that the review describes a real visit.

**Advanced answer and AI/maths:**
The distinction concerns the modeling objective. Generative models can also perform classification by generating labels, so the categories do not define exclusive application types. GenAI extends beyond language models.

A discriminative model estimates a target or decision boundary from inputs; a generative model represents a data distribution and can sample from it. Conditional generators also take inputs, so receiving a prompt does not make a model discriminative. Choose the formulation based on the output and uncertainty needed, rather than assuming generation is always the more advanced solution.

**Metrics and checks:** Compare task accuracy and calibration for prediction; compare validity, diversity, usefulness, and cost for generation. Likelihood alone does not establish that generated content meets user needs.

**Examples:**

**Example 1:**
A spam classifier predicts whether an email is spam. A generative model can draft an email or output a spam label when prompted.

**Example 2:**
A classifier flags a product review as negative, while a conditional generator drafts a reply. The generator's fluency does not guarantee that its reply follows the refund policy.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Discriminative** | predict a label or boundary |
| **Generative** | model and sample data |
| **Conditional** | generation can depend on inputs |

**Follow-up questions:**

- When would a dedicated classifier be preferable to a generative model?

**References:**

- [Google: What is machine learning?](https://developers.google.com/machine-learning/intro-to-ml/what-is-ml)

## Question: 2. What is a large language model?

**Topic:** LLM basics
**Difficulty:** Beginner

**Key terms:** [Large language model (LLM)](../GLOSSARY.md#large-language-model-llm) · [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer) · [Inference](../GLOSSARY.md#inference)

**Short answer:**
A large language model (LLM) is a neural model trained at substantial scale to represent patterns in token sequences. Generative LLMs use those patterns to produce text conditioned on supplied context.

**Simple answer and analogy:**

**In plain language:** A large language model learns patterns in language and uses the supplied text to predict or generate more text. It does not automatically know what is happening in the world right now.

**Analogy:** Think of an extremely capable text-completion system trained on many examples of writing. Like someone relying on old reference material, it may need current documents or tools to answer a question about today's stock or prices.

**Advanced answer and AI/maths:**
Many LLMs use transformers. Their training supports multiple language tasks, but fluent output does not establish correctness. A language model is one component of a chat application, which may additionally provide retrieval, tools, and conversation storage. There is no universal parameter threshold for “large.”

An LLM represents text as tokens and learns statistical structure through a large neural network. Its ability to continue text can support answering, extraction, and coding, but the underlying objective does not verify statements against the world. Capabilities depend on training data, architecture, post-training, and inference configuration. Treat the deployed system as the model plus prompts, retrieval, tools, and checks.

**Metrics and checks:** Evaluate task success, unsupported claims, latency, and cost on representative inputs. Model size and a public benchmark score do not substitute for application-specific measurements.

**Examples:**

**Example 1:**
The same generative LLM can summarize a paragraph or draft code when given different instructions.

**Example 2:**
The same model can summarize a document reliably when all facts are supplied yet fail to report today's inventory unless connected to a current data source.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Model** | learned token distribution |
| **Application** | model plus surrounding controls |
| **Knowledge** | weights are not a live database |

**Follow-up questions:**

- How does a base language model differ from an instruction-tuned model?

**References:**

- [Hugging Face: How do transformers work?](https://huggingface.co/learn/llm-course/en/chapter1/4)

## Question: 3. What are tokens, and why does tokenization matter?

**Topic:** Tokenization
**Difficulty:** Beginner

**Key terms:** [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer) · [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer) · [Context window](../GLOSSARY.md#context-window)

**Short answer:**
Tokens are units that a tokenizer maps to integer IDs for a model. They may represent whole words, word fragments, punctuation, or bytes.

**Simple answer and analogy:**

**In plain language:** A model reads and writes small units called tokens. A token may be a whole word, part of a word, punctuation, or another piece of text.

**Analogy:** Imagine packing a sentence into a set of reusable tiles. “Unbelievable” might require several tiles rather than one. Different tile sets pack the same sentence differently, which is why word count alone does not reliably predict the model's input size.

**Advanced answer and AI/maths:**
Subword methods such as byte-pair encoding balance vocabulary size against sequence length. Token counts depend on the tokenizer, language, and text; one word does not necessarily equal one token. Tokenization affects context usage and computational cost. Use the tokenizer associated with the model.

Tokenization maps text into a vocabulary-dependent sequence, often using subword units. Spaces, punctuation, code, and non-English text can tokenize differently, so character counts are only rough proxies. Token boundaries influence context budgets, truncation, cost, and exact-string tasks. Preserve the tokenizer version associated with a checkpoint; swapping vocabularies without compatible model training changes the meaning of token IDs.

**Metrics and checks:** Measure actual input/output token counts using the selected tokenizer. Report tokens per request by language and workload; a single words-to-tokens conversion can underestimate long-tail costs.

**Examples:**

**Example 1:**
A rare identifier may require several tokens even though a programmer sees it as one word.

**Example 2:**
A short serial number can consume many tokens despite containing no spaces. A multilingual support workflow should budget on real messages rather than extrapolating from English prose alone.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Tokens** | model-specific units |
| **IDs** | meaningful only with the matching vocabulary |
| **Budget** | count actual inputs and outputs |

**Follow-up questions:**

- What tradeoff arises when increasing a tokenizer's vocabulary size?

**References:**

- [Hugging Face: Tokenization algorithms](https://huggingface.co/docs/transformers/tokenizer_summary)

## Question: 4. What is an embedding?

**Topic:** Representations
**Difficulty:** Beginner

**Key terms:** [Embedding](../GLOSSARY.md#embedding) · [Vector, matrix, and tensor](../GLOSSARY.md#vector-matrix-and-tensor) · [Dot product and cosine similarity](../GLOSSARY.md#dot-product-and-cosine-similarity)

**Short answer:**
An embedding is a learned vector representation of an item, such as a token, sentence, or document.

**Simple answer and analogy:**

**In plain language:** An embedding turns an item into a list of numbers that helps compare it with other items. Similar items may end up close together according to what the model learned.

**Analogy:** Imagine a map that places documents near others about related subjects. Nearby addresses help you find candidates, but neighboring documents can still disagree. “The product is safe” and “the product is not safe” may discuss almost the same topic.

**Advanced answer and AI/maths:**
Embeddings encode relationships useful for their training objective. An LLM's input embedding maps a token ID to a vector; transformer layers then produce contextual representations. A sentence embedding used for retrieval is a different representation, designed or trained to support comparisons between texts. Similarity does not prove factual equivalence.

Embeddings place items in a learned vector space where the training objective encourages selected relationships. Similarity is therefore task-dependent: semantic resemblance is not factual equivalence, authorization, or entailment. Normalize consistently when using cosine similarity, and keep query/document encoders compatible. A vector index accelerates search but does not make an unsuitable embedding model appropriate for a domain.

**Metrics and checks:** Cosine similarity is the dot product divided by the product of vector norms. Evaluate recall@k and downstream task quality on domain queries, alongside index size and retrieval latency.

**Examples:**

**Example 1:**
A retrieval model may place “reset my password” near “recover account access,” helping match a query to relevant documentation.

**Example 2:**
“Treatment recommended” and “treatment not recommended” may be close in semantic space despite opposite implications. A medical retriever needs evidence-sensitive evaluation, not just visually plausible neighbor lists.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Vector** | learned representation |
| **Similarity** | objective-dependent |
| **Retrieval** | verify relevance and meaning separately |

**Follow-up questions:**

- Why might averaging token embeddings perform worse than a trained sentence embedding model?

**References:**

- [Google: Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings)

## Transformer architecture

## Question: 5. What is a transformer?

**Topic:** Architecture
**Difficulty:** Beginner

**Key terms:** [Transformer](../GLOSSARY.md#transformer) · [Attention and self-attention](../GLOSSARY.md#attention-and-self-attention) · [Queries, keys, and values (QKV)](../GLOSSARY.md#queries-keys-and-values-qkv) · [Multi-head attention](../GLOSSARY.md#multi-head-attention) · [Positional encoding and RoPE](../GLOSSARY.md#positional-encoding-and-rope) · [Encoder and decoder](../GLOSSARY.md#encoder-and-decoder) · [Feed-forward layer](../GLOSSARY.md#feed-forward-layer) · [Residual connection and layer normalization](../GLOSSARY.md#residual-connection-and-layer-normalization)

**Short answer:**
The Transformer architecture, introduced in the 2017 paper [**Attention Is All You Need**](https://arxiv.org/abs/1706.03762) by Vaswani and colleagues working with Google, is a neural network design that underpins modern AI model families associated with ChatGPT, Gemini, and Llama. It uses **attention** to connect information across token positions, allowing many positions to be processed in parallel during training. Ordinary autoregressive generation still produces new tokens step by step.

**Simple answer and analogy:**

**In plain language:** A Transformer lets each part of a text gather useful information from other allowed parts. It can process many known positions together while learning, although ordinary text generation still adds new pieces one at a time.

**Analogy:** Imagine a meeting where each participant can consult relevant notes from across the table instead of relying only on a message passed down a line. The analogy explains access to context, not human understanding or permission to see future text.

**Advanced answer and AI/maths:**

### What problem did it fix?

- **Old way — recurrent neural networks (RNNs):** An RNN updates its hidden state one sequence position at a time. Each update depends on the previous one, limiting parallel computation across positions. Learning relationships between distant words can also be difficult, although gated architectures such as LSTMs help; RNNs do not inevitably forget every early word.
- **Transformer approach:** Attention creates direct connections between permitted positions without requiring a recurrent chain. Training can process a known sequence's positions in parallel, improving hardware utilization. This makes distant context easier to access, but does not guarantee perfect long-range reasoning or unlimited memory.

“All at once” refers to parallel computation **within a layer over available tokens**. Layers still depend on earlier layers. In a causal model, masks prevent future-token access during training; at generation time, the next token is not known until it has been selected. See the [original paper's comparison with recurrent architectures](https://arxiv.org/html/1706.03762v7).

### Key building blocks

**1. Self-attention — which other tokens matter here?**

Self-attention lets a token combine information from other permitted positions to build its contextual representation. In *“The animal didn't cross the street because it was tired,”* useful context connects **“it”** with **“animal.”** This is an intuition for what the network can learn, not a guarantee that one attention head explicitly resolves the pronoun. An encoder can attend across the input; a causal decoder can attend only to the current and earlier positions. Models operate on **tokens**, which may be smaller than words.

**2. Queries, keys, and values — how does attention choose information?**

Learned projections produce three vectors from each token representation:

| Vector | Intuition | Role |
| --- | --- | --- |
| **Query (Q)** | What am I looking for? | Compared with keys to compute compatibility scores |
| **Key (K)** | What information can I be matched on? | Provides the matching signal for queries |
| **Value (V)** | What information do I pass along? | Combined using the resulting attention weights |

For one attention head, the computation is:

`Attention(Q, K, V) = softmax(QKᵀ / sqrt(d_k) + mask) V`

Here, `d_k` is the key/query dimension. Query-key dot products become scaled scores; masking excludes forbidden positions; softmax turns each query's scores into weights; those weights combine the value vectors. Q, K, and V are learned numerical representations, not literal questions or labels. [The original paper defines this operation as scaled dot-product attention](https://arxiv.org/html/1706.03762v7).

**3. Multi-head attention — several learned views**

Multiple heads use different learned projections, allowing different token relationships to contribute simultaneously. One may emphasize a syntactic relationship while another emphasizes nearby context, but heads do not have guaranteed human-assigned jobs such as “grammar” or “tone.” Their outputs are combined and projected back into the model representation.

**4. Positional information — where is each token?**

Attention needs position information to distinguish order. The original Transformer adds positional encodings to token embeddings. Other architectures use different schemes, including relative or rotary position methods, so “add a positional vector” is not a universal implementation rule. The sentences *“The dog chased the cat”* and *“The cat chased the dog”* contain the same words but have different meanings.

**5. Encoder and decoder — understanding a source and generating a target**

The original architecture uses an **encoder** to form contextual input representations and a **decoder** to generate a target sequence. Decoder self-attention is causal; cross-attention lets it use the encoder's output. This fits tasks such as translation. Transformer variants can instead be **encoder-only** or **decoder-only**; many chat-oriented language models use decoder-only architectures. See [Question 8](#question-8-how-do-encoder-only-decoder-only-and-encoder-decoder-models-differ) for that distinction.

**6. Feed-forward layers, residual connections, and normalization**

Attention mixes information across positions; feed-forward layers transform the resulting representation at each position. Residual connections preserve a path around a sublayer, and normalization helps control activation behavior during training. A Transformer therefore contains more than attention alone. For visual study, use [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).

**Metrics and checks:**

- **Training efficiency:** Compare tokens per second, peak memory, and time to reach a stated validation quality under comparable hardware and data. Parallelization does not imply a fixed speedup for every workload.
- **Attention scaling:** Dense attention considers roughly `n²` query-key pairs per head for sequence length `n`. Increasing length from 1,024 to 2,048 gives four times as many pairs. This does not mean total model runtime or memory must increase exactly fourfold; kernels, masking, and other layers matter.
- **Inference:** Measure prefill latency, time to first token, and decoding tokens per second separately. Parallel prompt processing does not eliminate the dependency between newly generated tokens.
- **Context use:** Test answer quality with evidence at different positions and distances. Accepting a long input is not proof that the model uses every part reliably.

**Examples:**

**Example 1 — pronoun context:**
In *“The animal didn't cross the street because it was tired,”* the surrounding words help identify the intended referent of “it.” Contrast this with *“The animal didn't cross the street because it was flooded,”* where “street” becomes the more plausible referent. Context changes the interpretation even though most words remain identical; the examples illustrate a reasoning task, not measured model performance.

**Example 2 — translation:**
An encoder processes *“The cat is sleeping.”* A decoder generates a French translation one token at a time while attending to the encoded source. During training, the known target can be shifted and processed across positions in parallel, with causal masking preventing each prediction from seeing its future answer.

**Example 3 — chat generation:**
For *“Explain gravity to a child,”* a decoder-only model processes the available prompt during prefill, then generates successive output tokens. A KV cache reuses earlier attention state to avoid recomputing it, but ordinary decoding still needs each selected token before continuing. See [Question 17](#question-17-what-are-prefill-decoding-and-the-kv-cache).

**Quick Cheat Sheet:**

**Memory aid: Q asks, K matches, V carries. Position supplies order; masks restrict visibility.**

| Component or distinction | Remember | Common trap |
| --- | --- | --- |
| **Self-attention** | Mix information across permitted token positions | Assuming every token can always see every other token |
| **Q / K / V** | Match queries to keys, then combine values | Treating attention scores as proof of reasoning |
| **Multi-head** | Several learned projections | Assuming each head has a fixed human-readable job |
| **Position** | Preserve sequence-order information | Assuming every model adds the original sinusoidal encoding |
| **Encoder / decoder** | Encode a source / generate a target | Assuming all Transformers contain both |
| **Feed-forward + residual + normalization** | Transform representations and support training | Thinking the architecture is only attention |
| **Training / generation** | Parallel known positions / sequential new tokens | Saying the whole answer is generated at once |

**Follow-up questions:**

- Why can causal language-model training process multiple target positions in parallel without leaking future tokens?
- How does self-attention differ from encoder-decoder cross-attention?
- Why do residual connections help train deep networks?
- What changes when sequence length doubles, and which costs must you measure rather than infer?

**References:**

- [Vaswani et al.: Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) — original architecture and [full-text explanation](https://arxiv.org/html/1706.03762v7).
- [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — optional visual walkthrough.
- [User-suggested attention video, starting at 0:05](https://www.youtube.com/watch?v=sznZ78HquPc&t=5s) — further viewing. The video and transcript could not be retrieved for this update; no explanation above is attributed to unverified video content.

## Question: 6. How does self-attention work?

**Topic:** Attention
**Difficulty:** Intermediate

**Key terms:** [Attention and self-attention](../GLOSSARY.md#attention-and-self-attention) · [Queries, keys, and values (QKV)](../GLOSSARY.md#queries-keys-and-values-qkv) · [Logit and softmax](../GLOSSARY.md#logit-and-softmax) · [Causal mask](../GLOSSARY.md#causal-mask)

**Short answer:**
Self-attention uses learned query, key, and value projections to combine information from positions in the same sequence.

**Simple answer and analogy:**

**In plain language:** Self-attention lets a token use surrounding information to shape its meaning. Some connections matter more than others, and the model learns how to weight them.

**Analogy:** The word “bank” means something different beside “river” than beside “loan.” Attention helps combine those clues, like highlighting relevant nearby passages before interpreting a sentence. A bright highlight alone does not prove the final interpretation is correct.

**Advanced answer and AI/maths:**
Scaled dot-product attention is `softmax(QKᵀ / √d_k + M)V`, where `d_k` is the key dimension and `M` masks disallowed positions with negative infinity. Query-key similarity determines weights over values. Multiple heads learn different projections. Causal masking prevents access to future tokens.

Self-attention forms queries, keys, and values from the same sequence. Query-key scores determine weights used to combine value vectors, with masking controlling which positions are visible. Multiple heads can learn different useful interactions, but interpreting a head as a single human concept is unreliable. High attention weight is also not proof that a token caused the final output.

**Metrics and checks:** Scaled dot-product attention is softmax(QKᵀ/sqrt(d_k) + mask)V. For standard dense attention, the score matrix has one entry per allowed query/key pair per head.

**Examples:**

**Example 1:**
When predicting a continuation after “The cat slept because it,” attention can incorporate earlier words such as “cat.”

**Visual: One attention head**

```mermaid
flowchart LR
    accTitle: One attention head
    accDescr: Queries and keys produce masked weights that mix values.
    X["Token representations"] --> Q["Q projection"]
    X --> K["K projection"]
    X --> V["V projection"]
    Q --> Scores["QKᵀ / √d_k + mask"]
    K --> Scores
    Scores --> Weights["Row-wise softmax"]
    Weights --> Mix["Weighted sum of V"]
    V --> Mix
```

This shows one head; a full attention layer combines multiple heads and applies an output projection. Concept reference: [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762).

![Causal attention mask for four token positions: each query can attend to itself and earlier positions; future positions are blocked.](../assets/diagrams/causal-attention.svg)

The cells show **allowed connections, not learned attention weights**. Masked future positions receive zero attention probability after softmax. Concept reference: [Vaswani et al.: Attention Is All You Need](https://arxiv.org/abs/1706.03762).

**Example 2:**
In “The trophy did not fit in the suitcase because it was too large,” context helps relate “it” to a plausible referent. Attention contributes to contextual representation without guaranteeing correct reasoning.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Q** | what seeks information |
| **K** | what can be matched |
| **V** | what gets combined |

**Follow-up questions:**

- Why divide attention scores by the square root of the key dimension?

**References:**

- [Vaswani et al.: Scaled dot-product and multi-head attention](https://arxiv.org/html/1706.03762v7)

## Question: 7. Why do transformers need positional information?

**Topic:** Position encoding
**Difficulty:** Intermediate

**Key terms:** [Positional encoding and RoPE](../GLOSSARY.md#positional-encoding-and-rope) · [Positional encoding and RoPE](../GLOSSARY.md#positional-encoding-and-rope) · [Context window](../GLOSSARY.md#context-window)

**Short answer:**
Attention needs a way to represent token positions and their relationships so that sequence order can influence processing.

**Simple answer and analogy:**

**In plain language:** Words need both meaning and order. Positional information tells the model where pieces occur so it can distinguish arrangements containing the same words.

**Analogy:** Put “dog,” “bites,” and “person” on cards. Without their order, you cannot tell who bit whom. Position information provides the equivalent of numbered places for the cards, though models implement that information in different ways.

**Advanced answer and AI/maths:**
Approaches include absolute position embeddings and rotary position embeddings (RoPE). RoPE rotates query and key vectors according to position, allowing their dot products to incorporate relative position. A position encoding scheme alone does not guarantee reliable performance at arbitrary sequence lengths.

Attention without positional information cannot distinguish arbitrary reorderings in the way language requires. Absolute embeddings, relative schemes, and rotary approaches encode position differently and interact with extrapolation beyond training lengths. A claimed maximum context length says little about whether important evidence is used reliably at every position. Test location, distance, and distractor effects rather than assuming a longer configuration preserves quality.

**Metrics and checks:** Measure retrieval or reasoning accuracy with evidence at the beginning, middle, and end, across multiple lengths. Separate accepted input length from effective task performance.

**Examples:**

**Example 1:**
“The dog chased the cat” and “The cat chased the dog” contain the same words but express different events.

**Example 2:**
“Dog bites person” and “person bites dog” share tokens but differ in order and meaning. A long-context assistant must also connect a definition near the start with an exception far later.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Order** | changes meaning |
| **Position scheme** | architecture-dependent |
| **Long context** | validate use, not just acceptance |

**Follow-up questions:**

- What can go wrong when using a model beyond the sequence lengths seen during training?

**References:**

- [Su et al.: RoFormer](https://arxiv.org/abs/2104.09864)

## Question: 8. How do encoder-only, decoder-only, and encoder-decoder models differ?

**Topic:** Model families
**Difficulty:** Intermediate

**Key terms:** [Encoder and decoder](../GLOSSARY.md#encoder-and-decoder) · [Cross-attention](../GLOSSARY.md#cross-attention) · [Causal mask](../GLOSSARY.md#causal-mask) · [Model families: BERT, GPT, and T5](../GLOSSARY.md#model-families-bert-gpt-and-t5)

**Short answer:**
Encoders build representations of input text, causal decoders generate continuations, and encoder-decoder models generate output conditioned on an encoded input.

**Simple answer and analogy:**

**In plain language:** An encoder builds a useful representation of an input. A decoder produces a sequence. Some systems combine both; others use only one kind of structure.

**Analogy:** In a translation office, one role studies the source and prepares notes, while another writes the translation using those notes. That resembles an encoder-decoder arrangement. It is a role analogy: modern models do not all contain two separate parts like this.

**Advanced answer and AI/maths:**

| Architecture | Typical attention pattern | Example family | Common use |
| --- | --- | --- | --- |
| Encoder-only | Bidirectional across the input | BERT | Classification and representation learning |
| Decoder-only | Causal within the sequence | GPT | Text continuation and chat |
| Encoder-decoder | Bidirectional encoder; causal decoder with cross-attention to encoder outputs | T5 | Translation and summarization |

These are typical uses, not strict task boundaries.

Encoder-only models typically build bidirectional representations for classification, tagging, or retrieval. Decoder-only models use causal attention for continuation. Encoder-decoder models encode a source and generate a target through a decoder that can attend to the encoded source. These are architectural patterns, not strict capability boundaries; training objectives and task interfaces also determine suitability.

**Metrics and checks:** Compare task quality, serving latency, and required output structure. For retrieval, embedding throughput matters; for translation, output quality and generation cost may dominate.

**Examples:**

**Example 1:**
For translation, an encoder-decoder model reads the source sentence and generates a target sentence token by token.

**Example 2:**
A search system can use an encoder for document embeddings and a decoder for answer generation. A translation model can instead use an encoder-decoder to condition generated text on the entire source sentence.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Encoder** | contextual representations |
| **Decoder** | causal continuation |
| **Encoder-decoder** | source-to-target generation |

**Follow-up questions:**

- How does cross-attention differ from self-attention?

**References:**

- [Hugging Face: Transformer architectures](https://huggingface.co/learn/llm-course/en/chapter1/6)

## Training and adaptation

## Question: 9. What is next-token prediction, and why is it self-supervised?

**Topic:** Pretraining objectives
**Difficulty:** Beginner

**Key terms:** [Autoregressive generation](../GLOSSARY.md#autoregressive-generation) · [Self-supervised learning](../GLOSSARY.md#self-supervised-learning) · [Cross-entropy and log loss](../GLOSSARY.md#cross-entropy-and-log-loss) · [Causal mask](../GLOSSARY.md#causal-mask)

**Short answer:**
Next-token prediction trains a model to predict each token from the preceding tokens. The text supplies its own targets, so separate human labels are unnecessary.

**Simple answer and analogy:**

**In plain language:** The model practices predicting the next token from the tokens already shown. The original text supplies the answers, so people do not need to label every prediction manually.

**Analogy:** Cover the next word in a book, guess it, then uncover it to check. Repeating that exercise provides many practice examples. It rewards predicting what the book says, even if the book contains a factual mistake.

**Advanced answer and AI/maths:**
Training commonly minimizes cross-entropy: the negative log probability assigned to the actual next token, averaged over target positions. Causal masking prevents future-token leakage. This objective rewards prediction of training text; it does not directly certify truth. Masked language modeling is a different objective that predicts hidden tokens from surrounding context.

Training constructs input/target pairs from the text itself by shifting token positions. A causal mask prevents each prediction from reading its future target. The loss usually sums or averages negative log probabilities over selected target positions. This objective teaches many patterns because predicting language requires useful representations, but it does not directly encode truthfulness, instruction compliance, or every downstream task.

**Metrics and checks:** Token cross-entropy is the mean of −log p(correct next token). State which tokens are masked and how losses are aggregated; changing the tokenizer or evaluated text can change the meaning of the score.

**Examples:**

**Example 1:**
For “Birds can fly,” the token sequence corresponding to “Birds can” provides context for predicting the next token.

**Example 2:**
From “water freezes at zero,” the model can learn to predict successive tokens without a human labeling each one. Training on an incorrect sentence still rewards reproducing its token pattern.

**Visual:**

![Toy training inputs The, cat, sat predict cat, sat, and an end-of-sequence token.](../assets/diagrams/shifted-targets.svg)

Token strings are illustrative; actual tokenization varies. A causal mask prevents seeing the target’s future context. Concept reference: [Hugging Face: causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling).

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Self-supervised** | labels come from data |
| **Shift** | predict the next position |
| **Causal mask** | prevent future-token leakage |

**Follow-up questions:**

- Why would access to future tokens invalidate causal language-model training?

**References:**

- [Hugging Face: Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)

## Question: 10. How do pretraining, fine-tuning, and inference differ?

**Topic:** Model lifecycle
**Difficulty:** Beginner

**Key terms:** [Pretraining and base model](../GLOSSARY.md#pretraining-and-base-model) · [Fine-tuning](../GLOSSARY.md#fine-tuning) · [Inference](../GLOSSARY.md#inference)

**Short answer:**
Pretraining learns broad patterns from data. Fine-tuning further trains an existing model for a domain, task, or behavior. Inference uses a trained model to produce outputs.

**Simple answer and analogy:**

**In plain language:** Pretraining builds broad abilities, fine-tuning adjusts learned behavior, and inference uses the resulting model. Providing a document during a request is usually not another training step.

**Analogy:** Think of general education, focused job training, and doing a task at work. Looking up a current price list while working supplies new information without necessarily changing the person's long-term training. The model stages differ in a similar way.

**Advanced answer and AI/maths:**
Both pretraining and fine-tuning update learned parameters, although some methods update only a subset or added adapters. Ordinary inference keeps those parameters fixed. Instructions or examples in a prompt change the context, not the model weights.

Pretraining learns broad representations from a large corpus; fine-tuning updates weights for a more targeted objective; inference runs a trained model to produce outputs. Prompting and retrieval normally change inputs without changing weights. Each stage needs separate data governance and evaluation: a successful training run can still produce a poorly calibrated or operationally unsuitable application.

**Metrics and checks:** Track training loss and held-out loss during learning, then application quality, latency, and cost during inference. Training throughput and user-visible generation speed are different measurements.

**Examples:**

**Example 1:**
Training on a broad text corpus, adapting to support conversations, and answering a customer question illustrate the three stages.

**Example 2:**
A model can be pretrained on general text, fine-tuned on support conversations, and supplied with a customer's current contract at inference through retrieval. Each step solves a different problem.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Pretrain** | broad learning |
| **Fine-tune** | update for a target objective |
| **Inference** | use the learned model |

**Follow-up questions:**

- What evidence would justify fine-tuning instead of improving the prompt?

**References:**

- [Hugging Face: Pretraining and fine-tuning](https://huggingface.co/learn/llm-course/en/chapter1/4)

## Question: 11. What are instruction tuning and RLHF?

**Topic:** Post-training
**Difficulty:** Intermediate

**Key terms:** [Supervised fine-tuning (SFT)](../GLOSSARY.md#supervised-fine-tuning-sft) · [RLHF and reward model](../GLOSSARY.md#rlhf-and-reward-model) · [RLHF and reward model](../GLOSSARY.md#rlhf-and-reward-model) · [Direct preference optimization (DPO)](../GLOSSARY.md#direct-preference-optimization-dpo)

**Short answer:**
Instruction tuning trains on examples of requested behavior. Reinforcement learning from human feedback (RLHF) uses human feedback to guide optimization toward preferred outputs.

**Simple answer and analogy:**

**In plain language:** Instruction tuning shows examples of how to respond to requests. Human-feedback training uses people's judgments to encourage responses they prefer. Neither guarantees that every answer is true.

**Analogy:** A trainee can learn from sample customer-service replies, then receive ratings comparing their replies with alternatives. If reviewers reward confident wording more than accuracy, the trainee may improve the style without improving the substance.

**Advanced answer and AI/maths:**
In a classic RLHF pipeline, supervised fine-tuning teaches responses, human comparisons train a reward model, and reinforcement learning optimizes the language model against that reward. This can improve helpfulness and instruction following, but preference rewards are imperfect proxies for correctness and safety. Post-training pipelines vary.

Instruction tuning uses demonstrations of desired responses, while preference-based alignment learns from comparisons or reward signals about response quality. Classic RLHF includes fitting a reward model and optimizing a policy; other preference methods use different optimization procedures. Human preference is not identical to factual correctness, and reward optimization can favor superficial style unless evaluation explicitly checks task completion and evidence.

**Metrics and checks:** Evaluate instruction adherence, factual support, refusal appropriateness, and regressions on held-out tasks. A rising reward-model score is not an independent measure of real-world improvement.

**Examples:**

**Example 1:**
Annotators prefer a clear, relevant answer over a rambling one; those comparisons provide a training signal.

**Example 2:**
Raters may prefer a polished long response even when a short answer is more accurate. A support assistant therefore needs policy and factual checks alongside preference judgments.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Demonstrations** | teach desired outputs |
| **Preferences** | compare outputs |
| **Reward** | proxy that needs independent validation |

**Follow-up questions:**

- What happens if a model learns to exploit weaknesses in the reward model?

**References:**

- [Ouyang et al.: Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

## Question: 12. What is the difference between parameters and hyperparameters?

**Topic:** Machine learning basics
**Difficulty:** Beginner

**Key terms:** [Parameter and weight](../GLOSSARY.md#parameter-and-weight) · [Hyperparameter](../GLOSSARY.md#hyperparameter) · [Learning rate (LR)](../GLOSSARY.md#learning-rate-lr)

**Short answer:**
Parameters are values learned during fitting, such as weights and additive bias terms. Hyperparameters are chosen settings controlling architecture, training, or inference, such as layer count, learning rate, and sampling temperature.

**Simple answer and analogy:**

**In plain language:** Parameters are values the model learns. Hyperparameters are settings chosen for how the model is built, trained, or used.

**Analogy:** Think of a radio that automatically adjusts internal controls to improve reception. Those learned adjustments resemble parameters; choosing how quickly it adjusts resembles a hyperparameter. Changing a generation setting does not mean the model has learned new facts.

**Advanced answer and AI/maths:**
An optimizer updates parameters using gradients. Engineers choose or search over hyperparameters. Generation controls such as temperature are inference settings; changing them does not retrain the model. Parameter count describes model size, not a count of stored facts.

Parameters are learned values such as weights; hyperparameters configure training or inference, such as learning rate or sampling temperature. Some choices, such as model width, determine the parameter count before training. Other settings affect serving without updating any weights. Reproducibility requires recording both the checkpoint and the configurations that generated it and served its outputs.

**Metrics and checks:** Report parameter count separately from active parameters, optimizer memory, and serving memory. Compare hyperparameters using validation data and record random seeds and software versions where relevant.

**Examples:**

**Example 1:**
Changing the learning rate affects training updates; changing temperature affects how tokens are selected from the trained model's outputs.

**Example 2:**
Changing a classifier's learned coefficient requires training, while changing its decision threshold may only alter deployment configuration. Similarly, lowering generation temperature does not retrain the LLM.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Parameters** | learned values |
| **Hyperparameters** | chosen settings |
| **Reproducibility** | checkpoint plus configuration |

**Follow-up questions:**

- Why can an excessively large learning rate prevent training from converging?

**References:**

- [Google: Machine learning glossary](https://developers.google.com/machine-learning/glossary#hyperparameter)

## Question: 13. What are zero-shot, few-shot, and in-context learning?

**Topic:** Adaptation through prompts
**Difficulty:** Beginner

**Key terms:** [Zero-shot and few-shot learning](../GLOSSARY.md#zero-shot-and-few-shot-learning) · [Prompt and prompt engineering](../GLOSSARY.md#prompt-and-prompt-engineering) · [Fine-tuning](../GLOSSARY.md#fine-tuning)

**Short answer:**
Zero-shot prompting supplies a task without demonstrations. Few-shot prompting includes a small number of examples. In-context learning adapts behavior using the supplied context without updating model weights.

**Simple answer and analogy:**

**In plain language:** You can describe a task without examples, or include a few demonstrations in the request. The demonstrations guide the current response without normally changing the model's learned weights.

**Analogy:** Give a colleague a blank expense form, or give them the form plus two correctly completed examples. The examples make the intended format clearer. They do not ensure success on unusual cases the examples never show.

**Advanced answer and AI/maths:**
Demonstrations communicate patterns such as output format or label meanings. Their quality, relevance, and order can affect results. This adaptation is not persistent training: later requests need the relevant context supplied again unless the application retains it.

In-context learning conditions a fixed model on task instructions and examples; it does not normally update weights. Examples communicate formats, decision boundaries, and exceptions, but can introduce label bias or accidental patterns. Zero-shot avoids demonstration tokens, while few-shot can improve consistency at added context cost. Select examples that cover meaningful variation and keep evaluation examples out of the prompt.

**Metrics and checks:** Compare held-out task success, format validity, input tokens, and latency for zero-shot and several demonstration sets. Test sensitivity to example order and class balance.

**Examples:**

**Example 1:**
Provide “excellent → positive” and “awful → negative,” then ask the model to label “wonderful.”

**Example 2:**
A ticket classifier shown only urgent examples may overpredict urgency. Include routine cases and ambiguous boundary cases, then check on separate tickets rather than reusing the demonstrations.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Zero-shot** | instruction without demonstrations |
| **Few-shot** | examples in context |
| **Learning** | no ordinary weight update |

**Follow-up questions:**

- How would you test whether few-shot examples actually improve performance?

**References:**

- [Brown et al.: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

## Inference and context

## Question: 14. How does an autoregressive LLM generate an answer?

**Topic:** Inference
**Difficulty:** Beginner

**Key terms:** [Autoregressive generation](../GLOSSARY.md#autoregressive-generation) · [Temperature and sampling](../GLOSSARY.md#temperature-and-sampling) · [Prefill and decoding](../GLOSSARY.md#prefill-and-decoding) · [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer)

**Short answer:**
It processes the prompt, computes scores for possible next tokens, selects one using a decoding strategy, and repeats with the selected token added to the context.

**Simple answer and analogy:**

**In plain language:** The model builds a response by choosing the next token, adding it to the text, and repeating. Earlier choices influence what comes later.

**Analogy:** It resembles completing a sentence one tile at a time: once you place “Dear,” certain next tiles become more likely. A locally sensible sequence can still produce a whole letter that misunderstands the request.

**Advanced answer and AI/maths:**
The scores are called logits; softmax converts them into probabilities. Greedy decoding selects the highest-scoring token, while sampling draws from a distribution. Generation stops at an end token, a configured stop condition, or an output limit. Greedy local choices do not guarantee the most probable complete sequence.

Autoregressive generation repeatedly predicts the next token conditioned on the prompt and previously generated tokens. Errors can therefore influence later continuation, and a locally likely token sequence need not form a correct solution. Decoding ends through stop tokens, configured limits, or external control. Streaming exposes partial output sooner but does not change the sequential dependency of ordinary decoding.

**Metrics and checks:** Measure time to first token, inter-token latency, output length, and completion rate. End-to-end latency includes queueing and prompt processing as well as decoding.

**Examples:**

**Example 1:**
Different first-token selections can lead the same prompt toward different complete answers.

**Example 2:**
A code generator that chooses the wrong variable early can consistently reuse it throughout a function. Syntax validity at each local step does not guarantee that the completed function meets the specification.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Loop** | predict then append |
| **Dependency** | prior output shapes the next step |
| **Stop** | completion conditions must be explicit |

**Follow-up questions:**

- Why does generating a longer answer usually increase latency?

**References:**

- [Hugging Face: Generation strategies](https://huggingface.co/docs/transformers/generation_strategies)

## Question: 15. What is a context window, and is it the same as memory?

**Topic:** Context limits
**Difficulty:** Beginner

**Key terms:** [Procedural memory](../GLOSSARY.md#procedural-memory) · [Context window](../GLOSSARY.md#context-window) · [Working state and memory](../GLOSSARY.md#working-state-and-memory) · [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer)

**Short answer:**
A context window is the token capacity available to a model request under its model and serving configuration. It differs from information learned in weights or persisted by an application. A larger window allows more context, but does not guarantee better recall, coherence, or reasoning.

**Simple answer and analogy:**

**In plain language:** The context window is how much material fits into the current request. Persistent memory is information an application stores and brings back later. Neither guarantees perfect recall.

**Analogy:** A desk holds the papers you can consult right now; a filing cabinet stores papers for another day. A bigger desk can hold more, but an important note can still be overlooked. Stored instructions also need to be correct and current.

**Advanced answer and AI/maths:**
For a typical decoder-only request, prompt tokens and generated tokens share a context budget; serving systems may impose additional limits. A larger window does not guarantee reliable use of every detail. The Lost in the Middle study found sensitivity to information position in the models it evaluated.

The context window bounds the tokens a model can process in a request; persistent memory requires an external mechanism that selects and supplies information across requests. Summaries and retrieved memories can lose details or preserve stale claims. Treat stored memory as data with provenance, retention, and access rules. A larger window reduces some truncation pressure but can add cost, latency, and distraction.

**Procedural memory** stores instructions for how to perform a task, such as searching approved sources and returning the top three results. Semantic memory stores facts, while episodic memory records past events. These are application design categories; an agent does not automatically learn or persist a reliable procedure merely by completing a task.

**Metrics and checks:** Track context tokens, truncation frequency, retrieval success, and task quality as conversations grow. Include system instructions, tool outputs, and reserved output capacity in the budget.

**Examples:**

**Example 1:**
With an illustrative 8,000-token total budget and a 6,000-token prompt, at most 2,000 tokens remain for generation before other constraints.

**Example 2:**
A travel assistant may remember a seating preference in a database while omitting last week's full conversation. Before booking, it should verify that the preference is current and applies to the present traveler.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Context** | current request capacity |
| **Memory** | stored and retrieved state |
| **Summary** | lossy representation, not perfect recall |

**Follow-up questions:**

- How would you preserve useful conversation information when the history exceeds the context limit?

**References:**

- [Google: Context window](https://developers.google.com/machine-learning/glossary#context-window)
- [Liu et al.: Lost in the Middle](https://arxiv.org/abs/2307.03172)

## Question: 16. What do temperature, top-k, and top-p control?

**Topic:** Sampling
**Difficulty:** Intermediate

**Key terms:** [Temperature and sampling](../GLOSSARY.md#temperature-and-sampling) · [Top-k and top-p](../GLOSSARY.md#top-k-and-top-p) · [Logit and softmax](../GLOSSARY.md#logit-and-softmax)

**Short answer:**
Temperature reshapes token probabilities. Top-k limits sampling to the k highest-scoring tokens. Top-p limits sampling to the smallest highest-probability set whose cumulative probability reaches a threshold.

**Simple answer and analogy:**

**In plain language:** These settings control how predictable or varied generated text is. They change which next tokens can be chosen and how strongly likely choices are favored.

**Analogy:** Imagine choosing a meal from a menu. Temperature changes how adventurous the choice is; top-k limits the shortlist by count; top-p limits it by accumulated preference. None checks whether the meal meets a dietary rule—that needs a separate check.

**Advanced answer and AI/maths:**
• Temperature: Scales the raw probability scores (logits) before they are converted into percentages. A low temperature (< 1.0) sharpens the curve to make outputs more predictable and factual. A high temperature (> 1.0) flattens the curve, giving less likely words a better chance and increasing creativity.
• Top-K: Restricts the selection pool to a fixed number (\(K\)) of the most probable next tokens. For example, a Top-K of 40 means the model only picks from the top 40 most likely words and ignores everything else.
• Top-P (Nucleus Sampling): Restricts the selection pool to a dynamic set of tokens whose cumulative probability reaches a threshold (\(P\), such as 0.9 or 90%). If a single word is very confident, the pool shrinks to just that word; if the model is unsure, the pool grows to include more creative options.

Temperature rescales logits before sampling; top-k retains a fixed number of candidates and top-p retains a probability-mass-based set. These controls change diversity and repetition, but do not verify facts. Their interaction depends on implementation order and model behavior. Even low-temperature output can vary because of serving details, so use deterministic validators when exact structure or business rules matter.

**Metrics and checks:** Evaluate task success and output diversity across repeated generations, with the decoding configuration recorded. Compare factual errors separately; lower randomness does not imply lower systematic error.

**Examples:**

**Example 1:**
With probabilities `[0.60, 0.25, 0.10, 0.05]`, top-p at `0.80` retains the first two candidates and renormalizes their probabilities.

**Example 2:**
Creative headline generation may benefit from varied samples, while invoice extraction may prioritize consistent schema compliance. Both still need task-specific checks rather than relying on temperature alone.

**Visual:**

![The same logits produce sharper or flatter probabilities at temperatures 0.5, 1, and 2.](../assets/diagrams/temperature.svg)

Synthetic probabilities without top-k or top-p filtering. Greedy decoding is a separate selection rule; lower temperature does not guarantee truth. Concept reference: [Hugging Face: generation strategies](https://huggingface.co/docs/transformers/generation_strategies).

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Temperature** | reshape probabilities |
| **Top-k** | fixed candidate count |
| **Top-p** | cumulative probability mass |

**Follow-up questions:**

- How can changing both temperature and top-p complicate an experiment?

**References:**

- [Hugging Face: Generation configuration](https://huggingface.co/docs/transformers/main_classes/text_generation)

## Question: 17. What are prefill, decoding, and the KV cache?

**Topic:** Inference efficiency
**Difficulty:** Intermediate

**Key terms:** [Prefill and decoding](../GLOSSARY.md#prefill-and-decoding) · [KV cache](../GLOSSARY.md#kv-cache) · [Grouped-query attention (GQA)](../GLOSSARY.md#grouped-query-attention-gqa) · [Throughput and concurrency](../GLOSSARY.md#throughput-and-concurrency)

**Short answer:**
Prefill processes the prompt. Decoding generates subsequent tokens. A key-value (KV) cache stores earlier attention keys and values so decoding can reuse them.

**Simple answer and analogy:**

**In plain language:** First the model processes the prompt. Then it generates new tokens. A cache saves parts of the earlier calculation so they do not have to be redone every time.

**Analogy:** Before writing a report, you read the source papers and make working notes. You reuse those notes as you write instead of rereading everything for every word. Keeping more notes saves repeated work but uses more desk space.

**Advanced answer and AI/maths:**
For a causal transformer, later tokens do not change earlier tokens' representations, enabling reuse. Caching reduces repeated computation but consumes memory, typically increasing with retained sequence length and batch size. It stores intermediate tensors, not finished answers, and does not remove the need to attend to relevant prior positions.

Prefill processes prompt tokens and creates reusable key/value state; decoding adds new tokens while attending to prior cached state. KV caching avoids recomputing earlier keys and values, but consumes memory that grows with sequence length and concurrent requests. Grouped-query attention changes the number of KV heads and therefore cache size. Weight quantization does not automatically imply the cache uses the same precision.

**Metrics and checks:** Approximate KV bytes = 2 × layers × batch × sequence length × KV heads × head dimension × bytes per element, before overhead. Measure prefill and decoding separately at realistic concurrency.

**Examples:**

**Example 1:**
After processing a long prompt, the model reuses its cached keys and values when generating each answer token.

**Visual: Prefill and cached decoding**

```mermaid
flowchart TD
    accTitle: Prefill and cached decoding
    accDescr: Prefill processes the prompt; decoding adds one token at a time and reuses cached keys and values.
    Prompt["Prompt tokens"] --> Prefill["Prefill: process prompt and store K/V"]
    Prefill --> Select["Select next token"]
    Select --> Stop{"Stop token or limit?"}
    Stop -->|Yes| Done["Return completion"]
    Stop -->|No| Decode["Process selected token using past K/V"]
    Decode --> Append["Append its K/V to cache"]
    Append --> Select
```

The cache stores attention keys and values at each layer. It saves recomputation; it does not extend the model’s supported context window. Concept reference: [Hugging Face: KV caching](https://huggingface.co/docs/transformers/cache_explanation).

**Example 2:**
With all other dimensions fixed, doubling a request's cached sequence length approximately doubles its KV storage. A server that fits one long request may still run out of memory when many such requests overlap. For an illustrative configuration with 32 layers, batch size 1, 8,192 cached tokens, 8 KV heads, head dimension 128, and two bytes per element, the formula gives 1,073,741,824 bytes, or 1 GiB, before allocator overhead. This excludes model weights and other buffers.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Prefill** | process prompt |
| **Decode** | generate incrementally |
| **KV cache** | saves compute while consuming memory |

**Follow-up questions:**

- Why can long concurrent requests exhaust memory even when the model weights fit on the device?

**References:**

- [Hugging Face: How caching works](https://huggingface.co/docs/transformers/cache_explanation)

## Evaluation and limitations

## Question: 18. What is perplexity, and what does it tell us?

**Topic:** Language-model evaluation
**Difficulty:** Intermediate

**Key terms:** [Perplexity](../GLOSSARY.md#perplexity) · [Cross-entropy and log loss](../GLOSSARY.md#cross-entropy-and-log-loss) · [Token and tokenizer](../GLOSSARY.md#token-and-tokenizer)

**Short answer:**
Perplexity is the exponential of average negative log-likelihood per token. Lower values indicate that a model assigns higher probability to the observed evaluation text.

**Simple answer and analogy:**

**In plain language:** Perplexity measures how surprised a language model is by the tokens that actually appear in a test passage. Tokens are the small pieces of text the model reads and predicts. Lower perplexity means it gave more probability to those observed pieces, on average. It is not simply the percentage of next-token guesses it got right.

**Analogy:** Imagine guessing the next word in “The cat sat on the…” A model that assigns high probability to “mat” or “floor” will be less surprised if one of those words appears than a model expecting “airplane” or “banana.” The score rewards the probability assigned to the word that actually appears, not just whether the model's single favorite guess wins.

**How to read the score:**

- **Lower:** The evaluated passage was more predictable to the model.
- **Higher:** The observed tokens received less probability on average. This can reflect unfamiliar subject matter, not just a badly trained model.
- **A score of 1:** The model assigned probability 1 to every evaluated target token. This describes that evaluated text, not a guarantee that it can never be wrong on other text.
- **A score of 10:** Its average uncertainty is comparable to choosing among ten equally likely options. It does not literally have ten choices at every step.

**Where the analogy stops:** Predicting words well does not prove understanding or factual accuracy. Compare models only on compatible test text, tokenization, and evaluation settings; a lower number under different conditions is not automatically an improvement.

**Advanced answer and AI/maths:**
Using natural logarithms, `perplexity = exp(cross-entropy)`. Compare results only under compatible tokenization, data, and context-evaluation protocols. Perplexity measures predictive fit, not directly factual accuracy, helpfulness, or application success. It is not directly defined in the same way for masked language models.

Perplexity is the exponential of mean negative log likelihood when natural logarithms are used. It summarizes how surprised a model is by reference tokens, not whether generated answers are helpful or correct. Comparisons require the same tokenization, evaluation text, and masking conventions. A model can achieve better language-model loss while becoming worse at following a particular instruction format or producing evidence-backed answers.


**Metrics and checks:** Perplexity = exp(cross-entropy in nats). Lower is better for predicting that reference distribution; scores across different tokenizers are generally not directly comparable.

**Examples:**

**Example 1:**
An average loss of approximately `0.693` nats per token corresponds to perplexity `2`.

**Example 2:**
A model that predicts common legal phrasing well may have low perplexity on contracts while still inventing a clause when asked a specific question about a missing section.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Loss** | average token surprise |
| **Perplexity** | exponential of that loss |
| **Limit** | not an application-quality score |

**Follow-up questions:**

- Why should a chatbot evaluation include measures beyond perplexity?

**References:**

- [Hugging Face: Perplexity of fixed-length models](https://huggingface.co/docs/transformers/perplexity)

## Question: 19. What is an LLM hallucination, and why can it happen?

**Topic:** Reliability
**Difficulty:** Beginner

**Key terms:** [Hallucination](../GLOSSARY.md#hallucination) · [Correctness and faithfulness](../GLOSSARY.md#correctness-and-faithfulness) · [Citation validity and support](../GLOSSARY.md#citation-validity-and-support) · [Abstention and coverage](../GLOSSARY.md#abstention-and-coverage)

**Short answer:**
A hallucination is generated content that is false or unsupported by the relevant evidence or input, even when it sounds plausible.

**Simple answer and analogy:**

**In plain language:** A hallucination is an answer that sounds plausible but contains false or unsupported information. The model can continue a familiar pattern even when the necessary facts are missing.

**Analogy:** Someone asked for a book quote might confidently finish it with words that sound right rather than checking the book. A model can do something similar, including inventing a convincing page reference. Fluent wording is not evidence.

**Advanced answer and AI/maths:**
Learning to predict text does not ensure truth: training data can contain misconceptions, and plausible continuations can fill gaps without evidence. Confident language is not a calibrated correctness score. As an engineering practice, verify important claims against trusted evidence and test whether a system can acknowledge missing information.

Hallucination covers unsupported or false generated content, but evaluation should distinguish incorrect world knowledge, unsupported claims about supplied evidence, fabricated citations, and invalid tool results. Causes include missing information, ambiguous instructions, poor retrieval, and generation that favors plausible continuation. Mitigations must target the cause: better evidence, explicit abstention, verification, or a deterministic computation may be more effective than a prompt warning.

**Metrics and checks:** Measure unsupported-claim rate, answer correctness, citation validity, and abstention coverage on labeled tasks. Define the unit: claims, responses, or conversations yield different denominators.

**Examples:**

**Example 1:**
A model supplies a convincing paper title and citation, but the paper does not exist.

**Example 2:**
A financial assistant can retrieve the correct report yet compute a percentage incorrectly. A calculator addresses that arithmetic failure, while adding more documents may only increase context noise.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Diagnose** | missing facts or bad use? |
| **Ground** | connect claims to evidence |
| **Abstain** | when support is insufficient |

**Follow-up questions:**

- How would you detect an answer that contradicts a supplied document?

**References:**

- [Lin et al.: TruthfulQA](https://arxiv.org/abs/2109.07958)

## Question: 20. Does a larger model always perform better?

**Topic:** Scaling and model selection
**Difficulty:** Intermediate

**Key terms:** [Large language model (LLM)](../GLOSSARY.md#large-language-model-llm) · [Parameter and weight](../GLOSSARY.md#parameter-and-weight) · [Baseline](../GLOSSARY.md#baseline) · [Cost per successful task](../GLOSSARY.md#cost-per-successful-task)

**Short answer:**
No. Performance depends on training data, compute allocation, architecture, adaptation, and the task, as well as parameter count.

**Simple answer and analogy:**

**In plain language:** A bigger model may handle some tasks better, but it can also cost more and respond more slowly. The useful question is whether it improves your actual application enough to justify that cost.

**Analogy:** You do not need a moving truck to deliver one envelope. A smaller vehicle may be quicker and cheaper for that job, while a larger one is useful for a full house move. Test the load you really need to carry.

**Advanced answer and AI/maths:**
The Chinchilla study demonstrated that a smaller model trained on more tokens could outperform larger models under a comparable training-compute budget. That result is not a universal model-selection rule. In practice, compare candidate models on representative tasks and measure quality, latency, and resource requirements together.

Larger models can improve some capabilities but may increase latency, serving memory, and cost without improving the target workflow enough to justify them. Data quality, post-training, retrieval, tools, and task specialization also matter. Compare complete configurations under the same input distribution and service constraints. Routing between models can help, but the router's errors and fallback costs must be included.

**Metrics and checks:** Plot quality against p95 latency and cost per successful task. Include failure/retry costs and evaluate difficult slices rather than selecting on average accuracy alone.

**Examples:**

**Example 1:**
For a narrow support-labeling task, evaluate whether a smaller adapted model meets accuracy requirements before accepting the cost of a larger one.

**Example 2:**
A small classifier may reliably route a fixed set of ticket categories, while a larger model handles unusual multilingual cases. Routing is worthwhile only if missed difficult cases remain acceptable.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Size** | one capability factor |
| **Baseline** | test a smaller suitable model |
| **Decision** | quality within latency and cost constraints |

**Follow-up questions:**

- How would you design a fair comparison between two models for your application?

**References:**

- [Hoffmann et al.: Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)

## Model families and checkpoint choices

## Question: 21. How do GANs, VAEs, and diffusion models generate data differently?

**Topic:** Generative model families
**Difficulty:** Intermediate

**Key terms:** [GAN](../GLOSSARY.md#gan) · [Variational autoencoder (VAE)](../GLOSSARY.md#variational-autoencoder-vae) · [Diffusion model](../GLOSSARY.md#diffusion-model) · [Latent representation](../GLOSSARY.md#latent-representation)

**Short answer:**
Generative adversarial networks (GANs) learn through competition between a generator and discriminator. Variational autoencoders (VAEs) learn a probabilistic latent representation. Diffusion models learn to reverse a corruption or noise process.

**Simple answer and analogy:**

**In plain language:** These are different ways to learn to generate data. A GAN learns through competition, a VAE learns a compact probabilistic representation, and a diffusion model learns to remove added noise.

**Analogy:** Think of a forger learning from a critic, a sketcher learning from compressed descriptions, and a restorer learning to recover pictures from progressively noisier copies. These are intuition aids, not claims that the systems work like people.

**Advanced answer and AI/maths:**
A GAN pairs a generator with a discriminator during training. A VAE optimizes reconstruction together with a regularizer on its approximate latent posterior; sampling uses a prior and decoder. A diffusion model learns denoising transitions, often conditioned on text or another signal. Training stability, sampling cost, fidelity, and diversity depend on the implementation; no family wins every task.

GANs learn through a generator/discriminator competition; VAEs optimize a probabilistic latent-variable objective with an approximate posterior; diffusion models learn to reverse a corruption process. These families have different training stability, sampling, and representation tradeoffs. Avoid reducing them to a single quality ranking: architecture, dataset, conditioning, and sampling procedure strongly affect results. Evaluate both sample quality and diversity, as well as task-specific constraints.

**Metrics and checks:** Compare validity, coverage/diversity, generation latency, and human task judgments. Distributional image metrics are useful proxies but depend on feature extraction and do not fully capture usefulness or memorization.

**Examples:**

**Example 1:**
Image generation may map noise through a GAN generator, decode a VAE latent sample, or iteratively denoise a diffusion sample. The discriminator and VAE encoder are not required for those basic sampling paths.

**Example 2:**
A VAE may be useful for exploring a smooth latent space, while a diffusion model may support detailed conditional image generation. A visually convincing output still needs checks for the requested attributes.

**Visual:**

![Three sampling paths: GAN generator, VAE decoder, and iterative diffusion denoising.](../assets/diagrams/generative-families.svg)

Basic generation paths only; training objectives and architecture variants differ. The primary references below support the concept.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **GAN** | adversarial training |
| **VAE** | latent probabilistic reconstruction |
| **Diffusion** | learn to reverse noise |

**Follow-up questions:**

- Why should sampling steps be included in a diffusion model’s latency evaluation?

**References:**

- [Goodfellow et al.: Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
- [Kingma and Welling: Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)
- [Ho et al.: Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

## Question: 22. Does a mixture-of-experts model run every expert for every token?

**Topic:** Sparse model architecture
**Difficulty:** Intermediate

**Key terms:** [Mixture of experts (MoE)](../GLOSSARY.md#mixture-of-experts-moe) · [Parameter and weight](../GLOSSARY.md#parameter-and-weight) · [Throughput and concurrency](../GLOSSARY.md#throughput-and-concurrency)

**Short answer:**
In a sparse mixture-of-experts (MoE) layer, a router selects a subset of expert components for each token. Active computation therefore differs from total stored parameter count.

**Simple answer and analogy:**

**In plain language:** A mixture-of-experts model can send each token through only some of its specialized components. It may still need to keep all components available in memory.

**Analogy:** A hospital directs a patient to relevant specialists rather than every doctor examining every case. The hospital still needs space and staff for its other services. Similarly, using fewer experts per token does not make the entire model small.

**Advanced answer and AI/maths:**
Experts commonly replace feed-forward sublayers while attention remains shared. Routing introduces load-balance, capacity, and communication concerns. Sparse activation can reduce arithmetic relative to activating every expert, but all required weights still need storage somewhere. Latency depends on hardware placement, batching, and communication as well as active parameters.

Sparse mixture-of-experts layers route each token to a subset of experts, separating total parameter count from the computation activated per token. The complete model may still need substantial memory to hold all experts. Routing balance, communication between devices, and expert capacity affect throughput. Sparse activation therefore does not mean the system costs the same as a dense model with only the active parameter count.

**Metrics and checks:** Report total and active parameters, tokens per second, expert-load distribution, communication overhead, and tail latency. Compare at equal quality and deployment configuration, not parameter count alone.

**Examples:**

**Example 1:**
An illustrative top-two router chooses two of eight experts for one token and combines their weighted outputs. This does not mean the whole model uses exactly one quarter of its parameters.

**Example 2:**
A token routed to two experts does not use every expert in that layer. If many tokens prefer the same experts, imbalance can still create bottlenecks despite apparently sparse computation.

**Visual:**

![A router activates two of four drawn experts and combines their outputs.](../assets/diagrams/mixture-of-experts.svg)

A schematic top-two layer; expert count and routing policy are model-specific. The primary references below support the concept.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Total** | all stored experts |
| **Active** | selected computation per token |
| **Bottleneck** | routing and communication matter |

**Follow-up questions:**

- When can communication erase the compute savings of sparse routing?

**References:**

- [Fedus et al.: Switch Transformers](https://arxiv.org/abs/2101.03961)

## Question: 23. How should you choose between a base checkpoint and an instruction-tuned checkpoint?

**Topic:** Model selection
**Difficulty:** Intermediate

**Key terms:** [Pretraining and base model](../GLOSSARY.md#pretraining-and-base-model) · [Supervised fine-tuning (SFT)](../GLOSSARY.md#supervised-fine-tuning-sft) · [Chat template and message role](../GLOSSARY.md#chat-template-and-message-role)

**Short answer:**
Choose the checkpoint whose training behavior fits the task and whose measured performance, format, license, and operational constraints meet your needs.

**Simple answer and analogy:**

**In plain language:** A base model mainly learns patterns for predicting text. An instruction-tuned model has additional practice responding to requests. Choose and test the version suited to the job.

**Analogy:** A person who has read many letters may be good at continuing their style; someone also trained in customer service has practiced answering requests. The difference is additional training for a role, not a guarantee of correct answers.

**Advanced answer and AI/maths:**
A base language model primarily learns continuation; instruction tuning encourages responses to requests. Chat formatting and role conventions are part of the checkpoint interface. An instruction-tuned model can still hallucinate or ignore constraints. A base checkpoint may suit specialized adaptation, but it requires task-specific validation rather than assuming that completion ability implies assistant behavior.

A base checkpoint is trained primarily for its foundational objective, while an instruction checkpoint has additional training for following requests and conversational behavior. The latter can still require its expected chat template, role tokens, and generation settings. Selecting a base model because it is less constrained may shift substantial work into data preparation and post-training. Evaluate the actual checkpoint and interface together.

**Metrics and checks:** Compare instruction adherence, task quality, formatting, and inappropriate refusals using identical task intent and each checkpoint's correct input format. Record the exact checkpoint revision.

**Examples:**

**Example 1:**
The same text, “Classify this ticket,” may elicit a continued document from a base model and a label from an instruction-tuned model. Test actual prompts and output contracts on representative cases.

**Example 2:**
A base model may continue a question with another question, while an instruction-tuned model answers it. Feeding malformed role delimiters to the instruction checkpoint can undermine that expected behavior.

**Visual:**

![A pretrained checkpoint can be adapted with demonstrations and preferences into an instruction-oriented checkpoint.](../assets/diagrams/base-instruction.svg)

A conceptual training path. Some pipelines use different stages or omit preference optimization. The primary references below support the concept.

**Quick Cheat Sheet:**

| Cue | Remember |
| --- | --- |
| **Base** | foundational training objective |
| **Instruction** | additional response training |
| **Template** | part of the model interface |

**Follow-up questions:**

- How can an incorrect chat template make a capable checkpoint look poor?

**References:**

- [Ouyang et al.: instruction following with human feedback](https://arxiv.org/abs/2203.02155)
