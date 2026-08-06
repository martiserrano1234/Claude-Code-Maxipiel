# Landing pielparatapizar.com

Landing de una sola página para el dominio `pielparatapizar.com` (propiedad de Martín), pensada como **página de destino de los anuncios de Google Ads**, no como sitio de SEO.

## Por qué existe

La palabra clave núcleo de la cuenta es la familia "piel para tapizar / piel para tapicería". En el análisis del 2026-08-05 se detectó que la nota de **página de destino** de esas keywords estaba en "Promedio" en todas — mientras que la nota del anuncio estaba en "Superior al promedio".

Hoy los anuncios mandan a una colección genérica de la tienda Shopify. El usuario que buscó "piel para tapizar" cae en un catálogo donde tiene que buscar.

Mejorar esa nota baja el CPC con la misma puja. Y como la campaña pierde ~90% de impresiones por presupuesto, clics más baratos se traducen directo en más volumen sin gastar más.

**Importante:** el dominio NO da ventaja de posicionamiento por sí solo. Google desactivó el beneficio de los dominios de coincidencia exacta en 2012. Montarle un sitio de contenido sería contraproducente — dividiría la autoridad con maxipiel.com. Su valor está en ser una landing enfocada para anuncios.

## Qué trae

- **Muro de los 24 colores reales en existencia**, con foto del material y precio — es el corazón de la página. Cada color enlaza a su producto en la tienda
- **Precios reales y visibles**: medio cuero $1,340 · cuero entero $2,590 · perforado $3,250
- **2 botones de WhatsApp** (arriba y al cierre) al `wa.me/5214791424121` con mensaje pre-cargado
- **2 botones a la tienda** apuntando a la colección `catalogo-hojas-piel` ("Hojas de Piel", 39 productos). Es el destino correcto: quien busca "piel para tapizar" quiere la hoja, no una categoría de mueble. Los 24 colores del muro enlazan cada uno a su producto individual.
- Secciones: muro de colores, cómo se vende (medidas en dm² y m²), cómo comprar, preguntas frecuentes
- Responsive, sin dependencias externas salvo gtag y las fotos del CDN de Shopify

> **Por qué con datos reales:** la primera versión era genérica — puras tarjetas de beneficios ("surtido constante", "te asesoramos") sin una sola foto. Se notaba hecha con IA justo por eso. Un tapicero quiere ver la piel y el precio, no adjetivos. Todo el contenido de la página sale ahora de la tienda.

## Prueba social — de dónde salen los números

La franja del hero (`+4,700 cueros en existencia · 24 colores · mismo día en León`) se **calcula de `productos.json`**, no está escrita a mano. El total se redondea hacia abajo a la centena para que nunca exagere aunque baje el inventario entre builds.

Se descartaron a propósito los conteos de Shopify (114 pedidos, 289 clientes): reflejan solo la tienda en línea, no el negocio real de León + mayoreo + Mercado Libre, y ponerlos haría ver a Maxipiel más chico de lo que es. **No inventar cifras de prueba social** — si no sale de un dato verificable, no va.

## Decisiones de diseño (auditadas con `design-taste-frontend`)

La página se rehizo pasando su pre-flight completo. Lo que cambió y por qué:

**La paleta sale del logo, no de un default.** La versión anterior usaba fondo crema `#fbf8f4` + acento latón `#8a5a2b` + texto espresso. Esa combinación exacta está prohibida por la skill: es la que toda IA escoge para marcas artesanales y vuelve la marca invisible. La paleta actual se extrajo del logo real del águila: rojo `#c02418`, dorado `#e49c48`, crema `#fce4c0`, negro cálido `#240c00`.

- **Acento único:** el rojo de marca, en toda la página
- **El dorado se reserva solo para cifras de precio** (regla documentada, aplicada sin excepción)
- **El verde de WhatsApp** es color de plataforma en su propio botón, no un acento de diseño. Se conserva porque el botón verde de WhatsApp es una convención que el tapicero mexicano reconoce al instante

**Un solo tema.** Antes la página iba oscuro → claro → oscuro, lo que se siente como cambiar de sitio a media navegación. Ahora es oscuro de corrido, con variante clara automática si el sistema del visitante lo pide. Ninguna sección invierte.

**8 familias de layout distintas**, sin repetir: split asimétrico (hero), franja de cifras sin tarjetas, muro de fotos, precios destacado-más-resto, trío asimétrico de trabajos, cita, acordeón, cierre centrado. Se eliminaron las dos rejillas de 3 tarjetas iguales (el patrón más delator).

**Hero disciplinado:** 3 elementos de texto (titular, subtítulo, botones). El bloque de precios y la franja de cifras se movieron abajo, donde corresponden.

**Cero em-dashes** en todo el texto visible. Es el tic más reconocible de texto generado por IA.

**Detalles técnicos:** el glifo de WhatsApp se define una vez como `<symbol>` y se reutiliza con `<use>` en los 3 botones (antes eran 3 copias del mismo path, 3.5 KB de más). Todas las imágenes llevan `width`/`height` para no provocar saltos de layout, y `alt` descriptivo.

### Lo que falta y necesita material de Maxipiel

Ya integrados (2026-08-05): logo en el nav (recortado con fondo transparente desde `logo maxipiel.jpeg`), 3 fotos de trabajos de clientes, y 1 testimonio real.

Lo que sigue faltando y no se resuelve con código:

