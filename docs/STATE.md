# State

Updated 2026-09-14 by Claude Code (Claude Opus 5).

## Phase

Two topics are open:

- **Pluggable monolith** (current focus): how to start a Python and Next.js product whose modules and vendors are pluggable by design, including the GenAI plane. Map: [topics/pluggable-monolith.md](topics/pluggable-monolith.md). Draft brief: [pluggable-monolith.html](pluggable-monolith.html) (published as an Artifact).
- **Context engineering** (paused): the components of the Hybrid Context Engine HLD. Map: [topics/context-engineering.md](topics/context-engineering.md).

## Now

The landscape for the pluggable monolith is researched and written (v0.1, evidence as of 2026-09-14), and the map is drafted with 12 concepts; concepts 1 to 6 are the Pareto core. The owner asked for progressive, Pareto-first lessons from scratch, each ending with a check question, and for labs to be containerised only at the end.

Lab 01 (ports and adapters) is concept 2 of the new map and concept 0 of context engineering. Steps 1 and 2 of 5 are done. The owner went straight from step 1 to step 2, so concept 1 (where seams go) hasn't had its own lesson yet; step 2's lesson used only its first rule.

## Next

1. The owner answers step 2's check question, which is recorded in the [latest log](log/2026-09-14-adapter-lab-step-2.md#done).
2. Lab 01 steps 3 to 5: the swap, conformance tests with a fake, and the leaks.
3. Teach concept 1 after the lab, as a short lesson that generalises from what the lab showed about a seam's cost and limits. The reason is that the owner chose to go concrete-first. If the owner wants the map's order instead, teach it before step 3.
4. The owner reviews the landscape, confirms or reorders the map, and answers its open questions ([§15](pluggable-monolith.html#open)): FastAPI or Django, where agents live, lab 01's home, and the lab domain.
5. Containerise lab 01 to the [lab standard](../labs/README.md), write its `docs/learn/` note and mark it done in both maps.
6. Host selected HTML documents on GitHub Pages. Still deferred; findings are in the [2026-09-13 log](log/2026-09-13-hld-and-repo-memory.md#researched-not-acted-on).

## Open questions

- The four in the landscape's §15. None block lab 01.

## Latest log

[2026-09-14 · Adapter lab step 2](log/2026-09-14-adapter-lab-step-2.md)
