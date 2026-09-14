# 2026-09-14 · Adapter lab step 2

Agent: Claude Code (Claude Opus 5)

## Goal

The owner finished step 1 of [lab 01](../../labs/01-adapter-pattern/README.md) and asked to continue. Build and teach step 2, the port.

## Done

- Built `step2_port/`: the core declares an `Embedder` port with its own error type, `acme_adapter.py` is the only file that knows Acme, and `main.py` picks the vendor. The results are in the lab's Observations.
- Taught it as a lesson. Because step 2 is where the lab first decides where a seam goes, the lesson opened with Parnas's rule from concept 1 of the [pluggable-monolith map](../topics/pluggable-monolith.md). Concept 1 itself has not been taught.
- Check question, not yet answered: Acme's SDK v3 returns plain lists instead of `Embedding` objects, and raises `acme.QuotaError` instead of `RateLimitError`. Which of step 2's three files change? If the adapter handled the lists but missed the new error, what would a user see during an Acme outage, and why can't the core fix that itself?

## Researched, not acted on

## Surprises
