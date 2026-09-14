---
plan_id: 01-C
phase: 1
wave: 2
title: "SOFIA-02 — Campaña Meta de proyecto/mayoreo que alimenta a Sofía con compradores grandes"
depends_on: [01-B]
requirements: [SOFIA-02]
files_modified:
  - .planning/phases/01-recuperar-el-flujo-hacia-sof-a-y-medir-el-clic-a-whatsapp/SOFIA-02-campana-mayoreo.md
autonomous: false
must_haves:
  - Una campaña Meta nueva de "proyecto/mayoreo" dirigida a Mensajes, creada en estado PAUSADO (sin gastar)
  - Público y copys que auto-filtran al comprador chico y llaman al de volumen
  - Las conversaciones caen en Sofía sin ningún cambio en su flujo de n8n
  - No se modifica ninguna campaña existente que ya rinda
---

# Plan 01-C — Campaña de proyecto/mayoreo (SOFIA-02)

**Objetivo:** traerle a Sofía compradores de volumen (los que a Sebastián más le gusta cerrar). La campaña se construye **nueva y en PAUSA** — no se enciende ni gasta hasta que Sebastián/Martín den el OK. Es 100% aditiva: no se toca ninguna campaña actual ni el flujo de Sofía.

<task id="01-C-1" autonomous="true">
<action>
Definir el segmento y el ángulo de la campaña de mayoreo: públicos de Meta candidatos (talleres de tapicería, mueblerías, fabricantes de muebles, y segmentos poco explotados: náutica, hotelería/restaurantes, tapicería automotriz) y 3–4 variantes de copy que filtran por volumen ("precio especial por volumen para talleres", "cotización para proyectos grandes", "¿cuántos metros necesitas?"). Escribir todo en SOFIA-02-campana-mayoreo.md. Sin crear nada en Meta todavía.
</action>
<read_first>
- Memoria: project_meta_ads_estructura (estructura de campañas, cuáles no tocar)
- .claude/rules/communication-style.md (tono externo: amigable, vendedor, para tapiceros)
- .planning/REQUIREMENTS.md (SOFIA-02)
</read_first>
<acceptance_criteria>
- SOFIA-02-campana-mayoreo.md define público(s), presupuesto sugerido/día y 3–4 copys que filtran por volumen
- El objetivo de la campaña es Mensajes (cae en Sofía), no tráfico web
- No se creó nada en Meta Ads en esta tarea
</acceptance_criteria>
</task>

<task id="01-C-2" autonomous="false">
<action>
Crear en Meta Ads (act_10152548466947929) la campaña de mayoreo en estado PAUSED: campaña + adset (público definido, objetivo Mensajes/routing a WhatsApp→Sofía) + 1–2 anuncios con los copys aprobados. Dejarla PAUSADA. Documentar los IDs creados en SOFIA-02-campana-mayoreo.md. NO activar (no gastar) — la activación y el presupuesto los aprueba Martín.
</action>
<read_first>
- SOFIA-02-campana-mayoreo.md (definición de 01-C-1)
- Memoria: project_meta_ads_estructura (routing WhatsApp/Sofía)
- Memoria: feedback_no_tocar_sofia
</read_first>
<acceptance_criteria>
- Existe una campaña nueva en Meta en estado PAUSED con su adset y anuncio(s)
- La campaña enruta las conversaciones a WhatsApp/Sofía sin cambios en el flujo de n8n
- SOFIA-02-campana-mayoreo.md registra los IDs de campaña/adset/anuncio y el estado PAUSED
- Ninguna campaña existente fue modificada
</acceptance_criteria>
</task>

## Verificación del plan

- Sebastián revisa la campaña pausada (público + copys + routing a Sofía).
- Se enciende solo con OK de presupuesto de Martín; luego se mide que las conversaciones de mayoreo aparecen en Sofía.
