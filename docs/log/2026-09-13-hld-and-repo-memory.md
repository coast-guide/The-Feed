# 2026-09-13 · HLD research and repo-as-memory setup

Agent: Claude Code (Claude Opus 5)

## Goal

Design the Hybrid Context Engine using current tools and evidence, then set the repo up so any agent can resume from any point.

## Done

- Researched and wrote the HLD: [hybrid-context-engine.html](../hybrid-context-engine.html).
- Created the public repo `coast-guide/The-Feed`; the first commit is `eb42cfe`.
- Set the repo up as the agents' memory: [ADR 0001](../decisions/0001-repo-as-agent-memory.md). The mechanisms behind it are in [session memory and compaction](../learn/session-memory-and-compaction.md).
- The owner resolved the HLD's five open questions: interface-first, scale-ready, source-agnostic, with compliance behind an interface. The result is HLD v0.2: decisions in [§11](../hybrid-context-engine.html#resolved), new [§4.1 Interfaces](../hybrid-context-engine.html#interfaces) and [§6.2 Policy and compliance](../hybrid-context-engine.html#policy).
- Added the owner's `/rigor` standard ("How to think") and the interface-first rule to [AGENTS.md](../../AGENTS.md).
- Reframed the repo after the owner's correction: it is for learning any topic. Added topic maps ([docs/topics/](../topics/README.md)) and the first one, [context engineering](../topics/context-engineering.md), with a draft order.
- Reviewed the whole repo for stale or repeated content. Removed the leftover agent-factory framing and the dead "Lab 01" reference, and dropped rules stated in more than one file. Reworded ADR 0001's option 3, which implied building happens here; its decision is unchanged, and the decisions rule now allows such corrections.
- Added the owner's lab standard: every lab is containerised, with its own README and a single `./lab` script as its only interface ([labs/README.md](../../labs/README.md), template in `labs/_template/`). Tested the template end to end with Docker 29.8.0 and Compose v5.1.4: up, run, inspect, logs and reset.

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
- I misread the owner's software-factory remark as the repo's subject and wrote it into the always-loaded README and STATE. It was only context for how finished topics get built. Both files are corrected.
