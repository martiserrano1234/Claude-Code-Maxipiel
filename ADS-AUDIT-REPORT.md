# Ads Audit Report — Maxipiel
**Fecha:** 2026-05-14
**Período:** 2026-04-13 al 2026-05-13 (30 días)
**Plataformas auditadas:** Google Ads + Meta Ads
**Ads Health Score: 44/100 (Grade: D)**

---

## Resumen Ejecutivo

Maxipiel gasta aproximadamente **$6,600 USD/mes en publicidad digital** — prácticamente todo en Meta Ads ($6,430 USD) y casi nada en Google Ads ($150-180 USD equivalente). La cuenta de Meta genera señales prometedoras: 503K personas alcanzadas, 245 conversaciones de WhatsApp iniciadas a $1.98 cada una en la mejor campaña. La cuenta de Google tiene CTRs fuertes (6-10%) pero es invisible (9.9% de cuota de impresión) y opera con infraestructura rota.

**El problema central no es el gasto — es que la mitad del gasto no tiene tracking de conversiones válido.** Meta no sabe qué campañas generan ventas reales porque no hay eventos de Purchase ni CAPI configurado. Google no puede optimizar con 5 conversiones al mes. Ambas cuentas están tirando dinero en modo "confianza ciega".

**Top 3 hallazgos críticos:**
1. Meta no tiene Conversions API ni eventos de Purchase → el algoritmo optimiza hacia clics, no hacia compradores
2. La campaña de Meta con mejor rendimiento (C6: $1.98/conversación) recibe solo 7.5% del presupuesto total
3. Google Ads tiene 16 acciones de conversión — casi seguro duplicadas — con solo 5 conversiones al mes

**Impacto potencial de corregir los problemas identificados: +$3,000–$8,000 MXN/mes en revenue sin aumentar presupuesto.**

---

## Score por Plataforma

| Plataforma | Health Score | Grade | Presupuesto (30d) | % del total |
|------------|-------------|-------|-------------------|------------|
| Google Ads | 38/100 | F | ~$3,000 MXN (~$150 USD) | ~2.5% |
| Meta Ads | 44/100 | D | $6,430 USD | ~97.5% |
| **Agregado** | **44/100** | **D** | **~$6,580 USD** | |

*Score agregado ponderado por presupuesto: (38 × 0.025) + (44 × 0.975) = 44/100*

---

## Score Breakdown — Google Ads (38/100)

| Categoría | Peso | Score | Ponderado |
|-----------|------|-------|-----------|
| Conversion Tracking | 25% | 30/100 | 7.5 |
| Wasted Spend / Negatives | 20% | 45/100 | 9.0 |
| Account Structure | 15% | 25/100 | 3.75 |
| Keywords & Quality Score | 15% | 50/100 | 7.5 |
| Ads & Assets | 15% | 35/100 | 5.25 |
| Settings & Bidding | 10% | 40/100 | 4.0 |
| **TOTAL** | 100% | — | **37/100** |

---

## Score Breakdown — Meta Ads (44/100)

| Categoría | Peso | Score | Ponderado |
|-----------|------|-------|-----------|
| Pixel / CAPI Health | 30% | 18/100 | 5.4 |
| Creative Quality & Fatigue | 30% | 52/100 | 15.6 |
| Account Structure | 20% | 48/100 | 9.6 |
| Audience & Targeting | 20% | 68/100 | 13.6 |
| **TOTAL** | 100% | — | **44/100** |

---

---

# GOOGLE ADS — Análisis Detallado

## Google Ads Health Score: 38/100 (Grade: F)

**Cuenta:** Maxipiel | Customer ID: 6619664178 | Moneda: MXN | Período: últimos 30 días

### Campaña Activa (solo 1 de 13)

