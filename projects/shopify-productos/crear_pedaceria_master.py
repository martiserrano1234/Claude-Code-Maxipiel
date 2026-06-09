import urllib.request, json, base64, time, sys
from pathlib import Path

TOKEN = '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'
SHOP = 'maxipiel.myshopify.com'
IMG_DIR = Path('C:/Users/danie/Downloads')

DISCLAIMER = '<p style="font-size:11px;color:#888;margin-top:20px;">* Los tonos del producto pueden presentar ligeras variaciones con respecto a las imágenes mostradas, debido a diferencias en la calibración de pantallas y al proceso natural del curtido de la piel.</p>'

DESCRIPCION = """<div style="font-family: sans-serif; max-width: 700px; color: #2d2d2d;">

<h2 style="color: #1a1a1a;">Pedacera De Piel Genuina — Elige Color, Peso y Tamaño de Pieza</h2>

<p>Paquetes de piel vacuna genuina para artesanía, tapicería, marroquinería y moda. Selecciona el color, el peso total y el tamaño de los pedazos que necesitas para tu proyecto.</p>

<h3>Tamaños de pieza disponibles</h3>
<ul>
  <li><strong>~15×15 cm ($20/kg)</strong> — Pedazos pequeños, ideales para accesorios, pulseras, monederos, escapularios y proyectos de detalle.</li>
  <li><strong>~40×40 cm ($50/kg)</strong> — Pedazos medianos, para carteras, bolsas pequeñas, fundas y proyectos de tamaño medio.</li>
  <li><strong>~80×80 cm ($80/kg)</strong> — Pedazos grandes, para tapicería, bolsas grandes, cinturones y proyectos que requieren superficies amplias.</li>
</ul>

<h3>Pesos disponibles</h3>
<ul>
  <li>5 Kg | 10 Kg | 20 Kg | 50 Kg</li>
</ul>

<h3>Características del material</h3>
<ul>
  <li>Piel vacuna 100% genuina y natural</li>
  <li>Grosor promedio: 1.2 a 1.8 mm (promedio 1.5 mm)</li>
  <li>Flexible, resistente y fácil de trabajar</li>
  <li>Puede presentar marcas o cicatrices naturales del animal — señal de autenticidad</li>
  <li>Envío nacional desde León, Guanajuato</li>
</ul>

<p style="background:#f5f5f5;padding:12px;border-radius:6px;margin-top:16px;">
  <strong>¿Tienes dudas sobre la cantidad o el color?</strong><br>
  Escríbenos por WhatsApp y te ayudamos a elegir lo que necesitas para tu proyecto.<br>
  <a href="https://wa.me/524791424121?text=Hola%20Maxipiel%2C%20me%20interesa%20la%20pedacera%20de%20piel%2C%20%C2%BFpueden%20ayudarme%3F" style="display:inline-block;margin-top:8px;background:#25D366;color:white;padding:10px 18px;border-radius:5px;text-decoration:none;font-weight:bold;">Escríbenos por WhatsApp</a><br>
  <small>Lunes a Sábado de 9am a 6pm</small>
</p>

""" + DISCLAIMER + "</div>"

# Color → sufijo de archivo de imagen
COLORES = [
    ('Café',          'Cafe'),
    ('Rojo Ladrillo', 'Ladrillo'),
    ('Miel',          'Miel'),
    ('Chocolate',     'Chocolate'),
    ('Gris',          'Gris'),
    ('Beige',         'Beige'),
    ('Camel',         'Camel'),
    ('Mixto',         'Mixto'),
]

PESOS = [5, 10, 20, 50]

# Precio por kg por tamaño de pieza
TAMANOS = [
    ('~15×15 cm',  20),
    ('~40×40 cm',  50),
    ('~80×80 cm',  80),
]

def img_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def api(url, data=None, method='GET'):
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)

# ── 1. Construir variantes ────────────────────────────────────────────────────
variantes = []
for color, _ in COLORES:
    for peso in PESOS:
        for tamano_label, precio_kg in TAMANOS:
            precio_total = peso * precio_kg
            variantes.append({
                'option1': color,
                'option2': f'{peso} Kg',
                'option3': tamano_label,
                'price': str(float(precio_total)),
                'taxable': True,
                'fulfillment_service': 'manual',
                'requires_shipping': True,
                'inventory_management': None,
            })

sys.stdout.buffer.write(f"Total variantes: {len(variantes)}\n".encode('utf-8'))

