# LouderMe — Official Releases

This **public binary distribution** repository belongs to **Michel's Lab** and is reserved exclusively for **LouderMe**. Development source code belongs to [michels-lab/LouderMe](https://github.com/michels-lab/LouderMe); Michel's Life is a completely separate application and distribution channel.

**Latest GitHub-published unified release (API checked 2026-10-21):** [Android v0.1.12 + Windows Desktop v0.1.13](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.12-desktop-v0.1.13), published 2026-10-12; six assets including APK, Setup, Portable and SHA-256 sidecars. This metadata check does not validate real audio output.

[Operación Granada — auditoría del repo de distribución y plugins](docs/GRANADA_DISTRIBUTION_PLUGIN_AUDIT_2026-10-21.md).

Current and future LouderMe unified stable releases contain **both Android and Windows** build artifacts under one release tag, with platform-specific version numbers and SHA-256 checksums. Older imported historical tags may contain only one platform:
- Android Direct APK: `LouderMe-vX.Y.Z-sideload.apk`
- Windows Setup: `LouderMe-Setup-vX.Y.Z.exe`
- Windows Portable: `LouderMe-Portable-vX.Y.Z.exe`

Direct update feeds: `louderme/latest.json` (Android) and `louderme-desktop/latest.json` (Windows). Google Play and Microsoft Store are provider-managed distribution channels.

## Legacy compatibility

Older installed builds query `michels-lab/michel-s-life-releases`. That repository's legacy LouderMe feeds and historic binaries MUST remain available until their old-client transition is independently confirmed. Do not remove or repoint assets to unpublished or unverified URLs.

## Provenance and security

Every migrated binary must match its original byte size, and where present its original SHA-256 sidecar. Future published builds must be sourced from verified LouderMe source releases. Do not store credentials, private signing keys, tokens, or user data in this repository. Its public content conveys no source-code license.

## Governance

Shared standards: [Michel-Software-Standards](https://github.com/michels-lab/Michel-Software-Standards). Each application retains its own project audit records and release identity. Michel's Lab slogan: **TOOLS WITH IDENTITY.**
