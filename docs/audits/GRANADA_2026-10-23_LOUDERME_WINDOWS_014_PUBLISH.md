# LouderMe Operación Granada — staged Windows v0.1.14 unified stable distribution

Date: 2026-10-23. Distribution repository: `michels-lab/LouderME-Releases`, **not** other apps.

## Expected inputs
- Android stays **v0.1.12 / versionCode 13** from `michels-lab/LouderMe` source SHA `ed0bd6da54c022ac05eba0b3760361f4bce056ff`. Preserve the original signed Android binary and SHA-256; do not build or re-sign Android.
- Windows becomes **v0.1.14**, with its `desktop-v0.1.14` source release expected from exact main merge commit `1477c47a3112d18e449a7eef64719d5655f1d1bb` of `michels-lab/LouderMe`, after Windows installed Setup/Home/About and Developer/APO gates pass.
- Release publisher is unchanged; branch modifies only the **staged** unified request JSON. This branch is not `main` and does not by itself publish binaries or change update feeds.

## Mandatory publish gates
1. Confirm source `desktop-v0.1.14` release exists with exactly four official Windows assets (Setup, Portable, two SHA-256 sidecars); validate all assets match released bytes and the source tag directly targets the requested SHA.
2. Confirm the exact Android `v0.1.12` tag still targets the canonical commit and includes the existing APK/checksum pair; do not alter Android's signing identity or versionCode.
3. Merge staged request to this **distribution** repository `main` only after both source releases are authenticated. The dedicated `publish-louderme-unified.yml` will independently download all six files, check checksums, refuse replacing an existing release with nonidentical bytes, publish the unique `louderme-android-v0.1.12-desktop-v0.1.14` tag and update both platform-specific manifest files.
4. Check public release is stable (not a candidate or prerelease), contains six official assets with nonzero sizes and checksums, Windows JSON feed points to v0.1.14, Android feed still v0.1.12. Confirm updater URLs resolve to that release.
5. Keep the older stable v0.1.13 and legacy update paths accessible. Never claim the new Windows binary removes the Equalizer APO dependency or passes physical acoustic verification; signed native driver issues #46/#48 remain OPEN.

## Product change
Windows v0.1.14 only updates recovery from an interrupted, consented −18 dB listening test, including fail-closed protection of externally modified Equalizer APO configuration. It is **not** evidence of global hardware DSP gain; actual physical playback still needs owner-side validation.

**Current status:** staged provenance, not public release; evidence must be updated with actual GitHub Actions job IDs, tag, assets and hashes after CI completion. Do not infer success from documentation or a queued workflow.