# ── 2. Construir imágenes ─────────────────────────────────────────────────────
imagenes = []
pos = 1
for color, sufijo in COLORES:
    if sufijo == 'Mixto':
        archivos = [f'Pedacera{sufijo}.png']
    else:
        archivos = [f'Rollo{sufijo}.png', f'Pedacera{sufijo}.png', f'PedaceraMonto{sufijo}.png']

    for archivo in archivos:
        path = IMG_DIR / archivo
        if path.exists():
            imagenes.append({
                'attachment': img_b64(path),
                'filename': archivo,
                'alt': f'Pedacera de piel genuina color {color} — Maxipiel León Guanajuato',
                'position': pos,
            })
            pos += 1
        else:
            sys.stdout.buffer.write(f"AVISO: no existe {archivo}\n".encode('utf-8'))

sys.stdout.buffer.write(f"Total imágenes: {len(imagenes)}\n".encode('utf-8'))

# ── 3. Crear el producto ──────────────────────────────────────────────────────
payload = json.dumps({'product': {
    'title': 'Pedacera De Piel Genuina — Elige Color, Peso y Tamaño',
    'body_html': DESCRIPCION,
    'vendor': 'Maxipiel',
    'product_type': 'Pedacería',
    'tags': 'pedaceria, piel genuina, artesania, tapiceria, marroquineria, Categorías_Marroquinería, Categorías_Calzado',
    'options': [
        {'name': 'Color',             'values': [c for c, _ in COLORES]},
        {'name': 'Peso',              'values': [f'{p} Kg' for p in PESOS]},
        {'name': 'Tamaño de pieza',   'values': [t for t, _ in TAMANOS]},
    ],
    'variants': variantes,
    'status': 'active',
}}, ensure_ascii=False).encode('utf-8')

sys.stdout.buffer.write(b"Creando producto maestro (sin imagenes)...\n")
resp = api(f'https://{SHOP}/admin/api/2024-01/products.json', data=payload, method='POST')
product = resp['product']
product_id = product['id']
sys.stdout.buffer.write(f"Producto creado: {product['title']} (ID: {product_id})\n".encode('utf-8'))

# ── 4. Subir imágenes una por una ────────────────────────────────────────────
sys.stdout.buffer.write(b"\nSubiendo imagenes...\n")
color_img_map = {}  # color → image_id (primera imagen de ese color)

for img_data in imagenes:
    img_payload = json.dumps({'image': {
        'attachment': img_data['attachment'],
        'filename':   img_data['filename'],
        'alt':        img_data['alt'],
        'position':   img_data['position'],
    }}, ensure_ascii=False).encode('utf-8')
    try:
        img_resp = api(f'https://{SHOP}/admin/api/2024-01/products/{product_id}/images.json', data=img_payload, method='POST')
        created_img = img_resp['image']
        filename_lower = img_data['filename'].lower()
        # Mapear color → primera imagen subida de ese color
        for color, sufijo in COLORES:
            if sufijo.lower() in filename_lower and color not in color_img_map:
                color_img_map[color] = created_img['id']
                break
        sys.stdout.buffer.write(f"  IMG OK: {img_data['filename']}\n".encode('utf-8'))
    except Exception as e:
        sys.stdout.buffer.write(f"  IMG ERROR {img_data['filename']}: {e}\n".encode('utf-8'))
    time.sleep(0.5)

sys.stdout.buffer.write(f"Mapa color→imagen: {list(color_img_map.keys())}\n".encode('utf-8'))

# ── 5. Asignar imagen por color a cada variante ───────────────────────────────
sys.stdout.buffer.write(b"\nAsignando imagenes por color a variantes...\n")

# Actualizar cada variante con su image_id
for variant in product['variants']:
    color = variant['option1']
    img_id = color_img_map.get(color)
    if img_id:
        payload_v = json.dumps({'variant': {'id': variant['id'], 'image_id': img_id}}).encode('utf-8')
        try:
            api(f'https://{SHOP}/admin/api/2024-01/variants/{variant["id"]}.json', data=payload_v, method='PUT')
        except Exception as e:
            sys.stdout.buffer.write(f"  ERROR variante {variant['id']}: {e}\n".encode('utf-8'))
        time.sleep(0.15)

sys.stdout.buffer.write(b"\nListo. Producto maestro de pedaceria creado con exito.\n")
sys.stdout.buffer.write(f"URL admin: https://{SHOP}/admin/products/{product_id}\n".encode('utf-8'))
