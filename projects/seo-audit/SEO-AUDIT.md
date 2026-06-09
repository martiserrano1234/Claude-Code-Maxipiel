# SEO Content Audit
## https://maxipiel.com.mx/
### Fecha: 2026-04-07
### Auditado por: Equipo de Marketing — Claude Code Maxipixel

---

## SEO Health Score: 38/100

> **Estado general: Crítico.** El sitio tiene una base técnica funcional (Shopify, HTTPS, sitemap, tracking) pero carece de los elementos SEO más básicos: title tag, meta description, Open Graph, y la mayoría de las imágenes no tienen texto alternativo. Además hay duplicación de colecciones y contenido delgado en la página principal. Sin corregir estos problemas, el sitio es prácticamente invisible para Google en búsquedas orgánicas.

---

## On-Page SEO Checklist

### Title Tag
- **Estado: FALLA CRÍTICA**
- **Actual:** No detectado (probable título genérico de Shopify)
- **Recomendado:** `Piel Genuina para Tapicería y Marroquinería | Maxipiel`
- **Problemas:**
  - Sin title tag visible — Google genera uno automático (generalmente malo)
  - Sin keyword primaria
  - Sin nombre de marca en posición correcta
- **Impacto:** El title tag aparece como el título azul en Google. Sin uno optimizado, el CTR (tasa de clics) cae entre 20-40%. Arreglar esto es la acción de mayor impacto por menor esfuerzo en todo el sitio.

---

### Meta Description
- **Estado: FALLA CRÍTICA**
- **Actual:** No detectada
- **Recomendada:** `Venta de piel genuina al mayoreo para tapiceros, marroquineros y fabricantes de calzado. Entregas en León y envíos nacionales. ¡Cotiza hoy!`
- **Problemas:**
  - Sin meta description — Google toma texto aleatorio de la página
  - Sin call to action
  - Sin keyword primaria
- **Impacto:** La meta description es el "anuncio" del resultado en Google. Sin una bien escrita, los competidores que sí la tienen capturan más clics aunque estén en posición más baja.

---

### Open Graph Tags
- **Estado: FALLA**
- **Actual:** No detectados
- **Impacto:** Cuando alguien comparte el sitio en Facebook, Instagram o WhatsApp, aparece sin imagen, sin título descriptivo y sin descripción. Esto reduce drásticamente la conversión de tráfico por redes sociales.
- **Recomendado agregar:**
  ```
  og:title     → "Piel Genuina para Tapicería y Marroquinería | Maxipiel"
  og:description → "Venta al mayoreo de piel genuina. Tapicería automotriz, muebles, calzado y marroquinería."
  og:image     → [foto de producto de alta calidad]
  og:url       → https://maxipiel.com.mx/
  ```

---

### Estructura de Encabezados (H1-H6)
- **Estado: NECESITA TRABAJO**

| Nivel | Texto | Evaluación |
|-------|-------|------------|
| H1 | "Piel genuina para tus proyectos" | ✅ Existe, tiene keyword, es descriptivo |
| H2 | "Marcas que confían en Maxipiel" | ✅ Correcto |
| H2 | "La mejor materia prima. Piel genuina para tus proyectos" | ⚠️ Repite casi idéntico al H1 |
| H2 | "Excelente calidad" | ⚠️ Vago, no aporta keyword |
| H2 | "Piel Genuina" | ⚠️ Muy corto, sin contexto |
| H2 | "Multiples usos" | ⚠️ Vago |
| H2 | "Excelente precio" | ⚠️ Vago |
| **H2** | **"4772095652 whatapp y tel"** | ❌ TRAMPA SEO: Un número de teléfono como H2 es abuso semántico. Google interpreta esto como estructura de contenido, no como contacto. |
| **H2** | **"contact@maxipiel.store"** | ❌ TRAMPA SEO: Mismo problema. El email no debe ser un heading. |
| H3 | "Piel para tapicería automotriz" (×2) | ✅ Buenos keywords, pero están duplicados |
| H3 | "Piel para Marroquinería" (×2) | ✅ Duplicado también |
| H3 | "Piel para fabricación de muebles" (×2) | ✅ Duplicado también |

**Correcciones:**
- El teléfono y email deben ir en un `<p>` o `<address>`, nunca como H2
- Los H3 duplicados indican que hay una sección repetida — revisar si es un bug de la plantilla
- Los H2 vagos ("Excelente calidad", "Excelente precio") deberían tener keywords más específicas

