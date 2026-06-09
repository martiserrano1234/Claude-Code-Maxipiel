# Ads Action Plan — Maxipiel
**Fecha:** 2026-05-14
**Ads Health Score actual: 44/100 (Grade: D)**
**Objetivo: 65/100 (Grade: C+) en 60 días**

---

## CRÍTICO — Antes de gastar más presupuesto

### 1. Instalar Conversions API (CAPI) en Shopify
**Plataforma:** Meta Ads | **Tiempo:** 2-3 horas | **Impacto:** Muy Alto
- Sin CAPI, el 30-40% de las conversiones son invisibles para Meta (post-iOS 14.5)
- Sin Purchase events, Meta optimiza hacia clickers curiosos, no compradores
- **Pasos:**
  1. Shopify Admin → Configuración → Apps → Meta (Facebook & Instagram)
  2. Activar Conversions API (toggle nativo de Shopify — no requiere código)
  3. Verificar en Meta Events Manager que Purchase, AddToCart, InitiateCheckout disparan
  4. Configurar deduplicación con event_id
- **Resultado esperado:** Meta empieza a optimizar hacia compradores reales → CPL de C6 baja de $1.98 a ~$1.20-1.50

### 2. Habilitar eventos estándar de Shopify en Meta Pixel
**Plataforma:** Meta Ads | **Tiempo:** 30 minutos | **Impacto:** Muy Alto
- Actualmente cero eventos de Purchase, AddToCart, InitiateCheckout
- **Pasos:**
  1. En la integración Meta de Shopify → activar "Track standard events"
  2. Verificar en Pixel Helper que disparan correctamente en el flujo de checkout
  3. Crear Custom Audience de "Personas que completaron Purchase en últimos 180 días"
  4. Usar esa audiencia para crear Lookalike 1%, 2%, 3%
- **Resultado esperado:** Lookalike de compradores activos disponible en ~7 días con suficiente volumen

---

## ALTA PRIORIDAD — Esta semana

### 3. Corregir estructura de Google Ads
**Plataforma:** Google Ads | **Tiempo:** 45-60 minutos | **Impacto:** Alto

**3a. Consolidar conversiones (10 min):**
- Reducir 16 acciones a 1 primaria + 2-3 secundarias
- Primaria: "WhatsApp — Conversación iniciada" (el evento más cercano a venta)
- Secundarias: LPV, click al número de teléfono

**3b. Cambiar bidding a Maximize Clicks (5 min):**
- Maximize Conversions con 5 conv/mes = algoritmo adivinando
- Maximize Clicks + CPC cap $15 MXN aumenta volumen y datos

**3c. Crear campaña de brand (10 min):**
- Nueva campaña: "Brand — Maxipiel"
- Keywords exactas: [maxipiel], [maxi piel], [maxipiel cuero], [maxipiel piel]
- Presupuesto: $30 MXN/día | Bidding: Maximize Clicks

**3d. Aumentar presupuesto de la campaña principal (2 min):**
- De $100 MXN/día a $250-300 MXN/día
- Con 9.99% SIS es imposible recolectar datos suficientes a $100/día

**3e. Lista de negativos "Consumidores finales" (10 min):**
Crear lista y aplicar a todas las campañas:
- [artículos en piel], [bolsa de piel], [zapatos de piel], [cinturón de piel]
- [piel artesanal], [manualidades], [costura], [ropa de piel], [billetera]

### 4. Consolidar Meta a 5-6 campañas
**Plataforma:** Meta Ads | **Tiempo:** 30-45 minutos | **Impacto:** Alto

**Estructura recomendada (5 campañas):**
1. **Awareness — Video** (fusionar C8 + C9 + C13): $1,500-2,000/mes, objetivo Reach/Video Views
2. **Conversión WA — Fría** (escalar C6 + absorber C3, C4, C11, C12): $2,500-3,000/mes, objetivo Leads/Messages
3. **Remarketing Web** (mantener C10): $800/mes, objetivo Conversions
4. **Remarketing Video** (nuevo): $500/mes, audiencia de viewers 75%+ de video, objetivo Messages
5. **Brand/Tráfico directo** (consolidar C1 + C2): $800/mes, objetivo Traffic

**Acción:**
- Pausar C3, C5, C11, C12 de inmediato
- Migrar sus presupuestos a C6
- Fusionar C2 con C1 (corregir primero el URL roto de C1)

---

## MEDIA PRIORIDAD — Este mes

