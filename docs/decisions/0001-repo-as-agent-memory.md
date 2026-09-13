# 0001 · The repo is the agents' memory

Status: accepted
Date: 2026-09-13

## Context and problem

Every agent session starts blank, and long sessions are compacted into a summary. Claude Code's auto memory and session transcripts exist only on the machine that produced them. The mechanics are in [session memory and compaction](../learn/session-memory-and-compaction.md). We need any agent, on any machine, to pick up from any point.

## Considered options

1. Tool-local memory: Claude Code auto memory and saved transcripts.
2. Memory kept in the repo, behind an agent-neutral entry point (`AGENTS.md`).
3. A spec-driven framework such as GitHub Spec Kit. It suits building features, not a learning log; revisit when building starts.

## Decision

Option 2.

- `AGENTS.md` is the single operating manual. `CLAUDE.md` is a symlink to it, because Claude Code reads `CLAUDE.md` and not `AGENTS.md`.
- `AGENTS.md` imports `README.md` and `docs/STATE.md`, so Claude Code reloads the current state at session start and after compaction.
- Knowledge is split by how long it lives: state is overwritten, the log is append-only, learn notes are edited in place, decisions are immutable, and labs are reproducible.
- Claude Code's auto memory is off for this project, so there is no second, machine-local memory.
- A checkpoint means updating the files, committing and pushing.

## Consequences

- The work survives compaction, the end of a session and a lost machine. Any agent that reads `AGENTS.md` can resume.
- Resuming is only as good as the last checkpoint, so the protocol in `AGENTS.md` asks for frequent ones.
- Everything is public. No secrets or raw transcripts can be committed, so raw sessions are not archived.
- Windows needs Developer Mode or admin rights for the symlink. The fallback is a one-line `CLAUDE.md` containing `@AGENTS.md`.
