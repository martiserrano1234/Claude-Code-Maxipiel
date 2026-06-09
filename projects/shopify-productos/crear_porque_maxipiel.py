import urllib.request, json, sys

TOKEN = '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'
SHOP = 'maxipiel.myshopify.com'

CONTENT = """<div style="font-family: sans-serif; max-width: 860px; margin: 0 auto; color: #2d2d2d; padding: 20px;">

<h1 style="color: #1a1a1a; font-size: 2em; margin-bottom: 8px;">¿Por qué Maxipiel?</h1>
<p style="color: #888; font-size: 1.1em; margin-top: 0;">La respuesta honesta a la pregunta que todo tapicero se hace antes de cambiar de proveedor.</p>

<hr style="border: none; border-top: 2px solid #e8ddd0; margin: 28px 0;">

<h2 style="color: #1a1a1a;">Maxipiel vs tu proveedor local</h2>
<table style="width:100%; border-collapse: collapse; margin-top: 16px; font-size: 0.95em;">
  <thead>
    <tr style="background: #f9f6f2;">
      <th style="padding: 12px 16px; text-align: left; border-bottom: 2px solid #e8ddd0;">Factor</th>
      <th style="padding: 12px 16px; text-align: center; border-bottom: 2px solid #e8ddd0; color: #8B5E3C;">Maxipiel</th>
      <th style="padding: 12px 16px; text-align: center; border-bottom: 2px solid #e8ddd0;">Distribuidor local</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #f0ece6;">
      <td style="padding: 12px 16px;">Origen de la piel</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>Directo de curtiembre en León</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Revendedor con markup</td>
    </tr>
    <tr style="background: #fafafa; border-bottom: 1px solid #f0ece6;">
      <td style="padding: 12px 16px;">Precios</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>Visibles y fijos en catálogo</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Cotización manual, variable</td>
    </tr>
    <tr style="border-bottom: 1px solid #f0ece6;">
      <td style="padding: 12px 16px;">Variedad de colores</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>Más de 30 colores en stock</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Inventario limitado</td>
    </tr>
    <tr style="background: #fafafa; border-bottom: 1px solid #f0ece6;">
      <td style="padding: 12px 16px;">Cobertura</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>Todo México con seguimiento</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Solo local o zona limitada</td>
    </tr>
    <tr style="border-bottom: 1px solid #f0ece6;">
      <td style="padding: 12px 16px;">Muestrario</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>Disponible para compra</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Rara vez disponible</td>
    </tr>
    <tr style="background: #fafafa;">
      <td style="padding: 12px 16px;">Compra online</td>
      <td style="padding: 12px 16px; text-align: center; color: #8B5E3C;"><strong>24/7 desde cualquier dispositivo</strong></td>
      <td style="padding: 12px 16px; text-align: center;">Solo en persona o por teléfono</td>
    </tr>
  </tbody>
</table>

<hr style="border: none; border-top: 2px solid #e8ddd0; margin: 40px 0;">

<h2 style="color: #1a1a1a;">Lo que dicen tapiceros que nos eligieron</h2>

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-top: 20px;">
  <div style="background: #f9f6f2; border-radius: 8px; padding: 20px; border-left: 3px solid #8B5E3C;">
    <p style="font-style: italic; margin: 0 0 12px; font-size: 0.95em;">"Tapicé los asientos de un Corolla y quedaron increíbles. La piel es suave, resistente y el color llegó exacto al de la foto."</p>
    <strong style="font-size: 0.85em; color: #888;">Carlos M. — Tapicero automotriz · León, Gto.</strong>
  </div>
  <div style="background: #f9f6f2; border-radius: 8px; padding: 20px; border-left: 3px solid #8B5E3C;">
    <p style="font-style: italic; margin: 0 0 12px; font-size: 0.95em;">"Pedí el negro semi-liso para tapizar un Mustang y quedó espectacular. Ya hice mi segundo pedido y no compro en otro lado."</p>
    <strong style="font-size: 0.85em; color: #888;">Roberto S. — Tapicero · Guadalajara, Jal.</strong>
  </div>
  <div style="background: #f9f6f2; border-radius: 8px; padding: 20px; border-left: 3px solid #8B5E3C;">
    <p style="font-style: italic; margin: 0 0 12px; font-size: 0.95em;">"Compré el Camel para tapizar una sala completa. Llegó uniforme en color y textura, sin defectos. Muy superior a lo que conseguía localmente."</p>
    <strong style="font-size: 0.85em; color: #888;">Héctor V. — Tapicero de muebles · Tijuana, B.C.</strong>
  </div>
</div>

<hr style="border: none; border-top: 2px solid #e8ddd0; margin: 40px 0;">

<h2 style="color: #1a1a1a;">Empresas que confían en nuestra piel</h2>
<p>Marcas como <strong>Caterpillar, Flexi y Prima</strong> han usado piel de Maxipiel en sus proyectos. Si exigen calidad industrial, nosotros la entregamos.</p>

<hr style="border: none; border-top: 2px solid #e8ddd0; margin: 40px 0;">

<h2 style="color: #1a1a1a;">¿Listo para hacer tu primer pedido?</h2>
<p>Explora nuestro catálogo completo o pide un muestrario para ver los colores en físico antes de decidir.</p>

<div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 16px;">
  <a href="/collections" style="display:inline-block; background:#1a1a1a; color:white; padding:12px 28px; border-radius:6px; text-decoration:none; font-weight:bold;">Ver catálogo completo</a>
  <a href="/collections/muestrarios" style="display:inline-block; background:transparent; color:#8B5E3C; padding:12px 28px; border-radius:6px; text-decoration:none; font-weight:bold; border: 2px solid #8B5E3C;">Pedir muestrario</a>
</div>

<p style="margin-top: 24px; color: #888; font-size: 0.9em;">¿Tienes dudas? Escríbenos a <a href="mailto:contact@maxipiel.store" style="color:#8B5E3C;">contact@maxipiel.store</a> o por WhatsApp al <a href="https://wa.me/524791424121" style="color:#8B5E3C;">477 209 4121</a>.</p>

</div>"""

payload = json.dumps({'page': {
    'title': '¿Por qué Maxipiel?',
    'handle': 'por-que-maxipiel',
    'body_html': CONTENT,
    'published': True
}}, ensure_ascii=False).encode('utf-8')

req = urllib.request.Request(f'https://{SHOP}/admin/api/2024-01/pages.json', data=payload, method='POST')
req.add_header('X-Shopify-Access-Token', TOKEN)
req.add_header('Content-Type', 'application/json; charset=utf-8')
with urllib.request.urlopen(req) as r:
    p = json.load(r)['page']

sys.stdout.buffer.write(f'OK: {p["title"]}\n'.encode('utf-8'))
sys.stdout.buffer.write(f'URL: https://www.maxipiel.com/pages/{p["handle"]}\n'.encode('utf-8'))
