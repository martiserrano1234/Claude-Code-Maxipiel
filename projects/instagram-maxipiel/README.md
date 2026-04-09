# Instagram Maxipiel — Profesionalización + Automatización

**Estado:** Activo — arquitectura definida, pendiente implementación
**Responsable:** Felix
**Cuenta:** [@maxipielmx](https://www.instagram.com/maxipielmx)
**ID Instagram:** 25766253203074987

---

## Diagnóstico actual (2026-03-13)

- **Seguidores:** 107 | **Siguiendo:** 18 | **Posts:** 99
- **Problema principal:** Contenido genérico de artesanía reutilizado, sin identidad de marca, sin producto real de Maxipiel
- **Engagement:** Casi cero (0-2 likes por post)
- **Frecuencia actual:** ~3 reels/día — demasiado, penaliza el alcance
- **Error en perfil:** El link del website apunta a "SecretCamouflage" en lugar de maxipiel.com.mx
- **Acceso API:** Token de Instagram conectado (corto plazo, renovar periódicamente)

---

## Objetivo

Automatizar publicaciones diarias de Instagram con contenido generado por IA (Higgsfield Soul 2.0), con aprobación humana vía WhatsApp antes de publicar. Que se vea 100% profesional y realista.

---

## Arquitectura del flujo automatizado

```
n8n (cron diario ~10am)
    → Google Sheets: sacar tema/prompt del día
    → Claude: refinar prompt para Soul Standard
    → Higgsfield API: generar imagen (Soul Standard)
    → Polling hasta status "completed" → URL de imagen
    → Higgsfield API: convertir a video (DoP Standard)
    → Polling hasta status "completed" → URL de video
    → Claude: generar caption + hashtags en tono Maxipiel
    → WhatsApp: enviar preview + caption + botones Aprobar/Rechazar
    → Esperar respuesta (webhook)
    → Si aprueba: Instagram Graph API → publicar como Reel
    → Google Sheets: marcar como publicado
```

---

## Stack técnico

| Herramienta | Función | Estado |
|-------------|---------|--------|
| **n8n** | Orquestador del flujo completo | Conectado |
| **Higgsfield API** | Generación de imagen y video con IA | Pendiente — necesita API Key + créditos |
| **Claude (API)** | Refinamiento de prompts + generación de captions | Disponible |
| **Instagram Graph API** | Publicación oficial de posts/reels | Pendiente — necesita configuración |
| **WhatsApp Business** | Aprobación humana antes de publicar | Pendiente — elegir proveedor |
| **Google Sheets** | Banco de temas/prompts + registro de publicaciones | Pendiente — crear hoja |

---

## Higgsfield API — Detalles técnicos

**Base URL:** `https://platform.higgsfield.ai`

**Autenticación:**
```
Authorization: Key {api_key}:{api_key_secret}
```

### Paso 1 — Generar imagen (Soul Standard)
```bash
POST https://platform.higgsfield.ai/higgsfield-ai/soul/standard
{
  "prompt": "...",
  "aspect_ratio": "9:16",
  "resolution": "720p"
}
```
Responde con `request_id`. Luego hacer polling:
```
GET https://platform.higgsfield.ai/requests/{request_id}/status
```
Estados: `queued` → `in_progress` → `completed`
Cuando completa, devuelve URL de la imagen.

### Paso 2 — Convertir imagen a video (DoP Standard)
```bash
POST https://platform.higgsfield.ai/higgsfield-ai/dop/standard
{
  "image_url": "URL_de_imagen_anterior",
  "prompt": "slow cinematic movement, leather texture, premium feel",
  "duration": 5
}
```
Mismo proceso de polling. Devuelve URL del video.

### Modelos disponibles en la cuenta
| Modelo | Tipo | Uso |
|--------|------|-----|
| `higgsfield-ai/soul/standard` | Text to Image | Generar imagen base |
| `higgsfield-ai/dop/lite` | Image to Video | Video rápido, menor calidad |
| `higgsfield-ai/dop/standard` | Image to Video | Video balanceado |
| `higgsfield-ai/dop/turbo` | Image to Video | Video más rápido |
| `soul/character` | Text to Image | Con personaje específico |
| `soul/reference` | Text to Image | Con imagen de referencia |
| `popcorn/auto` | Text to Image | Auto-optimizado |

---

## Modelos de imagen alternativos (también en la API)
- `reve/text-to-image`
- `bytedance/seedream/v4/edit`
- `kling-video/v2.1/pro/image-to-video`
- `bytedance/seedance/v1/pro/image-to-video`

---

## Pasos para implementar

### 1. Higgsfield (pendiente Felix)
- [ ] Crear API Key en cloud.higgsfield.ai → API Keys → "+ Create API Key"
- [ ] Guardar el `api_key` y `api_key_secret` (solo se muestran una vez)
- [ ] Revisar precios en higgsfield.ai/pricing
- [ ] Comprar créditos (calcular: 2 runs/día × 30 días = ~60 runs/mes mínimo)

### 2. Instagram Graph API (pendiente)
- [ ] Verificar que la cuenta @maxipielmx es Instagram Business
- [ ] Conectar a una Página de Facebook si no está conectada
- [ ] Obtener token de larga duración para la Graph API
- [ ] Configurar nodo de Instagram en n8n

### 3. WhatsApp para aprobación (pendiente — elegir uno)
- **WATI** (~$49/mes) — más fácil, tiene botones interactivos
- **Meta Cloud API** (gratis con límites) — ya tienen acceso Meta por los Ads
- **Twilio** (~$0.05/mensaje) — confiable, fácil de integrar con n8n

### 4. Google Sheets — banco de contenido (pendiente)
Crear hoja con columnas:
- `fecha` | `tema` | `prompt_base` | `status` | `url_publicacion`

### 5. Workflow n8n (pendiente — armar una vez que estén las credenciales)
- Sebastián o Felix pueden pedirle a Claude Code que lo construya cuando tengan las keys

---

## Estrategia de contenido

### 3 Pilares
1. **Producto en acción** — texturas, colores, rollos, cortes de piel Maxipiel
2. **UGC con IA** — tapiceros usando piel, resultado final (asientos, muebles, autos, motos)
3. **Contenido educativo** — guías para tapiceros: metros por proyecto, grosor, tipos de piel

### Frecuencia objetivo
| Formato | Frecuencia |
|---------|-----------|
| Reels UGC (Higgsfield) | 2x semana |
| Fotos de producto | 2x semana |
| Carrusel educativo | 1x semana |

**Total:** 4-5 posts/semana (no más — más frecuencia penaliza alcance)

### Horario
Publicar entre 9-11am hora México (UTC-6), con variación de ±30 min para que no se vea automatizado.

---

## Prompts base para Soul Standard (Maxipiel)

```
"Premium leather rolls in rich cognac brown, studio lighting, cinematic depth of field, 
professional photography style, leather texture detail, luxury material"

"Automotive leather upholstery in deep burgundy red, close-up texture shot, 
premium quality, workshop setting, professional lighting"

"Leather swatches fan arrangement showing multiple rich colors, 
top-down view, clean background, product photography"
```

---

## Notas importantes

- El cliente objetivo es **el tapicero**, no el dueño del mueble/auto
- Coherencia visual entre posts de Instagram y anuncios activos en Meta Ads
- El video final debe tener aspecto 9:16 (vertical) para Reels
- La aprobación por WhatsApp es clave — da control sin romper el flujo
- **No publicar más de 1 vez al día** para no penalizar el algoritmo
