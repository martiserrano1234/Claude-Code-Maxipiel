import urllib.request, json

TOKEN = 'TU_SHOPIFY_TOKEN'
SHOP = 'maxipiel.myshopify.com'
THEME_ID = '144344481892'
IMG_TALLER = 'https://cdn.shopify.com/s/files/1/0700/9045/7188/t/3/assets/banner-taller-maxipiel.png'
IMG_ROLLOS = 'https://cdn.shopify.com/s/files/1/0700/9045/7188/t/3/assets/banner-hero-maxipiel.png'

# ── 1. CUSTOM LIQUID para el hero slideshow ──────────────────────────────────
HERO_LIQUID = f"""
<div class="mp-slideshow" id="mpSlideshow">

  <div class="mp-slide mp-slide--active" style="background-image: url('{IMG_TALLER}')">
    <div class="mp-slide__overlay"></div>
    <div class="mp-slide__content mp-slide__content--left">
      <p class="mp-slide__eyebrow">Directo de las curtiembres de León · Sin intermediarios</p>
      <h1 class="mp-slide__heading">Piel genuina<br>para tapiceros</h1>
      <p class="mp-slide__sub">Automotriz · Muebles · Marroquinería</p>
      <a href="/collections/materia-prima" class="mp-slide__btn">Ver colores disponibles</a>
    </div>
  </div>

  <div class="mp-slide" style="background-image: url('{IMG_ROLLOS}')">
    <div class="mp-slide__overlay"></div>
    <div class="mp-slide__content mp-slide__content--center">
      <p class="mp-slide__eyebrow">Compra hoy y recíbelo directo en tu taller</p>
      <h2 class="mp-slide__heading">Envíos gratis<br>a todo México</h2>
      <a href="/collections/materia-prima" class="mp-slide__btn">Comprar ahora</a>
    </div>
  </div>

  <div class="mp-dots" id="mpDots">
    <span class="mp-dot mp-dot--active" onclick="mpGoTo(0)"></span>
    <span class="mp-dot" onclick="mpGoTo(1)"></span>
  </div>

</div>

<style>
.mp-slideshow {{ position: relative; width: 100%; overflow: hidden; height: 680px; }}
.mp-slide {{
  position: absolute; inset: 0;
  background-size: cover; background-position: center;
  opacity: 0; transition: opacity 0.8s ease; pointer-events: none;
}}
.mp-slide--active {{ opacity: 1; pointer-events: auto; }}
.mp-slide__overlay {{
  position: absolute; inset: 0;
  background: linear-gradient(to right, rgba(0,0,0,0.62) 0%, rgba(0,0,0,0.2) 60%, transparent 100%);
}}
.mp-slide__content--center .mp-slide__overlay {{
  background: rgba(0,0,0,0.45);
}}
.mp-slide__content {{
  position: absolute; top: 50%; transform: translateY(-50%);
  padding: 0 60px; max-width: 640px; color: #fff;
}}
.mp-slide__content--center {{
  left: 50%; transform: translate(-50%,-50%);
  text-align: center; max-width: 700px;
}}
.mp-slide__eyebrow {{
  font-size: 13px; letter-spacing: 2px; text-transform: uppercase;
  margin: 0 0 12px; color: #fff; text-shadow: 0 1px 6px rgba(0,0,0,0.8);
}}
.mp-slide__heading {{
  font-size: clamp(32px, 5vw, 60px); font-weight: 800;
  line-height: 1.1; margin: 0 0 28px; color: #fff;
  text-shadow: 0 2px 12px rgba(0,0,0,0.9);
}}
.mp-slide__sub {{
  font-size: 13px; letter-spacing: 1.5px; text-transform: uppercase;
  color: rgba(255,255,255,0.75); margin: -16px 0 24px;
  text-shadow: 0 1px 6px rgba(0,0,0,0.8);
}}
.mp-slide__btn {{
  display: inline-block; background: #fff; color: #1a1a1a;
  padding: 14px 32px; border-radius: 3px; font-weight: 700;
  font-size: 14px; letter-spacing: 1px; text-decoration: none;
  text-transform: uppercase; transition: background 0.2s;
}}
.mp-slide__btn:hover {{ background: #e8e8e8; }}
.mp-dots {{ position: absolute; bottom: 16px; right: 24px; display: flex; gap: 6px; }}
.mp-dot {{
  width: 7px; height: 7px; border-radius: 50%;
  background: rgba(255,255,255,0.45); cursor: pointer; transition: background 0.3s;
}}
.mp-dot--active {{ background: #fff; }}

@media (max-width: 749px) {{
  .mp-slideshow {{ height: 480px; }}
  .mp-slide__content {{ padding: 0 24px; max-width: 100%; }}
  .mp-slide__content--center {{ left: 50%; padding: 0 20px; }}
  .mp-slide__heading {{ font-size: 32px; }}
  .mp-slide__overlay {{
    background: linear-gradient(to bottom, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.65) 100%);
  }}
  .mp-slide__content {{ top: auto; bottom: 60px; transform: none; }}
  .mp-slide__content--center {{ top: auto; bottom: 60px; transform: translateX(-50%); }}
  .mp-nav {{ display: none; }}
}}
</style>

<script>
(function(){{
  var slides = document.querySelectorAll('#mpSlideshow .mp-slide');
  var dots   = document.querySelectorAll('#mpSlideshow .mp-dot');
  var current = 0;
  var timer;

  function show(n) {{
    slides[current].classList.remove('mp-slide--active');
    dots[current].classList.remove('mp-dot--active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('mp-slide--active');
    dots[current].classList.add('mp-dot--active');
  }}

  window.mpGoTo = function(n) {{ clearInterval(timer); show(n); startAuto(); }};

  function startAuto() {{
    timer = setInterval(function() {{ show(current + 1); }}, 25000);
  }}
  startAuto();
}})();
</script>
"""

