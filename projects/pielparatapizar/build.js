/**
 * Genera index.html con los productos REALES de la tienda Shopify.
 *
 * Uso:  node build.js
 *
 * DESIGN READ (skill design-taste-frontend):
 *   Landing de anuncios para tapiceros profesionales que compran materia prima.
 *   Lenguaje comercial orientado a producto y confianza, sobre CSS nativo con
 *   fotografia real como visual principal.
 *   Diales: DESIGN_VARIANCE 6 · MOTION_INTENSITY 3 · VISUAL_DENSITY 4
 *   El comprador es pragmatico: busca color, medida y precio. No viene por animaciones.
 *
 * PALETA: extraida del logo real de Maxipiel (aguila en escudo), no de un default.
 *   rojo #c02418 · dorado #e49c48 · crema #fce4c0 · negro calido #240c00
 *   Acento unico: el rojo de marca. El dorado se reserva SOLO para cifras de precio
 *   (regla documentada y aplicada en toda la pagina). El verde de WhatsApp es color
 *   de plataforma en su boton, no un acento de diseño.
 *
 * Ver README para refrescar datos y para las reglas que sigue esta pagina.
 */

const fs = require('fs');
const path = require('path');

const items = JSON.parse(fs.readFileSync(path.join(__dirname, 'productos.json'), 'utf8'));

// Prueba social calculada del inventario real. Nunca se inventa.
// Se redondea hacia abajo a la centena para no exagerar si baja el inventario.
const stockTotal = items.reduce((s, x) => s + (x.inv || 0), 0);
const stockRedondo = (Math.floor(stockTotal / 100) * 100).toLocaleString('es-MX');
const stockMinimo = Math.min(...items.map(x => x.inv || 0));

const WA = 'https://wa.me/5214791424121';
const MSG = encodeURIComponent('Hola Maxipiel, quiero cotizar piel para tapizar.');
// Colección "Hojas de Piel" (39 productos). Es el destino correcto para esta
// landing: el comprador que busca "piel para tapizar" quiere la hoja, no una
// categoría de mueble. Verificado 2026-08-05.
const TIENDA = 'https://www.maxipiel.com/collections/catalogo-hojas-piel';
const TEL = '4772095652';

const foto = (url, w) => `${url}?width=${w}`;

// Glifo de marca de WhatsApp (Simple Icons). Se define UNA vez como <symbol>
// al inicio del body y los botones lo reutilizan con <use>, para no repetir
// el mismo path 3 veces. Es una marca de plataforma, no un icono dibujado a mano.
const spriteWA = `<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.8 11.8 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.9 11.9 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.82 11.82 0 0 0-3.48-8.413Z"/></symbol></svg>`;

const btnWA = (id, txt) =>
  `<a class="btn btn-wa" id="${id}" href="${WA}?text=${MSG}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg><span>${txt}</span></a>`;

// --- muro de colores reales ---
const swatches = items.map((it, i) => `
        <a class="sw" href="https://www.maxipiel.com/products/${it.h}" target="_blank" rel="noopener">
          <img src="${foto(it.img, 400)}" alt="Piel color ${it.t} para tapizar" loading="${i < 8 ? 'eager' : 'lazy'}" width="400" height="400">
          <span>${it.t}</span>
        </a>`).join('');

// mosaico del hero: 4 fotos reales
const mosaico = items.slice(0, 4).map((it, i) => `
        <img src="${foto(it.img, 420)}" alt="Piel color ${it.t}" ${i < 2 ? 'fetchpriority="high"' : 'loading="lazy"'} width="420" height="420">`).join('');

const html = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Piel para Tapizar en León | ${items.length} colores en existencia | Maxipiel</title>
<meta name="description" content="Cuero top grain para tapizar muebles, salas y autos. Cuero entero de 5 m² desde $2,590 o medio cuero desde $1,340. ${items.length} colores en existencia. Entrega en León, Gto. y envíos a todo México.">
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://www.pielparatapizar.com/">
<meta property="og:url" content="https://www.pielparatapizar.com/">
<meta property="og:type" content="website">
<meta property="og:title" content="Piel para Tapizar | ${items.length} colores en existencia">
<meta property="og:description" content="Cuero top grain para tapicería. Hoja completa de 5 m² desde $2,590. Desde León, Gto. a todo México.">
<meta property="og:image" content="${foto(items[0].img, 1200)}">
<meta property="og:locale" content="es_MX">
<link rel="preconnect" href="https://cdn.shopify.com">
<link rel="preload" href="fonts/rubik-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="img/logo.png">

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-17085508378"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-17085508378');
</script>

