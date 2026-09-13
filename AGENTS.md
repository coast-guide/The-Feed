# AGENTS.md

How to work in this repo, for any agent or person. Claude Code reads this file through the `CLAUDE.md` symlink.

## Start every session here

Read these two files first. Claude Code imports them automatically, both at start and after compaction:

- @README.md
- @docs/STATE.md

Then check `git status` and `git log --oneline -10`, and read the latest log entry that STATE links to.

## Where things live

| Path | Holds | Rule |
| --- | --- | --- |
| `docs/STATE.md` | The handoff: phase, current focus, next steps, open questions | Overwrite it; keep it under 50 lines |
| `docs/log/` | What happened in each session | Append-only, one file per session |
| `docs/topics/` | One map per topic: its goal and an ordered list of concepts with their status | Edit in place |
| `docs/learn/` | Distilled knowledge, one concept per file, shared across topics | Edit in place; the only home for that concept |
| `docs/decisions/` | Decisions not already recorded in a design doc (the HLD keeps its own) | Never change an accepted decision; supersede it |
| `labs/` | Containerised experiments, one folder each | Drive a lab only through its `./lab` script |
| `docs/*.html` | Selected long-form documents | See [HTML documents](#html-documents) |

Each folder's `README.md` gives its file format.

## How to think

These rules come from the owner's `/rigor` standard and apply to every task.

1. **Establish today's date first.** Treat training knowledge as possibly stale, and research the current state of anything that changes, such as tools, versions, prices and benchmarks.
2. **Start with zero assumptions.** Read the relevant context (this repo, STATE, the sources) before concluding anything.
3. **Back every claim with evidence.** Verify it at the primary source (official docs, release APIs, papers), not in search snippets or summaries. Write dates as YYYY-MM-DD, put an "as of" date on facts that change, mark vendor-reported numbers, and say plainly what you couldn't verify.
4. **Think independently.** Reason like a scientist and an architect, weighing alternatives and failure scenarios. When the evidence contradicts the owner, a source or an earlier decision, say so and recommend a course instead of simply complying.
5. **Add value, not volume.** Bring the risk, the better option or the fact that changes the decision. Give one recommendation and the trigger that would change it. Cut generic filler.

## Rules

1. **One home per fact.** Before writing, find where the fact already lives and link to it. Never restate it in another file.
2. **The repo is the only memory.** Chat history, compaction summaries, transcripts and tool-local memory are temporary. Anything worth keeping goes into a file here. For this reason Claude Code's machine-local auto memory is turned off in `.claude/settings.json`.
3. **The repo is public.** Never commit secrets, tokens, credentials, personal data or raw session transcripts. Sanitise command output before putting it in a lab.
4. **Pareto.** Capture the few ideas that explain most of a topic, in the note format from `docs/learn/README.md`. Link to code, official docs or git history instead of copying them.
5. **Interface-first, scale-ready, source-agnostic.** Put every external dependency behind an interface with swappable adapters, design every tier to scale out from the start, and assume no particular source, database or vendor. The HLD applies this in its [§3 and §4.1](docs/hybrid-context-engine.html#principles).

## Checkpoints

A checkpoint moves the current state out of the conversation and into the repo. Make one after each unit of work, before anything risky or long, when the context is filling up, and before ending a session.

1. Update `docs/STATE.md` so that a fresh agent could continue without this conversation.
2. Add to the session's log entry, and file anything new where the table above says it lives.
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), for example `docs(learn): add compaction note`.
4. Push. An unpushed checkpoint is lost with the machine.

## Learning loop

1. Start each topic with a map in `docs/topics/`, using the format in that folder's README.
2. Work through the map in order. For each concept: pose a question, run a lab that makes it visible, record what you observe, distil it into a `docs/learn/` note, and record any decision.
3. Update the concept's status in the map, then checkpoint.

## HTML documents

Markdown is the default. A few long-form documents are standalone HTML, such as the HLD. Each is a complete HTML document and the source of truth. To show one as a claude.ai Artifact, publish a copy without its doctype, `html`, `head` and `body` wrapper, because the Artifact host adds its own. To add one:

1. Save it as `docs/<slug>.html` with a `<title>`.
2. Add a row to the Documents table in `README.md`.
3. Checkpoint.

Hosting for these isn't set up yet; `docs/STATE.md` tracks it.
