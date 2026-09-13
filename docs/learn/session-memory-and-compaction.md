# Session memory and compaction

As of 2026-09-13. The Claude Code specifics are verified against its [memory](https://code.claude.com/docs/en/memory) and [context window](https://code.claude.com/docs/en/context-window) docs.

## What

An agent session is one context window. It starts with only what the tool loads automatically; everything after that is conversation. When the window fills, the tool compacts it, replacing the conversation with a summary. Anything that existed only in the conversation survives only as well as that summary captures it.

## Why it matters in production

Long-running and autonomous agents work across many context windows and many machines. Without durable state outside the window, agents redo work, lose decisions, or declare work finished too early. Anthropic reported exactly these failure modes for long-running agents ([2025-11-26](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)).

## How it works (Claude Code)

- **Loaded at start:**
  - the system prompt;
  - `CLAUDE.md` files from the working directory upward, concatenated rather than overriding each other;
  - their `@imports`, resolved relative to the importing file, up to four hops deep;
  - unscoped `.claude/rules/`;
  - the first 200 lines or 25 KB of auto memory's `MEMORY.md`;
  - environment info, including git status and recent commits.
- **Loaded lazily:** `CLAUDE.md` files in subdirectories and path-scoped rules, when Claude reads a matching file.
- **After compaction:**
  - re-injected from disk: the project-root `CLAUDE.md` with its imports, unscoped rules, auto memory and the plan-mode plan;
  - re-read: up to five of the most recently edited files;
  - re-injected up to a cap: the bodies of invoked skills;
  - summarised along with everything else: context that hooks added earlier;
  - added back explicitly: the output of SessionStart hooks whose matcher is `compact`.
- **Auto memory is machine-local.** It lives in `~/.claude/projects/<project>/memory/`. The `autoMemoryDirectory` setting accepts only absolute or `~/` paths, so it can't point to a path that moves with the repo. Setting `autoMemoryEnabled: false` turns it off for one project.
- **AGENTS.md** is the cross-tool instruction file, stewarded by the Agentic AI Foundation and read by Codex, Cursor, Copilot, Jules and others ([agents.md](https://agents.md/)). Claude Code doesn't read it: link it with a symlink, or with a `CLAUDE.md` that contains `@AGENTS.md`.
- **Long-running harness patterns:**
  - Anthropic, 2025-11. An initializer agent writes a progress file, a JSON feature list and `init.sh`. JSON was chosen because the model is "less likely to inappropriately change or overwrite" it than Markdown. Each later session reads the git log and progress file, checks the app still works, does one piece of work, commits and updates the progress file.
  - Anthropic, 2026-04 ([reported by InfoQ](https://infoq.com/news/2026/04/anthropic-three-agent-harness-ai/)). Instead of compacting, it resets the context and passes structured handoff artifacts to the next agent. It also moves evaluation to a separate agent from the one generating the work.

## What breaks

- Instructions given only in chat are gone after compaction. Put them in `AGENTS.md`.
- Imported files load in every session and cost context every time, so keep them short.
- `CLAUDE.md` is delivered as a user message, not as the system prompt. It guides behaviour but doesn't enforce it; use hooks or permissions for anything that must happen.
- Block-level HTML comments in `CLAUDE.md` are stripped before injection, so an instruction hidden in one is never seen.
- An out-of-date handoff misleads the next session, which is why a checkpoint updates STATE first.

## Evidence

- Claude Code docs, checked 2026-09-13: [memory](https://code.claude.com/docs/en/memory), [context window](https://code.claude.com/docs/en/context-window), [hooks](https://code.claude.com/docs/en/hooks).
- Labs: none yet.

## Open questions

- What does a compaction summary actually keep? Inspect a real one.
- How do Codex and Cursor layer nested `AGENTS.md` files, compared with Claude Code's `CLAUDE.md`?
