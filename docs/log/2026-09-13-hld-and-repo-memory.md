# 2026-09-13 · HLD research and repo-as-memory setup

Agent: Claude Code (Claude Opus 5)

## Goal

Design the Hybrid Context Engine using current tools and evidence, then set the repo up so any agent can resume from any point.

## Done

- Researched and wrote the HLD: [hybrid-context-engine.html](../hybrid-context-engine.html).
- Created the public repo `coast-guide/The-Feed`; the first commit is `eb42cfe`.
- Set the repo up as the agents' memory: [ADR 0001](../decisions/0001-repo-as-agent-memory.md). The mechanisms behind it are in [session memory and compaction](../learn/session-memory-and-compaction.md).

## Researched, not acted on

GitHub Pages for selected HTML documents, deferred by the user. Findings as of 2026-09-13:

- Free for public repos on GitHub Free. Each repo gets one site, and every file is served at its own path.
- Limits: a 1 GB site, a soft 100 GB/month bandwidth cap, and a soft 10 builds/hour for branch builds. Commercial and e-commerce sites aren't allowed.
- Latest actions: `actions/checkout` v7.0.1, `configure-pages` v6.0.0, `upload-pages-artifact` v5.0.0, `deploy-pages` v5.0.1. Pin them by commit SHA.
- Sketched plan:
  - Publish only a dedicated folder, through an Actions workflow.
  - Generate the README Documents table from each file's `<title>` and `<meta name="description">`.
  - Keep HTML sources as Artifact-compatible fragments and add the doctype wrapper at build time.

## Surprises

- Web search gave Pages action versions two majors out of date (v3/v4). The GitHub releases API showed the real ones, which is why AGENTS.md now requires primary sources.
- Several third-party guides say Claude Code falls back to reading `AGENTS.md`. The official docs say it doesn't.
