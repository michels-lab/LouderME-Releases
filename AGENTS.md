# Michel's Lab — LouderMe distribution agent rules

This repository is a **public binary/update distribution channel**, not the application's source repository. The source lives in `michels-lab/LouderMe`. The cross-project policy authority is `michels-lab/Michel-Software-Standards`: read its current `GLOBAL_RULES.md`, `standards/REPOSITORY_DISTRIBUTION_STANDARD.md` and `docs/AGENT_OPERATING_PROTOCOL.md` before making changes. Application-only managed child-agent blocks are not copied to distribution repositories.

## Continuous independent work while CI runs (mandatory)

After submitting a PR or starting a build, check, review or external verification, **do not remain idle or request another "continue" prompt**. Preserve each pending workstream's repository, branch, exact source SHA, run/check ID, result status and required next validation. Immediately advance another genuinely independent, eligible, unclaimed task (prefer a different repository) without changing pending evidence into PASS. Respect existing non-stale task claims; same-repository overlap requires explicit `parallel_safe: true` and distinct `parallel_scope` values from the master coordinator. Revisit the original exact candidate before any merge, closure or release. If there is no safe independent task, report the actual blocker rather than inventing work.

## Distribution safety boundaries

- No release creation, tag, upload, asset overwrite, update-feed modification or provider submission without explicit owner authorization and exact same-artifact validation.
- Never publish an artifact for a different Michel's Lab product in this channel.
- Preserve immutable historical download URLs and verified SHA-256/provenance; do not infer a signed or installed pass from a build pass.
- Documentation and agent-governance changes must not touch release-intent triggers or publish workflows.
- Keep product-specific release audit/history in this distribution repository; shared policy belongs in the master.