<style>
/* Rubik variable, servida desde el propio dominio: un solo archivo de 34 KB,
   subset latin (cubre todos los acentos del español). Sin peticiones a Google.
   font-display:swap para que el texto se lea desde el primer frame. */
@font-face{
  font-family:'Rubik';
  src:url('fonts/rubik-latin.woff2') format('woff2-variations');
  font-weight:300 900;
  font-style:normal;
  font-display:swap;
}

/* ============================================================
   Tokens. Un solo tema a la vez: oscuro por defecto (expresion
   de marca), claro si el sistema lo pide. Ninguna seccion invierte.
   ============================================================ */
:root{
  --bg:#191310; --bg2:#221a15; --line:#38291f;
  --txt:#f6ece0; --txt2:#b9a893;
  --accent:#c02418; --accent-alto:#d93a2b;
  --precio:#e49c48;              /* dorado de marca, SOLO para cifras de precio */
  --wa:#25D366;                  /* color de plataforma, solo en su boton */
  --r:12px;                      /* escala de radio unica en toda la pagina */
  --max:1120px;
}
@media (prefers-color-scheme: light){
  :root{
    --bg:#f5f5f4; --bg2:#fdfdfc; --line:#dcd8d3;
    --txt:#1f1d1b; --txt2:#615a53;
    --accent:#a81f14; --accent-alto:#c02418;
    --precio:#8a5a12;
  }
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--txt);
  font-family:'Rubik',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  line-height:1.55;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
img{display:block;max-width:100%;height:auto}
a{color:inherit}
.wrap{max-width:var(--max);margin:0 auto;padding:0 20px}

/* ---------- nav: una sola linea, 68px ---------- */
.nav{border-bottom:1px solid var(--line);background:var(--bg)}
.nav .wrap{height:68px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.marca{display:flex;align-items:center;gap:11px;text-decoration:none}
.marca img{height:38px;width:auto}
.marca b{font-size:17px;letter-spacing:-.2px}
.marca span{display:block;font-size:11.5px;color:var(--txt2);font-weight:400;letter-spacing:.2px}
.nav-der{display:flex;align-items:center;gap:14px}
.nav-tel{font-size:14.5px;color:var(--txt2);text-decoration:none;white-space:nowrap}
.nav-tel:hover{color:var(--txt)}

/* ---------- botones ---------- */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;
  padding:14px 22px;border-radius:var(--r);font-size:16px;font-weight:700;
  text-decoration:none;border:0;cursor:pointer;white-space:nowrap;
  transition:transform .12s ease,background-color .12s ease}
.btn:active{transform:translateY(1px)}
.btn svg{width:19px;height:19px;flex:none}
.btn-wa{background:var(--wa);color:#08130a}
.btn-wa:hover{background:#1fbb59}
.btn-sec{background:transparent;color:var(--txt);border:1px solid var(--line);
  padding:14px 22px;border-radius:var(--r);font-weight:700;font-size:16px;
  text-decoration:none;display:inline-flex;align-items:center;white-space:nowrap;
  transition:border-color .12s ease}
.btn-sec:hover{border-color:var(--accent)}
.nav .btn{padding:10px 16px;font-size:14.5px}

/* ---------- hero: split asimetrico ---------- */
.hero{padding:56px 0 60px}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:44px;align-items:center}
.hero h1{margin:0 0 16px;font-size:clamp(30px,4.4vw,52px);line-height:1.06;
  letter-spacing:-1.4px;font-weight:800}
.hero h1 b{color:var(--accent);font-weight:800}
.hero .sub{margin:0 0 26px;font-size:17.5px;color:var(--txt2);max-width:44ch}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px}
.mosaico{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.mosaico img{aspect-ratio:1;object-fit:cover;width:100%;border-radius:var(--r)}

/* ---------- franja de cifras: sin tarjetas ---------- */
.cifras{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--bg2)}
.cifras .wrap{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;padding-top:26px;padding-bottom:26px}
.cifras div b{display:block;font-size:27px;font-weight:800;letter-spacing:-.7px;line-height:1.2}
.cifras div span{font-size:14px;color:var(--txt2)}

