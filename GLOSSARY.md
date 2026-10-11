# AI and GenAI Terminology Glossary

[Back to the README](README.md) · [Quick revision](CHEAT_SHEET.md)

This glossary contains **275 entries** defining the AI, ML, GenAI, mathematical, and supporting engineering vocabulary used in this repository. Each entry starts with a concise **Definition**, followed by an **Explanation** that adds context, a distinction, or a practical caveat. Related terms are sometimes grouped to make their differences clear. Use your browser’s Find command for an acronym or full term.

Question banks, design scenarios, and notebook exercises link to relevant entries through **Key terms**. The long answers remain the place for worked examples, diagrams, detailed metrics, and implementation references. Product and organization names in source credits are not treated as technical definitions.

## Contents

- [Core AI concepts](#core-ai-concepts)
- [Data preparation and validation](#data-preparation-and-validation)
- [Learning mechanics and traditional models](#learning-mechanics-and-traditional-models)
- [Metrics and evaluation](#metrics-and-evaluation)
- [Language models and generation](#language-models-and-generation)
- [Prompting and fine-tuning](#prompting-and-fine-tuning)
- [Retrieval and RAG terminology](#retrieval-and-rag-terminology)
- [Agents, orchestration, and software delivery](#agents-orchestration-and-software-delivery)
- [Serving, reliability, and supporting terms](#serving-reliability-and-supporting-terms)
- [Mathematical and statistical supporting terms](#mathematical-and-statistical-supporting-terms)
- [Terminology conventions](#terminology-conventions)
- [References and usage](#references-and-usage)

## Core AI concepts

[Examples and deeper explanations](questions/ai-foundations.md). Further reference: [Google ML Glossary](https://developers.google.com/machine-learning/glossary).

### Algorithm

**Definition:** A specified procedure for solving a problem or computing a result.

**Explanation:** A training algorithm produces a fitted model; a serving algorithm uses it.

### Artificial intelligence (AI)

**Definition:** The field of building systems that perform tasks associated with intelligence.

**Explanation:** It includes learned models, search, planning, and hand-written rules; AI does not imply human-like understanding.

### Baseline

**Definition:** A reference system used to judge whether a proposed change helps.

**Explanation:** A simple constant predictor or basic retrieval pipeline can expose unnecessary complexity.

### Classification

**Definition:** Predicting membership in discrete categories.

**Explanation:** Binary classification has two classes; multiclass classification chooses among several; multilabel classification permits multiple labels per example.

### Clustering

**Definition:** Grouping examples according to a chosen similarity or density criterion.

**Explanation:** Clusters are not necessarily known classes, and their usefulness depends on representation and distance choice.

### Computer vision

**Definition:** Computational methods for extracting information from images or video.

**Explanation:** Image classification and object detection are different tasks with different output contracts.

### Dataset and corpus

**Definition:** A dataset is a collection of examples; a corpus is a collection of documents or other language material.

**Explanation:** Sampling, provenance, and duplicates influence what conclusions the collection supports.

### Deep learning (DL)

**Definition:** Machine learning using neural networks with multiple processing layers.

**Explanation:** Layers learn intermediate representations; deep learning can perform prediction or generation.

### Discriminative model

**Definition:** A model that predicts a target from inputs, often by estimating class probabilities or a decision boundary.

**Explanation:** A spam classifier predicts a label; it need not model how complete email messages are generated.

### Distribution

**Definition:** A description of how probability is allocated across possible observations.

**Explanation:** Training and deployment may have different distributions even when column names are identical.

### Feature

**Definition:** An input attribute or representation used by a model.

**Explanation:** Features may be supplied measurements or learned representations; they must be available when the prediction is made.

### Generalization

**Definition:** Performance on relevant examples not used to fit or select the model.

**Explanation:** A high training score does not establish useful behavior on new customers or future dates.

### Generative AI (GenAI)

**Definition:** AI that generates content such as text, images, audio, or code from a learned distribution.

**Explanation:** A generated answer can be fluent without being factual; generation and verification are separate operations.

### Generative model

**Definition:** A model of a data distribution that can support generating new samples.

**Explanation:** Conditional generation also uses inputs, such as a prompt; taking inputs does not make a generator discriminative.

### Ground truth

**Definition:** The reference outcome treated as correct for a particular evaluation.

**Explanation:** It may come from verified records or adjudicated humans; document uncertainty and disagreements instead of assuming perfection.

### Hyperparameter

**Definition:** A setting chosen outside ordinary parameter fitting that controls training, architecture, or inference.

**Explanation:** Learning rate and tree depth are examples; select settings with validation data rather than test results.

### Inference

**Definition:** Using a fitted model to obtain predictions or generated outputs.

**Explanation:** In these engineering discussions, inference usually means model execution; statistical inference can instead mean drawing conclusions about a population.

### Label and target

**Definition:** The outcome a supervised learning procedure is trained to predict.

**Explanation:** A label can be wrong or noisy; a reference answer is not automatically unquestionable ground truth.

### Machine learning (ML)

**Definition:** Methods that learn patterns or decision rules from data rather than specifying every rule manually.

**Explanation:** Learning a spam classifier from labeled messages is ML; applying a fixed blocklist alone is not.

### Model

**Definition:** A parameterized or otherwise specified mapping used to make predictions or generate outputs.

**Explanation:** Distinguish the model from the full application, which also includes data, retrieval, tools, and policies.

### Multimodal model

**Definition:** A model that processes or generates more than one data modality.

**Explanation:** A model accepting text and images is multimodal even if it produces only text.

### Natural language processing (NLP)

**Definition:** Computational methods for analyzing or generating human language.

**Explanation:** Translation, text classification, retrieval, and summarization are NLP tasks; not every NLP system is an LLM.

### Parameter and weight

**Definition:** A value learned during model fitting, such as a neural-network weight or regression coefficient.

**Explanation:** A weight's magnitude alone does not establish feature importance or a causal effect.

### Regression

**Definition:** Predicting a numerical quantity whose magnitude has meaning.

**Explanation:** Forecasting delay in minutes is regression; predicting an integer-coded shipment category is classification.

### Reinforcement learning (RL)

**Definition:** Learning a policy through actions and reward feedback from an environment.

**Explanation:** Actions can affect future observations, so optimizing immediate reward may not maximize long-term return.

### Self-supervised learning

**Definition:** Learning with targets constructed from the data itself.

**Explanation:** Next-token prediction uses later tokens as targets, avoiding manual labeling of each prediction.

### Supervised learning

**Definition:** Learning from examples paired with desired targets.

**Explanation:** The target might be a class, a price, or a response; target quality and deployment-relevant splits matter.

### Training and fitting

**Definition:** The process of adjusting a model using data and an objective.

**Explanation:** A decreasing training loss shows progress on that objective, not necessarily improvement on unseen examples.

### Unsupervised learning

**Definition:** Learning structure from data without task-specific target labels.

**Explanation:** Clustering finds groups, but those groups still need interpretation and validation for the intended use.

## Data preparation and validation

[Examples and deeper explanations](questions/ai-foundations.md). Further reference: [scikit-learn: validation and splitting](https://scikit-learn.org/stable/modules/cross_validation.html).

### Categorical encoding

**Definition:** Representing categories numerically without assuming their IDs are meaningful measurements.

**Explanation:** One-hot encoding uses indicator columns; define behavior for unseen categories before deployment.

### Class imbalance

**Definition:** Unequal frequencies of target classes.

**Explanation:** A model predicting only the majority class can achieve high accuracy while missing important positives.

### Class weighting

**Definition:** Giving examples different loss weights according to their classes.

**Explanation:** It changes learning incentives, but does not by itself select an appropriate deployment decision threshold.

### Concept drift

**Definition:** A change in the relationship between inputs and the target.

**Explanation:** A policy change can invalidate a prediction rule even when individual input histograms remain similar.

### Cross-validation (CV)

**Definition:** Repeated fitting and evaluation over different training-validation partitions.

**Explanation:** In k-fold CV, each fold is evaluated once; all learned preprocessing must be refitted inside each training fold.

### Data augmentation

**Definition:** Creating modified training examples intended to preserve task-relevant labels.

**Explanation:** Image flips or wording changes are valid only when they preserve the meaning required by the task.

### Data drift

**Definition:** A change in the input distribution over time or across environments.

**Explanation:** Drift is a signal to investigate, not proof that predictive quality has degraded.

### Data leakage

**Definition:** Use of information during development that would not legitimately be available for the prediction being evaluated.

**Explanation:** Future features, duplicate subjects, and fitting preprocessing before splitting can all produce optimistic scores.

### Data provenance and lineage

**Definition:** Records of where data or artifacts came from and how they were transformed.

**Explanation:** Source IDs, versions, and timestamps help trace a wrong answer to parsing, retrieval, or generation.

### Dimensionality reduction

**Definition:** Representing data with fewer dimensions.

**Explanation:** Reduced size can simplify computation, but discarded directions may contain task-relevant information.

### Distribution shift

**Definition:** A difference between training/evaluation conditions and the population where a model is used.

**Explanation:** Changes in inputs, labels, or their relationship can undermine generalization.

### Feature scaling

**Definition:** Adjusting numeric feature scales, such as subtracting a training mean and dividing by a training standard deviation.

**Explanation:** It affects distance-based and regularized models; fit scale parameters on training data only.

### Feature selection

**Definition:** Choosing a subset of original input features.

**Explanation:** Unlike PCA, it can reduce which source measurements must be collected; supervised selection belongs inside training folds.

### Group split

**Definition:** A partition that keeps related examples from the same entity together.

**Explanation:** Hold out patients rather than individual scans when deployment involves previously unseen patients.

### Imputation

**Definition:** Replacing missing values according to a specified rule or fitted model.

**Explanation:** The reason data is missing may be informative; fit imputers on training data and consider missing-value indicators.

### Nested cross-validation

**Definition:** Cross-validation with an inner selection loop and an outer assessment loop.

**Explanation:** The outer loop estimates the performance of the selection procedure, not merely a configuration chosen on the same folds.

### Normalization

**Definition:** Rescaling values according to a specified convention.

**Explanation:** Unit-vector normalization, min-max scaling, and layer normalization are different operations; name which one is intended.

### Outlier

**Definition:** An observation unusual relative to the chosen reference distribution.

**Explanation:** It may be an error or a valid rare event; automatic removal can erase exactly the cases that matter.

### Preprocessing pipeline

**Definition:** A sequence of transformations that prepares inputs for modeling or retrieval.

**Explanation:** Save fitted transformations and apply the same definitions at serving time; a pipeline cannot fix an invalid feature definition.

### Resampling and SMOTE

**Definition:** Resampling changes the training sample composition; SMOTE creates minority examples by interpolation between neighbors.

**Explanation:** Synthetic Minority Over-sampling Technique belongs inside training folds, not before splitting; categorical IDs cannot be interpolated meaningfully as ordinary numbers.

### Stratification

**Definition:** Sampling or splitting to preserve specified group proportions.

**Explanation:** Preserving class ratios does not prevent the same customer or future information from leaking across partitions.

### Synthetic data

**Definition:** Artificially constructed examples rather than directly observed records.

**Explanation:** Validate correctness and diversity; generated examples can replicate a teacher model's biases and errors.

### Target encoding

**Definition:** Encoding a category with a statistic derived from target values.

**Explanation:** Use training-only, cross-fitted estimates so a row's own label does not leak into its features.

### Temporal split

**Definition:** A partition that trains on earlier observations and evaluates on later ones.

**Explanation:** It must also respect label arrival times and overlapping forecast windows; sorting dates alone may not prevent leakage.

### Test set

**Definition:** Data reserved to assess the finalized procedure.

**Explanation:** Changing the system after studying test failures turns those examples into development information.

### Training set

**Definition:** The examples used to fit model parameters and learned preprocessing.

**Explanation:** Statistics learned from validation or test records must not leak into this fitting process.

### Validation set

**Definition:** Held-out development examples used to select models, thresholds, or other settings.

**Explanation:** Repeated selection adapts the procedure to this set, so it is not an untouched final assessment.

## Learning mechanics and traditional models

[Examples and deeper explanations](questions/ai-foundations.md). Further reference: [scikit-learn: supervised learning](https://scikit-learn.org/stable/supervised_learning.html).

### Activation function

**Definition:** A function applied to a unit's input to transform its output, often nonlinearly.

**Explanation:** ReLU is max(0,x); sigmoid maps to (0,1); tanh maps to (−1,1). Nonlinearity makes stacked layers more expressive than one affine map.

### Backpropagation

**Definition:** Applying the chain rule backward through a computation graph to calculate gradients efficiently.

**Explanation:** Backpropagation computes derivatives; an optimizer uses them to choose updates.

### Batch size and epoch

**Definition:** Batch size is the number of examples processed together; an epoch is one pass through the training dataset.

**Explanation:** Microbatches can be accumulated before an update, so batch size, update count, and data exposure are distinct.

### DBSCAN

**Definition:** Density-Based Spatial Clustering of Applications with Noise: clustering through dense neighborhood connectivity.

**Explanation:** It can find nonconvex groups and label sparse points as noise; one density scale may fail when groups have very different densities.

### Decision tree

**Definition:** A model that routes inputs through feature tests to a leaf prediction.

**Explanation:** Depth and minimum leaf support control flexibility; small leaves can memorize noise.

### Dropout

**Definition:** Randomly masking selected activations during training as a regularization method.

**Explanation:** Standard inference usually disables dropout or replaces its effect with the framework's corresponding scaling convention.

### Early stopping

**Definition:** Ending training when a monitored validation criterion no longer improves sufficiently.

**Explanation:** It limits unnecessary fitting; use validation data rather than repeatedly selecting on the final test set.

### Ensemble and bagging

**Definition:** An ensemble combines models; bagging trains models on resampled datasets and aggregates predictions.

**Explanation:** Diverse errors can improve reliability, but correlated mistakes can persist across every member.

### Gradient

**Definition:** The vector of local derivatives of a scalar objective with respect to parameters.

**Explanation:** It indicates local sensitivity; its negative gives a direction of steepest decrease under ordinary Euclidean geometry.

### Gradient accumulation

**Definition:** Combining gradients from multiple microbatches before an optimizer update.

**Explanation:** It increases effective batch size without storing all examples' activations simultaneously; long sequences can still exceed memory.

### Gradient boosting

**Definition:** Sequentially adding learners to improve an ensemble's objective.

**Explanation:** Each addition corrects aspects of the current prediction; learning rate, learner complexity, and iteration count affect overfitting.

### Gradient descent

**Definition:** Updating parameters using a negative gradient step; stochastic variants estimate gradients from sampled examples or mini-batches.

**Explanation:** Step size matters: a poor learning rate can cause divergence or very slow optimization.

### Heteroscedasticity

**Definition:** Error variance that changes with the inputs or predicted level.

**Explanation:** A widening residual funnel is one clue; appropriate uncertainty methods differ from fixing a misspecified mean function.

### Impurity and Gini

**Definition:** A measure of label mixture within a tree node; Gini impurity is 1 minus the sum of squared class proportions.

**Explanation:** Splits seek improvement in a chosen criterion, but greedy local choices do not guarantee a globally optimal tree.

### Irreducible noise

**Definition:** Outcome variation that cannot be predicted from the available inputs under the assumed data-generating process.

**Explanation:** In squared-error regression, it forms the noise term alongside squared bias and variance; better inputs may change what is irreducible.

### k-means

**Definition:** Clustering by minimizing squared distances from points to assigned centroids.

**Explanation:** A centroid is a cluster mean and inertia is the summed squared distance; more clusters trivially reduce this objective.

### k-nearest neighbors (kNN)

**Definition:** Predicting from the labels or values of nearby training examples.

**Explanation:** The distance function and feature scales determine neighbors; small k is more local, while large k smooths predictions.

### Kernel and RBF

**Definition:** A kernel computes similarity corresponding to an inner product in a feature space; an RBF kernel uses distance-based similarity.

**Explanation:** The radial basis function scale controls locality; this ML meaning differs from a GPU computation kernel.

### L1 and L2 penalties

**Definition:** L1 penalizes absolute parameter values; L2 penalizes squared values.

**Explanation:** Lasso commonly uses L1 and may yield sparse coefficients; ridge uses L2 and shrinks coefficients. Feature scale affects both.

### Learning curve

**Definition:** A learning curve shows performance versus training size or progress; a validation curve varies a hyperparameter.

**Explanation:** Compare training and held-out scores to investigate underfitting, variance, or diminishing returns.

### Learning rate (LR)

**Definition:** The scale controlling the size of an optimizer's update.

**Explanation:** A schedule changes that scale during training; larger is not always faster in useful convergence.

### Linear regression

**Definition:** Modeling a numerical target as a linear combination of supplied features, often fitted by minimizing squared residuals.

**Explanation:** “Linear” means linear in coefficients; transformed features can represent curved relationships in the original inputs.

### Logistic regression

**Definition:** A classifier modeling log-odds as a linear function of features.

**Explanation:** Binary probability is sigmoid of the linear score; choosing a classification threshold is a separate decision.

### Loss function

**Definition:** A numerical objective that training seeks to minimize, possibly combined with penalties.

**Explanation:** The loss is a proxy for desired behavior, so improving it need not improve every user-facing metric.

### Naive Bayes

**Definition:** A probabilistic classifier that factors feature likelihoods by assuming features are independent given the class.

**Explanation:** Correlated evidence can make probabilities overconfident even when class ranking remains useful.

### Neural network

**Definition:** A composition of parameterized layers that transforms inputs into outputs.

**Explanation:** A neuron is a computational unit, not a faithful biological simulation; depth and width describe different architectural dimensions.

### Optimizer and momentum

**Definition:** A rule for updating parameters from gradients and possibly accumulated state.

**Explanation:** Momentum uses past update information; Adam adapts updates using running gradient statistics. Their state contributes to training memory.

### Permutation importance

**Definition:** The change in a fitted model's score after shuffling a feature on evaluation data.

**Explanation:** It measures reliance under that perturbation, not causality; correlated substitutes can hide joint importance.

### Principal component analysis (PCA)

**Definition:** An unsupervised linear projection onto orthogonal directions of maximum variance.

**Explanation:** Explained variance measures retained spread, not retained predictive usefulness; scaling changes the result.

### Random forest

**Definition:** An ensemble of randomized decision trees with aggregated predictions.

**Explanation:** Randomized data/features encourage diversity; averaging often reduces the variance of individual trees.

### Regularization

**Definition:** Constraints or penalties intended to reduce harmful sensitivity or complexity and improve generalization.

**Explanation:** Stronger regularization can underfit; validate the tradeoff rather than assuming more is better.

### Residual

**Definition:** The difference between an observed outcome and its prediction.

**Explanation:** Residual plots can reveal missing structure or changing error spread; this is distinct from a neural-network residual connection.

### Statistical bias

**Definition:** Systematic error in a learning procedure's average prediction relative to the target function.

**Explanation:** High bias can cause underfitting. This differs from a neural-network bias parameter and from social or fairness bias.

### Support vector machine (SVM)

**Definition:** A margin-based model whose boundary depends on selected training examples called support vectors.

**Explanation:** Soft-margin training trades boundary width against violations; raw decision scores are not automatically calibrated probabilities.

### Transfer learning

**Definition:** Reusing knowledge or representations from a previously trained model for another task.

**Explanation:** Freezing a backbone and training a new head is one approach; transfer quality depends on source and target compatibility.

### Variance and overfitting

**Definition:** Variance measures sensitivity of fitted predictions to the sampled training data; overfitting means fitting training details that do not generalize.

**Explanation:** Remember “V” in o“V”erfitting, but complexity alone is not the definition and distribution shift can also create a train/test gap.

## Metrics and evaluation

[Examples and deeper explanations](questions/evaluation.md). Further reference: [scikit-learn: model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html).

### A/B test

**Definition:** An experiment assigning eligible units to alternative system versions to compare outcomes.

**Explanation:** Randomize at a unit that limits contamination and define metrics and stopping rules before interpreting results.

### Ablation

**Definition:** Removing or changing a component to test its contribution under controlled conditions.

**Explanation:** Retraining may be needed when removing learned components; one ablation does not prove the same contribution in every configuration.

### Abstention and coverage

**Definition:** Abstention declines to answer; answer coverage is the fraction of eligible cases answered.

**Explanation:** Selective risk is error among answered cases. Report both so refusing everything cannot masquerade as a perfect system.

### Accuracy

**Definition:** Correct predictions divided by all evaluated predictions.

**Explanation:** State how abstentions are handled; high accuracy can conceal a classifier that misses nearly every rare positive.

### Benchmark and evaluation slice

**Definition:** A benchmark is a defined test collection and procedure; a slice is a meaningful subset such as a language or task type.

**Explanation:** Aggregate gains can hide regressions on rare but important slices.

### Bootstrap

**Definition:** Estimating sampling variation by repeatedly resampling observed units with replacement.

**Explanation:** Resample independent units such as conversations, not correlated turns; bootstrap sampling is also used to train bagged models.

### Calibration and Brier score

**Definition:** Calibration means predicted probabilities agree with observed outcome frequencies in comparable cases.

**Explanation:** Binary Brier score is mean((p−y)²); it measures probability quality but is not a pure calibration-only statistic.

### Citation validity and support

**Definition:** Citation validity checks that a reference exists; support checks whether its contents justify the associated claim.

**Explanation:** A plausible URL does not establish entailment. Citation precision counts supporting citations among evaluated citations under a stated rubric.

### Confidence interval

**Definition:** An interval produced by a method with a stated long-run coverage property under its assumptions.

**Explanation:** A frequentist 95% interval is not a 95% probability that this fixed parameter lies inside the realized interval.

### Confusion matrix

**Definition:** Counts of predicted classes against reference classes.

**Explanation:** For a chosen positive class: TP is a correct positive, TN a correct negative, FP a false alarm, and FN a missed positive.

### Correctness and faithfulness

**Definition:** Correctness means answering the task accurately; faithfulness means claims are supported by the supplied evidence.

**Explanation:** Grounding connects claims to evidence. An answer can faithfully repeat an outdated source yet be wrong for a current question.

### Cross-entropy and log loss

**Definition:** Loss based on the negative logarithm of probability assigned to the observed target.

**Explanation:** Confidently wrong predictions receive large penalties; specify aggregation, token masking, and logarithm base.

### DCG and nDCG

**Definition:** Discounted cumulative gain rewards relevant items near the top; nDCG divides it by the ideal ranking's gain (IDCG).

**Explanation:** One convention sums (2^relevance−1)/log2(rank+1). Specify gain convention and zero-ideal handling.

### Decision threshold

**Definition:** A cutoff that turns a score into a decision.

**Explanation:** Choose it using validation data and error costs or review capacity; 0.5 is not universally optimal.

### Discrimination

**Definition:** Ability to rank cases so relevant or positive cases receive higher scores.

**Explanation:** A model can rank well while being overconfident; calibration answers a different question.

### F1 score

**Definition:** The harmonic mean of precision and recall: 2TP/(2TP+FP+FN).

**Explanation:** It ignores true negatives and does not encode arbitrary business costs; define behavior when its denominator is zero.

### Inter-rater agreement

**Definition:** Consistency among human or model raters on the same cases.

**Explanation:** Cohen's kappa adjusts categorical agreement for chance for two raters; agreement does not prove that the rubric measures the right thing.

### LLM-as-a-judge

**Definition:** Using a language model to assess outputs against a rubric.

**Explanation:** The judge can have position, verbosity, and shared-model biases; calibrate it against independently reviewed examples.

### Macro and micro averaging

**Definition:** Macro averages class metrics equally; micro pools their underlying counts before computing a metric.

**Explanation:** Support-weighted averages favor frequent classes. State the averaging convention and inspect minority classes separately.

### Mean absolute error (MAE)

**Definition:** The mean absolute difference between predictions and observed numeric targets.

**Explanation:** It has target units and treats error magnitude linearly; compare only compatible targets and scales.

### Mean reciprocal rank (MRR)

**Definition:** The average of 1 divided by the first relevant result's rank, using zero when no relevant result is found.

**Explanation:** It rewards an early first hit but ignores additional relevant results; specify any rank cutoff.

### Mean squared error and RMSE

**Definition:** MSE averages squared residuals; root mean squared error is its square root.

**Explanation:** RMSE has target units and emphasizes large misses more strongly than MAE.

### Paired comparison

**Definition:** Comparing systems on the same evaluation cases.

**Explanation:** Analyze within-case differences to reduce task-mix variation, while accounting for repeated generations and dependent cases.

### Perplexity

**Definition:** Exponential of average token negative log likelihood when natural logarithms are used.

**Explanation:** It measures surprise on reference text, not factuality or instruction following; tokenizer and evaluation data must match for comparison.

### Precision and recall

**Definition:** Precision is TP/(TP+FP); recall is TP/(TP+FN).

**Explanation:** Recall is also true-positive rate (TPR). False-positive rate (FPR) is FP/(FP+TN), not 1 minus precision. Numerical precision has a separate meaning.

### Precision-recall curve and AP

**Definition:** A PR curve plots precision against recall; average precision summarizes precision weighted by recall gains.

**Explanation:** Average precision and trapezoidal PR area use different aggregation rules; the positive-class prevalence affects interpretation.

### Precision@k and recall@k

**Definition:** Precision@k is relevant hits divided by k; recall@k is relevant hits divided by all known relevant items.

**Explanation:** Define relevance units, duplicates, short result lists, and queries with no relevant items before aggregation.

### R-squared (R²)

**Definition:** 1 − SSE/SST, comparing prediction squared error with variation around the evaluation-set target mean.

**Explanation:** SSE sums squared residuals; SST sums squared deviations from that mean. R² can be negative and needs special handling for constant targets.

### Robustness and adversarial evaluation

**Definition:** Testing whether intended behavior survives perturbations, failures, or deliberately hostile inputs.

**Explanation:** Define the invariant and actual attack outcome; rejecting suspicious wording is weaker evidence than preventing unauthorized actions.

### ROC-AUC

**Definition:** Area under a receiver operating characteristic curve plotting TPR against FPR across thresholds.

**Explanation:** It measures ranking discrimination over operating points, not probability calibration or quality at one required threshold.

### Rubric and adjudication

**Definition:** A rubric specifies scoring criteria; adjudication resolves disagreements into a reviewed label or decision.

**Explanation:** Keep initial independent ratings so agreement is not inflated by discussion before labeling.

### Silhouette score

**Definition:** A clustering score comparing within-cluster distance with distance to the nearest alternative cluster.

**Explanation:** It depends on distance geometry and does not establish business usefulness; report how noise and singleton groups are handled.

## Language models and generation

[Examples and deeper explanations](questions/genai-foundations.md). Further reference: [Attention Is All You Need](https://arxiv.org/abs/1706.03762) and [Hugging Face: KV caching](https://huggingface.co/docs/transformers/cache_explanation).

### Attention and self-attention

**Definition:** Attention forms weighted combinations of value representations; self-attention derives its queries, keys, and values from the same sequence.

**Explanation:** Masks define allowed information flow, so causal tokens cannot read future tokens.

### Autoregressive generation

**Definition:** Generating each new token conditional on earlier tokens.

**Explanation:** A local probability choice can influence later output; fluent continuation does not prove a correct overall answer.

### Causal mask

**Definition:** A restriction preventing a sequence position from attending to future positions.

**Explanation:** It allows parallel training on known text without leaking later targets into earlier predictions.

### Context window

**Definition:** The token capacity available to a model request under its model and serving configuration.

**Explanation:** Include instructions, history, tool results, and output reservation as required by the interface; capacity is not persistent memory.

### Cross-attention

**Definition:** Attention whose queries come from one representation sequence and keys/values from another.

**Explanation:** An encoder-decoder can use it to condition generated tokens on the encoded source.

### Diffusion model

**Definition:** A generative model trained to reverse a corruption or noise process.

**Explanation:** Sampling applies a learned denoising procedure; step count, solver, and conditioning affect quality and latency.

### Dot product and cosine similarity

**Definition:** Dot product sums corresponding component products; cosine divides that result by the two vector lengths.

**Explanation:** Cosine emphasizes direction and is undefined for zero-length vectors unless an application specifies a convention.

### Embedding

**Definition:** A learned vector representation of an item such as a token, document, or image.

**Explanation:** Nearby vectors reflect the training objective's similarity, not guaranteed factual equivalence or permission to access the item.

### Encoder and decoder

**Definition:** An encoder builds contextual input representations; a generative decoder predicts an output sequence.

**Explanation:** Encoder-only, decoder-only, and encoder-decoder architectures expose different information flows; not every Transformer contains both.

### Feed-forward layer

**Definition:** A neural transformation applied at each position without recurrent dependence on other positions; MLP means multilayer perceptron.

**Explanation:** In a Transformer, attention mixes positions and the feed-forward block transforms each resulting representation.

### GAN

**Definition:** A generative adversarial network trained through competition between a generator and discriminator.

**Explanation:** Convincing samples need not cover the whole data distribution; quality and diversity require separate checks.

### Grouped-query attention (GQA)

**Definition:** Attention where multiple query heads share key/value heads.

**Explanation:** Sharing reduces KV storage compared with separate KV heads for every query head; exact quality and speed depend on the model.

### Hallucination

**Definition:** Generated content that is false or unsupported relative to the task's evidence requirements.

**Explanation:** Distinguish missing knowledge, fabricated citations, and incorrect calculations because they need different remedies.

### KV cache

**Definition:** Stored attention keys and values reused across generation steps.

**Explanation:** It avoids recomputing earlier states but grows with sequence length and concurrency; KV-head count can differ from query-head count.

### Large language model (LLM)

**Definition:** A large learned model of language patterns used for text prediction or generation.

**Explanation:** Its weights are not a live database; application capabilities also depend on retrieval, tools, prompts, and checks.

### Latent representation

**Definition:** An internal representation not directly observed as the original input or target.

**Explanation:** A latent vector can encode useful factors without its coordinates having simple human-interpretable meanings.

### Logit and softmax

**Definition:** Logits are unnormalized model scores; softmax converts a score vector into nonnegative values summing to one.

**Explanation:** Those values describe the model's distribution, not a guarantee of calibrated real-world confidence.

### Mixture of experts (MoE)

**Definition:** A model that routes inputs to selected expert components.

**Explanation:** Sparse MoE can activate only some experts per token while still storing all experts; active and total parameters are different counts.

### Model families: BERT, GPT, and T5

**Definition:** Names of model families illustrating encoder, generative decoder, and text-to-text encoder-decoder designs.

**Explanation:** BERT expands to Bidirectional Encoder Representations from Transformers; GPT to Generative Pre-trained Transformer; T5 to Text-to-Text Transfer Transformer.

### Multi-head attention

**Definition:** Attention using multiple learned projection sets whose outputs are combined.

**Explanation:** Heads can capture different relationships but do not have guaranteed jobs such as grammar or sentiment.

### Positional encoding and RoPE

**Definition:** Methods that supply order or relative-position information to a sequence model.

**Explanation:** The original Transformer adds positional encodings; rotary position embeddings rotate query/key representations. These are not identical mechanisms.

### Prefill and decoding

**Definition:** Prefill processes available prompt tokens; decoding generates continuation tokens.

**Explanation:** Separate their latency and memory behavior when diagnosing serving performance.

### Queries, keys, and values (QKV)

**Definition:** Learned representations used to match information requests to available content and combine that content.

**Explanation:** Q asks, K matches, V carries; this intuition is not a literal semantic label on each vector component.

### Recurrent neural network (RNN)

**Definition:** A network with state updated sequentially from earlier state and current input.

**Explanation:** Long short-term memory (LSTM) adds gates to help manage information; recurrence limits parallelism across dependent positions.

### Residual connection and layer normalization

**Definition:** A residual connection adds a sublayer's input to its output; layer normalization normalizes features within a representation.

**Explanation:** Both support trainability, but placement and implementation vary; a regression residual is a different concept.

### Temperature and sampling

**Definition:** Temperature rescales logits before a random draw from a model distribution.

**Explanation:** Lower temperature concentrates probability; sampling changes diversity, not whether a claim is supported.

### Token and tokenizer

**Definition:** A token is a model input/output unit; a tokenizer maps content into token IDs.

**Explanation:** Tokens can be subwords or punctuation rather than whole words; the tokenizer must match the checkpoint.

### Top-k and top-p

**Definition:** Top-k sampling limits candidate tokens by count; top-p sampling uses a cumulative probability-mass cutoff.

**Explanation:** Retrieval top-k instead means the number of ranked documents returned; the same notation refers to different operations.

### Transformer

**Definition:** A neural architecture combining attention with feed-forward transformations, residual paths, and normalization.

**Explanation:** Known positions can be processed in parallel during training; ordinary causal generation still adds new tokens sequentially.

### Variational autoencoder (VAE)

**Definition:** A latent-variable generative model trained with an approximate posterior and a probabilistic reconstruction objective.

**Explanation:** Its latent representation can support sampling and interpolation; generated quality depends on modeling and training choices.

### Vector, matrix, and tensor

**Definition:** A vector is an ordered numeric list, a matrix a two-dimensional numeric array, and a tensor the more general multidimensional structure.

**Explanation:** Dimensions describe shape; matching shapes alone does not mean two embedding spaces are compatible.

## Prompting and fine-tuning

[Examples and deeper explanations](questions/fine-tuning.md). Further reference: [LoRA](https://arxiv.org/abs/2106.09685), [QLoRA](https://arxiv.org/abs/2305.14314), and [DPO](https://arxiv.org/abs/2305.18290).

### Activation checkpointing

**Definition:** Saving memory by recomputing some intermediate activations during backpropagation instead of retaining all of them.

**Explanation:** This trades computation for memory; it is different from saving model weights or durable workflow progress.

### Adapter

**Definition:** A small trainable component added to or associated with a pretrained model for adaptation.

**Explanation:** An adapter needs its compatible base and configuration; switching adapters is not equivalent to replacing the entire model.

### Catastrophic forgetting

**Definition:** Loss of previously useful capabilities during subsequent training.

**Explanation:** Evaluate retained abilities separately from target-task generalization; target improvements can coexist with broad regressions.

### Chain-of-thought and reasoning trace

**Definition:** Intermediate reasoning text generated while solving or explaining a task.

**Explanation:** A persuasive trace is not proof of correctness or a faithful account of internal computation; validate checkable outcomes.

### Chat template and message role

**Definition:** A chat template serializes messages into the model's expected token format; roles identify their intended functions.

**Explanation:** Correct formatting helps interpretation, but privileged access must be enforced by the application.

### Checkpoint

**Definition:** Saved model state for loading or resuming training; in agent execution, a saved record of workflow progress.

**Explanation:** A model checkpoint is not an execution checkpoint. Neither term alone specifies all configuration needed for safe reproduction.

### Continued pretraining (CPT)

**Definition:** Additional training on text using a language-modeling objective after initial pretraining.

**Explanation:** It can adapt to domain language but does not by itself teach the desired instruction-response format.

### Direct preference optimization (DPO)

**Definition:** A training approach that uses preferred/rejected response pairs and a reference policy in a direct preference objective.

**Explanation:** Unlike a classic RLHF pipeline, it need not fit a separate reward model and run online RL; preference biases still matter.

### Fine-tuning

**Definition:** Updating pretrained model parameters for a more specific distribution or objective.

**Explanation:** It changes learned behavior; retrieving current facts at inference usually does not update weights.

### Knowledge distillation

**Definition:** Training a student using outputs, distributions, or representations from a teacher model.

**Explanation:** Agreement is a supervision signal, not the final goal; students can copy teacher errors.

### Loss masking and padding

**Definition:** Loss masking excludes selected tokens from the objective; padding equalizes shapes; truncation drops content to meet limits.

**Explanation:** Inspect which target tokens survive and receive loss; otherwise a run may train the wrong behavior.

### Low-rank adaptation (LoRA)

**Definition:** Adapting selected weight matrices with a trainable low-rank update while freezing the base.

**Explanation:** Rank controls update capacity and parameter cost; r(d_in+d_out) parameters adapt one d_out by d_in matrix.

### Parameter-efficient fine-tuning (PEFT)

**Definition:** Adapting a model by training a relatively small subset of parameters or added components.

**Explanation:** Frozen base weights and activations still consume memory, so trainable-parameter savings are not total-memory savings.

### Policy and return

**Definition:** In RL, a policy selects actions from observations or state, and return aggregates rewards over time.

**Explanation:** Discounted return weights later rewards by powers of a factor gamma; “policy” can instead mean a business rule in application discussions.

### Pretraining and base model

**Definition:** Pretraining learns broad patterns before task-specific adaptation; a base checkpoint is the resulting model before instruction-focused post-training.

**Explanation:** Base models may continue text rather than follow a request as a conversational assistant would.

### Prompt and prompt engineering

**Definition:** A prompt is the input context and instructions supplied to a model; prompt engineering designs and evaluates that input.

**Explanation:** A prompt can specify behavior but does not enforce permissions or guarantee correctness.

### Prompt injection

**Definition:** Untrusted content attempting to redirect a model's instructions or actions.

**Explanation:** Retrieved pages and tool results can carry attacks; delimiters help organization but do not enforce security boundaries.

### QLoRA and NF4

**Definition:** QLoRA trains low-rank adapters with a quantized frozen base; NF4 is the NormalFloat 4-bit representation used in the original method.

**Explanation:** Stored weight precision differs from computation and optimizer precision; verify the exported serving configuration separately.

### RLHF and reward model

**Definition:** Reinforcement learning from human feedback uses human judgments to help define a reward signal for policy optimization.

**Explanation:** A classic pipeline learns a reward model from comparisons; optimizing its score does not guarantee real-world correctness.

### Structured output and schema

**Definition:** Structured output follows a machine-readable contract; a schema defines allowed fields, types, and constraints.

**Explanation:** JavaScript Object Notation (JSON) syntax can be valid while the values violate business rules or contain invented facts.

### Supervised fine-tuning (SFT)

**Definition:** Fine-tuning on examples of inputs and desired outputs.

**Explanation:** Instruction tuning is SFT focused on following requests; demonstrations need consistent policies and held-out evaluation.

### Zero-shot and few-shot learning

**Definition:** Performing a task from instructions alone or from a small number of demonstrations in the input context.

**Explanation:** In-context learning normally does not update weights; demonstration selection and order can influence results.

## Retrieval and RAG terminology

[Examples and deeper explanations](questions/rag.md). Further reference: [RAG survey](https://arxiv.org/abs/2312.10997), [CRAG](https://arxiv.org/abs/2401.15884), and [Self-RAG](https://arxiv.org/abs/2310.11511).

### Agentic RAG

**Definition:** RAG in which an agent selects retrieval actions and may inspect and retrieve again.

**Explanation:** Bound calls, time, and permissions; added autonomy needs measured benefits over a fixed pipeline.

### Chunk and overlap

**Definition:** A chunk is a retrievable segment; overlap repeats part of neighboring segments.

**Explanation:** Small chunks can lose context and large chunks can dilute relevance; overlap also increases duplication and storage.

### Corrective RAG (CRAG)

**Definition:** A research approach that evaluates retrieved evidence and triggers corrective retrieval or refinement.

**Explanation:** The original method includes web retrieval; a private application must still constrain which fallback sources are permitted.

### Dense and sparse retrieval

**Definition:** Dense retrieval searches learned vectors; sparse representations have many zero-valued dimensions, often associated with terms.

**Explanation:** Sparse is not always synonymous with hand-written lexical scoring; learned sparse retrievers also exist.

### Entailment

**Definition:** A relationship in which evidence justifies a claim under the stated interpretation and assumptions.

**Explanation:** Sharing keywords with a claim is not sufficient support; qualifications and negation can reverse meaning.

### Entity resolution

**Definition:** Determining which records or mentions refer to the same real-world entity.

**Explanation:** Confusing two companies with similar names can create incorrect graph relationships and misleading retrieval results.

### Freshness and deletion propagation

**Definition:** Freshness measures how current served information is; deletion or revocation propagation removes stale content or access across derived systems.

**Explanation:** Updating an index does not invalidate every cached answer automatically.

### Gold-context evaluation

**Definition:** Testing generation with known relevant evidence supplied directly.

**Explanation:** Comparing it with the full pipeline helps separate retrieval failure from failure to use evidence.

### Hybrid retrieval

**Definition:** Combining complementary retrieval signals, commonly lexical and dense search.

**Explanation:** Fusion requires evaluation on actual queries; hybrid does not automatically mean more accurate.

### Ingestion and indexing

**Definition:** Ingestion converts sources into usable records; indexing builds structures for efficient retrieval.

**Explanation:** Parsing, permissions, document versions, and deletion propagation affect whether retrieved evidence is trustworthy.

### Knowledge graph and Graph RAG

**Definition:** A knowledge graph represents entities and relationships; Graph RAG retrieves graph-connected evidence for generation.

**Explanation:** Multi-hop questions need several linked relationships; every necessary edge needs trustworthy provenance.

### Lexical retrieval and BM25

**Definition:** Retrieval based on term matches; BM25 scores matches using term frequency, document frequency, and length normalization.

**Explanation:** It is useful for exact codes and rare names, but may miss semantically related wording without shared terms.

### Naive, Advanced, and Modular RAG

**Definition:** Naive retrieves then generates; Advanced improves pipeline stages; Modular composes interchangeable components.

**Explanation:** These broad design categories overlap with hybrid, graph, and agentic approaches rather than forming exclusive levels.

### Parent-child and multi-vector retrieval

**Definition:** Parent-child retrieval searches small segments then expands context; multi-vector retrieval stores multiple representations for one content unit.

**Explanation:** Both need stable links back to the source and permission checks on everything expanded or returned.

### Query rewriting and decomposition

**Definition:** Rewriting changes a search query's expression; decomposition separates it into smaller evidence needs.

**Explanation:** Preserve entities, dates, and negation so improved recall does not come from changing the user's question.

### Reciprocal rank fusion (RRF)

**Definition:** Combining ranked lists by summing contributions such as 1/(c+rank) for each item.

**Explanation:** It avoids comparing incompatible raw scores; document identity, rank cutoff, and the constant c still matter.

### Reranker

**Definition:** A model or procedure that reorders an already retrieved candidate set.

**Explanation:** It can improve ordering but cannot recover evidence missing from the candidates.

### Retrieval-augmented generation (RAG)

**Definition:** Generating an answer using external evidence retrieved for the request.

**Explanation:** Retrieval can improve access to current facts but does not guarantee that the answer uses them correctly.

### Self-RAG

**Definition:** A research method training a model to decide when to retrieve and critique evidence and outputs using reflection tokens.

**Explanation:** A generic prompt asking for self-review is not equivalent to the original trained method.

### Text-to-SQL

**Definition:** Translating a natural-language request into Structured Query Language for a database.

**Explanation:** Executable SQL can still use wrong joins or filters; verify semantic results and enforce permissions independently.

### Vector index and approximate nearest neighbors

**Definition:** A structure for similarity search over vectors; approximate nearest-neighbor search trades exactness for efficiency.

**Explanation:** Measure neighbor recall separately from evidence relevance; fast search cannot repair an unsuitable representation.

## Agents, orchestration, and software delivery

[Examples and deeper explanations](questions/agents.md). Further reference: [Google ML Glossary: agents](https://developers.google.com/machine-learning/glossary#agent) and the component references in the linked question banks.

### Acceptance criteria

**Definition:** Observable requirements that determine whether an artifact or task meets its intended contract.

**Explanation:** Specify conditions and measurement methods so completion is not based on confidence or presentation quality.

### Action space

**Definition:** The set of actions available to an agent under its interface and permissions.

**Explanation:** A narrower action space can simplify planning and limit consequences of mistakes.

### Agent

**Definition:** Software that selects actions from observations and state to pursue a task.

**Explanation:** Autonomy is bounded by available tools and permissions; an agent's final message is not evidence that an external action succeeded.

### Artifact and digest

**Definition:** An artifact is a produced file or bundle; a digest identifies its bytes; a revision identifies a recorded version.

**Explanation:** Link tests and approvals to the exact deployed artifact, not merely a branch name that can move.

### Authentication and authorization

**Definition:** Authentication establishes identity; authorization determines permitted access or actions.

**Explanation:** An access-control list (ACL) is one permission representation. A model deciding something is useful does not authorize it.

### Canary, shadow, and rollback

**Definition:** A canary exposes a limited audience; shadow execution processes real inputs without serving its outputs; rollback restores a prior configuration.

**Explanation:** State migrations and external effects may prevent complete reversal even when old code is restored.

### CI/CD

**Definition:** Continuous integration checks integrated changes frequently; continuous delivery keeps validated releases deployable; continuous deployment automatically releases eligible changes.

**Explanation:** “CI” can also mean confidence interval in statistics; this repository uses CI/CD for software delivery.

### Deadline and cancellation

**Definition:** A deadline limits task duration; cancellation requests that ongoing or future work stop.

**Explanation:** Neither automatically rolls back a completed external write; cancellation must account for uncertain effects.

### Deterministic check

**Definition:** A rule whose result is fixed for the same relevant inputs and execution conditions.

**Explanation:** Schema validation and exact arithmetic can be checked mechanically; determinism does not make an incorrect rule correct.

### Durable execution

**Definition:** Execution that persists enough progress to resume after interruption.

**Explanation:** Checkpointing progress does not guarantee exactly-once external effects; ambiguous operations still need reconciliation.

### Feature flag

**Definition:** A configuration switch controlling whether a behavior is exposed.

**Explanation:** It can separate deployment from activation, but does not replace compatibility tests or access control.

### Guardrail

**Definition:** A constraint, check, or intervention intended to limit undesired behavior.

**Explanation:** A model-based filter is fallible; authorization and resource limits should use trusted runtime enforcement.

### Human-in-the-loop

**Definition:** A workflow involving human judgment or authorization at specified points.

**Explanation:** Approval should refer to a concrete action and version; changing its amount or target can invalidate it.

### Idempotency

**Definition:** Repeating a logical operation has the same intended effect as applying it once.

**Explanation:** An idempotency key lets a service recognize repeated requests; its scope and retention must match the operation.

### Invariant

**Definition:** A property required to remain true across valid operations or state transitions.

**Explanation:** A refund total never exceeding the approved amount is an invariant that can be checked independently of generated prose.

### Lease and fencing token

**Definition:** A lease grants temporary ownership; a fencing token identifies a newer ownership generation.

**Explanation:** Reject writes from expired owners even if they resume after a replacement worker starts.

### Merge queue and semantic conflict

**Definition:** A merge queue serializes integration with checks; a semantic conflict is incompatible behavior without necessarily conflicting text edits.

**Explanation:** Validate the combined revision rather than relying only on individually passing branches.

### Orchestration

**Definition:** Coordination of tasks, workers, dependencies, shared state, and recovery.

**Explanation:** It governs system progress beyond an individual agent's next-action decision.

### Planning and termination

**Definition:** Planning organizes actions toward a goal; termination defines when execution ends.

**Explanation:** Verified completion, missing authority, or exhausted budgets are different terminal outcomes.

### Procedural memory

**Definition:** Stored instructions or procedures describing how to perform a task.

**Explanation:** An agent might retrieve a saved search-and-summarize procedure. This differs from semantic memory for facts and episodic memory for past events; persistence does not imply automatic learning or verified correctness.

### Pull request (PR)

**Definition:** A proposed code change submitted for review and integration.

**Explanation:** In metric discussions PR instead means precision–recall; spell out the meaning when both occur nearby.

### Regression test and mutation testing

**Definition:** Regression tests check that existing behavior remains valid; mutation testing changes code to see whether tests detect faults.

**Explanation:** Line coverage alone measures execution, not the strength of assertions or specification correctness.

### Retry and backoff

**Definition:** A retry repeats an operation; backoff delays repeats; jitter randomizes the delay to reduce synchronized bursts.

**Explanation:** Bound attempts across the whole task tree and distinguish transient from permanent failures.

### Sandbox and least privilege

**Definition:** A sandbox restricts execution resources; least privilege grants only the access needed for a task.

**Explanation:** Isolation reduces consequences of unsafe code or misleading instructions but needs correctly configured boundaries.

### Shared state and optimistic concurrency

**Definition:** Shared state is data accessed by multiple workers; optimistic concurrency accepts updates only if the expected version is still current.

**Explanation:** Version checks prevent stale writes from silently overwriting newer progress.

### Side effect and reconciliation

**Definition:** A side effect changes external state; reconciliation determines what actually happened when local and external records disagree.

**Explanation:** A timeout after a write is ambiguous: retry only after checking state or using a valid idempotency mechanism.

### Software factory

**Definition:** A coordinated delivery system spanning requirements, implementation, verification, integration, release, and feedback.

**Explanation:** It is broader than a coding assistant; useful autonomy still requires evidence gates and human responsibility.

### Supervisor and handoff

**Definition:** A supervisor assigns and integrates work; a handoff transfers a task contract and evidence to another worker.

**Explanation:** Peer coordination distributes those responsibilities but still needs ownership and conflict-resolution rules.

### Task graph and critical path

**Definition:** A graph records task dependencies; a directed acyclic graph has no cycles; the critical path limits completion time.

**Explanation:** Parallel workers cannot bypass true dependencies, and integration adds work beyond worker execution.

### Tool calling

**Definition:** A model producing a structured proposal to invoke an external operation.

**Explanation:** The runtime validates arguments, checks authorization, executes the operation, and returns its result.

### Workflow

**Definition:** A coordinated sequence or graph of operations with defined control flow.

**Explanation:** A workflow can contain model calls and agentic steps without making every transition model-selected.

### Working state and memory

**Definition:** Working state records current task progress; persistent memory stores selected information across tasks.

**Explanation:** Model context, runtime memory capacity, and stored user preferences are distinct uses of the word memory.

## Serving, reliability, and supporting terms

[Examples and deeper explanations](questions/production-engineering.md). Further reference: [Google SRE: service objectives](https://sre.google/sre-book/service-level-objectives/) and [OpenTelemetry: traces](https://opentelemetry.io/docs/concepts/signals/traces/).

### Admission control and backpressure

**Definition:** Admission control limits accepted work; backpressure slows producers; load shedding rejects work to preserve service.

**Explanation:** Bounded queues make overload explicit instead of converting it into unbounded waiting and resource exhaustion.

### Amdahl's law

**Definition:** A bound on parallel speedup determined by the fraction of work that remains serial.

**Explanation:** With serial fraction s and p workers, ideal speedup is at most 1/(s+(1−s)/p), before coordination overhead.

### API and SDK

**Definition:** An application programming interface defines program interactions; a software development kit packages tools for using an interface.

**Explanation:** An API request can fail or time out independently of whether an external action completed.

### Atomic operation and transaction

**Definition:** An atomic operation is indivisible at its defined boundary; a transaction groups work with specified consistency and failure guarantees.

**Explanation:** A database transaction does not automatically include an external API call, so cross-system side effects need additional coordination.

### Big-O notation

**Definition:** A notation describing how a resource bound grows with input size, ignoring constant factors.

**Explanation:** O(n²) growth does not predict exact elapsed time or memory on a particular implementation.

### Bytes and memory units

**Definition:** A byte is eight bits; GB means 10^9 bytes, while GiB means 2^30 bytes.

**Explanation:** Distinguish stored weights, activations, optimizer state, and KV memory when estimating whether a workload fits.

### Circuit breaker and fallback

**Definition:** A circuit breaker temporarily blocks calls to an unhealthy dependency; a fallback supplies an alternative path.

**Explanation:** The alternative still needs valid quality, privacy, and schema behavior; a fast wrong answer is not a successful recovery.

### Continuous batching

**Definition:** Serving requests together while allowing sequences to enter or leave as generation progresses.

**Explanation:** It improves utilization for variable-length requests, but scheduling and queue delays still affect user latency.

### Cost per successful task

**Definition:** Total included cost divided by verified successful tasks or accepted changes.

**Explanation:** Include failed attempts and state whether human review, infrastructure, and tool costs are counted.

### CPU, GPU, and accelerator

**Definition:** A CPU handles general computation; a graphics processing unit supports extensive parallel numeric work; an accelerator specializes computation.

**Explanation:** Hardware suitability depends on kernels, memory, and workload, not just nominal peak operations.

### Error budget

**Definition:** The amount of failure permitted by an SLO over its window.

**Explanation:** A 99.9% success target allows 0.1% bad eligible events; budget burn describes how quickly that allowance is consumed.

### Floating-point formats

**Definition:** Finite-bit representations of real numbers with a sign, exponent, and significand.

**Explanation:** Float32 uses 32 bits per value; float16 and bfloat16 use 16 but trade range and precision differently. Storage size excludes metadata and buffers.

### HTTP

**Definition:** Hypertext Transfer Protocol, a request-response protocol used by many model and tool services.

**Explanation:** Status 200 indicates protocol-level success, not that a generated answer is correct or satisfies its schema.

### Latency and percentiles

**Definition:** Latency is elapsed time for a defined operation; p95 is the value at or below which about 95% of observations fall.

**Explanation:** Report workload and measurement boundaries; averaging percentiles across servers does not generally yield the overall percentile.

### Little's Law

**Definition:** In a stable system, average in-flight work equals arrival rate times average time in the system.

**Explanation:** Use consistent boundaries and units and average latency, not p95, for L = lambda × W.

### Numerical precision and quantization

**Definition:** Numerical precision is the representational detail of stored/computed numbers; quantization maps values to a smaller representation set.

**Explanation:** This differs from classification precision. Smaller weights do not guarantee faster inference or unchanged quality.

### Observability and SRE

**Definition:** Observability supports inferring system behavior from outputs; site reliability engineering applies engineering methods to dependable operations.

**Explanation:** Metrics show trends, logs record events, and traces show request paths; monitoring needs defined responses to detected problems.

### Optical character recognition (OCR)

**Definition:** Converting text visible in images into machine-readable text.

**Explanation:** Reading order and table extraction errors can corrupt evidence before retrieval even begins.

### Rate limit and quota

**Definition:** A rate limit bounds activity per interval; a quota caps allocated usage or resources.

**Explanation:** Per-tenant limits prevent one customer's burst from exhausting shared capacity.

### Response, semantic, and prefix caches

**Definition:** Response caches reuse answers, semantic caches reuse by similarity, and prefix caches reuse model computation for matching prefixes.

**Explanation:** Their validity conditions differ; account for identity, evidence versions, model settings, and permissions.

### Service-level indicator (SLI)

**Definition:** A measured property of service behavior, such as the fraction of eligible requests completing successfully.

**Explanation:** Define eligibility and success from the user's perspective; HTTP success can still contain an unusable model output.

### Service-level objective (SLO)

**Definition:** A target for an SLI over a stated evaluation window.

**Explanation:** A 99.9% request-success objective differs from a time-based availability objective.

### Speculative decoding

**Definition:** A draft mechanism proposes tokens that a target model verifies in groups.

**Explanation:** Suitable acceptance/correction algorithms can preserve the target sampling distribution; speed depends on acceptance and overhead.

### Tenant

**Definition:** A customer or security scope sharing application infrastructure with others.

**Explanation:** Enforce isolation in retrieval, caches, tools, and logs; shared infrastructure does not imply shared access.

### Throughput and concurrency

**Definition:** Throughput is completed work per unit time; concurrency is the amount in progress simultaneously.

**Explanation:** More concurrent work can increase queueing and memory pressure without increasing useful throughput.

### Time to first token (TTFT)

**Definition:** Time from a stated request start to the first generated token received at the measured boundary.

**Explanation:** Inter-token latency measures subsequent streaming gaps; fast TTFT can coexist with slow full completion.

### Time to live (TTL)

**Definition:** A duration after which cached data or a temporary resource is no longer considered valid.

**Explanation:** TTL limits reuse time but does not guarantee freshness before expiry; permissions or source changes may require earlier invalidation.

### Trace and span

**Definition:** A trace connects operations for one request or task; a span records one operation's timing and metadata.

**Explanation:** Propagate identities across tools and workers while redacting sensitive content and limiting metric-label cardinality.

### VM and container

**Definition:** A virtual machine virtualizes a machine environment; a container isolates processes using operating-system facilities.

**Explanation:** Both can support reproducible agent execution, but their isolation properties and configuration differ.

## Mathematical and statistical supporting terms

[Examples and deeper explanations](questions/ai-foundations.md). Further reference: [scikit-learn: linear models](https://scikit-learn.org/stable/modules/linear_model.html) and the validation references in the linked question bank.

### Conditional probability

**Definition:** Conditional probability describes an event given information; a prior precedes observed evidence and a posterior incorporates it.

**Explanation:** A likelihood treats observed data as fixed while varying model parameters; it is not itself a probability distribution over parameters.

### Covariance and correlation

**Definition:** Covariance measures joint linear variation; correlation standardizes that relationship by the variables' spread.

**Explanation:** Correlation does not prove causation, and low linear correlation does not exclude nonlinear dependence.

### Eigenvalue and singular value

**Definition:** Eigenvalues describe scaling along a square matrix's eigenvectors; singular values describe the strengths of orthogonal directions in a matrix decomposition.

**Explanation:** PCA can use either a covariance eigendecomposition or a singular-value decomposition of centered data.

### Entropy

**Definition:** A measure of uncertainty in a probability distribution, commonly −sum p log p.

**Explanation:** The logarithm base sets units; entropy of predictions is not by itself a calibrated confidence estimate.

### Exclusive OR (XOR)

**Definition:** A Boolean operation that is true when exactly one of two inputs is true.

**Explanation:** The two-input XOR labels cannot be separated by a single line in the original two-dimensional input space.

### Fairness bias

**Definition:** Systematic disparities or harmful patterns affecting people or groups in data, predictions, or decisions.

**Explanation:** This differs from the bias term in bias–variance analysis; evaluation needs explicitly chosen fairness criteria and context.

### Gradient clipping

**Definition:** Limiting gradient magnitude before an optimizer update.

**Explanation:** It can stabilize very large updates but does not repair incorrect data or a badly chosen objective.

### Independent and identically distributed (IID)

**Definition:** Independent observations do not probabilistically depend on one another; identically distributed observations follow the same distribution.

**Explanation:** Multiple turns from one conversation may violate independence, affecting splits and uncertainty estimates.

### Matrix rank

**Definition:** The number of linearly independent columns or rows in a matrix.

**Explanation:** LoRA limits an update's rank; retrieval rank instead means a result's position in an ordered list.

### Mean, variance, and standard deviation

**Definition:** The mean is an arithmetic average; statistical variance measures average squared deviation from a mean; standard deviation is its square root.

**Explanation:** Prediction variance across training samples is a particular use of variance. Fold standard deviation is not automatically a confidence interval.

### Neural-network bias parameter

**Definition:** An additive learned offset in a unit such as z = w·x + b.

**Explanation:** The offset b differs from statistical prediction bias and fairness bias; an affine map combines a linear map and an offset.

### Prevalence

**Definition:** The proportion of evaluated cases belonging to the positive class.

**Explanation:** Precision can change when prevalence changes even if a model's true- and false-positive rates stay similar.

### Random seed and RNG

**Definition:** A seed initializes a pseudorandom number generator (RNG).

**Explanation:** Fixed seeds help reproduce sampled operations, but parallel kernels and changing runtimes can still prevent identical results.

### Sensitivity and specificity

**Definition:** In binary classification, sensitivity is recall; specificity is TN/(TN+FP), the fraction of negatives correctly rejected.

**Explanation:** Outside classification, sensitivity can mean response to a perturbation, so identify the intended meaning.

### Statistical significance

**Definition:** A decision about compatibility with a null hypothesis under a specified statistical test.

**Explanation:** A p-value is not the probability that a change is useful or that the null hypothesis is true; also report effect size and uncertainty.

### Vector norm

**Definition:** A function measuring vector size under a specified convention.

**Explanation:** The Euclidean norm is the square root of the sum of squared components; unit normalization divides by a nonzero norm.

## Terminology conventions

| Term with multiple meanings | State which meaning you intend |
| --- | --- |
| **Bias** | Statistical prediction bias, an additive model parameter, or social/fairness bias |
| **Precision** | Reliability of positive predictions or numerical representation precision |
| **Recall / sensitivity** | Positive-class detection; retrieval recall uses relevant evidence as its unit |
| **Rank** | Matrix independence dimension or position in a search result list |
| **Checkpoint** | Saved model state, durable execution progress, or activation recomputation strategy |
| **Normalization** | Feature scaling, unit-vector scaling, probability normalization, or layer normalization |
| **Top-k** | A sampling candidate limit or a retrieval result cutoff |
| **Memory** | Hardware storage, attention KV state, current context, or persistent application facts |
| **Policy** | An RL action-selection rule or a business/security requirement |
| **CI** | Continuous integration in software delivery; confidence interval in statistics |
| **Regression** | A numeric prediction task or a deterioration in previously working software behavior |

For every metric, state the positive class or relevance unit, numerator, denominator, cutoff, and aggregation where applicable. Define handling of empty sets and zero denominators. Numerical examples in the repository are illustrative unless explicitly identified as measured results.

## References and usage

The definitions and explanations here are original concise teaching text, consolidated with the existing question bank. The supplied glossaries were reviewed for vocabulary coverage and terminology cross-checks; this is not a reproduction of their entries. Technical detail is supported by primary documentation and research papers linked above and beside the full answers.

- [Google: Machine Learning Glossary](https://developers.google.com/machine-learning/glossary) — reference vocabulary for ML, neural networks, generative AI, and agents.
- [ML Cheatsheet: Glossary](https://ml-cheatsheet.readthedocs.io/en/latest/glossary.html) — supplementary study vocabulary for foundational concepts and mathematical notation.
- [GeeksforGeeks: 50 Machine Learning Terms Explained](https://www.geeksforgeeks.org/machine-learning/50-machine-learning-terms-explained/) — supplementary beginner vocabulary checklist; primary references govern technical distinctions.

When contributing, expand an unfamiliar acronym on first substantive use, link the relevant definition, and explain any application-specific meaning. Add or refine an entry when a new technical term appears. Keep a definition short; use the explanation to prevent a common misunderstanding and the question bank for the full treatment.
