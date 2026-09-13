# Labs

Runnable experiments, each making one concept visible. Every lab is containerised, so it runs the same way on any machine with Docker, whether a person or an agent runs it.

## Standard

1. **Start from the template.** Copy [`_template/`](_template/) to `NN-<slug>/`, numbered in order across all topics.
2. **Everything runs in containers.** The lab's `compose.yaml` defines its stack, with one container or as many as the lab needs. The host needs only Docker and Bash (on Windows, use WSL).
3. **One interface: `./lab`.** Each lab's `./lab` script is the only way to drive its stack, for people and agents alike.
   - Keep its standard commands (`./lab help` lists them) and adapt `run` and `inspect` to the lab.
   - Every command except `shell` is non-interactive and exits non-zero on failure.
   - For a new operation, add a command to the script instead of calling `docker` directly.
4. **A dedicated README.** Each lab's `README.md` follows the template's: question, stack, how to run, what to inspect, observations and findings.
5. **Reproducible and safe to publish.** Pin every image to a version tag and never use `latest`. Secrets go in the lab's `.env`, which git ignores; commit a `.env.example` listing only the variable names.
