---
plan_id: 01-A
phase: 1
wave: 1
title: "MEAS-01 — Cerrar el clic-a-WhatsApp como conversión confiable en Google Ads"
depends_on: []
requirements: [MEAS-01]
files_modified:
  - .planning/phases/01-recuperar-el-flujo-hacia-sof-a-y-medir-el-clic-a-whatsapp/MEAS-01-estado-conversion.md
autonomous: true
must_haves:
  - El clic-a-WhatsApp queda registrado como conversión en Google Ads (cuenta 6619664178)
  - Se puede leer por campaña cuántos clic-a-WhatsApp genera cada una
  - No se modifica ni rompe ninguna campaña ni conversión existente que ya funcione
---

# Plan 01-A — Cerrar el clic-a-WhatsApp (MEAS-01)

**Objetivo:** dejar la conversión clic-a-WhatsApp midiendo bien en Google Ads. Es el cimiento de "primero medir, luego escalar" — sin esto, la Fase 2 (Google Ads) va a ciegas. Es config aditiva, **no gasta dinero** y no toca campañas que ya rinden.

## Contexto

El disparador de conversión se instaló el 2026-08-05 y quedaron **2 pasos pendientes en orden** (ver memoria `project_google_ads_conversiones`). Esta es la palanca de menor riesgo y mayor apalancamiento de toda la fase.

<task id="01-A-1" autonomous="true">
<action>
Leer el estado actual del disparador clic-a-WhatsApp en la cuenta de Google Ads (6619664178) vía MCP: listar las acciones de conversión existentes y su estado (activa / sin registrar / oculta), y confirmar cuáles son los 2 pasos pendientes documentados. NO editar nada todavía — solo diagnosticar. Escribir el hallazgo en MEAS-01-estado-conversion.md.
</action>
<read_first>
- Memoria: project_google_ads_conversiones (los 2 pasos pendientes y el orden)
- Memoria: reference_google_ads_oauth (cómo renovar token si el MCP da error de auth)
- .planning/REQUIREMENTS.md (MEAS-01)
</read_first>
<acceptance_criteria>
- MEAS-01-estado-conversion.md lista las acciones de conversión de la cuenta 6619664178 con su estado
- El documento nombra explícitamente los 2 pasos pendientes y en qué orden van
- No se ejecutó ninguna mutación (mutate) en esta tarea
</acceptance_criteria>
</task>

<task id="01-A-2" autonomous="true">
<action>
Ejecutar los 2 pasos pendientes en el orden correcto para dejar la conversión activa y contando (es configuración de medición, aditiva, sin gasto). Tras aplicarlos, verificar que la acción de conversión aparece en estado activo/registrando y que el reporte permite ver conversiones por campaña. Actualizar MEAS-01-estado-conversion.md con el antes/después.
</action>
<read_first>
- MEAS-01-estado-conversion.md (diagnóstico de la tarea 01-A-1)
- Memoria: project_google_ads_conversiones
</read_first>
<acceptance_criteria>
- La acción de conversión clic-a-WhatsApp queda en estado activo/registrando en Google Ads
- Un reporte por campaña muestra la columna de conversiones (aunque el conteo aún sea 0 por ser reciente)
- MEAS-01-estado-conversion.md documenta el antes/después y qué se cambió
- Ninguna otra conversión o campaña existente fue modificada
</acceptance_criteria>
</task>

## Verificación del plan

- Correr un query de Google Ads que liste conversiones por campaña y confirmar que la de clic-a-WhatsApp ya figura.
- Confirmar con el usuario (Sebastián) que ve el conteo empezando a moverse en 24–48h.
