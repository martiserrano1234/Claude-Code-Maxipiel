# MEAS-01 — Estado del clic-a-WhatsApp en Google Ads

**Fecha:** 2026-09-18 · **Cuenta:** 6619664178 (MCC 4020002227)
**Estado:** ⛔ BLOQUEADO por autenticación — no se pudo ejecutar de forma autónoma.

## Qué pasó

Al consultar Google Ads por MCP, respondió `invalid_grant`: el **refresh token está caducado**. Es exactamente lo previsto en la nota `reference_google_ads_oauth`: la app OAuth está en modo "Prueba" y el token caduca cada ~7 días.

No pude leer el estado de la conversión ni marcarla como principal porque la cuenta no autentica.

## Los 2 pasos que quedan (cuando la auth vuelva)

Según `project_google_ads_conversiones`, conversión "Click WhatsApp - Landing Maxipiel" (id `7530529669`):

1. **Confirmar que ya cuenta conversiones** (query a `conversion_action` + métricas). El disparador se instaló el 2026-08-05, así que ya debería haber datos.
2. **Marcarla como PRINCIPAL** — hoy tiene `include_in_conversions_metric=false`, por eso Google reporta 0 y optimiza a ciegas. Se intentará por API (mutate); si el API no lo permite, se hace en la interfaz.
3. (~2 semanas después, NO ahora) cambiar la puja de la campaña "Búsqueda - Tapiceros Piel" de Cuota de Impresiones a Maximizar Conversiones. Cambia cómo gasta → se deja para cuando la medición esté sólida y con visto bueno.

## Desbloqueo — dos caminos

- **Parche (rápido, manual, dura 1 semana):** renovar el token por OAuth Playground con la cuenta maxipielmercadotecnia@gmail.com y correr `node scripts/renovar-token-google-ads.js "1//04..."`, luego reiniciar Claude Code. Detalle en `reference_google_ads_oauth`.
- **Arreglo de RAÍZ (recomendado, elimina el trabajo manual para siempre):** en Google Cloud Console → APIs y servicios → Pantalla de consentimiento OAuth → **PUBLICAR APLICACIÓN**. Con la app publicada el token deja de caducar cada semana. Requiere acceso al proyecto de Google Cloud (lo tiene Felix).

**Recomendación:** empujar el arreglo de raíz con Felix. Es UNA acción manual que mata el problema recurrente — justo lo que Sebastián quiere evitar (hacer cosas a mano cada semana).

---
*Sin cambios ejecutados. Reintentar los 2 pasos en cuanto la cuenta vuelva a autenticar.*
