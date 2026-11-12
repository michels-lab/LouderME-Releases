# LouderMe — Official Releases

This **public binary distribution** repository belongs to **Michel's Lab** and is reserved exclusively for **LouderMe**. Development source code belongs to [michels-lab/LouderMe](https://github.com/michels-lab/LouderMe); Michel's Life is a completely separate application and distribution channel.

**Latest verified stable release (API checked 2026-11-12):** [LouderMe Android v0.1.14 + Windows Desktop v0.1.19](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.14-desktop-v0.1.19). This is the final unified **Boost 100–300%** release: Android Direct signed APK (`versionCode 15`), Windows x64 Setup + Portable, and three SHA-256 sidecars, **six assets total**. Source tags `v0.1.14` and `desktop-v0.1.19` both point to `09f50a02c6feff6e8173fe9b4741bef607501333`. [Android CI](https://github.com/michels-lab/LouderMe/actions/runs/43315685300), [Windows release CI](https://github.com/michels-lab/LouderMe/actions/runs/43315685361) and [unified publisher](https://github.com/michels-lab/LouderME-Releases/actions/runs/43326490451) all succeeded. Android APK SHA-256: `dd61f42d9c528a5294b12e0aeb46ca23a78f52960ae11ae87595afb00202470e`; Windows Setup: `fe58241970223b82feb71e4ebc65a320cf9d67bf9b87b982027282647a6da00f`; Windows Portable: `f8e750bc9ed9b661b89cf7b9ed29371ad436679f4fb2d2c679c139defbcc837e`. Both official updater manifests have these versions and actual asset digests. Windows Global Boost requires user-installed/configured **Equalizer APO**, and Android session-0 support remains device-dependent. +9.54 dB is a digital *target* at 300%, not physically verified loudness or distortion-free playback. A native signed Windows virtual audio driver, acoustic A/B proof and Google Play production approval remain outside this release. No prerelease/RC.

**Verificación del propietario (2026-11-12):** después de probar la aplicación publicada, el propietario confirmó que **ya comprobó que todo funciona**. Queda asentada la aceptación funcional del paquete estable Android v0.1.14 / Windows v0.1.19, incluido el ajuste de Boost hasta **300%**. Esta declaración no equivale a un ensayo acústico cuantitativo ni acredita un driver nativo independiente. La trazabilidad y el alcance de la aceptación están en [RELEASE_AUDIT_LOG.md](RELEASE_AUDIT_LOG.md); el software y los checksums ya publicados no cambian por este registro.

**Previous stable release (2026-11-10):** [Android v0.1.13 + Windows v0.1.18](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.13-desktop-v0.1.18), released with six verified assets and the predecessor versions before 300% Boost.

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