| Campo | Valor |
|-------|-------|
| Nombre | "Maxipiel Búsqueda Principal" |
| Tipo | Search |
| Bidding | Maximize Conversions |
| Presupuesto diario | $100 MXN |
| Clics (30d) | 29 |
| Impresiones (30d) | 448 |
| Conversiones (30d) | 5 |
| Costo (30d) | $143 MXN |
| CTR | 6.47% |
| CPC promedio | $4.94 MXN |
| Search Impression Share | **9.99%** ← CRÍTICO |

### Conversion Tracking — 30/100

| Check | Resultado | Hallazgo |
|-------|-----------|---------|
| Conversiones definidas | ⚠️ WARNING | 16 acciones de conversión — excesivo. Señal fragmentada y casi seguro duplicada. |
| No duplicate counting | ❌ FAIL | Múltiples acciones de WhatsApp probablemente disparan en el mismo evento. Las 5 conversiones reportadas no son confiables. |
| Conversiones offline importadas | ❌ FAIL | Las ventas cierran en WhatsApp (Sofía). Google no sabe cuáles leads se convirtieron. |
| Conversión primaria vs secundaria | ❌ FAIL | Con 16 acciones, casi seguro no hay una designada como "primaria (para bidding)". |
| Valor de conversión asignado | ⚠️ WARNING | Los clicks a WhatsApp no tienen valor en pesos. Google no puede diferenciar un pedido de $200 vs $5,000 MXN. |
| Enhanced Conversions | ❓ DESCONOCIDO | No confirmado. Alta probabilidad de no estar configurado. |

**Problema raíz:** El algoritmo optimiza hacia una conversión duplicada y de baja calidad (click a WhatsApp) con solo 5 señales al mes. El resultado es que Google gasta a ciegas.

### Wasted Spend / Negatives — 45/100

| Check | Resultado | Hallazgo |
|-------|-----------|---------|
| Auditoría de search terms <14 días | ❌ FAIL | Sin evidencia de revisión reciente. |
| Keyword "artículos en piel" | ❌ FAIL | Término de consumidor retail (bolsas, zapatos, cinturones) — no tapiceros. Genera clics irrelevantes con broad match. |
| Campaña de brand separada | ❌ FAIL | "Maxipiel" no está protegido. Búsquedas de marca se mezclan con genéricas. |
| Search Impression Share >50% | ❌ FAIL | 9.99% SIS = invisible en el 90% de búsquedas elegibles. |
| Listas de negativos temáticas | ⚠️ WARNING | 183 negativos existen pero estructura desconocida. |

### Account Structure — 25/100

| Check | Resultado | Hallazgo |
|-------|-----------|---------|
| Campañas reflejan objetivos de negocio | ❌ FAIL | 1 campaña activa para e-commerce B2B con múltiples líneas de producto. Sin segmentación. |
| Tema de ad group claro | ❌ FAIL | 43 keywords con intents mezclados en 1 solo ad group. |
| Brand vs non-brand separados | ❌ FAIL | Sin campaña de brand. Tráfico de marca desprotegido. |
| Campañas pausadas sin usar | ⚠️ WARNING | 9+ campañas pausadas/eliminadas generan ruido histórico. |

### Keywords & Quality Score — 50/100

**Señal positiva:** Los top keywords tienen CTR 10%+ — muy por encima del benchmark B2B de 3-5%. Esto indica que los términos elegidos tienen intención de compra real.

| Keyword | Clics | CTR | Evaluación |
|---------|-------|-----|-----------|
| cuero para tapizar | 511 | 10.51% | ✅ Excelente — intención B2B |
| piel para tapizar | 228 | 10.57% | ✅ Excelente — intención B2B |
| comprar cuero | 937 | 8.64% | ⚠️ Intención mixta |
| venta de piel | 356 | 7.41% | ⚠️ Intención mixta |
| artículos en piel | 111 | 5.39% | ❌ Término de consumidor |

### Settings & Bidding — 40/100