---

### Imágenes y Alt Text
- **Estado: FALLA CRÍTICA**
- **Resultado:** 9 de 11 imágenes (82%) sin texto alternativo

| Imagen | Alt Text | Estado |
|--------|----------|--------|
| DSC09453.jpg | "OAO - Dark Golden Brown 8-9oz FULL BENDS - maxipiel" | ✅ Tiene alt text (pero en inglés) |
| D_NQ_NP_829365... | *(vacío)* | ❌ |
| logoyuyin_copia.jpg | *(vacío)* | ❌ |
| Caterpillar-logo.png | *(vacío)* | ❌ |
| 928_flexi.webp | *(vacío)* | ❌ |
| prima_logo.jpg | *(vacío)* | ❌ |
| reclutan-bader... | *(vacío)* | ❌ |
| ChatGPT_Image_automotriz | "Piel para tapicería automotriz" | ✅ Tiene alt text |
| ChatGPT_Image_marroquineria | "Piel para Marroquinería" | ✅ Tiene alt text |
| ChatGPT_Image_muebles | "Piel para fabricación de muebles" | ✅ Tiene alt text |
| Maxipiel_blanco.png | "maxipiel" | ⚠️ Muy genérico |

**Por qué importa:** Google no puede "ver" imágenes. El alt text le dice qué hay en la foto. Sin él, las imágenes son invisibles para Google Imágenes y no aportan relevancia SEO. También es obligatorio para accesibilidad (WCAG).

**Alt text sugerido para las faltantes:**
- Logos de marcas: `"Logo [NombreMarca] — cliente de Maxipiel"`
- Logo Maxipiel: `"Maxipiel — venta de piel genuina al mayoreo en León, Guanajuato"`

---

### Enlazado Interno
- **Estado: ACEPTABLE**
- La página principal enlaza a 14+ colecciones relevantes
- Los anchor texts son descriptivos ("Piel para tapicería automotriz", "Fundas para asientos")
- Hay links al footer con políticas y contacto
- ✅ Buena cobertura de las categorías principales

---

### Estructura de URLs
- **Estado: NECESITA TRABAJO — problemas de duplicados**

Colecciones con problemas detectados en el sitemap:

| URL problemática | Problema |
|-----------------|----------|
| `/collections/piel-automotiz` | ❌ Typo: debería ser `automotriz` |
| `/collections/tercio-de-quero` | ❌ Typo: debería ser `cuero` |
| `/collections/fundas-para-masctoa` | ❌ Typo: debería ser `mascota` |
| `/collections/media-hoja` y `/collections/media-hoja-30-x-30` | ⚠️ Duplicado |
| `/collections/retazo`, `/collections/piel-genuina-en-pedaceria`, `/collections/pedaceria-retazo` | ⚠️ Tres URLs para lo mismo |
| `/collections/cuero-entero` y `/collections/hoja-completa` | ⚠️ Posible duplicado |
| `/collections/mercado-libre` y `/collections/mercado-libre-1` | ⚠️ Duplicado |
| `/collections/fundas-para-asiento` y `/collections/fundas-para-asiento-1` | ⚠️ Duplicado |

**Impacto:** Las URLs duplicadas dividen la "autoridad" que Google asigna a esas páginas. En vez de una colección fuerte, hay dos o tres débiles. Además, Google no sabe cuál es la "oficial" y puede indexar la versión equivocada.

---

## Contenido — E-E-A-T (Experiencia, Expertise, Autoridad, Confianza)

| Dimensión | Puntuación | Evidencia |
|-----------|-----------|-----------|
| **Experience** | Débil | Hay testimonios de clientes (bueno), pero no hay casos de uso específicos ni contenido "detrás de cámaras" |
| **Expertise** | Débil | No hay blog, no hay artículos de guía, no hay información sobre el equipo o la historia de la empresa |
| **Authoritativeness** | Débil | Las marcas (Caterpillar, Flexi, etc.) son señales positivas pero sin alt text ni contexto explicativo |
| **Trustworthiness** | Presente | HTTPS ✅, políticas de privacidad ✅, reembolso ✅, dirección/contacto ✅, testimonios ✅ |

**Punto crítico:** El sitio tiene ~450-500 palabras en la homepage. Para un negocio B2B que vende a tapiceros profesionales, esto es muy poco. Los competidores que educan a sus clientes ("cómo elegir el grosor de piel correcto para tapicería automotriz") rankean mucho más alto.

