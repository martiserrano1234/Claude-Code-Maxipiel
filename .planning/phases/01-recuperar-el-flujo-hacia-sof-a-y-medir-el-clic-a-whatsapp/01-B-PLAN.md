---
plan_id: 01-B
phase: 1
wave: 1
title: "SOFIA-01 — Recuperar el volumen de conversaciones que llegan a Sofía"
depends_on: []
requirements: [SOFIA-01]
files_modified:
  - .planning/phases/01-recuperar-el-flujo-hacia-sof-a-y-medir-el-clic-a-whatsapp/SOFIA-01-propuesta-presupuesto.md
autonomous: false
must_haves:
  - Diagnóstico con números reales de por qué cayeron los chats a Sofía (~314 → ~123/quincena)
  - Una propuesta concreta de reasignación de presupuesto (de dónde sale, a dónde va, cuánto) lista para que Martín apruebe
  - NO se ejecuta ningún cambio de presupuesto sin el OK de Martín; NO se toca el flujo de Sofía en n8n
---

# Plan 01-B — Recuperar el flujo de chats a Sofía (SOFIA-01)

**Objetivo:** devolver a Sofía el volumen de conversaciones que perdió (de ~314 a ~123 por quincena). La causa ya está identificada: el presupuesto se desvió a una campaña de tráfico a Shopify que genera 0 chats. Esta palanca es la de retorno más rápido a tu comisión.

**Regla dura:** aquí NO se gasta ni se mueve presupuesto por cuenta propia. Se produce una **propuesta** para Martín. No se toca el flujo de Sofía en n8n.

<task id="01-B-1" autonomous="true">
<action>
Sacar de Meta Ads (act_10152548466947929) los números frescos de las últimas 4 quincenas por campaña: conversaciones iniciadas (onsite_conversion.messaging_conversation_started_7d), costo por conversación, gasto y frecuencia. Comparar la campaña de Mensajes que alimenta a Sofía contra la campaña de tráfico "Tapiceros Tienda (Shopify)". Escribir el diagnóstico en SOFIA-01-propuesta-presupuesto.md con una tabla clara.
</action>
<read_first>
- Memoria: project_meta_ads_estructura (qué campañas son de Felix y cuáles de Sebastián — NO tocar las de Sebastián)
- .planning/REQUIREMENTS.md (SOFIA-01)
</read_first>
<acceptance_criteria>
- SOFIA-01-propuesta-presupuesto.md contiene una tabla con conversaciones/costo/gasto por campaña de las últimas ~4 quincenas
- El documento cuantifica la caída (de ~314 a ~123) y el gasto que se fue a tráfico sin chats
- No se ejecutó ninguna mutación en Meta Ads
</acceptance_criteria>
</task>

<task id="01-B-2" autonomous="false">
<action>
Redactar la propuesta de reasignación para Martín: cuánto presupuesto mover, DE qué campaña (la de tráfico a Shopify que no genera chats) HACIA la campaña de Mensajes de Sofía, el retorno esperado en chats/quincena, y el riesgo. Dejarla en SOFIA-01-propuesta-presupuesto.md en un formato corto que Sebastián le pueda reenviar a Martín por WhatsApp. NO aplicar el cambio de presupuesto — queda en espera del OK.
</action>
<read_first>
- SOFIA-01-propuesta-presupuesto.md (diagnóstico de 01-B-1)
- Memoria: feedback_no_tocar_sofia (no tocar n8n)
- .claude/rules/communication-style.md (tono)
</read_first>
<acceptance_criteria>
- La propuesta dice montos concretos (de dónde sale, a dónde va, cuánto) y el retorno esperado en chats
- Está redactada lista para reenviar a Martín, en español, tono claro
- El documento marca explícitamente "PENDIENTE: aprobación de Martín antes de aplicar"
- No se ejecutó ningún cambio de presupuesto en Meta Ads
</acceptance_criteria>
</task>

## Verificación del plan

- Sebastián revisa la propuesta y la envía a Martín.
- Solo tras el OK de Martín se aplica la reasignación (en un plan de ejecución aparte) y se mide la recuperación de chats hacia ~300/quincena.