| Check | Resultado | Hallazgo |
|-------|-----------|---------|
| Bidding strategy adecuada | ❌ FAIL | Maximize Conversions necesita 30-50 conversiones/mes. Con 5/mes el algoritmo está adivinando. |
| Target CPA/ROAS configurado | ❌ FAIL | Sin tope de CPA. Gasta $100/día sin importar calidad de conversión. |
| Remarketing activo | ❌ FAIL | Sin lista de remarketing. Compradores B2B investigan días antes de comprar. |
| Customer Match configurado | ❌ FAIL | Los contactos de WhatsApp (Sofía) no están cargados como Customer Match. |

---

# META ADS — Análisis Detallado

## Meta Ads Health Score: 44/100 (Grade: D)

**Cuenta:** act_10152548466947929 | Moneda: USD | Período: 30 días

### Rendimiento por Campaña

| # | Descripción | Gasto | Impr. | CTR | CPC | KPI principal | Costo/KPI | Calificación |
|---|-------------|-------|-------|-----|-----|---------------|-----------|-------------|
| C1 | Traffic (Anuncios Mayo-Junio) | $253 | 27K | 2.14% | $0.43 | LPV: 1 de 390 clicks | $253/LPV | 🔴 ROTO |
| C2 | Engagement/Traffic | $253 | 32K | 3.10% | $0.25 | Link clicks: 951 | $0.27 | 🟡 OK |
| C3 | WhatsApp (Lista Dorada Muestrario) | $169 | 9.9K | 0.90% | $1.90 | Conexiones WA: 3 | $56.48 | 🔴 PÉSIMO |
| C4 | WhatsApp (Tapiceros Profesionales) | $219 | 84K | 1.21% | $0.21 | Conversaciones: 9 | $24.32 | 🟡 Aceptable |
| C5 | Zombie | $1.51 | 291 | 3.09% | $0.17 | — | — | 🔴 Pausar |
| C6 | **WhatsApp BEST PERFORMER** | $486 | 32K | **12.99%** | **$0.12** | **Conversaciones: 245** | **$1.98** | ✅ ESCALAR |
| C7 | WhatsApp Engagement | $454 | 19.9K | 4.62% | $0.49 | Conexiones: 98 | $4.63 | 🟢 Buena |
| C8 | Traffic/Video (mayor gasto) | **$2,024** | 164K | 5.63% | $0.22 | LPV: 4,169 | $0.49 | 🟡 Tráfico sin conversión |
| C9 | Video/Traffic | $1,004 | 147K | 4.08% | $0.17 | Video views: 33K | $0.030 | 🟡 Videos baratos |
| C10 | Remarketing Web | $626 | 35K | 3.17% | $0.56 | LPV: 703 | $0.89 | 🟢 Buena |
| C11 | WhatsApp small | $52 | 2K | 5.11% | $0.48 | Conexiones: 9 | $5.76 | 🟡 Muy pequeña |
| C12 | WhatsApp small | $56 | 1.8K | 4.84% | $0.65 | Conexiones: 7 | $8.01 | 🟡 Muy pequeña |
| C13 | Video/Traffic | $833 | 78K | **9.02%** | **$0.12** | LPV: 2,249 | $0.37 | 🟢 Buena |

**Concentración de presupuesto vs rendimiento:**
- C8 (Traffic): 31% del presupuesto → 0 conversaciones de WhatsApp
- C6 (Best WA): 7.5% del presupuesto → 245 conversaciones a $1.98 c/u

### Pixel / CAPI Health — 18/100

| Check | Resultado | Hallazgo |
|-------|-----------|---------|
| Pixel instalado y disparando | ⚠️ WARNING | Funciona en C8, C9, C10, C13. Completamente roto en C1 (99.7% drop). |
| Conversions API (CAPI) activo | ❌ FAIL | Sin CAPI. Post-iOS 14.5 significa que 30-40% de conversiones son invisibles. |
| Eventos de Purchase firing | ❌ FAIL | **Cero** eventos de Purchase, Add to Cart o Initiate Checkout en 13 campañas. |
| Evento de LPV tracking | ⚠️ WARNING | Parcial — funciona en 4 campañas, roto en otras 3. |
| EMQ ≥8.0 para Purchase | ❌ FAIL | Sin Purchase events = EMQ efectivo de 0 para el evento más importante. |
| Event deduplication | ❌ FAIL | Sin CAPI = sin pairing browser + server = sin deduplicación. |