/* ---------- secciones ---------- */
section{padding:60px 0}
h2{font-size:clamp(23px,2.9vw,31px);margin:0 0 10px;letter-spacing:-.7px;line-height:1.15}
.lead{color:var(--txt2);margin:0 0 30px;font-size:16.5px;max-width:62ch}

/* ---------- muro de colores ---------- */
.muro{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:13px}
.sw{text-decoration:none;display:block}
.sw img{aspect-ratio:1;object-fit:cover;width:100%;border-radius:var(--r);
  border:1px solid var(--line);transition:transform .15s ease}
.sw:hover img{transform:scale(1.035)}
.sw span{display:block;margin-top:8px;font-size:13.5px;font-weight:600;color:var(--txt2)}

/* ---------- precios: destacado + resto ---------- */
.precios{display:grid;grid-template-columns:1.25fr 1fr;gap:16px}
.pz{border:1px solid var(--line);border-radius:var(--r);padding:26px;background:var(--bg2)}
.pz.top{display:flex;flex-direction:column;justify-content:center;
  border-color:var(--accent);background:linear-gradient(180deg,var(--bg2),var(--bg))}
.pz h3{margin:0;font-size:19px}
.pz .med{font-size:14px;color:var(--txt2);margin:3px 0 12px}
.pz .cifra{font-size:38px;font-weight:800;letter-spacing:-1.4px;color:var(--precio);line-height:1}
.pz.chico .cifra{font-size:27px}
.pz p{margin:12px 0 0;font-size:14.5px;color:var(--txt2)}
.precios .col{display:grid;gap:16px}

/* ---------- trabajos: trio asimetrico ---------- */
.trabajos{display:grid;grid-template-columns:1.4fr 1fr;gap:14px}
.trabajos img{width:100%;height:100%;object-fit:cover;border-radius:var(--r)}
.trabajos .lado{display:grid;gap:14px}
.trabajos .grande img{aspect-ratio:4/5}
.trabajos .lado img{aspect-ratio:16/11}

/* ---------- testimonio ---------- */
.cita{background:var(--bg2);border-left:3px solid var(--accent);
  border-radius:0 var(--r) var(--r) 0;padding:30px 32px;max-width:760px}
.cita p{margin:0 0 16px;font-size:20px;line-height:1.45;letter-spacing:-.3px}
.cita cite{font-style:normal;font-size:14.5px;color:var(--txt2)}
.cita cite b{color:var(--txt);font-weight:700}

/* ---------- faq ---------- */
details{border-bottom:1px solid var(--line);padding:16px 0}
details summary{cursor:pointer;font-weight:650;font-size:16px;list-style:none;
  display:flex;justify-content:space-between;gap:16px;align-items:center}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";color:var(--accent);font-size:21px;font-weight:700;line-height:1}
details[open] summary::after{content:"–"}
details p{margin:12px 0 2px;font-size:15px;color:var(--txt2);max-width:70ch}

/* ---------- cierre centrado ---------- */
.cierre{text-align:center;border-top:1px solid var(--line);background:var(--bg2)}
.cierre .lead{margin-left:auto;margin-right:auto}
.cierre .hero-cta{justify-content:center}

footer{border-top:1px solid var(--line);padding:26px 0;font-size:14px;color:var(--txt2)}
footer a{color:var(--txt);text-decoration:none}
footer .wrap{display:flex;flex-wrap:wrap;gap:8px 22px;justify-content:space-between}

@media(max-width:900px){
  .hero .wrap{grid-template-columns:1fr;gap:30px}
  .precios{grid-template-columns:1fr}
  .trabajos{grid-template-columns:1fr}
  .trabajos .lado{grid-template-columns:1fr 1fr}
}
@media(max-width:640px){
  .hero{padding:36px 0 40px}
  section{padding:44px 0}
  .nav-tel{display:none}
  .marca span{display:none}
  .cifras .wrap{grid-template-columns:1fr;gap:16px}
  .cifras div b{font-size:23px}
  .btn,.btn-sec{flex:1 1 100%}
  .muro{grid-template-columns:repeat(auto-fill,minmax(108px,1fr));gap:10px}
  .cita{padding:22px 22px}
  .cita p{font-size:17.5px}
}
/* ---------- estados iniciales de animacion ----------
   Solo se aplican si la clase .anim esta en <html>, y esa clase la pone un
   script que se quita solo si Motion no carga. Sin JS o con el CDN caido,
   NADA queda oculto: la pagina se ve completa. */