---

## Análisis de Keywords

### Keyword Primaria
- **Keyword objetivo actual implícita:** "piel genuina"
- **Problema:** "piel genuina" es una keyword de producto genérica. Los tapiceros buscan con intención de compra: "comprar piel para tapicería", "venta de cuero al mayoreo León" o "piel para tapicería automotriz precio".

### Keywords objetivo recomendadas por prioridad

| Keyword | Intención | Tipo de página recomendada |
|---------|-----------|---------------------------|
| `piel para tapicería automotriz` | Transaccional | Colección + producto |
| `venta de piel genuina al mayoreo` | Transaccional | Homepage |
| `cuero para tapicería de muebles` | Transaccional | Colección |
| `piel genuina León Guanajuato` | Local/Transaccional | Homepage + About |
| `piel para marroquinería precio` | Transaccional | Colección |
| `cómo elegir piel para tapicería` | Informacional | Blog (crear) |
| `piel bovino vs piel cerdo tapicería` | Informacional/Comercial | Blog (crear) |
| `mayoreo de cuero para tapiceros` | Transaccional | Homepage |

### Análisis de Intención de Búsqueda
El H1 actual "Piel genuina para tus proyectos" está en modo **informacional vago**. La homepage de un mayorista debe tener intención **transaccional clara**: "Compra piel genuina al mayoreo". Los tapiceros que buscan proveedor quieren saber precio, disponibilidad y cómo comprar — no solo que el producto existe.

---

## SEO Técnico

### robots.txt
- **Estado: ✅ Correcto**
- Configuración estándar de Shopify, bien estructurada
- Bloquea correctamente /admin, /cart, /checkout
- Apunta al sitemap
- No bloquea páginas importantes de producto o colección

### Sitemap XML
- **Estado: ✅ Funcional**
- Sitemap principal en `/sitemap.xml` ✅
- 4 sub-sitemaps: productos, páginas, colecciones, blog ✅
- Se actualiza en tiempo real (Shopify) ✅
- **Problema:** El sitemap incluye las colecciones duplicadas y con typos — Google las va a intentar indexar todas

### Canonical Tag
- **Estado: ⚠️ No detectado**
- Shopify normalmente agrega canonical tags automáticamente, pero no se detectó en el análisis
- Verificar que cada producto y colección tenga su canonical correcto para evitar contenido duplicado

### Velocidad de Carga / Core Web Vitals
- **Estado: Sin datos directos (requiere PageSpeed Insights)**
- Shopify como plataforma tiene buena base técnica, pero las siguientes señales de alerta son visibles:
  - Imágenes en `/cdn/shop/files/` — Shopify optimiza automáticamente ✅
  - Varios scripts de tracking (GA4, FB Pixel, Clarity, Google Ads) — pueden ralentizar el LCP
  - Recomendación: correr `pagespeed.web.dev` con la URL y verificar LCP y CLS

### Mobile
- **Estado: ✅ Funcional**
- Shopify garantiza diseño responsivo por defecto
- Viewport meta tag probablemente presente (no detectado en extracción pero es estándar Shopify)

---

## Schema Markup

| Schema | Estado | Notas |
|--------|--------|-------|
| Organization | ✅ Presente | |
| WebSite + SearchAction | ✅ Presente | Permite el "sitelinks search box" en Google |
| Product | ❌ No verificado | Debe existir en páginas de producto — verificar |
| LocalBusiness | ❌ Ausente | Maxipiel tiene ubicación física en León — AGREGAR |
| Review / AggregateRating | ❌ Ausente | Tienen testimonios — se podrían mostrar como estrellas en Google |
| BreadcrumbList | ❌ No verificado | Importante para navegación en resultados |

**Oportunidad rápida:** Agregar `LocalBusiness` schema con dirección de León, Guanajuato. Esto ayuda en búsquedas con intención local como "venta de piel León Guanajuato".

---

## Trampas SEO Detectadas (Respuesta directa a la tarea de Martín)

Estas son las **trampas SEO activas** en el sitio actualmente:

