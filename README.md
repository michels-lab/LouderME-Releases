# LouderMe — Official Releases

This **public binary distribution** repository belongs to **Michel's Lab** and is reserved exclusively for **LouderMe**. Development source code belongs to [michels-lab/LouderMe](https://github.com/michels-lab/LouderMe); Michel's Life is a completely separate application and distribution channel.

**Latest verified stable release (API checked 2026-11-17):** [Android Direct v0.1.15 + Windows Desktop v0.1.21](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.15-desktop-v0.1.21), **stable, not RC**, six published assets: unchanged permanently signed APK (Android versionCode 16), Windows x64 Setup and Portable binaries, plus the three SHA-256 checksum sidecars. Android source tag `v0.1.15` points to `56d9340b9c856ade36a1c3b423e815953ed4fa88`; Windows source tag `desktop-v0.1.21` points to `636cabe68b4840ff88836decb3fa01fedf5f8075`. The [Windows installed-binary/visual release pipeline](https://github.com/michels-lab/LouderMe/actions/runs/44202331212) and [unified publisher](https://github.com/michels-lab/LouderME-Releases/actions/runs/44202720915) passed, and the Android v0.1.15 APK is **the same already validated and signed binary** from the [Android source release](https://github.com/michels-lab/LouderMe/releases/tag/v0.1.15).

- **Android Direct v0.1.15 APK SHA-256:** `74994244dc675de417976c0a96d19bd3c815cf33236c6d99a0704192fd30a0b1` (unchanged).
- **Windows Desktop v0.1.21 Setup SHA-256:** `636010b73b8a3fbcd89978ed8a3162b20e8b3307a6965dcf6459ce6c889d5789`.
- **Windows Desktop v0.1.21 Portable SHA-256:** `dfec5625c71e77b32f936be6a2445113950f67440d0f30854167fd711df6ee3a`.

Both official updater manifests now reference this public release and exact asset digests. Windows v0.1.21 replaces the old white audio-output ComboBox with a LouderMe-dark picker and a separate "Follow Windows default output" checkbox, device labels and connection badges. Volume/mute remain 0–100% for one exact selected physical output; Boost up to 300% is requested via Equalizer APO on an attached output. **Owner acceptance of this new visual design is pending installation on a personal Windows machine**; CI validation is not physical audio certification. The experimental independent native Windows driver and publishing to Microsoft Store or Google Play production are outside this release. No Developer Edition/RC published.

**Verificación del propietario (2026-11-12):** después de probar la aplicación publicada, el propietario confirmó que **ya comprobó que todo funciona**. Queda asentada la aceptación funcional del paquete estable Android v0.1.14 / Windows v0.1.19, incluido el ajuste de Boost hasta **300%**. Esta declaración no equivale a un ensayo acústico cuantitativo ni acredita un driver nativo independiente. La trazabilidad y el alcance de la aceptación están en [RELEASE_AUDIT_LOG.md](RELEASE_AUDIT_LOG.md); el software y los checksums ya publicados no cambian por este registro.

**Previous stable release (2026-11-17):** [Android v0.1.15 + Windows v0.1.20](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.15-desktop-v0.1.20). Earlier [Android v0.1.14 + Windows v0.1.19](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.14-desktop-v0.1.19) remains archived without overwritten assets. Historical [Android v0.1.13 + Windows v0.1.18](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.13-desktop-v0.1.18) also remains available.

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