# ── 2. Carrusel estilo Nike ──────────────────────────────────────────────────
CARRUSEL_LIQUID = """
{%- assign col = collections['piel-automotriz'] -%}
<div class="mpcar-wrap">
  <div class="mpcar-header">
    <h2 class="mpcar-title">Nuestras pieles más populares.</h2>
    <div class="mpcar-header-right">
      <a class="mpcar-viewall" href="{{ col.url }}">Ver todo</a>
      <button class="mpcar-arrow mpcar-arrow--prev" id="mpcarPrev">&#8249;</button>
      <button class="mpcar-arrow mpcar-arrow--next" id="mpcarNext">&#8250;</button>
    </div>
  </div>
  <div class="mpcar-viewport" id="mpcarViewport">
    <div class="mpcar-track" id="mpcarTrack">
      {%- for product in col.products limit: 8 -%}
      <div class="mpcar-card">
        <a href="{{ product.url }}" class="mpcar-img-link">
          {%- if product.featured_image -%}
            <img
              src="{{ product.featured_image | image_url: width: 600 }}"
              alt="{{ product.title | escape }}"
              class="mpcar-img"
              loading="lazy"
              width="600" height="600">
          {%- endif -%}
        </a>
        <div class="mpcar-info">
          <p class="mpcar-name">{{ product.title }}</p>
          <p class="mpcar-sub">Piel genuina Top Grain</p>
          <p class="mpcar-price">{{ product.price_min | money }}</p>
        </div>
      </div>
      {%- endfor -%}
    </div>
  </div>
</div>

<style>
.mpcar-wrap { padding: 48px 0; background: #fff; }
.mpcar-header {
  display: flex; align-items: flex-start; justify-content: space-between;
  padding: 0 40px 24px;
}
.mpcar-title { font-size: clamp(22px, 2.5vw, 32px); font-weight: 700; margin: 0; color: #111; }
.mpcar-header-right { display: flex; align-items: center; gap: 12px; flex-shrink: 0; }
.mpcar-viewall {
  font-size: 14px; font-weight: 600; color: #111; text-decoration: none;
  border-bottom: 1px solid #111; padding-bottom: 2px;
}
.mpcar-viewall:hover { opacity: 0.6; }
.mpcar-arrow {
  width: 40px; height: 40px; border-radius: 50%; border: 1px solid #ddd;
  background: #fff; cursor: pointer; font-size: 22px; display: flex;
  align-items: center; justify-content: center; transition: background 0.2s;
  color: #111;
}
.mpcar-arrow:hover { background: #f5f5f5; }
.mpcar-arrow:disabled { opacity: 0.3; cursor: default; }
.mpcar-viewport { overflow: hidden; padding: 0 40px; }
.mpcar-track {
  display: flex; gap: 16px;
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  will-change: transform;
}
.mpcar-card { flex: 0 0 calc(25% - 12px); min-width: 0; }
.mpcar-img-link { display: block; overflow: hidden; border-radius: 4px; aspect-ratio: 1/1; }
.mpcar-img {
  width: 100%; height: 100%; object-fit: cover;
  transition: transform 0.4s ease;
}
.mpcar-img-link:hover .mpcar-img { transform: scale(1.04); }
.mpcar-info { padding: 14px 2px 0; }
.mpcar-name { font-size: 16px; font-weight: 700; color: #111; margin: 0 0 3px; line-height: 1.3; }
.mpcar-sub { font-size: 14px; color: #757575; margin: 0; font-weight: 400; line-height: 1.4; }
.mpcar-price { font-size: 16px; color: #111; margin: 10px 0 0; font-weight: 700; }

@media (max-width: 749px) {
  .mpcar-header { padding: 0 16px 16px; flex-wrap: wrap; gap: 12px; }
  .mpcar-viewport { padding: 0 16px; }
  .mpcar-card { flex: 0 0 calc(50% - 8px); }
  .mpcar-arrow { display: none; }
}
</style>

<script>
(function() {
  var track    = document.getElementById('mpcarTrack');
  var viewport = document.getElementById('mpcarViewport');
  var prev     = document.getElementById('mpcarPrev');
  var next     = document.getElementById('mpcarNext');
  var cards    = track.querySelectorAll('.mpcar-card');
  var visible  = window.innerWidth <= 749 ? 2 : 4;
  var total    = cards.length;
  var cw = 0;
  var offsetPx = 0;  // posición actual en píxeles (libre, sin snap)
  var cardPos  = 0;  // solo para los botones

  function getCardW() { return cards[0].offsetWidth + 16; }
  function maxPx()    { return (total - visible) * cw; }

  function goToPx(px, animate) {
    px = Math.max(0, Math.min(px, maxPx()));
    offsetPx = px;
    track.style.transition = animate ? 'transform 0.35s ease-out' : 'none';
    track.style.transform  = 'translate3d(-' + px + 'px,0,0)';
    cardPos = Math.round(px / cw);
    prev.disabled = offsetPx <= 0;
    next.disabled = offsetPx >= maxPx();
  }

  // botones — snap a tarjeta
  prev.addEventListener('click', function() {
    cw = getCardW(); cardPos = Math.max(0, cardPos - 1); goToPx(cardPos * cw, true);
  });
  next.addEventListener('click', function() {
    cw = getCardW(); cardPos = Math.min(total - visible, cardPos + 1); goToPx(cardPos * cw, true);
  });

  // mouse drag — libre
  var dragging = false, startX = 0, startPx = 0, lastX = 0, lastT = 0, velX = 0, rafId;
  track.addEventListener('mousedown', function(e) {
    cw = getCardW(); dragging = true; startX = e.clientX; startPx = offsetPx;
    lastX = startX; lastT = Date.now(); velX = 0;
    track.style.transition = 'none'; track.style.cursor = 'grabbing';
    e.preventDefault();
  });
  window.addEventListener('mousemove', function(e) {
    if (!dragging) return;
    var now = Date.now(), dt = now - lastT || 1;
    velX = (lastX - e.clientX) / dt; lastX = e.clientX; lastT = now;
    cancelAnimationFrame(rafId);
    var dx = startX - e.clientX;
    rafId = requestAnimationFrame(function() {
      track.style.transform = 'translate3d(-' + Math.max(0, Math.min(startPx + dx, maxPx())) + 'px,0,0)';
    });
  });
  window.addEventListener('mouseup', function(e) {
    if (!dragging) return;
    cancelAnimationFrame(rafId); dragging = false; track.style.cursor = 'grab';
    var finalPx = Math.max(0, Math.min(startPx + (startX - e.clientX) + velX * 120, maxPx()));
    goToPx(finalPx, true);
  });

  // touch — libre, bloquea scroll vertical si swipe horizontal
  var tStartX = 0, tStartY = 0, tStartPx = 0, tLastX = 0, tLastT = 0, tVel = 0, tDir = null;
  track.addEventListener('touchstart', function(e) {
    cw = getCardW(); tStartX = e.touches[0].clientX; tStartY = e.touches[0].clientY;
    tLastX = tStartX; tLastT = Date.now(); tVel = 0; tStartPx = offsetPx; tDir = null;
    track.style.transition = 'none';
  }, { passive: true });
  track.addEventListener('touchmove', function(e) {
    var x = e.touches[0].clientX, y = e.touches[0].clientY;
    if (!tDir) {
      if (Math.abs(x-tStartX)>6||Math.abs(y-tStartY)>6) tDir=Math.abs(x-tStartX)>Math.abs(y-tStartY)?'h':'v';
      else return;
    }
    if (tDir==='v') return;
    e.preventDefault();
    var now=Date.now(), dt=now-tLastT||1; tVel=(tLastX-x)/dt; tLastX=x; tLastT=now;
    track.style.transform='translate3d(-'+Math.max(0,Math.min(tStartPx+(tStartX-x),maxPx()))+'px,0,0)';
  }, { passive: false });
  track.addEventListener('touchend', function(e) {
    if (tDir!=='h') return;
    var diff = tStartX - e.changedTouches[0].clientX;
    goToPx(tStartPx + diff + tVel * 120, true);
  }, { passive: true });

  // trackpad — libre
  var wTimer, wRaf, wBase = 0, wAccum = 0, wLocked = false;
  viewport.addEventListener('wheel', function(e) {
    if (Math.abs(e.deltaX) <= Math.abs(e.deltaY)) return;
    e.preventDefault();
    if (!wLocked) { cw = getCardW(); wBase = offsetPx; wAccum = 0; wLocked = true; }
    wAccum += e.deltaX;
    cancelAnimationFrame(wRaf);
    var a=wAccum, b=wBase, m=maxPx();
    wRaf = requestAnimationFrame(function() {
      track.style.transition='none';
      track.style.transform='translate3d(-'+Math.max(0,Math.min(b+a,m))+'px,0,0)';
    });
    clearTimeout(wTimer);
    wTimer = setTimeout(function() {
      goToPx(wBase + wAccum, true); wAccum = 0; wLocked = false;
    }, 80);
  }, { passive: false });

  window.addEventListener('resize', function() { cw = getCardW(); goToPx(offsetPx, false); });
  cw = getCardW(); goToPx(0, false);
})();
</script>
"""

