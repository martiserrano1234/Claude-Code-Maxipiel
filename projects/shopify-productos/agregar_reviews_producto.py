import urllib.request, json

TOKEN = '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'
SHOP = 'maxipiel.myshopify.com'
THEME_ID = '144344481892'

def get_asset(key):
    req = urllib.request.Request(
        f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]={key}'
    )
    req.add_header('X-Shopify-Access-Token', TOKEN)
    with urllib.request.urlopen(req) as r:
        return json.load(r)['asset']['value']

def put_asset(key, value):
    payload = json.dumps({'asset': {'key': key, 'value': value}}).encode('utf-8')
    req = urllib.request.Request(
        f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload, method='PUT'
    )
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)


# ── SNIPPET: snippets/resenas-producto.liquid ─────────────────────────────────
REVIEWS_SNIPPET = """
<section class="rp-section">
  <div class="rp-inner">
    <h2 class="rp-title">Lo que dicen nuestros clientes</h2>

    <div class="rp-track-wrap" id="rpWrap">
      <div class="rp-track" id="rpTrack">

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Llevo años comprando piel aquí y nunca me ha fallado. La calidad es consistente y los colores son exactos a lo que se ve en fotos. Mis clientes siempre quedan contentos."</p>
          <p class="rp-author">— Carlos M., tapicero automotriz · León, Gto.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Pedí el negro semi-liso para tapizar un Mustang y quedó espectacular. La piel es suave, resistente y muy fácil de trabajar. Ya hice mi segundo pedido."</p>
          <p class="rp-author">— Roberto S., tapicero · Guadalajara, Jal.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"El envío llegó en 5 días a CDMX, bien empacado y en perfectas condiciones. La piel King Ranch es exactamente lo que buscaba para un proyecto western que tenía pendiente."</p>
          <p class="rp-author">— Miguel A., tapicero · Ciudad de México</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Compré el muestrario primero para ver los colores y fue la mejor decisión. Ya elegí el Vino Chocolate para los sillones de un restaurante y quedaron increíbles."</p>
          <p class="rp-author">— Ana L., diseñadora de interiores · Monterrey, N.L.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"El precio es muy competitivo para la calidad que ofrecen. Busqué mucho antes de decidirme y Maxipiel ganó por calidad, variedad de colores y tiempo de entrega."</p>
          <p class="rp-author">— Javier R., taller de tapicería · Querétaro, Qro.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Llevo 3 compras y cada vez el servicio mejora. Lo que más valoro es que cuando tuve una duda sobre el grosor de la piel, me respondieron rápido por WhatsApp y me ayudaron a elegir bien."</p>
          <p class="rp-author">— Fernando T., tapicero automotriz · Puebla, Pue.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Pedí el Camel para tapizar una sala completa. La piel llegó uniforme en color y textura, sin defectos. Muy superior a lo que conseguía localmente. Ya no compro en otro lado."</p>
          <p class="rp-author">— Héctor V., tapicero de muebles · Tijuana, B.C.</p>
        </div>

        <div class="rp-card">
          <div class="rp-stars">★★★★★</div>
          <p class="rp-text">"Excelente material. Usé el Gris Oxford para un proyecto de oficina y el cliente quedó tan contento que me recomendó con otros clientes. Gracias Maxipiel."</p>
          <p class="rp-author">— Luis E., tapicero · San Luis Potosí, S.L.P.</p>
        </div>

      </div>
    </div>

    <div class="rp-btns">
      <button class="rp-btn" id="rpPrev" aria-label="Anterior">&#8592;</button>
      <button class="rp-btn" id="rpNext" aria-label="Siguiente">&#8594;</button>
    </div>
  </div>
</section>

<style>
.rp-section {
  background: #faf8f5;
  padding: 56px 20px;
  overflow: hidden;
}
.rp-inner {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}
.rp-title {
  font-size: clamp(20px, 3vw, 28px);
  font-weight: 700;
  color: #201504;
  margin: 0 0 32px;
  text-align: center;
  letter-spacing: 0.3px;
}
.rp-track-wrap {
  overflow: hidden;
  cursor: grab;
  user-select: none;
}
.rp-track-wrap:active { cursor: grabbing; }
.rp-track {
  display: flex;
  gap: 20px;
  will-change: transform;
}
.rp-card {
  flex: 0 0 320px;
  background: #fff;
  border-radius: 8px;
  padding: 28px 24px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  border: 1px solid #ece9e3;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.rp-stars {
  color: #c9943a;
  font-size: 18px;
  letter-spacing: 2px;
}
.rp-text {
  font-size: 14px;
  line-height: 1.7;
  color: #3d3d3d;
  margin: 0;
  flex: 1;
  font-style: italic;
}
.rp-author {
  font-size: 12px;
  color: #888;
  margin: 0;
  font-weight: 600;
}
.rp-btns {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: 28px;
}
.rp-btn {
  width: 42px; height: 42px;
  border-radius: 50%;
  border: 1px solid #c9943a;
  background: transparent;
  color: #c9943a;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex; align-items: center; justify-content: center;
}
.rp-btn:hover { background: #c9943a; color: #fff; }
@media (max-width: 768px) {
  .rp-card { flex: 0 0 280px; }
}
</style>

<script>
(function(){
  const wrap = document.getElementById('rpWrap');
  const track = document.getElementById('rpTrack');
  if (!wrap || !track) return;

  const CW = () => track.children[0] ? track.children[0].getBoundingClientRect().width + 20 : 340;
  let offsetPx = 0, cardPos = 0, isDragging = false, startX = 0, startOff = 0, velX = 0, lastX = 0, rafId = null, tDir = null;

  function maxOff() { return Math.max(0, track.scrollWidth - wrap.clientWidth); }
  function clamp(v) { return Math.min(maxOff(), Math.max(0, v)); }

  function goToPx(px, animate) {
    offsetPx = clamp(px);
    track.style.transition = animate ? 'transform 0.35s ease' : 'none';
    track.style.transform = 'translate3d(-' + offsetPx + 'px,0,0)';
  }

  document.getElementById('rpPrev').onclick = function() {
    cardPos = Math.max(0, cardPos - 1);
    goToPx(cardPos * CW(), true);
  };
  document.getElementById('rpNext').onclick = function() {
    cardPos = Math.min(track.children.length - 1, cardPos + 1);
    goToPx(cardPos * CW(), true);
  };

  // Mouse drag
  wrap.addEventListener('mousedown', function(e) {
    isDragging = true; startX = e.clientX; startOff = offsetPx; velX = 0; lastX = e.clientX;
    cancelAnimationFrame(rafId);
  });
  document.addEventListener('mousemove', function(e) {
    if (!isDragging) return;
    velX = e.clientX - lastX; lastX = e.clientX;
    rafId = requestAnimationFrame(function() { goToPx(startOff - (e.clientX - startX), false); });
  });
  document.addEventListener('mouseup', function() {
    if (!isDragging) return;
    isDragging = false;
    goToPx(offsetPx - velX * 120, true);
  });

  // Touch
  wrap.addEventListener('touchstart', function(e) {
    startX = e.touches[0].clientX; startOff = offsetPx; velX = 0; lastX = startX; tDir = null;
  }, { passive: true });
  wrap.addEventListener('touchmove', function(e) {
    const dx = e.touches[0].clientX - startX;
    const dy = e.touches[0].clientY - (e.touches[0].clientY || 0);
    if (!tDir) tDir = Math.abs(dx) > Math.abs(dy) ? 'h' : 'v';
    if (tDir === 'h') { e.preventDefault(); velX = e.touches[0].clientX - lastX; lastX = e.touches[0].clientX; goToPx(startOff - dx, false); }
  }, { passive: false });
  wrap.addEventListener('touchend', function() {
    goToPx(offsetPx - velX * 120, true);
  });

  // Trackpad
  let wDebounce;
  wrap.addEventListener('wheel', function(e) {
    if (Math.abs(e.deltaX) < Math.abs(e.deltaY)) return;
    e.preventDefault();
    goToPx(offsetPx + e.deltaX, false);
    clearTimeout(wDebounce);
    wDebounce = setTimeout(function() { goToPx(offsetPx, true); }, 80);
  }, { passive: false });
})();
</script>
"""

# ── Subir snippet ─────────────────────────────────────────────────────────────
print("Subiendo snippets/resenas-producto.liquid...")
put_asset('snippets/resenas-producto.liquid', REVIEWS_SNIPPET)
print("OK")

# ── Agregar sección al product.json ──────────────────────────────────────────
print("Modificando templates/product.json...")
raw = get_asset('templates/product.json')
tmpl = json.loads(raw)

if 'resenas-producto' in tmpl['sections']:
    print("Ya existe — no se modifica.")
else:
    # Agregar nueva sección tipo custom_liquid que renderiza el snippet
    tmpl['sections']['resenas-producto'] = {
        "type": "custom-liquid",
        "settings": {
            "custom_liquid": "{% render 'resenas-producto' %}"
        }
    }
    # Insertar en el order entre main y related-products
    order = tmpl['order']
    if 'related-products' in order:
        idx = order.index('related-products')
        order.insert(idx, 'resenas-producto')
    else:
        order.append('resenas-producto')

    put_asset('templates/product.json', json.dumps(tmpl, ensure_ascii=False, indent=2))
    print("OK — sección de reseñas agregada antes de 'Productos relacionados'")

print("\nListo. Verifica en cualquier página de producto de maxipiel.com")