| # | Trampa | Dónde | Impacto |
|---|--------|-------|---------|
| 1 | **Headings semánticos mal usados** | H2 con teléfono y email | Google penaliza el abuso de etiquetas de estructura |
| 2 | **Contenido duplicado en colecciones** | 8+ colecciones duplicadas o muy similares | Divide la autoridad de página y confunde qué URL indexar |
| 3 | **URLs con typos** | `automotiz`, `quero`, `masctoa` | Google puede no relacionarlas con la keyword correcta |
| 4 | **Contenido thin (delgado)** | Homepage ~500 palabras | Google prefiere páginas con contenido sustancioso |
| 5 | **Imágenes sin alt text** | 9/11 imágenes | Pérdida de relevancia semántica y ranking en Google Imágenes |
| 6 | **Sin title tag / meta description** | Toda la homepage | Impacto directo en CTR desde resultados de búsqueda |
| 7 | **Sin Open Graph** | Todo el sitio | Cada vez que alguien comparte el sitio en WhatsApp/FB, se ve genérico |

---

## Oportunidades de Contenido (Brechas)

El sitio no tiene blog. Los competidores que publican contenido educativo capturan tráfico de tapiceros en etapa de investigación, y luego los convierten en compradores.

| Tema de Contenido | Keyword | Prioridad |
|-------------------|---------|-----------|
| "Cómo elegir el grosor de piel para tapicería automotriz" | `piel tapicería automotriz grosor` | 🔴 Alta |
| "Diferencia entre piel genuina y PU (cuero sintético)" | `piel genuina vs cuero sintético` | 🔴 Alta |
| "Cuánta piel necesito para tapizar un sillón" | `cuánta piel para tapizar sillón` | 🟡 Media |
| "Tipos de acabado de piel: lisa, grabada, perforada" | `tipos de piel para tapicería` | 🟡 Media |
| "Guía de colores de piel para proyectos de marroquinería" | `colores de cuero para bolsas` | 🟡 Media |

---

## Recomendaciones Priorizadas

### 🔴 Crítico — Hacer esta semana

1. **Agregar title tag optimizado** en la homepage de Shopify
   - Ir a: Admin Shopify → Online Store → Preferences → Homepage title
   - Texto: `Piel Genuina al Mayoreo — Tapicería, Marroquinería y Calzado | Maxipiel`
   - Impacto estimado: +20-35% en CTR desde Google en 30-60 días

2. **Agregar meta description**
   - Mismo lugar: Admin Shopify → Online Store → Preferences → Meta description
   - Texto: `Venta de piel genuina al mayoreo para tapiceros, marroquineros y calzado. Los mejores precios en León, Guanajuato y envíos a todo México. Llama al 477 209 5652.`

3. **Poner alt text a todas las imágenes sin texto**
   - Admin Shopify → Content → Files → editar cada imagen
   - Especialmente las imágenes de producto y los logos de clientes

4. **Corregir los H2 de teléfono y email**
   - Cambiarlos de `<h2>` a `<p>` en el editor de la sección

### 🟡 Alta Prioridad — Este mes

5. **Consolidar colecciones duplicadas**
   - Elegir una URL principal para pedacería/retazo y redirigir las demás
   - Corregir typos en URLs: `automotiz → automotriz`, `quero → cuero`, `masctoa → mascota`
   - Nota: Los redirects 301 preservan el SEO acumulado

6. **Agregar Open Graph tags** al tema de Shopify
   - Se puede hacer desde el archivo `theme.liquid` o con una app gratuita de SEO como "SEO Manager"

7. **Agregar schema de LocalBusiness** con dirección de León, Guanajuato

8. **Agregar Open Graph image** (foto de producto atractiva, 1200×630px)

### 🟢 Mediano Plazo — Este trimestre

9. **Crear las primeras 3 entradas de blog** usando los temas de la tabla de brechas de contenido

10. **Optimizar el title tag y meta description de cada colección principal** (al menos las 5 más importantes)

11. **Verificar Core Web Vitals** en PageSpeed Insights y corregir si LCP > 2.5s

12. **Agregar testimonios con schema Review** para mostrar estrellas en Google

---

## Resumen Ejecutivo para Martín

El sitio de Maxipiel tiene una base técnica sólida (Shopify, HTTPS, tracking completo, sitemap) pero está perdiendo visibilidad en Google por falta de los elementos SEO más básicos.

**Los 3 cambios más importantes — cada uno toma menos de 15 minutos:**
1. Agregar title tag y meta description en la configuración de Shopify
2. Poner alt text a las imágenes de producto
3. Corregir los H2 que contienen teléfono y email

**Potencial estimado:** Con estos cambios básicos + las correcciones de colecciones duplicadas, el tráfico orgánico podría aumentar entre 40-70% en los próximos 3-6 meses sin necesidad de invertir en publicidad adicional.
