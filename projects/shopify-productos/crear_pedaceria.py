import urllib.request, json, base64, time, sys
from pathlib import Path

TOKEN = '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'
SHOP = 'maxipiel.myshopify.com'
IMG_DIR = Path('C:/Users/danie/Downloads')
PRECIO = '800.00'

DISCLAIMER = '<p style="font-size:11px;color:#888;margin-top:20px;">* Los tonos del producto pueden presentar ligeras variaciones con respecto a las imágenes mostradas, debido a diferencias en la calibración de pantallas y al proceso natural del curtido de la piel.</p>'

DESC_BASE = """<div style="font-family: sans-serif; max-width: 700px; color: #2d2d2d;">

<h2 style="color: #1a1a1a;">Pedacera De Piel Genuina 5 Kg — Color {color}</h2>

<p>Paquetes de 5 Kg de Piel Vacuna para Artesanía y Tapicería en Color {color}.</p>

<p>¿Buscas piel de calidad para tus proyectos de artesanía, tapicería, marroquinería o moda? Te ofrecemos paquetes de 5 kg de piel vacuna genuina, flexible, resistente y delgada, ideal para crear carteras, monederos, pulseras, escapularios y mucho más.</p>

<p>Cada paquete contiene 5 kg del color que selecciones al hacer tu compra. El grueso promedio de la piel es de 1.2 a 1.8 mm, con un promedio de 1.5 mm.</p>

<p>Los paquetes contienen pedazos de piel de diferentes tamaños, desde 30 x 30 cm hasta 60 x 60 cm. Los ejemplos de los tamaños se muestran en las fotos. Todos los paquetes tienen un promedio similar de pedazos grandes, para que aproveches al máximo tu compra.</p>

<p>La piel que ofrecemos es 100% auténtica y natural, por lo que puede presentar algunas marcas o cicatrices propias del animal. Estas marcas son sellos de la autenticidad y la legitimidad del cuero, y le dan un toque único y original a tus creaciones.</p>

<p>Manejamos todo tipo de piel, diferentes colores, en pedacera, rollos, etc. Si tienes alguna duda o consulta, no dudes en preguntar.</p>

<p style="background:#f5f5f5;padding:12px;border-radius:6px;margin-top:16px;">
  <strong>¿Tienes dudas sobre la cantidad o el color?</strong><br>
  Escríbenos por WhatsApp y te ayudamos.<br>
  <a href="https://wa.me/524791424121?text=Hola%20Maxipiel%2C%20me%20interesa%20la%20pedacera%20de%20piel%20{color_encoded}%2C%20%C2%BFpueden%20ayudarme%3F" style="display:inline-block;margin-top:8px;background:#25D366;color:white;padding:10px 18px;border-radius:5px;text-decoration:none;font-weight:bold;">Escríbenos por WhatsApp</a><br>
  <small>Lunes a Sábado de 9am a 6pm</small>
</p>

{disclaimer}
</div>"""

DESC_MIXTO = """<div style="font-family: sans-serif; max-width: 700px; color: #2d2d2d;">

<h2 style="color: #1a1a1a;">Pedacera De Piel Genuina 5 Kg — Mixto (2 Tonos a Elegir)</h2>

<p>Paquetes de 5 Kg de Piel Vacuna para Artesanía y Tapicería en combinación de dos colores a tu elección.</p>

<p>¿Buscas variedad para tus proyectos? El paquete Mixto incluye pedacería en dos tonos de piel genuina que tú eliges al hacer tu compra. Ideal para proyectos que requieren combinación de colores o para tapiceros que quieren probar distintos tonos.</p>

<p>Cada paquete contiene 5 kg distribuidos entre los dos colores seleccionados. El grueso promedio de la piel es de 1.2 a 1.8 mm, con un promedio de 1.5 mm.</p>

<p>Los paquetes contienen pedazos de piel de diferentes tamaños, desde 30 x 30 cm hasta 60 x 60 cm. Todos los paquetes tienen un promedio similar de pedazos grandes, para que aproveches al máximo tu compra.</p>

<p>La piel que ofrecemos es 100% auténtica y natural, por lo que puede presentar algunas marcas o cicatrices propias del animal. Estas marcas son sellos de la autenticidad y la legitimidad del cuero.</p>

<p><strong>Importante:</strong> Al realizar tu compra, indícanos en los comentarios del pedido los dos tonos que deseas. Manejamos colores como: negro, café, gris, miel, chocolate, camel, beige, rojo ladrillo y más.</p>

<p style="background:#f5f5f5;padding:12px;border-radius:6px;margin-top:16px;">
  <strong>¿Quieres combinar colores específicos?</strong><br>
  Escríbenos por WhatsApp y te ayudamos a armar tu paquete.<br>
  <a href="https://wa.me/524791424121?text=Hola%20Maxipiel%2C%20me%20interesa%20la%20pedacera%20mixta%2C%20%C2%BFpueden%20ayudarme%3F" style="display:inline-block;margin-top:8px;background:#25D366;color:white;padding:10px 18px;border-radius:5px;text-decoration:none;font-weight:bold;">Escríbenos por WhatsApp</a><br>
  <small>Lunes a Sábado de 9am a 6pm</small>
</p>

{disclaimer}
</div>"""

