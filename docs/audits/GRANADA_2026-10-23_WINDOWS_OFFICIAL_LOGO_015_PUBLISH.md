# Operación Granada — LouderMe official Windows logo stable release verification

Date: 2026-10-23. Sole product: LouderMe / Michel's Lab.

## Why this release exists
Owner supplied a real Windows LouderMe screenshot showing `auderMe` rather than `LouderMe` in the header, because the independently painted wave had a 150px minimum in an 88px column and overlapped the first letter. Also a generic titlebar WinForms icon. LouderMe source PR #104, merge commit `af8f8ef1f2e5d1e0ef29eb3e4801b89a60e0ec0e`, uses the canonical Option 4 `official-lockup.svg` and original product icon, adds runtime 480/600px layout regression and canonical-logo raster palette check, and assigns Windows-only version 0.1.15.

## Release source identities — immutable gates
- Preserve **signed Android 0.1.12 / code 13** at existing source SHA `ed0bd6da54c022ac05eba0b3760361f4bce056ff`. No new Android build or signature.
- Windows `desktop-v0.1.15` MUST be present as a successful stable source release at exact SHA `af8f8ef1f2e5d1e0ef29eb3e4801b89a60e0ec0e`, with unique new `LouderMe-Setup-v0.1.15.exe` and `LouderMe-Portable-v0.1.15.exe` plus SHA-256 sidecars. Source Windows release CI must pass actual installer startup, image/ICO product identity, Home/About screenshots, settings isolation, updater and APO contracts.
- This staging branch modifies **only** the unified publisher request JSON plus independent audit; it does not change public feeds, downloaded binaries or earlier release tags.

## Before accepting unified publication
1. Confirm source Windows release tag points exactly to the expected SHA and all four assets are uploaded, nonzero, stable (not draft/candidate).
2. Confirm Android source tag unchanged, complete APK and checksum.
3. Merge publisher request to dedicated distribution repo `main` only after both source releases exist. Publisher must verify all binary SHA-256, original source tag SHAs, six-asset immutability and execute its concurrent-audit Git push recovery (PR #8).
4. Verify public tag `louderme-android-v0.1.12-desktop-v0.1.15`, six assets, both `latest.json` updater manifests and previous releases remain accessible.
5. Public Windows installer is still **Equalizer APO-based**. This visual fix makes no sound-pressure/virtual-driver claims; physical hardware testing for native driver remains separate.

Current state: pre-publication staging, release gate not assumed passed.
