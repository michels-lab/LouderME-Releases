# LouderMe — Public Release Channel Audit Log

## 2026-10-11 — Completed product-exclusive release cleanup (follow-up)

- **Owner clarification:** No LouderMe release entries should remain visible in Michel's Life, including historical entries.
- **Verification before deletion:** every one of the 13 old LouderMe releases was already present in `michels-lab/LouderME-Releases` with equal asset names, byte sizes and GitHub SHA-256 digests. Deletion workflow refused unknown release tags or mismatches.
- **Removal:** [one-time clean-up job 38136855295](https://github.com/michels-lab/michel-s-life-releases/actions/runs/38136855295) completed successfully. Removed exactly 13 original LouderMe releases and tags from Michel's Life release repository, without deleting any Michel's Life release; `v3.0.216` remained Latest.
- **GitHub UI validation:** [Michel's Life releases](https://github.com/michels-lab/michel-s-life-releases/releases) now list zero LouderMe releases; [LouderMe releases](https://github.com/michels-lab/LouderME-Releases/releases) own their release history and current stable assets.
- **Consequence:** historical **manually pinned GitHub binary** URLs under the old product's `/releases/download/louderme-*/...` paths have ceased working; consumers must use the dedicated LouderMe release URLs. Exactly two old `latest.json` update-feed *metadata aliases* stay in Michel's Life source tree solely because prior LouderMe builds hard-coded those feed paths; both refer to verified binaries hosted in this LouderMe-only repository. Obsolete old LouderMe docs/request files and one-time deletion workflows were removed after success.
- **Safety:** no production binary was re-signed/rebuilt to clean up the old channel. The new Android v0.1.11 may have distinct signer continuity requirements; keep pre-migration legacy feeds on their compatible known baseline unless an in-place update has been verified. This clean-up does not itself authorize a new release.


## 2026-10-11 — Public-release repository isolation

- **Problem:** historical LouderMe GitHub release assets and Windows/Android update manifests were publicly hosted inside `michels-lab/michel-s-life-releases`, making Michel's Life appear to have LouderMe as its Latest release.
- **Decision:** dedicated product-specific, public `michels-lab/LouderME-Releases` with shared Android+Windows bundles under each LouderMe versioned release; source code remains in `michels-lab/LouderMe`.
- **Implementation:** installed `.github/workflows/import-louderme-history.yml` and `.github/workflows/publish-louderme-unified.yml`; imported all **13** historical LouderMe releases without deleting originals; seeded `louderme/latest.json` and `louderme-desktop/latest.json`.
- **Validation:** [importer job 38135343442](https://github.com/michels-lab/LouderME-Releases/actions/runs/38135343442) succeeded. Every imported release had source SHA256 sidecars checked where provided and source/target asset names and byte sizes compared. Current latest unified release `louderme-android-v0.1.10-desktop-v0.1.11` has GitHub asset digests matching the exact manifest checksums: APK `de092ebbc9516395a588f22092075ac7293d291a0f49d3655773b5c6bba1be38`; Setup `59d63eb8f775d1b2f2b81abbe1f079762f56f065e0b9813e99b9a127eb946b18`; Portable `a4da3e98d79f8960ae7a69ef70ff1a24a1945acb011606350a4f0e4c99dc1a4a`.
- **Old channel compatibility:** [Michel's Life release PR #13](https://github.com/michels-lab/michel-s-life-releases/pull/13) merged; removed all three legacy LouderMe publication workflows and redirected both **old URLs** for Android/Windows update manifest download assets to this repository. Historical old-release binary tags retained temporarily for manually pinned links.
- **Application adoption:** [LouderMe PR #57](https://github.com/michels-lab/LouderMe/pull/57) merged. New Android and Windows source builds prefer this repo's official feeds and have legacy URL fallback; both Android and Windows CI passed.
- **GitHub UI:** [old-channel correction job 38135555046](https://github.com/michels-lab/michel-s-life-releases/actions/runs/38135555046) succeeded, setting Michel's Life v3.0.216 as latest in its own repo. This repo's Latest is LouderMe Android v0.1.10 + Windows v0.1.11.
- **Remaining:** real installed Android/Windows update smoke for the next published version; verify future publisher using a newly approved release request (do not auto-publish unsigned/unapproved new versions); eventually choose a retention policy for old manually pinned historic binary URLs. Do not delete old assets while links remain important.
- **Release impact:** no new app version published solely for this migration; existing public app binaries are unchanged.


## 2026-10-11 — Verified coordinated v0.1.11 publication

- **Authorization:** after explicitly approving permanent Android signing migration (the owner is the sole current user), four GitHub Actions Secrets were configured. Source [LouderMe Android run 38135593485, attempt 2](https://github.com/michels-lab/LouderMe/actions/runs/38135593485) passed build, real emulator Home/About check, package uniqueness guard, verified permanent JKS certificate, APK signature and source release publication.
- **New Android signing identity:** public certificate SHA-256 `4a5bb9d9456a656821c3c1105854bda17e24273fd0d09e9495edd5b01e783aa3`; previous signer differed. Existing Android v0.1.10 and earlier must be uninstalled before v0.1.11 installation (potential loss of app-local data). The private signer and its passwords are **never** stored here.
- **Source provenance:** Android `v0.1.11` source tag commit `3da93843afd235bf4dffaa6e6b053db42dfddc71` (versionCode 12), APK SHA-256 `5f433a6ad3d9437855b71cde0b0ce2e81d74864d7a53c663dc29b81f6c113ecf`; Windows `desktop-v0.1.11` source release already passed installation, startup and UI checks. No virtual driver/experimental native audio routing is included in the shipped Windows installer.
- **Unified release:** [Android v0.1.11 + Windows v0.1.11](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.11-desktop-v0.1.11). [Official publisher 38136377304](https://github.com/michels-lab/LouderME-Releases/actions/runs/38136377304) completed successfully, verified checksums/source Android tag, uploaded all six binaries/checksum assets and updated `louderme/latest.json` and `louderme-desktop/latest.json`, both now at 0.1.11.
- **Compatibility:** older installed Android Direct binaries must not be told to in-place update across this intentional signer change; legacy update URLs remain available for compatibility. New Direct APK (v0.1.11+) uses the dedicated LouderME release feed. Windows native driver hardware/system-wide audio remains a separate future milestone.

## 2026-10-12 — LouderME v0.1.12 unified stable published

- **Source:** `michels-lab/LouderMe` commit `ed0bd6da54c022ac05eba0b3760361f4bce056ff`; both `v0.1.12` and `desktop-v0.1.12` source tags point to that commit.
- **Source release gates:** Android run `38217270239` passed permanent signing and final **signed release APK** installed emulator screenshots for Home/About at two viewports. Windows build run `38217270238` and release run `38217270242` passed installer launch/visual checks and asset creation.
- **Public publication:** [run 38231448218](https://github.com/michels-lab/LouderME-Releases/actions/runs/38231448218) passed. [Public unified v0.1.12 release](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.12-desktop-v0.1.12) holds six artifacts, all matching source asset digests and published update feeds.
- **Direct updater:** `louderme/latest.json` versionCode `13`, versionName `0.1.12`, APK SHA-256 `0947e7f6b21f4c5beb10ebebe914d3420586504aa0bac7de42d1a565625a68a7`. `louderme-desktop/latest.json` Windows `0.1.12`, Setup SHA-256 `9bc5def136fc35d01317e9892d599f6aefe5701758fafbf20941c0b459707501`, Portable SHA-256 `b18953af1fbd5d023a828c37eb8b691b1ee88297e91fa9ab6e684de670dcd324`.
- **No implied physical validation:** hardware audio, virtual driver, Windows Authenticode and Play Store publication remain outside this release evidence.

## 2026-10-12 — Publisher source and immutability hardening candidate

- **Finding:** previous publisher verified Android source tag but not Windows tag and allowed `--clobber` of published release assets on rerun. That could silently mutate a public binary without changing the release identity.
- **Correction in review:** enforce Windows source tag against optional `windows_source_sha` (defaults to `source_sha` for coordinated builds); validate release version syntax; reruns compare all six published GitHub SHA-256 asset digests with the exact verified source binaries and refuse any mismatch. Matching reruns may still repair incomplete update manifests without re-uploading assets.
- **Status:** code review and syntax/CI validation required before merge. No additional binary release needed for this maintenance.

## 2026-10-12 — Windows owner-test v0.1.13 public release verified

- **Owner authorization:** publish a real Windows installer to official Releases so the owner can perform physical audio-function testing; do not require a prior owner audio A/B check as a condition of releasing the test installer.
- **Windows source release:** `michels-lab/LouderMe` tag `desktop-v0.1.13` at commit `b7dc88ce0745bf53cb89de46543f92564a34b97c`. GitHub Actions [desktop release run 38293414965](https://github.com/michels-lab/LouderMe/actions/runs/38293414965) **passed** native build, APO contract, installed UI/startup, uninstall, rendered Home/About and checksum generation.
- **Official unified release:** [Android v0.1.12 + Windows v0.1.13](https://github.com/michels-lab/LouderME-Releases/releases/tag/louderme-android-v0.1.12-desktop-v0.1.13); [publisher run 38293724019](https://github.com/michels-lab/LouderME-Releases/actions/runs/38293724019) **passed**, six files verified.
- **Desktop updater:** `louderme-desktop/latest.json` now advertises `0.1.13`, `LouderMe-Setup-v0.1.13.exe` SHA-256 `ea15f59759c6fd65634e7115fac21cc19ed630b0216a0cef33ed02184aafd03a`, Portable SHA-256 `6b47a374c858b462bc06464cba3eb8b77c01d4ae0172847d1a7ec2f24d5aedf0`. Android remains v0.1.12 with the unchanged APK SHA-256 `0947e7f6b21f4c5beb10ebebe914d3420586504aa0bac7de42d1a565625a68a7`.
- **Unresolved product issue:** owner reports prior Windows v0.1.12 GUI worked but audio Boost/EQ did not. v0.1.13 adds explicit Equalizer APO diagnostics, activation and user-operated attenuation test; it **does not** bundle or replace Equalizer APO and cannot be called physically proven. Issue #74 remains open until owner's actual Windows-device A/B test; no native virtual-driver processing or Authenticode signature is implied.


## 2026-10-20 — Orden permanente GRANADA GRANDE (gobernanza; no release)

- El propietario exige bloques **más grandes y ambiciosos**, con entregables relacionados y funcionamiento de extremo a extremo. Vigente el protocolo maestro en `michels-lab/Michel-Software-Standards/standards/GRANADA_CONTINUOUS_BLOCK_PROTOCOL.md` y la copia local `.michelslab/GRANADA.md`.
- Para el siguiente comando GRANADA: leer HEAD, issues, PR abiertos, claims y este log; escoger un paquete de **tres o más entregables sustanciales relacionados cuando haya alcance real**, incluyendo implementación, prueba del flujo principal, errores/reintentos y validación. Un solo P0 indivisible puede ser suficiente; no inventar trabajo artificial.
- Si cualquier parte está ocupada por otra rama, requiere equipo físico, una cuenta de proveedor, resultados científicos que solo existen en el portátil o autorización del propietario, **aparcar con evidencia y pasar a otra subparte independiente**. Conservar identidad visual, datos, credenciales y estándares de publicación.
- Registro obligatorio: A/B/C con estados separados, ruta/PR/sha, QA **ejecutado** (no simplemente escrito), bloqueos, recuperación, reentrada. Esta actualización de política **no significa ninguna funcionalidad del producto implementada, probada ni publicada**.
- Repositorio: `michels-lab/LouderME-Releases`. En los siguientes bloques aplicar este alcance sin modificar los PR activos o trabajos no relacionados.
