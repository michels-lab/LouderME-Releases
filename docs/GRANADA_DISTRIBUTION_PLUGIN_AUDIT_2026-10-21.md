# Operación Granada — auditoría del repositorio de distribución

**Corte:** 2026-10-21 UTC. **Tipo:** repositorio público exclusivo de **binarios de LouderMe**, no repo fuente y no Michel's Life. [Auditoría app/plugins/CI en fuente](https://github.com/michels-lab/LouderMe/blob/main/docs/GRANADA_APP_PLUGIN_AUDIT_2026-10-21.md) · [Política central de plugins](https://github.com/michels-lab/Michel-Software-Standards/blob/main/docs/CHATGPT_PLUGIN_LEDGER.md).

## Verificación directa
- [GitHub releases/latest](https://github.com/michels-lab/LouderME-Releases/releases/latest) devolvió tag **`louderme-android-v0.1.12-desktop-v0.1.13`**, publicado el 2026-10-12; **6 activos**: APK Android v0.1.12, Windows Setup/Portable v0.1.13 y tres archivos SHA256.
- El README del **repo fuente LouderMe** indica todavía v0.1.12 para Windows en su sección inicial: hallazgo de desfase descriptivo con el tag realmente publicado. No inferir una versión diferente del ejecutable sin descargarlo y validarlo.
- Aquí **no se ejecutaron** artefactos Windows/Android, ni ensayo WASAPI, controlador virtual, firma de instalación o ganancia acústica; un tag y checksum adjunto no prueban salida física de audio.

## Herramientas y fronteras
- **GitHub (ChatGPT)**: instalado, usado para auditoría de estructura, releases, bitácoras. Requiere validación separada del release.
- **Supabase, Drive, Docs, Spreadsheets, Gmail, Calendar, Contacts**: instalados en ChatGPT, **no implican integraciones de esta app** ni dependencias del canal binario.
- **Sin Vercel ni hosting adicional**: no necesario ni aprobado; no activar plan facturable.
- Preservar feeds `louderme/latest.json` y `louderme-desktop/latest.json`, releases históricos y redirecciones de compatibilidad antiguas en `michel-s-life-releases` hasta validar migración.
- No almacenar claves de firma, tokens, datos privados ni cambiar el binario con una edición documental.

**Estado:** INVENTARIO REMOTO DOCUMENTADO / PUBLICACIÓN ANTERIOR VERIFICADA EN API / SIN NUEVA RELEASE NI QA FÍSICA.
