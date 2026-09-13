# Context engineering

Started 2026-09-13. Claude proposed this order as a draft; the owner may reorder it.

## Goal

Understand each component of the [Hybrid Context Engine HLD](../hybrid-context-engine.html) well enough to defend its decisions and brief autonomous agents to build it. The HLD is the draft brief.

## Concepts

| # | Concept | Why it matters | HLD | Status |
| --- | --- | --- | --- | --- |
| 0 | Interfaces and adapters | The HLD's first principle: every component is an adapter behind a port, which keeps each choice reversible | [§3](../hybrid-context-engine.html#principles), [§4.1](../hybrid-context-engine.html#interfaces) | in progress: [lab 01](../../labs/01-adapter-pattern/README.md) |
| 1 | Question classes | Shows why top-k retrieval alone fails, and what each kind of question needs | [§2](../hybrid-context-engine.html#questions) | not started |
| 2 | Hybrid retrieval | Lexical plus dense search, fused, is the core retrieval loop | [§5.4](../hybrid-context-engine.html#projections) | not started |
| 3 | Reranking | Added +13.2 nDCG@10 to ViDoRe V3's text pipeline | [§5.5](../hybrid-context-engine.html#serving) | not started |
| 4 | Retrieval evaluation | Every later lab needs a way to measure its result | [§6.5](../hybrid-context-engine.html#eval) | not started |
| 5 | Parsing and chunking | Retrieval can't beat the quality of the text it searches | [§5.2](../hybrid-context-engine.html#understand) | not started |
| 6 | Embeddings and vector indexes | Where cost and scale are decided | [§5.4](../hybrid-context-engine.html#projections), [§7](../hybrid-context-engine.html#sizing) | not started |
| 7 | Permission-aware retrieval | The enterprise requirement that can't be compromised | [§6.1](../hybrid-context-engine.html#perm) | not started |
| 8 | Semantic layer and text-to-SQL | The structured half of the corpus | [§5.5](../hybrid-context-engine.html#serving) | not started |
| 9 | Entity linking | Joins documents to database rows | [§5.4](../hybrid-context-engine.html#projections) | not started |
| 10 | Planning hybrid questions | Typed handoffs and sufficiency checks across SQL and documents | [§5.5](../hybrid-context-engine.html#serving) | not started |
| 11 | Agent interface and agent-side context | How agents consume what the engine returns: MCP tools, context windows, compaction | [§5.6](../hybrid-context-engine.html#interface) | in progress: [note](../learn/session-memory-and-compaction.md) |
| 12 | Ingestion at scale | Connectors, change feeds and durable workflows | [§5.1](../hybrid-context-engine.html#connect) | not started |
| 13 | Policy and security | Data-flow policy and prompt injection | [§6.2](../hybrid-context-engine.html#policy), [§6.3](../hybrid-context-engine.html#security) | not started |