- **Fotos de MUEBLES tapizados.** Las 3 fotos que hay son de tapicería automotriz (asiento de camioneta, asiento trasero, par de asientos con rombos). La página vende sobre todo piel para salas y sillones, así que falta al menos una sala o sillón terminado.
- **Más testimonios.** Solo hay uno utilizable. Ver abajo.

> La skill `landing-page-design` sugiere generar imágenes hero con IA (`belt` / inference.sh). **No hacerlo aquí**: Maxipiel vende un material físico donde la autenticidad es el argumento de venta, y una foto generada se nota y resta credibilidad. Fotos reales o nada.

## Testimonios: qué hay y qué no

**Judge.me está instalado** en la tienda y tiene exactamente **2 reseñas** en total:

1. **5 estrellas, Jose Martinez, 2026-06-11**, sobre Cuero Top Grain Oxblood. Es la que está en la página, recortada a 3 líneas según la regla de citas. Habla de encuadernación, no de tapicería, pero es real y verificable.
2. **2 estrellas, 2026-08-03**, sobre la pedacería: *"Buena calidad de piel, mala descripción. Decía 80 cm x 80 cm aprox. y me llegaron piezas muy por debajo de esas medidas"*. No se usa, y **conviene atenderla**: es un problema de descripción de producto que va a seguir generando devoluciones.

**Google Maps no se pudo leer.** Las reseñas se cargan con JavaScript y no son accesibles sin la API de Google Places (requiere clave y facturación). Si se quieren esos testimonios, hay dos caminos: copiarlos a mano, o dar de alta la API de Places.

## Cómo se genera

La página se arma con `build.js` a partir de `productos.json`:

```
node build.js
```

`productos.json` trae los 24 colores con foto, precio e inventario, sacados de la colección `piel-para-muebles` vía Admin API de Shopify. Las fotos se sirven directo del CDN de Shopify con `?width=` — no se descarga ni duplica ninguna imagen, así que si cambian la foto de un producto en la tienda, la landing se actualiza sola.

### Refrescar los datos

Cuando cambien colores, precios o existencias, volver a sacar el JSON (necesita el token de Admin API, ver memoria `reference_shopify_admin_api`):

```bash
curl -s -H "X-Shopify-Access-Token: $TOKEN" -H "Content-Type: application/json" \
 -d '{"query":"{ collectionByHandle(handle:\"piel-para-muebles\"){ products(first:30){edges{node{ title handle totalInventory featuredImage{url} priceRangeV2{minVariantPrice{amount}} }}} } }"}' \
 "https://maxipiel.myshopify.com/admin/api/2024-10/graphql.json"
```

Quedarse con los que tengan foto e inventario > 0, mapear a `{t,h,img,p,inv}` y volver a correr `node build.js`.

> Los precios del hero (`$1,340 / $2,590 / $3,250`) están escritos a mano en `build.js` porque son los rangos de la línea Top Grain. Si cambian, actualizarlos ahí.

### Rastreo

- Etiqueta de Google Ads `AW-17085508378` en el `<head>`
- Listener delegado que dispara la conversión `AW-17085508378/IrTfCIWH64YcEJrWgNM_` ("Click WhatsApp") en cualquier clic a WhatsApp — el mismo evento que se instaló en el tema de Shopify el 2026-08-05
- Los parámetros `gclid`, `gbraid`, `wbraid`, `gad_source` y `utm_*` se copian automáticamente a los enlaces de la tienda, para no romper la atribución cuando el usuario salta de la landing a Shopify

## Cómo desplegarla

Mismo patrón que `projects/descuento-landing`: es un `index.html` estático.

1. En Vercel, **New Project → Import** este repo (o subir la carpeta directo)
2. Root directory: `projects/pielparatapizar`
3. Framework preset: **Other** (sin build, es HTML plano)
4. Deploy

### Apuntar el dominio

`pielparatapizar.com` **no resuelve todavía** — está comprado pero sin DNS configurado (verificado 2026-08-05).

1. En Vercel → Project → Settings → Domains → agregar `pielparatapizar.com` y `www.pielparatapizar.com`
2. Vercel muestra los registros a crear. En el registrador donde Martín compró el dominio:
   - `A` de `@` → `76.76.21.21`
   - `CNAME` de `www` → `cname.vercel-dns.com`
3. Esperar la propagación (de minutos a unas horas) y que Vercel emita el certificado SSL

> Los valores exactos los da Vercel al agregar el dominio — usar esos, no los de este README, por si cambian.

## Después de desplegar

1. **Probar la conversión**: abrir la landing, tocar el botón de WhatsApp y confirmar en Google Ads → Objetivos → Conversiones que se registró (tarda unas horas en aparecer)
2. **Apuntar los anuncios**: cambiar la URL final del grupo "Piel Tapiceria General" (id `199093372753`) a `https://pielparatapizar.com/`
3. **Medir contra lo actual**: dejar el grupo "Hojas y Mayoreo" (id `202036849587`) apuntando a Shopify por unas semanas y comparar tasa de conversión y nota de página de destino entre los dos

No cambiar las dos cosas al mismo tiempo — si se mueven ambas no se sabe cuál causó la diferencia.

## Pendiente relacionado

`maxipiel.com.mx` está sirviendo contenido idéntico a `maxipiel.com` (mismo peso al byte, verificado 2026-08-05). Contenido duplicado en dos dominios es un problema de SEO real y conviene resolverlo — lo normal es un redirect 301 de uno al otro. Revisar antes de sumar un tercer dominio al ecosistema.