.anim [data-anim]{opacity:0}
.anim [data-anim="up"]{transform:translateY(18px)}
.anim [data-anim="pop"]{transform:scale(.96)}

@media (prefers-reduced-motion: reduce){
  html{scroll-behavior:auto}
  *{transition:none !important;animation:none !important}
  .anim [data-anim]{opacity:1 !important;transform:none !important}
}
</style>
<script>
  /* Marca que vamos a animar, salvo que el visitante pida menos movimiento.
     El temporizador de seguridad revela todo si Motion nunca carga; el modulo
     lo cancela en cuanto Motion responde, para no matar los efectos de scroll. */
  (function(){
    try{
      if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      var h = document.documentElement;
      h.classList.add('anim');
      window.__revelarTodo = function(){
        h.classList.remove('anim');
        document.querySelectorAll('.sw').forEach(function(s){
          s.style.opacity = ''; s.style.transform = '';
        });
      };
      window.__animSeguro = setTimeout(window.__revelarTodo, 2500);
    }catch(e){}
  })();
</script>
</head>
<body>
${spriteWA}

<nav class="nav">
  <div class="wrap">
    <a class="marca" href="/">
      <img src="img/logo.png" srcset="img/logo.png 1x, img/logo@2x.png 2x" alt="Maxipiel" width="98" height="96" style="height:38px;width:auto">
      <span style="display:block"><b style="display:block">Maxipiel</b><span>León, Gto.</span></span>
    </a>
    <div class="nav-der">
      <a class="nav-tel" href="tel:${TEL}">477 209 5652</a>
      ${btnWA('wa-nav', 'WhatsApp')}
    </div>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <div>
      <h1 data-anim="up">Piel para tapizar,<br><b>${items.length} colores</b> en existencia</h1>
      <p class="sub" data-anim="up">Cuero top grain para salas, sillones, sillas y automotriz. Te vendemos una hoja o el material de todo un taller.</p>
      <div class="hero-cta" data-anim="up">
        ${btnWA('wa-hero', 'Cotizar por WhatsApp')}
        <a class="btn-sec" id="store-hero" href="${TIENDA}" target="_blank" rel="noopener">Ver catálogo completo</a>
      </div>
    </div>
    <div class="mosaico" data-anim="pop">${mosaico}
    </div>
  </div>
</header>

<div class="cifras">
  <div class="wrap">
    <div data-anim="up"><b data-cuenta="${stockTotal}">+${stockRedondo}</b><span>cueros en almacén hoy</span></div>
    <div data-anim="up"><b>${items.length}</b><span>colores listos para salir</span></div>
    <div data-anim="up"><b>Mismo día</b><span>entrega en León, envíos a todo México</span></div>
  </div>
</div>

