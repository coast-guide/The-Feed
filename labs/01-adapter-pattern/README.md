# Lab 01 · What does the adapter pattern buy, and what can't it hide?

Date: 2026-09-13 · Versions: Python 3.12.13, standard library only
Topics: [context engineering](../../docs/topics/context-engineering.md), concept 0; [pluggable monolith](../../docs/topics/pluggable-monolith.md), concept 2

## Question

A core (here, a tiny semantic search) depends on vendors it doesn't control. What does putting an interface and adapters between them buy, what does it cost, and what still leaks through?

## Stack

Plain Python on the host, no dependencies. The owner asked to containerise at the end rather than the start (2026-09-13), so until then this lab is an exception to [labs/README.md](../README.md) rule 2.

- `vendors/`: two fictional embedding SDKs with deliberately different shapes. Treat them as code you can't change.
  - `acme.py`: client object, batches of at most 4, results as objects, `RateLimitError`.
  - `zenith.py`: module function, one text per call, results as nested dicts, `ZenithError(code)`.
  - `_toy_model.py`: the fake model behind both. Same length vectors, different spaces.

## Steps

Each step is a folder; diff neighbouring folders to see what changed.

| Step | Folder | Idea |
| --- | --- | --- |
| 1 | `step1_direct/` | The pain: the core calls a vendor directly |
| 2 | `step2_port/` | The port: the core defines the interface it needs |
| 3 | `step3_swap/` | The swap: a second adapter, and the core doesn't change |
| 4 | `step4_conformance/` | Proof: one test suite every adapter must pass, plus a fake |
| 5 | `step5_leaks/` | Limits: what an interface can't hide |

## Run

From this folder:

```sh
python3 -m step1_direct.search
python3 -m step1_direct.search_zenith
diff step1_direct/search.py step1_direct/search_zenith.py
```

## Observations

- **Step 1.** Both versions return the same answers. Switching vendor changed 21 lines, in both core functions: the import, the client, the call shape, the response shape, the batching rule and the error type.

## Findings

To come: a `docs/learn/` note once the lab is complete.
