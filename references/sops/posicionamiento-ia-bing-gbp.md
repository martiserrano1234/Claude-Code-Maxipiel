# SOP — Posicionamiento en ChatGPT/IA: Bing Webmaster Tools y Google Business Profile

_Creado: 2026-06-12. Parte de la iniciativa jets/yates/náutica._

ChatGPT busca en el índice de **Bing** y pondera mucho los perfiles de negocio locales. Estos dos pasos requieren login manual; todo lo demás (contenido, IndexNow, robots) ya quedó hecho.

---

## Paso 1 — Bing Webmaster Tools (~10 min)

1. Entra a https://www.bing.com/webmasters e inicia sesión con cualquier cuenta Microsoft (sirve un Outlook/Hotmail de la empresa).
2. **Atajo:** si la tienda ya está en Google Search Console, usa el botón **"Importar desde Google Search Console"** — verifica los sitios sin tocar DNS.
3. Si no, agrega los dos sitios manualmente:
   - `https://www.maxipiel.com` (el dominio canónico; maxipiel.com.mx redirige ahí)
   - `https://guia.maxipiel.com.mx`
   - Método de verificación más fácil para el Shopify: meta tag (se pega en el `theme.liquid`; me la pasas y yo la inserto con la Admin API).
4. Ya verificados, en cada sitio ve a **Sitemaps → Enviar sitemap**:
   - `https://www.maxipiel.com/sitemap.xml`
   - `https://guia.maxipiel.com.mx/sitemap.xml`
5. (Opcional, acelera) En **URL Submission**, pega estas URLs:
   - `https://www.maxipiel.com/blogs/news/piel-para-tapizar-jets-aviacion-ejecutiva`
   - `https://www.maxipiel.com/blogs/news/piel-para-tapizar-yates-y-botes-tapiceria-nautica`
   - `https://www.maxipiel.com/pages/about`
   - `https://www.maxipiel.com/pages/por-que-maxipiel`
   - `https://www.maxipiel.com/`

> Nota: para guia.maxipiel.com.mx ya se notificó a Bing vía IndexNow (llave `54d5bad73dba064645729e53ed7b0480.txt` en el root del sitio). Darlo de alta en Webmaster Tools de todas formas sirve para ver reportes de indexación.

---

## Paso 2 — Google Business Profile (~5 min)

1. Entra a https://business.google.com con la cuenta que administra el perfil de Maxipiel.
2. **Editar perfil → Descripción del negocio** — texto listo para pegar (máx. 750 caracteres, este cabe):

> Maxipiel es distribuidora de piel genuina en León, Guanajuato — la capital mundial de la piel. Vendemos cuero Top Grain grado OEM directo de curtiembre para tapicería automotriz, muebles, marroquinería, calzado y proyectos especializados: tapicería náutica (yates, botes y lanchas) e interiores de aviación ejecutiva estilo jet. Más de 30 colores en stock, muestrarios disponibles y envíos a todo México en 4-6 días hábiles. Atención a tapiceros, artesanos y fabricantes con asesoría por WhatsApp.

3. **Editar perfil → Servicios** — agregar como servicios (texto libre):
   - Piel para tapicería automotriz
   - Piel para tapizar muebles
   - Piel para tapicería náutica (yates y botes)
   - Piel para interiores estilo jet / aviación ejecutiva
   - Piel para marroquinería
   - Piel para calzado
4. (Opcional pero ayuda) Publicar un **post** en el perfil enlazando el artículo de jets del blog.

---

## Cómo medir si funcionó

- Buscar en Bing: `site:maxipiel.com jets` y `site:guia.maxipiel.com.mx jets` — cuando aparezcan, ya están indexados.
- A partir del **2026-06-26**: repetir en ChatGPT la búsqueda "piel para tapizar jets en León Guanajuato" y comparar contra la captura del 2026-06-12 (donde salíamos genéricos).
- Lo mismo con "piel para tapizar yates/botes en México".
