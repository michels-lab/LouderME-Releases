## Preventive agent contract — recurring-error guard (owner mandate 2026-10-21)

**Mandatory for every maintainer, QA, release, audit and developer-twin agent, regardless of model/provider.** Read the authoritative [Michel's Lab prevention standard](https://github.com/michels-lab/Michel-Software-Standards/blob/main/standards/AGENT_RECURRENCE_PREVENTION_STANDARD.md) before any development, audit, README status edit or release claim. These are instructions and deterministic checks, **not proof a separate live agent executed**.

1. **root-cause first:** For a recurring bug or false status, reproduce the failure, identify the owning code/process and why its earlier regression coverage failed. A bitácora, reopened issue, CSS workaround, renamed check or another prompt alone is NOT remediation.
2. **Same-failure regression:** Add at least one negative fixture/test that fails on the previously broken behavior and passes on the repair. Preserve affected workflows and data; for hardware/accounts/manual-only checks keep that gate PENDING, never silently turn it green.
3. **exact-head evidence:** Fetch latest main HEAD, active PRs/claims, required workflow runs, release tag and provider state separately. Only the same exact source SHA plus actual applicable validation can close the gate. A workflow name, release existence, old screenshot or green unrelated job is not proof.
4. **owning repo truth:** Put detailed findings, prevention steps, status and owner-specific follow-up in this product's audit and bitácora. **README** must directly link the owning audit and show the correct latest stable release metadata from GitHub's authoritative tag/assets, not a candidate version. Shared standards stay in Michel-Software-Standards; cross-product references are links only, never imported implementation.
5. **Cost/privacy:** no extra subscription, paid plugin, host, token, external account, install, dataset upload or user relationship/audio/scientific action without specific approval. Check privacy and domain boundaries (OpenFOAM only in scientific products; never in unrelated apps); no secrets in logs.
6. **Fail closed and explain:** Missing/in-progress/red CI, absent permissions or conflicting repo/release docs must be recorded as BLOCKED. Do not merge/publish a functional claim on documentation-only checks. Preventive agent/README drift is checked by the master read-only recurring guard, but this does not replace runtime QA. Reply in the conversation with ONE consolidated table of actual changes, errors, validations and remaining work rather than forcing the owner to open each repo.

This section is a preventive contract; follow product-specific rules below. Distribution repos own binaries and manifests only; source products own behavior and regression tests.

# Michel's Lab — LouderMe distribution agent rules

## Owner's Granada release authority — 2026-10-21

When the owner invokes **Operación Granada for this specific product**, agents MAY complete release integration, final versioning and **publish the official final STABLE release** without asking for a second release command, **only after all product-specific current-SHA tests, installed/device/runtime/scientific/privacy gates, validated artifacts, signing/integrity and update/distribution requirements have passed**. It is conditional authority, NOT an instruction to ship unfinished code on every Granada. **No RC, beta, prerelease, preview release or publication for other products.** A distribution repository may receive only its own app's verified final assets, never initiate independent releases. Follow master `GLOBAL_RULES.md` and `standards/RELEASE_PROTOCOL.md`; record tag, provenance, published assets and exact result. If any gate is missing, do not release and continue another independent block.


This repository is a **public binary/update distribution channel**, not the application's source repository. The source lives in `michels-lab/LouderMe`. The cross-project policy authority is `michels-lab/Michel-Software-Standards`: read its current `GLOBAL_RULES.md`, `standards/REPOSITORY_DISTRIBUTION_STANDARD.md` and `docs/AGENT_OPERATING_PROTOCOL.md` before making changes. Application-only managed child-agent blocks are not copied to distribution repositories.

## Continuous independent work while CI runs (mandatory)

After submitting a PR or starting a build, check, review or external verification, **do not remain idle or request another "continue" prompt**. Preserve each pending workstream's repository, branch, exact source SHA, run/check ID, result status and required next validation. Immediately advance another genuinely independent, eligible, unclaimed task (prefer a different repository) without changing pending evidence into PASS. Respect existing non-stale task claims; same-repository overlap requires explicit `parallel_safe: true` and distinct `parallel_scope` values from the master coordinator. Revisit the original exact candidate before any merge, closure or release. If there is no safe independent task, report the actual blocker rather than inventing work.

## Distribution safety boundaries

- No release creation, tag, upload, asset overwrite, update-feed modification or provider submission without owner authorization (including targeted Granada after all product gates pass) and exact same-artifact validation.
- Never publish an artifact for a different Michel's Lab product in this channel.
- Preserve immutable historical download URLs and verified SHA-256/provenance; do not infer a signed or installed pass from a build pass.
- Documentation and agent-governance changes must not touch release-intent triggers or publish workflows.
- Keep product-specific release audit/history in this distribution repository; shared policy belongs in the master.

## GRANADA — Regla permanente de continuación del propietario

Cuando el propietario diga **GRANADA**, se aparca con trazabilidad cualquier pendiente inacabado/bloqueado/en QA/propiedad de otra rama, y se aborda **el siguiente bloque grande independiente**. Consultar primero `.michelslab/GRANADA.md` y la norma maestra `standards/GRANADA_CONTINUOUS_BLOCK_PROTOCOL.md`; respetar claims, PRs y colisiones de archivos. Registrar SHA, tests y punto de retorno; no cerrar pendientes falsamente ni publicar releases sin autorización.
