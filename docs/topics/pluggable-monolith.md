# Pluggable monolith

Started 2026-09-14. Claude proposed this order as a draft; the owner may reorder it.

## Goal

Understand how to start a product as one codebase, with a Python backend and a Next.js UI, whose modules and vendors can be added, swapped or removed while the change stays inside that module plus one line of wiring. This includes the GenAI plane: model aliases, the gateway, routing and agents as modules. The understanding should be deep enough to defend each choice and to brief autonomous agents to scaffold such a project. The draft brief is the [Pluggable Monolith landscape](../pluggable-monolith.html).

Concepts 1 to 6 are the Pareto core; the rest apply them.

## Concepts

| # | Concept | Why it matters | Source | Status |
| --- | --- | --- | --- | --- |
| 1 | Where seams go: information hiding and balanced coupling | Decides what deserves an interface, since making everything pluggable is itself a cost | [§2](../pluggable-monolith.html#atoms) | not started |
| 2 | Ports and adapters | The mechanism behind every swap | [§2](../pluggable-monolith.html#atoms) | in progress: [lab 01](../../labs/01-adapter-pattern/README.md) |
| 3 | Module anatomy: public API, internals, owned data | The unit you add or remove | [§4](../pluggable-monolith.html#module), [§6](../pluggable-monolith.html#data) | not started |
| 4 | Boundary enforcement and the deletion test | Boundaries that don't fail the build erode, and coding agents erode them faster | [§7](../pluggable-monolith.html#enforce) | not started |
| 5 | Composition root and plugins | Makes removal a one-line change at build, boot or run time | [§8](../pluggable-monolith.html#compose) | not started |
| 6 | The model plane: aliases, gateway, routing | The most volatile dependency, and what an alias can't hide | [§10.2](../pluggable-monolith.html#models) | not started |
| 7 | Module communication: calls, events, outbox | How modules cooperate without knowing each other | [§5](../pluggable-monolith.html#talk) | not started |
| 8 | Contract-first frontend | Next.js feature modules on a generated client | [§9](../pluggable-monolith.html#web) | not started |
| 9 | AI features as modules | Tools over module APIs; MCP, AG-UI and A2A at the edges | [§10.3](../pluggable-monolith.html#ai-modules) | not started |
| 10 | Evals and tracing | How you know a model or prompt swap is safe | [§10.5](../pluggable-monolith.html#evals) | not started |
| 11 | Durable execution | Long-running agents and human approvals | [§10.4](../pluggable-monolith.html#durable) | not started |
| 12 | Extraction | Moving a module out without touching its callers | [§11](../pluggable-monolith.html#evolve) | not started |