# ── 3. Carrusel de reseñas ───────────────────────────────────────────────────
RESENAS_LIQUID = """
<div class="mpr-wrap">
  <div class="mpr-header">
    <h2 class="mpr-title">Lo que dicen nuestros clientes</h2>
    <div class="mpr-header-right">
      <button class="mpr-arrow mpr-arrow--prev" id="mprPrev">&#8249;</button>
      <button class="mpr-arrow mpr-arrow--next" id="mprNext">&#8250;</button>
    </div>
  </div>

  <div class="mpr-viewport" id="mprViewport">
    <div class="mpr-track" id="mprTrack">

      <!-- 5 estrellas -->
      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Tapicé los asientos de mi Corolla y quedaron increíbles. La piel es suave, resistente al calor y el color negro semi-liso se ve muy profesional."</p>
        <div class="mpr-footer"><span class="mpr-user">Carlos Mendoza</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Hice unas bolsas con el cuero café y mis clientas quedaron encantadas. Calidad de primera, se nota que es piel genuina desde que la abres."</p>
        <div class="mpr-footer"><span class="mpr-user">Ana Martínez</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Retapicé un sillón con el Top Grain Negro y se ve como recién salido de fábrica, mejor que el original. El envío llegó rápido y bien empacado."</p>
        <div class="mpr-footer"><span class="mpr-user">José Herrera</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <!-- 4 estrellas -->
      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"Muy buena piel, llegó rápido a Monterrey. El color gris oxford es exactamente como se ve en la foto. Le quito una estrella porque el empaque podría mejorar."</p>
        <div class="mpr-footer"><span class="mpr-user">Miguel Ramírez</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"Pedí medio cuero camel para probar y la calidad superó mis expectativas. Ya hice mi segundo pedido, ahora cuero entero. Excelente relación calidad-precio."</p>
        <div class="mpr-footer"><span class="mpr-user">Laura Gutiérrez</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <!-- más reseñas -->
      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Piel real, no sintético. Usé el vino chocolate para retapizar unas sillas de oficina y el resultado fue espectacular. Mis clientes no podían creer el precio."</p>
        <div class="mpr-footer"><span class="mpr-user">Liliana Rocha</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"El negro grabado italiano es una locura, se ve carísimo. Lo usé para tapizar las puertas de un auto y el cliente quedó más que satisfecho."</p>
        <div class="mpr-footer"><span class="mpr-user">Ricardo Torres</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"Usé el cuero vino para unas carteras y el acabado es muy profesional. La textura es consistente en toda la pieza. Volveré a pedir sin duda."</p>
        <div class="mpr-footer"><span class="mpr-user">Luis Vélez</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Retapicé 6 sillas de comedor con el color hueso y quedaron elegantísimas. Buen tamaño, buen grosor, muy limpia. Calidad de primera por el precio."</p>
        <div class="mpr-footer"><span class="mpr-user">Jimena Rojo</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"El negro semi-liso es exactamente lo que buscaba para mi pickup. Fácil de trabajar, no se estira de más y el acabado queda muy profesional."</p>
        <div class="mpr-footer"><span class="mpr-user">Héctor González</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="mpr-text">"Compré cuero conac para una chamarra y la textura es hermosa. Ya varios me preguntaron dónde lo conseguí. Sin duda el mejor proveedor de piel en línea."</p>
        <div class="mpr-footer"><span class="mpr-user">Arturo Navarro</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

      <div class="mpr-card">
        <div class="mpr-stars mpr-stars--4">&#9733;&#9733;&#9733;&#9733;<span class="mpr-star-empty">&#9733;</span></div>
        <p class="mpr-text">"Muy buena opción para marroquinería. Es piel real, se trabaja bien con la máquina de coser y el color camel no destiñe. Ya lo recomendé con mis colegas."</p>
        <div class="mpr-footer"><span class="mpr-user">Fernando Castillo</span><span class="mpr-badge">&#10003; Verificado</span></div>
      </div>

    </div>
  </div>
</div>

<style>
.mpr-wrap { padding: 60px 0; background: #f5f5f0; }
.mpr-header { display: flex; align-items: center; justify-content: space-between; padding: 0 40px 28px; }
.mpr-title { font-size: clamp(20px, 2.2vw, 28px); font-weight: 700; color: #111; margin: 0; }
.mpr-header-right { display: flex; gap: 10px; }
.mpr-arrow {
  width: 40px; height: 40px; border-radius: 50%; border: 1px solid #ccc;
  background: #fff; cursor: pointer; font-size: 22px;
  display: flex; align-items: center; justify-content: center;
  color: #111; transition: background 0.2s;
}
.mpr-arrow:hover { background: #eee; }
.mpr-arrow:disabled { opacity: 0.3; cursor: default; }
.mpr-viewport { overflow: hidden; padding: 0 40px; }
.mpr-track {
  display: flex; gap: 16px;
  will-change: transform;
  transition: transform 0.4s cubic-bezier(0.25,0.46,0.45,0.94);
}
.mpr-card {
  flex: 0 0 calc(33.333% - 11px);
  background: #fff; border-radius: 12px;
  padding: 28px 24px; box-sizing: border-box;
  display: flex; flex-direction: column; gap: 16px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.mpr-stars { color: #f5a623; font-size: 20px; letter-spacing: 2px; }
.mpr-stars--4 .mpr-star-empty { color: #ddd; }
.mpr-text { font-size: 14px; color: #333; line-height: 1.65; margin: 0; flex: 1; }
.mpr-footer { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.mpr-user { font-size: 13px; font-weight: 700; color: #111; }
.mpr-badge { font-size: 12px; color: #4a9d6f; font-weight: 500; }

@media (max-width: 749px) {
  .mpr-wrap { padding: 40px 0; }
  .mpr-header { padding: 0 16px 20px; }
  .mpr-viewport { padding: 0 16px; }
  .mpr-card { flex: 0 0 85%; }
}
</style>

<script>
(function() {
  var track    = document.getElementById('mprTrack');
  var viewport = document.getElementById('mprViewport');
  var prev     = document.getElementById('mprPrev');
  var next     = document.getElementById('mprNext');
  var cards    = track.querySelectorAll('.mpr-card');
  var total    = cards.length;
  var visible  = window.innerWidth <= 749 ? 1 : 3;
  var cw = 0, offsetPx = 0, cardPos = 0;
  function getCardW() { return cards[0].offsetWidth + 16; }
  function maxPx()    { return (total - visible) * cw; }

  function goToPx(px, animate) {
    px = Math.max(0, Math.min(px, maxPx()));
    offsetPx = px; cardPos = Math.round(px / cw);
    track.style.transition = animate ? 'transform 0.35s ease-out' : 'none';
    track.style.transform  = 'translate3d(-' + px + 'px,0,0)';
    prev.disabled = offsetPx <= 0;
    next.disabled = offsetPx >= maxPx();
  }

  prev.addEventListener('click', function() { cw=getCardW(); cardPos=Math.max(0,cardPos-1); goToPx(cardPos*cw,true); });
  next.addEventListener('click', function() { cw=getCardW(); cardPos=Math.min(total-visible,cardPos+1); goToPx(cardPos*cw,true); });

  var dragging=false, startX=0, startPx=0, lastX=0, lastT=0, velX=0, rafId;
  track.addEventListener('mousedown', function(e) {
    cw=getCardW(); dragging=true; startX=e.clientX; startPx=offsetPx;
    lastX=startX; lastT=Date.now(); velX=0;
    track.style.transition='none'; track.style.cursor='grabbing'; e.preventDefault();
  });
  window.addEventListener('mousemove', function(e) {
    if (!dragging) return;
    var now=Date.now(),dt=now-lastT||1; velX=(lastX-e.clientX)/dt; lastX=e.clientX; lastT=now;
    cancelAnimationFrame(rafId);
    var dx=startX-e.clientX;
    rafId=requestAnimationFrame(function(){ track.style.transform='translate3d(-'+Math.max(0,Math.min(startPx+dx,maxPx()))+'px,0,0)'; });
  });
  window.addEventListener('mouseup', function(e) {
    if (!dragging) return;
    cancelAnimationFrame(rafId); dragging=false; track.style.cursor='grab';
    goToPx(startPx+(startX-e.clientX)+velX*120, true);
  });

  var tStartX=0,tStartY=0,tStartPx=0,tLastX=0,tLastT=0,tVel=0,tDir=null;
  track.addEventListener('touchstart', function(e) {
    cw=getCardW(); tStartX=e.touches[0].clientX; tStartY=e.touches[0].clientY;
    tLastX=tStartX; tLastT=Date.now(); tVel=0; tStartPx=offsetPx; tDir=null;
    track.style.transition='none';
  }, { passive: true });
  track.addEventListener('touchmove', function(e) {
    var x=e.touches[0].clientX, y=e.touches[0].clientY;
    if (!tDir) { if(Math.abs(x-tStartX)>6||Math.abs(y-tStartY)>6) tDir=Math.abs(x-tStartX)>Math.abs(y-tStartY)?'h':'v'; else return; }
    if (tDir==='v') return;
    e.preventDefault();
    var now=Date.now(),dt=now-tLastT||1; tVel=(tLastX-x)/dt; tLastX=x; tLastT=now;
    track.style.transform='translate3d(-'+Math.max(0,Math.min(tStartPx+(tStartX-x),maxPx()))+'px,0,0)';
  }, { passive: false });
  track.addEventListener('touchend', function(e) {
    if (tDir!=='h') return;
    goToPx(tStartPx+(tStartX-e.changedTouches[0].clientX)+tVel*120, true);
  }, { passive: true });

  var wTimer,wRaf,wBase=0,wAccum=0,wLocked=false;
  viewport.addEventListener('wheel', function(e) {
    if (Math.abs(e.deltaX)<=Math.abs(e.deltaY)) return;
    e.preventDefault();
    if (!wLocked) { cw=getCardW(); wBase=offsetPx; wAccum=0; wLocked=true; }
    wAccum+=e.deltaX;
    cancelAnimationFrame(wRaf);
    var a=wAccum,b=wBase,m=maxPx();
    wRaf=requestAnimationFrame(function(){ track.style.transition='none'; track.style.transform='translate3d(-'+Math.max(0,Math.min(b+a,m))+'px,0,0)'; });
    clearTimeout(wTimer);
    wTimer=setTimeout(function(){ goToPx(wBase+wAccum,true); wAccum=0; wLocked=false; },80);
  }, { passive: false });

  window.addEventListener('resize', function() { cw=getCardW(); goToPx(offsetPx,false); });
  cw=getCardW(); goToPx(0,false);
  track.style.cursor='grab';
})();
</script>
"""

