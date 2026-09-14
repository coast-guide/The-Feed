# 2026-09-14 · Pluggable monolith landscape

Agent: Claude Code (Claude Opus 5)

## Goal

Start a second topic, separate from the HLD: how to set up a new product as a monolith (Python backend, Next.js UI) whose modules are decoupled and pluggable by design, and how GenAI (model routers and the like) shapes that design. The owner asked for research and the full landscape first, as of today, with the Pareto-first teaching to follow.

## Done

- Researched current versions from the PyPI, npm, Node.js, endoflife.date and GitHub APIs, and the patterns, tools and 2026 research from primary sources.
- Wrote the landscape as an HTML document: [pluggable-monolith.html](../pluggable-monolith.html), using the HLD's styles. It is published as a claude.ai Artifact and listed in the README's Documents table.
- Drafted the topic map [pluggable-monolith.md](../topics/pluggable-monolith.md), with 12 concepts; concepts 1 to 6 are the Pareto core.
- Lab 01 (ports and adapters) now serves both topics: it is concept 2 of the new map, and its README links to both.

## Researched, not acted on

- Nx and other build tools that span both languages were not evaluated; the landscape flags Nx 23 as the alternative to test.
- Feature-Sliced Design versus plain feature packages for Next.js: the landscape recommends starting with plain packages, and the lab will test it.
- GitHub Pages hosting for HTML documents is still deferred.

## Surprises

- Google's Service Weaver, often cited as the modular-monolith framework, has been archived. Its notice says adoption needed rewrites of large parts of existing applications.
- LLMRouterBench (2026-01) found that many routing methods, commercial routers included, fail to reliably beat a simple baseline. This is why the landscape recommends static routing first.
- A 2026 benchmark found coding agents strongly tend to generate monolithic code, which makes CI-enforced boundaries more important, not less.
- The LiteLLM PyPI compromise (2026-03-24) is the concrete case for isolating and pinning the model gateway.
- A search summary dated Kraken's monolith post to June 2026; the post itself is from 2023-07-11. Another reminder to read the primary source.
- FastAPI's own "bigger applications" layout groups code by technical layer (`routers/`), not by module, so the module structure has to come from us.
