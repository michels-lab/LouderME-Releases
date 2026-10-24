# Operación Granada — LouderMe Windows visual hotfix 0.1.16 distribution gates

Date: 2026-10-24. Product owner evidence: public Windows v0.1.15 displayed blank/collapsed About cards and a disconnected white logo plate; original EQ looked like a form rather than a graphical seven-band control.

## Product source implementation
- LouderMe source PR #107, main merge SHA `796c857e5128d4fbfa120e6e1eb091f0f7dbced8`, fixes four About cards, auto-scroll to top, compact label bounds, official brand SVG dark-transparent rendering and author studio magenta bitmap artifact. The seven-band graphic now supports live mouse drag at 0.5 dB intervals, preserving original numeric EQ/preset/Equalizer APO controls.
- Its exact-head Windows CI `40117533908` and Android CI `40117533782` passed. Six actual rendered Windows screenshots (Home/About/EQ at 600×520 and 900×700) were inspected individually, with SHA-bound installed-executable evidence, and both About and EQ were legible. These are UI evidence, *not* acoustic or native-driver proof.
- Separate Windows-only versioned release PR #108 defines stable v0.1.16; **its merge commit SHA and release source assets must be retrieved and checked, not inferred from this text**.

## Immutable unified release plan

1. Keep original signed Android **v0.1.12 / versionCode 13**, source SHA `ed0bd6da54c022ac05eba0b3760361f4bce056ff`, and its APK + SHA-256 sidecar unchanged. No Android rebuild, re-sign or flavor change.
2. Require a successful Windows stable source release `desktop-v0.1.16`, exact tag commit equal to merged release PR #108's SHA and four complete Windows assets (`LouderMe-Setup-v0.1.16.exe`, `LouderMe-Portable-v0.1.16.exe`, plus two SHA-256 files).
3. Only after evidence for (1) and (2), update dedicated distributor `louderme/unified-source-request.json` from Windows 0.1.15 to 0.1.16 with **exact new source merge SHA**. Do not alter Android fields. Merge through an authenticated PR; never overwrite old releases or bypass hash validation.
4. The stable distributor must check all six byte digests and immutable source tags and publish only `louderme-android-v0.1.12-desktop-v0.1.16`, non-draft/non-prerelease. Confirm both platform `latest.json` feeds updated, Windows to 0.1.16 and Android still 0.1.12; previous stable bundles remain accessible.
5. If publisher fails due Git push race, recover with the dedicated fail-closed workflow; do not assume creating release assets implies successful feed synchronization.

No RC, no changes to other apps, and no false claim that Equalizer APO has been replaced by a certified native Windows virtual audio driver.