# ── 3b. Sección "De León para todo México" ───────────────────────────────────
NOSOTROS_LIQUID = """
<section class="mpn-wrap">
  <div class="mpn-inner">

    <div class="mpn-left">
      <p class="mpn-eyebrow">León, Guanajuato · Capital mundial de la piel</p>
      <h2 class="mpn-heading">El cuero que mueve a los mejores tapiceros de México.</h2>
      <p class="mpn-body">
        Somos Maxipiel, una empresa 100% mexicana ubicada en León, Guanajuato — la capital mundial de la piel.
        Nos especializamos en la venta de cuero genuino para tapiceros, diseñadores y artesanos que exigen lo mejor en sus proyectos.
      </p>
      <p class="mpn-body">
        Trabajamos directamente con las curtiembres de León para ofrecerte piel de la más alta calidad al mejor precio,
        sin intermediarios. Eso significa que cada metro de cuero que recibes pasó por un proceso de selección
        estricto antes de llegar a tus manos.
      </p>

      <div class="mpn-pillars">
        <div class="mpn-pillar">
          <span class="mpn-pillar__icon">&#9679;</span>
          <div>
            <strong>Tapicería Automotriz</strong>
            <p>Cuero grado automotriz resistente al calor, fricción y uso diario. Ideal para asientos, tableros, puertas y volantes.</p>
          </div>
        </div>
        <div class="mpn-pillar">
          <span class="mpn-pillar__icon">&#9679;</span>
          <div>
            <strong>Tapicería para Muebles</strong>
            <p>Sofás, sillas, cabeceras y sillones con el acabado que tus clientes esperan — duradero y fácil de mantener.</p>
          </div>
        </div>
        <div class="mpn-pillar">
          <span class="mpn-pillar__icon">&#9679;</span>
          <div>
            <strong>Marroquinería</strong>
            <p>Piel fina para bolsas, carteras, cintos y accesorios. Trabajamos con pieles de corte y acabado superior.</p>
          </div>
        </div>
        <div class="mpn-pillar">
          <span class="mpn-pillar__icon">&#9679;</span>
          <div>
            <strong>Envíos a todo México</strong>
            <p>Comprás hoy y tu pedido sale desde León hacia tu taller. Empaque seguro y seguimiento incluido.</p>
          </div>
        </div>
      </div>

      <a href="/collections/materia-prima" class="mpn-btn">Ver colección completa</a>
    </div>

    <div class="mpn-right">
      <div class="mpn-stat">
        <span class="mpn-stat__num">+30</span>
        <span class="mpn-stat__label">colores disponibles</span>
      </div>
      <div class="mpn-stat">
        <span class="mpn-stat__num">Piel<br>Premium</span>
        <span class="mpn-stat__label">calidad automotriz certificada</span>
      </div>
      <div class="mpn-stat">
        <span class="mpn-stat__num">4-6</span>
        <span class="mpn-stat__label">días hábiles de entrega</span>
      </div>
      <div class="mpn-stat">
        <span class="mpn-stat__num">León</span>
        <span class="mpn-stat__label">capital mundial de la piel</span>
      </div>
    </div>

  </div>
</section>

<style>
.mpn-wrap {
  background: #201504;
  padding: 80px 0;
}
.mpn-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  gap: 80px;
  align-items: center;
}
.mpn-left {
  flex: 1;
  min-width: 0;
}
.mpn-eyebrow {
  font-size: 11px;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: #a08060;
  margin: 0 0 16px;
}
.mpn-heading {
  font-size: clamp(26px, 3.5vw, 44px);
  font-weight: 800;
  color: #ffffff;
  line-height: 1.15;
  margin: 0 0 20px;
}
.mpn-body {
  font-size: 16px;
  line-height: 1.7;
  color: #b0b0b0;
  margin: 0 0 32px;
}
.mpn-btn {
  display: inline-block;
  background: #a08060;
  color: #fff;
  padding: 14px 30px;
  border-radius: 3px;
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 1px;
  text-decoration: none;
  text-transform: uppercase;
  transition: background 0.2s;
}
.mpn-btn:hover { background: #8a6a4a; }
.mpn-pillars {
  display: flex;
  flex-direction: column;
  gap: 18px;
  margin: 0 0 36px;
}
.mpn-pillar {
  display: flex;
  gap: 14px;
  align-items: flex-start;
}
.mpn-pillar__icon {
  color: #a08060;
  font-size: 8px;
  margin-top: 6px;
  flex-shrink: 0;
}
.mpn-pillar strong {
  display: block;
  color: #ffffff;
  font-size: 14px;
  font-weight: 700;
  margin-bottom: 4px;
}
.mpn-pillar p {
  color: #888;
  font-size: 13px;
  line-height: 1.6;
  margin: 0;
}
.mpn-right {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px;
  flex-shrink: 0;
  width: 380px;
}
.mpn-stat {
  background: #3a2510;
  padding: 28px 24px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.mpn-stat__num {
  font-size: 36px;
  font-weight: 800;
  color: #ffffff;
  line-height: 1;
}
.mpn-stat__label {
  font-size: 12px;
  color: #888;
  line-height: 1.4;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
@media (max-width: 749px) {
  .mpn-inner {
    flex-direction: column;
    gap: 48px;
    padding: 0 20px;
  }
  .mpn-right {
    width: 100%;
  }
  .mpn-wrap { padding: 56px 0; }
}
</style>
"""