<section>
  <div class="wrap">
    <h2 data-anim="up">Los ${items.length} colores que tenemos hoy</h2>
    <p class="lead" data-anim="up">Fotos del material real, no renders. Ningún color baja de ${stockMinimo} piezas en almacén, así que no te quedas a media sala esperando resurtido. Toca cualquiera para ver medidas y disponibilidad.</p>
    <div class="muro">${swatches}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 data-anim="up">Cómo se vende</h2>
    <p class="lead" data-anim="up">La piel se vende por pieza, no por metro lineal como la tela. Estas son las medidas que manejamos.</p>
    <div class="precios">
      <div class="pz top">
        <h3>Cuero entero</h3>
        <p class="med">500 dm², alrededor de 5 m²</p>
        <div class="cifra">$2,590</div>
        <p>La hoja completa. Es lo que más conviene por metro y lo que piden los talleres. Una sala de 3 piezas normalmente lleva entre 3 y 5.</p>
      </div>
      <div class="col">
        <div class="pz chico">
          <h3>Medio cuero</h3>
          <p class="med">250 dm², alrededor de 2.5 m²</p>
          <div class="cifra">$1,340</div>
        </div>
        <div class="pz chico">
          <h3>Entero perforado</h3>
          <p class="med">Para asientos que necesitan respirar</p>
          <div class="cifra">$3,250</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 data-anim="up">Trabajos hechos con nuestra piel</h2>
    <p class="lead" data-anim="up">Tapicería automotriz de clientes que nos compran el material. Si quieres ver más, pídelas por WhatsApp y te mandamos el álbum completo.</p>
    <div class="trabajos">
      <div class="grande"><img src="img/trabajo1.jpg" alt="Asiento de camioneta retapizado en piel color camel" loading="lazy" width="800" height="800"></div>
      <div class="lado">
        <img src="img/trabajo2.jpg" alt="Asiento trasero de automóvil tapizado en piel color conac" loading="lazy" width="800" height="800">
        <img src="img/trabajo3.jpg" alt="Par de asientos tapizados en piel azul con costura de rombos" loading="lazy" width="800" height="800">
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 data-anim="up">Lo que dicen quienes ya compraron</h2>
    <div class="cita">
      <p>“Encontré esta hermosa pieza de piel. La textura al tacto es sumamente tersa. Definitivamente volveré a comprar en este sitio.”</p>
      <cite><b>Jose Martinez</b>, sobre el Cuero Top Grain Oxblood. Reseña verificada, 5 estrellas.</cite>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 data-anim="up">Preguntas frecuentes</h2>
    <p class="lead" data-anim="up">Lo que más nos preguntan los tapiceros antes de su primer pedido.</p>

    <details><summary>¿Cuánto material necesito para una sala?</summary>
      <p>Depende del modelo, pero una sala de 3 piezas normalmente lleva entre 3 y 5 cueros enteros. Mándanos foto por WhatsApp y te lo calculamos antes de que compres, así no te sobra ni te falta.</p></details>

    <details><summary>¿Puedo comprar solo una hoja?</summary>
      <p>Sí. No manejamos mínimos. Puedes llevarte medio cuero, un cuero entero o el material de todo un taller.</p></details>

    <details><summary>¿Hay descuento por volumen?</summary>
      <p>Sí, el precio baja conforme sube la cantidad. Los precios de arriba son por pieza suelta. Dinos cuánto necesitas y te pasamos tu precio.</p></details>

    <details><summary>¿Es piel genuina o sintética?</summary>
      <p>Genuina. Es cuero top grain, la capa superior de la piel. Nada de vinil, cuerina ni sintéticos.</p></details>

    <details><summary>¿Hacen envíos fuera de León?</summary>
      <p>Sí, por paquetería a todo México. En León entregamos local, normalmente el mismo día.</p></details>

    <details><summary>¿Puedo ver el color antes de comprar?</summary>
      <p>Las fotos de los colores son del material real. Si quieres verlo de cerca te mandamos más fotos y video por WhatsApp, y si estás en León puedes pasar al local.</p></details>
  </div>
</section>

<section class="cierre">
  <div class="wrap">
    <h2 data-anim="up">¿Qué vas a tapizar?</h2>
    <p class="lead" data-anim="up">Mándanos foto de tu proyecto y te decimos cuánto material necesitas y cuánto te sale. Lunes a Sábado de 10:00 a 18:00.</p>
    <div class="hero-cta">
      ${btnWA('wa-final', 'Cotizar por WhatsApp')}
      <a class="btn-sec" id="store-final" href="${TIENDA}" target="_blank" rel="noopener">Ver catálogo completo</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <span><b>Maxipiel</b>, León, Guanajuato. Envíos a todo México.</span>
    <span>WhatsApp <a href="${WA}" target="_blank" rel="noopener">479 142 4121</a> · Tel. <a href="tel:${TEL}">477 209 5652</a> · <a href="https://www.maxipiel.com" target="_blank" rel="noopener">maxipiel.com</a></span>
  </div>
</footer>

<script>
(function(){
  /* Conversion de Google Ads al tocar cualquier boton de WhatsApp */
  document.addEventListener('click', function(e){
    var t = e.target;
    if(!t || !t.closest) return;
    var a = t.closest('a[href*="wa.me"], a[href*="api.whatsapp.com"], a[href*="web.whatsapp.com"]');
    if(!a) return;
    if(typeof window.gtag !== 'function') return;
    window.gtag('event', 'conversion', { 'send_to': 'AW-17085508378/IrTfCIWH64YcEJrWgNM_' });
  }, true);

  /* Pasar gclid y utm_* a los enlaces de la tienda para no perder la atribucion */
  try {
    var qs = window.location.search;
    if (qs && qs.length > 1) {
      var p = new URLSearchParams(qs), keep = new URLSearchParams();
      ['gclid','gbraid','wbraid','gad_source','utm_source','utm_medium','utm_campaign','utm_term','utm_content']
        .forEach(function(k){ if(p.get(k)) keep.set(k, p.get(k)); });
      var extra = keep.toString();
      if (extra) {
        document.querySelectorAll('a[href*="maxipiel.com"]').forEach(function(a){
          a.href += (a.href.indexOf('?') === -1 ? '?' : '&') + extra;
        });
      }
    }
  } catch(err){ /* si falla, los enlaces siguen funcionando normal */ }
})();
</script>

