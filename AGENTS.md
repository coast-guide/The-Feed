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
| `docs/learn/` | Distilled knowledge, one concept per file | Edit in place; the only home for that concept |
| `docs/decisions/` | Architecture decision records | Never edit an accepted one; supersede it |
| `labs/` | Runnable experiments, one folder each | Commands must reproduce the observations |
| `docs/*.html` | Selected long-form documents | See [HTML documents](#html-documents) |

Each folder's `README.md` gives its file format.

## Rules

1. **One home per fact.** Before writing, find where the fact already lives and link to it. Never restate it in another file.
2. **The repo is the only memory.** Chat history, compaction summaries, transcripts and tool-local memory are temporary. Anything worth keeping goes into a file here. For this reason Claude Code's machine-local auto memory is turned off in `.claude/settings.json`.
3. **The repo is public.** Never commit secrets, tokens, credentials, personal data or raw session transcripts. Sanitise command output before putting it in a lab.
4. **Pareto.** Record what, why, how, and what breaks in production. Link to code, official docs or git history instead of copying them.
5. **Primary sources, absolute dates.** Verify external facts at the source (official docs, release APIs, papers), not in search snippets. Write dates as YYYY-MM-DD, put an "as of" date on facts that change, and mark vendor-reported numbers.

## Checkpoints

A checkpoint moves the current state out of the conversation and into the repo. Make one after each unit of work, before anything risky or long, when the context is filling up, and before ending a session.

1. Update `docs/STATE.md` so that a fresh agent could continue without this conversation.
2. Add to the session's log entry. New knowledge goes in `docs/learn/` and new decisions in `docs/decisions/`, linked from the log.
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), for example `docs(learn): add compaction note`.
4. Push. An unpushed checkpoint is lost with the machine.

## Learning loop

For each topic: pose a question, run a lab that makes the mechanism visible, record what you observe, distil it into a `docs/learn/` note, record any decision, and checkpoint.

## HTML documents

Markdown is the default. A few long-form documents are standalone HTML, such as the HLD. To add one:

1. Save it as `docs/<slug>.html` with a `<title>`.
2. Add a row to the Documents table in `README.md`.
3. Checkpoint.

Hosting for these isn't set up yet; `docs/STATE.md` tracks it.