# ── 4. Nuevo index.json del homepage ─────────────────────────────────────────
nuevo_homepage = {
  "sections": {

    "hero_slideshow": {
      "type": "custom-liquid",
      "settings": {
        "custom_liquid": HERO_LIQUID,
        "color_scheme": "scheme-1",
        "padding_top": 0,
        "padding_bottom": 0
      }
    },

    "featured_collection_carousel": {
      "type": "custom-liquid",
      "settings": {
        "custom_liquid": CARRUSEL_LIQUID,
        "color_scheme": "scheme-1",
        "padding_top": 0,
        "padding_bottom": 0
      }
    },

    "collection_categories": {
      "type": "collection-list",
      "blocks": {
        "cat_automotriz": {
          "type": "featured_collection",
          "settings": { "collection": "piel-automotriz" }
        },
        "cat_muebles": {
          "type": "featured_collection",
          "settings": { "collection": "piel-para-muebles" }
        },
        "cat_marroquineria": {
          "type": "featured_collection",
          "settings": { "collection": "piel-para-marroquineria" }
        },
        "cat_accesorios": {
          "type": "featured_collection",
          "settings": { "collection": "accesorios" }
        },
        "cat_muestrarios": {
          "type": "featured_collection",
          "settings": { "collection": "muestrarios" }
        }
      },
      "block_order": ["cat_automotriz", "cat_muebles", "cat_marroquineria", "cat_accesorios", "cat_muestrarios"],
      "settings": {
        "title": "Explora nuestra piel",
        "heading_size": "h2",
        "image_ratio": "square",
        "columns_desktop": 5,
        "color_scheme": "scheme-4",
        "show_view_all": False,
        "columns_mobile": "2",
        "swipe_on_mobile": False,
        "padding_top": 48,
        "padding_bottom": 48
      }
    },

    "divider_marcas": {
      "type": "rich-text",
      "blocks": {
        "heading_marcas": {
          "type": "heading",
          "settings": {
            "heading": "Marcas que confían en Maxipiel",
            "heading_size": "h2"
          }
        }
      },
      "block_order": ["heading_marcas"],
      "settings": {
        "desktop_content_position": "center",
        "content_alignment": "center",
        "color_scheme": "scheme-2",
        "full_width": True,
        "padding_top": 36,
        "padding_bottom": 0
      }
    },

    "logos_marcas": {
      "type": "multicolumn",
      "blocks": {
        "logo1": { "type": "column", "settings": { "image": "shopify://shop_images/D_NQ_NP_829365-MLA74845230692_032024-F_1.jpg", "title": "", "text": "", "link_label": "", "link": "" } },
        "logo2": { "type": "column", "settings": { "image": "shopify://shop_images/logoyuyin_copia.jpg", "title": "", "text": "", "link_label": "", "link": "" } },
        "logo3": { "type": "column", "settings": { "image": "shopify://shop_images/Caterpillar-logo-PNG.png", "title": "", "text": "", "link_label": "", "link": "" } },
        "logo4": { "type": "column", "settings": { "image": "shopify://shop_images/928_flexi.webp", "title": "", "text": "", "link_label": "", "link": "" } },
        "logo5": { "type": "column", "settings": { "image": "shopify://shop_images/prima_logo.jpg", "title": "", "text": "", "link_label": "", "link": "" } },
        "logo6": { "type": "column", "settings": { "image": "shopify://shop_images/reclutan-para-bader-ab46efad390e12ff64050d7914b2cbdb.jpg", "title": "", "text": "", "link_label": "", "link": "" } }
      },
      "block_order": ["logo1","logo2","logo3","logo4","logo5","logo6"],
      "settings": {
        "title": "",
        "heading_size": "h2",
        "image_width": "full",
        "image_ratio": "adapt",
        "button_label": "",
        "button_link": "",
        "columns_desktop": 6,
        "column_alignment": "center",
        "background_style": "none",
        "color_scheme": "scheme-2",
        "columns_mobile": "2",
        "swipe_on_mobile": True,
        "padding_top": 12,
        "padding_bottom": 36
      }
    },

    "banner_mayoreo": {
      "type": "rich-text",
      "blocks": {
        "texto_mayoreo": {
          "type": "text",
          "settings": {
            "text": "<p><strong>Venta al Mayoreo · Los mejores precios · Expertos en la industria de la piel</strong></p>"
          }
        }
      },
      "block_order": ["texto_mayoreo"],
      "settings": {
        "desktop_content_position": "center",
        "content_alignment": "center",
        "color_scheme": "scheme-3",
        "full_width": True,
        "padding_top": 4,
        "padding_bottom": 4
      }
    },

    "nosotros": {
      "type": "custom-liquid",
      "settings": {
        "custom_liquid": NOSOTROS_LIQUID,
        "color_scheme": "scheme-1",
        "padding_top": 0,
        "padding_bottom": 0
      }
    },

    "resenas": {
      "type": "custom-liquid",
      "settings": {
        "custom_liquid": RESENAS_LIQUID,
        "color_scheme": "scheme-2",
        "padding_top": 0,
        "padding_bottom": 0
      }
    }

  },
  "order": [
    "hero_slideshow",
    "featured_collection_carousel",
    "collection_categories",
    "divider_marcas",
    "logos_marcas",
    "banner_mayoreo",
    "nosotros",
    "resenas"
  ]
}

# ── 3. Subir a Shopify ────────────────────────────────────────────────────────
payload = json.dumps({
    'asset': {
        'key': 'templates/index.json',
        'value': json.dumps(nuevo_homepage, ensure_ascii=False)
    }
}).encode('utf-8')

url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json'
req = urllib.request.Request(url, data=payload, method='PUT')
req.add_header('X-Shopify-Access-Token', TOKEN)
req.add_header('Content-Type', 'application/json')

with urllib.request.urlopen(req) as r:
    resp = json.load(r)
    key = resp.get('asset', {}).get('key', '')
    print(f'Homepage actualizado: {key}')
    print('Listo — revisa https://www.maxipiel.com')
