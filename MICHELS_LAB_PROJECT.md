# Michel's Lab Project Governance — LouderMe Releases

This is the dedicated, public **LouderMe Android and Windows release channel**, separate from both the LouderMe application source repository (`michels-lab/LouderMe`) and the Michel's Life release channel.

## Authority and scope
- Cross-project policy authority: `michels-lab/Michel-Software-Standards`.
- Machine-readable project declaration: `.michelslab/project.yml` (`role: distribution`).
- Local truth about public release assets, immutable downloads, update manifests and historical transitions: this repository's `README.md` and `RELEASE_AUDIT_LOG.md`.
- Local agent process: `AGENTS.md` and current master `GLOBAL_RULES.md`.

## Reporting and verification
Promote reusable security, version, licensing, CI or release-policy changes to the master standards repository. Keep actual release history and status here. Record source HEAD, validated build/run SHA, exact binary digest and **published** provider/customer artifact state independently.

A pending GitHub Actions run must not idle unrelated eligible work or be described as PASS. Continue independent work under master claim/parallel-scope rules, then return to the original candidate before any merge or release. Publication always requires explicit authorization and the separately validated release-channel workflow. Never copy Michel's Life artifacts into this channel.

## Safety
Never commit secrets, replace historical release assets in place or silently alter updater feeds. No distribution actions are authorized merely by editing this governance document.
