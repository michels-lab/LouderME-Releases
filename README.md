# LouderMe — Official Releases

This **public binary distribution** repository belongs to **Michel's Lab** and is reserved exclusively for **LouderMe**. Development source code belongs to [michels-lab/LouderMe](https://github.com/michels-lab/LouderMe); Michel's Life is a completely separate application and distribution channel.

**Latest verified stable release (API checked 2026-11-17):** [LouderMe Android Direct v0.1.15 + Windows Desktop v0.1.20](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.15-desktop-v0.1.20). This is a **stable, not RC**, unified release with **six verified assets**: permanently signed Android Direct APK (`versionCode 16`), Windows x64 Setup + Portable, plus three SHA-256 sidecars. Both source tags `v0.1.15` and `desktop-v0.1.20` point to the exact validated source commit `56d9340b9c856ade36a1c3b423e815953ed4fa88`. [Android source release and signed final APK QA](https://github.com/michels-lab/LouderMe/actions/runs/44048560498), [Windows source release, installer and installed GUI QA](https://github.com/michels-lab/LouderMe/actions/runs/44048560387) and [unified six-asset publisher](https://github.com/michels-lab/LouderME-Releases/actions/runs/44049980764) finished successfully.

- **Android APK SHA-256:** `74994244dc675de417976c0a96d19bd3c815cf33236c6d99a0704192fd30a0b1`.
- **Windows Setup SHA-256:** `cf74ec159255b89e0b645f85d7be1b74c8e85841dfd58f1668d8e57dd397f163`.
- **Windows Portable SHA-256:** `bace2efa281c27f250102ec3b3a8cfc243b200b9eb8f93607e4fd574f280c57f`.

Both official update feeds now reference these exact published versions, URLs and digests. **User acceptance is still pending**: this release was requested specifically to test Android Boost 275/300% restoration, Windows endpoint-specific volume/mute, and final Boost slider commitment on real devices. Windows global Boost still requires **Equalizer APO** installed on the actual output; the independent Windows virtual driver is not shipped. Android public `session-0` compatibility varies by OEM and third-party app. The 300% signal target is about +9.54 dB digital amplitude, not guaranteed physical loudness or distortion-free audio. No Microsoft Store, Google Play production, RC or Developer release was published.

**Verificación del propietario (2026-11-12):** después de probar la aplicación publicada, el propietario confirmó que **ya comprobó que todo funciona**. Queda asentada la aceptación funcional del paquete estable Android v0.1.14 / Windows v0.1.19, incluido el ajuste de Boost hasta **300%**. Esta declaración no equivale a un ensayo acústico cuantitativo ni acredita un driver nativo independiente. La trazabilidad y el alcance de la aceptación están en [RELEASE_AUDIT_LOG.md](RELEASE_AUDIT_LOG.md); el software y los checksums ya publicados no cambian por este registro.

**Previous stable release (2026-11-12):** [Android v0.1.14 + Windows v0.1.19](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.14-desktop-v0.1.19), the earlier owner-accepted 300% release. Historical [Android v0.1.13 + Windows v0.1.18](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.13-desktop-v0.1.18) also remains available.

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