def img_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def create_product(payload):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        f'https://{SHOP}/admin/api/2024-01/products.json',
        data=data, method='POST'
    )
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)['product']

# Color → (nombre_display, sufijo_archivo, color_encoded_wa)
colores = [
    ('Café',               'Cafe',     'Caf%C3%A9'),
    ('Rojo Ladrillo',      'Ladrillo', 'Rojo%20Ladrillo'),
    ('Miel',               'Miel',     'Miel'),
    ('Chocolate',          'Chocolate','Chocolate'),
    ('Gris',               'Gris',     'Gris'),
    ('Beige',              'Beige',    'Beige'),
    ('Camel',              'Camel',    'Camel'),
]

errores = []

for nombre, sufijo, wa_enc in colores:
    print(f"\nCreando: Pedacera {nombre}...")

    img1 = IMG_DIR / f'Rollo{sufijo}.png'
    img2 = IMG_DIR / f'Pedacera{sufijo}.png'
    img3 = IMG_DIR / f'PedaceraMonto{sufijo}.png'

    imagenes = []
    for i, img_path in enumerate([img1, img2, img3], 1):
        if img_path.exists():
            imagenes.append({
                'attachment': img_b64(img_path),
                'filename': img_path.name,
                'alt': f'Pedacera de piel genuina 5kg color {nombre} — Maxipiel León Guanajuato',
                'position': i
            })
        else:
            print(f"  AVISO: no existe {img_path.name}")

    import urllib.parse
    desc = DESC_BASE.format(
        color=nombre,
        color_encoded=urllib.parse.quote(nombre),
        disclaimer=DISCLAIMER
    )

    payload = {
        'product': {
            'title': f'Pedacera De Piel Genuina 5 Kg Color {nombre}',
            'body_html': desc,
            'vendor': 'Maxipiel',
            'product_type': 'Pedacería',
            'tags': 'pedaceria, piel genuina, artesania, tapiceria, marroquineria',
            'variants': [{
                'option1': '5 Kg',
                'price': PRECIO,
                'inventory_management': None,
                'fulfillment_service': 'manual',
                'requires_shipping': True,
            }],
            'options': [{'name': 'Tamaño', 'values': ['5 Kg']}],
            'images': imagenes,
            'status': 'active',
        }
    }

    try:
        prod = create_product(payload)
        sys.stdout.buffer.write(f"  OK: {prod['title']} (ID: {prod['id']})\n".encode('utf-8'))
        time.sleep(1)
    except Exception as e:
        sys.stdout.buffer.write(f"  ERROR: {e}\n".encode('utf-8'))
        errores.append(nombre)

# Producto Mixto
print("\nCreando: Pedacera Mixto...")
img_mixto = IMG_DIR / 'PedaceraMixto.png'
imagenes_mixto = []
if img_mixto.exists():
    imagenes_mixto.append({
        'attachment': img_b64(img_mixto),
        'filename': 'PedaceraMixto.png',
        'alt': 'Pedacera de piel genuina 5kg mixto dos tonos — Maxipiel León Guanajuato',
        'position': 1
    })

payload_mixto = {
    'product': {
        'title': 'Pedacera De Piel Genuina 5 Kg Mixto (2 Tonos a Elegir)',
        'body_html': DESC_MIXTO.format(disclaimer=DISCLAIMER),
        'vendor': 'Maxipiel',
        'product_type': 'Pedacería',
        'tags': 'pedaceria, piel genuina, artesania, tapiceria, marroquineria, mixto',
        'variants': [{
            'option1': '5 Kg',
            'price': PRECIO,
            'inventory_management': None,
            'fulfillment_service': 'manual',
            'requires_shipping': True,
        }],
        'options': [{'name': 'Tamaño', 'values': ['5 Kg']}],
        'images': imagenes_mixto,
        'status': 'active',
    }
}

try:
    prod = create_product(payload_mixto)
    sys.stdout.buffer.write(f"  OK: {prod['title']} (ID: {prod['id']})\n".encode('utf-8'))
except Exception as e:
    sys.stdout.buffer.write(f"  ERROR: {e}\n".encode('utf-8'))
    errores.append('Mixto')

print(f"\n{'='*40}")
print(f"Completado. Errores: {len(errores)}")
if errores:
    print(f"Con error: {errores}")
else:
    print("Todos los productos creados correctamente.")