<script type="module">
/* ============================================================
   Movimiento con Motion. Cada animacion tiene una razon:
     hero      -> jerarquia: lleva la vista del titular al boton
     mosaico   -> el producto entra en escena
     cifra     -> subraya el dato de confianza (inventario real)
     muro      -> 24 fotos de golpe abruman; entran escalonadas
     secciones -> ritmo de lectura al bajar
   Si el CDN falla o el visitante pide menos movimiento, la pagina
   se muestra completa y estatica. Nunca queda contenido oculto.
   ============================================================ */

const quieto = matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!quieto) {
  try {
    /* Motion 13 no exporta stagger desde el bundle del DOM, asi que el
       escalonado se calcula a mano con delay por indice. Importar stagger
       tiraria un error y dejaria la pagina sin animar. */
    const { animate, inView } = await import('https://cdn.jsdelivr.net/npm/motion@13/+esm');

    /* Motion cargo: cancelar la red de seguridad para que los efectos de
       scroll sigan vivos. La clase .anim se queda; las animaciones ganan
       porque escriben estilos en linea, que pesan mas que la regla CSS. */
    clearTimeout(window.__animSeguro);

    const suave = [0.16, 1, 0.3, 1];

    /* Keyframes explicitos (de -> a) para no depender del estado calculado */
    const subir = (el, i = 0, dur = .55) =>
      animate(el, { opacity: [0, 1], y: [18, 0] },
        { duration: dur, delay: i * 0.075, ease: suave });

    /* Entrada del hero, en secuencia: titular, texto, botones */
    document.querySelectorAll('.hero [data-anim="up"]').forEach((el, i) => subir(el, i, .6));
    const mos = document.querySelector('.mosaico');
    if (mos) animate(mos, { opacity: [0, 1], scale: [.96, 1] },
      { duration: .7, delay: .12, ease: suave });

    /* Cifra de inventario: cuenta hacia arriba para que el ojo se detenga ahi */
    const cifra = document.querySelector('[data-cuenta]');
    if (cifra) {
      const meta = parseInt(cifra.dataset.cuenta, 10) || 0;
      const fin = cifra.textContent;
      inView(cifra.closest('.cifras'), () => {
        animate(0, meta, {
          duration: 1.1, ease: 'easeOut',
          onUpdate: v => { cifra.textContent = '+' + (Math.floor(v / 100) * 100).toLocaleString('es-MX'); },
          onComplete: () => { cifra.textContent = fin; }
        });
      }, { amount: 0.5 });
    }

    /* Secciones y franja de cifras: aparecen al entrar en pantalla */
    document.querySelectorAll('section [data-anim], .cifras [data-anim]').forEach(el => {
      inView(el, () => subir(el), { amount: 0.2 });
    });

    /* Muro de colores: 24 fotos de golpe abruman, entran escalonadas */
    const muro = document.querySelector('.muro');
    if (muro) {
      const swatches = [...muro.querySelectorAll('.sw')];
      swatches.forEach(s => { s.style.opacity = '0'; });
      inView(muro, () => {
        swatches.forEach((s, i) => {
          animate(s, { opacity: [0, 1], y: [14, 0] },
            { duration: .5, delay: Math.min(i * 0.028, .8), ease: suave });
        });
      }, { amount: 0.1 });
    }

  } catch (e) {
    /* Motion no cargo o algo trono: revelar todo tal cual, sin animar */
    clearTimeout(window.__animSeguro);
    if (window.__revelarTodo) window.__revelarTodo();
  }
}
</script>
</body>
</html>
`;

fs.writeFileSync(path.join(__dirname, 'index.html'), html);
console.log('index.html generado con ' + items.length + ' colores reales (' + (html.length / 1024).toFixed(1) + ' KB)');
