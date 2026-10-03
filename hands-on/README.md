# Hands-on Python Exercises

[Back to the main README](../README.md) · [System design scenarios](../system-design/README.md)

Practice eight interview exercises in two matching notebooks:

- [Questions notebook](questions.ipynb): problem statements, embedded data, function/class stubs, and visible checks.
- [Answers notebook](answers.ipynb): the same problems and checks, with reference implementations and explanations of tradeoffs.

Use Python 3.10 or newer. Exercise code uses only the standard library and runs offline: no API keys, model downloads, accelerator, or external dataset are required. You need a Jupyter-compatible notebook environment to open and run the notebooks. These are small educational implementations, not production libraries.

## Sections

| Section | Exercises | Main skills |
| --- | --- | --- |
| ML data and metrics | 1. Group-aware split; 2. Binary classification metrics | Leakage prevention, reproducibility, edge cases |
| Retrieval and RAG | 3. Overlapping chunks; 4. Authorized vector retrieval | Boundaries, cosine similarity, ranking, isolation |
| Evaluation and validation | 5. Retrieval metrics; 6. Structured-response validation | Ranking quality, schemas, explicit failure behavior |
| Production utilities | 7. Bounded retries; 8. Scoped expiring cache | Failure classification, retry budgets, cache correctness |

Exercises 1–3 are suitable for an initial coding screen; 4–8 add intermediate design and debugging discussion. Allow approximately 15–30 minutes per exercise, including tests and explanation. They can be attempted independently after running the shared setup cell.

## Run locally

If you already have a notebook environment, select a compatible Python kernel and open the questions notebook. For a new JupyterLab environment, run these commands from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyterlab
python -m jupyterlab hands-on/questions.ipynb
```

On Windows, create the environment with `python -m venv .venv` and activate it in PowerShell with `.venv\Scripts\Activate.ps1` instead of the `source` command. Package installation needs internet access; the exercises themselves do not. See the [official JupyterLab installation guide](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) for other environments.

## Practice workflow

1. Run the shared setup cell, then read an exercise's contract and sample data.
2. Implement its marked stub without changing the provided checks.
3. Run the exercise's checks and add your own edge cases. The supplied checks are useful examples, not an exhaustive grader.
4. Explain complexity, assumptions, and what you would change for production.
5. Compare with the corresponding answer only after attempting a solution. Different implementations can be correct.
6. Restart the kernel and run the completed notebook from top to bottom to catch hidden state dependencies.

The questions notebook intentionally raises `NotImplementedError` in unfinished exercises, so **Run All stops at the first unsolved check**. To work out of order, run setup plus the chosen exercise's implementation and check cells. The answers notebook is intended to run top to bottom with every check passing.

## For interviewers

Select exercises appropriate to the role and ask candidates to describe their reasoning before coding. Assess correctness against the written contract, handling of boundaries, clarity, and ability to explain tradeoffs. The discussion prompts connect these small functions to the [system design scenarios](../system-design/README.md); do not require candidates to reproduce the reference implementation exactly.