### 5. Reescribir el Welcome Message de WhatsApp en C3
**Plataforma:** Meta Ads | **Tiempo:** 1-2 horas | **Impacto:** Medio
- C3 tiene 70 welcome_message_views pero solo 3 conversiones (4.3%)
- El problema es el mensaje de bienvenida, no el anuncio
- **Acción:** Revisar el mensaje inicial de Sofía para este flujo
- Usar el mensaje de C6 como referencia (la campaña con mejor conversión)
- **Objetivo:** Subir view-to-connection rate de 4.3% a 15-20%

### 6. Configurar Customer Match en Google
**Plataforma:** Google Ads | **Tiempo:** 15 minutos | **Impacto:** Medio
- Cargar lista de números/emails de clientes activos de Sofía
- Google usa esta lista para encontrar buyers similares
- **Pasos:** Herramientas → Administrador de audiencias → Listas de clientes → Subir CSV
- También crear campaña de remarketing para visitantes del sitio que no compraron

### 7. Agregar extensiones de anuncio en Google
**Plataforma:** Google Ads | **Tiempo:** 20 minutos | **Impacto:** Medio
- Sitelinks: "Ver colores disponibles", "Pedir muestra", "Envíos a todo México", "Por qué Maxipiel"
- Callouts: "Directo de curtiembre", "Precio fijo sin regateo", "Envío en 4-6 días", "30+ colores"
- Structured snippets: Tipos de piel (Napa, Corrugado, Semi-liso, Grabado)

### 8. Crear audiencia video-viewer para remarketing en Meta
**Plataforma:** Meta Ads | **Tiempo:** 15 minutos | **Impacto:** Medio
- C8 y C13 tienen 90K+ video views combinados — estas personas ya conocen la marca
- **Pasos:** Audiencias → Custom Audience → Video → 75%+ de tiempo visto → últimos 60 días
- Crear campaña de WhatsApp apuntando solo a esta audiencia
- Mensaje específico: "Ya viste nuestro cuero — ¿te mandamos una muestra?"

---

## LARGO PLAZO — Este trimestre

### 9. Importar conversiones offline (Sofía → Google/Meta)
**Tiempo:** 4-8 horas | **Impacto:** Transformador
- Actualmente ninguna plataforma sabe qué conversaciones de WhatsApp resultaron en ventas
- **Plan:** n8n workflow que cuando Sofía marca una venta como cerrada → importa la conversión a Google Ads + Meta Ads Offline Events
- **Resultado:** Las plataformas aprenden a optimizar hacia compradores reales, no hacia leads curiosos

### 10. Segmentar campañas por tipo de tapicero
**Tiempo:** 2-3 días | **Impacto:** Alto
- Tapicero de taller pequeño (2-5 metros/mes) vs fabricante mediano (20+ metros/mes)
- Mensajes diferentes, presupuestos diferentes, bidding diferente
- En Google: ad groups separados con keywords de volumen vs calidad
- En Meta: audiencias separadas con creative orientado a tickets distintos

### 11. Test de Advantage+ Shopping Campaign
**Plataforma:** Meta Ads | **Tiempo:** 2-3 horas | **Impacto:** Alto
- Requiere: CAPI activo + Purchase events + catálogo de productos sincronizado
- **Plan:** Una vez activo CAPI, crear 1 ASC con el catálogo de Shopify
- Presupuesto inicial: $500 USD/mes
- Objetivo: Compras directas en Shopify sin pasar por WhatsApp

---

## Proyección de Mejora

| Plazo | Score actual | Score proyectado | Acciones completadas |
|-------|-------------|-----------------|---------------------|
| Semana 1 | 44/100 | 50/100 | Quick wins + consolidación Meta + bidding Google |
| Mes 1 | 50/100 | 58/100 | CAPI + estructura Google + conversiones |
| Mes 2 | 58/100 | 65/100 | Offline imports + audiencias avanzadas |
| Trimestre | 65/100 | 72/100 | ASC + segmentación + optimización continua |

---

## Revenue Impact Estimado

| Acción | Impacto mensual est. | Confianza | Timeline |
|--------|---------------------|-----------|----------|
| Pausar C1 + C3 + redirigir a C6 | +$2,000-4,000 MXN en leads | Alta | Hoy |
| Escalar C6 al doble de presupuesto | +125 conversaciones WA/mes | Alta | Esta semana |
| Corregir Google Ads bidding + budget | +$1,500-3,000 MXN | Media | Esta semana |
| CAPI + Purchase events | +$3,000-8,000 MXN | Alta | 2-3 semanas |
| Offline conversion import | +$2,000-5,000 MXN | Media | 4-6 semanas |
| **Total potencial** | **$8,500-20,000 MXN/mes** | | |

---

*Generado por AI Ads Suite — `/ads audit` — 2026-05-14*
*Referencia: ADS-AUDIT-REPORT.md | ADS-QUICK-WINS.md*