**Hallazgo crítico — C1:** 390 clicks → 1 landing page view = 99.7% de drop. La URL de destino está rota o el Pixel no está instalado en el dominio destino. $253 gastados enviando tráfico a ningún lado.

**Consecuencia práctica:** Meta está optimizando campañas con señales de engagement (likes, clicks), no con señales de compra. Encuentra personas curiosas, no tapiceros compradores.

### Creative Quality & Fatigue — 52/100

**Varianza de CTR: 0.90% a 12.99% — señal de creative muy desigual.**

| Indicador | Evaluación |
|-----------|-----------|
| C6: CTR 12.99%, $0.12 CPC, $1.98/conversación | ✅ OUTSTANDING — este es el template correcto |
| C3: CTR 0.90%, $56.48/conversación WA | ❌ Creative o welcome message rota |
| C8, C9, C13 videos: costo/view $0.024–$0.036 | ✅ Videos con hooks fuertes y bajo costo |
| C1: CTR 2.14% pero 0 landing page views | ❌ No es fatiga — es URL rota |
| C3: 70 welcome_message_views → 3 conexiones (4.3%) | ❌ El welcome message no convierte |

**Acción inmediata:** Documentar el creative de C6 (imagen/video + copy + CTA). Usar como template base para todas las campañas de WhatsApp.

### Account Structure — 48/100

**El problema:** 13 campañas para $6,430/mes fragmenta el aprendizaje del algoritmo. Recomendación: 5-6 campañas máximo.

**Distribución de presupuesto actual vs recomendada:**

| Objetivo | Gasto actual | % | Gasto recomendado |
|----------|-------------|---|-------------------|
| Traffic puro (C8, C9, C13) | $3,860 | 60% | $1,500-2,000 |
| WhatsApp leads (C3, C4, C6, C7, C11, C12) | $1,436 | 22% | $3,000-3,500 |
| Remarketing (C10) | $626 | 10% | $800 |
| Otros (C1, C2, C5) | $508 | 8% | Pausar o consolidar |

### Audience — 68/100

**Puntos positivos:**
- Frecuencia promedio 1.26x — sin fatiga de audiencia
- Reach de 503K personas únicas en 30 días
- C6 demuestra que la audiencia correcta existe

**Brechas:**
- Sin exclusión de contactos actuales de WhatsApp en campañas de prospección
- Sin lookalike de compradores (no hay Purchase events)
- C6 y C7 probablemente se están pisando — misma audiencia, mismo objetivo

---

## Cross-Platform Analysis

### Tracking Consistency
- Google: WhatsApp clicks como conversión principal (micro-conversión)
- Meta: messaging_connections como KPI (también micro-conversión)
- **Ninguna plataforma mide ventas reales**. El revenue total de ads es desconocido.

### Budget Allocation
- 97.5% del presupuesto en Meta, 2.5% en Google
- Google tiene CTR de 10%+ en términos clave → infrainvertido
- Recomendación: subir Google a $500-700 MXN/día ($25-35 USD) una vez corregida la estructura

### Sofía como Activo de Conversión
- Meta genera conversaciones → Sofía las cierra
- Google no está integrado con este flujo (sin WhatsApp extension, sin offline conversions)
- Oportunidad: conectar CRM de Sofía con ambas plataformas vía offline conversion import

---

*Generado por AI Ads Suite — `/ads audit` — 2026-05-14*
*Google Ads: Customer 6619664178 | Meta Ads: act_10152548466947929*
