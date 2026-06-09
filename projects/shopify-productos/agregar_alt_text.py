import urllib.request, json, time

TOKEN = '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'
SHOP = 'maxipiel.myshopify.com'

def get(url):
    req = urllib.request.Request(url)
    req.add_header('X-Shopify-Access-Token', TOKEN)
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def put(url, payload):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='PUT')
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def make_alt(title, position):
    # Limpiar título para alt text
    t = title.strip()
    # Si es Cuero Top Grain, formato específico
    if 'Top Grain' in t or 'top grain' in t.lower():
        color = t.replace('Cuero Top Grain', '').replace('cuero top grain', '').strip()
        alt = f"Cuero Top Grain {color} para tapicería — Maxipiel León Guanajuato"
    elif 'Muestrario' in t or 'muestrario' in t.lower():
        alt = f"{t} — Colores de piel genuina Maxipiel León Guanajuato"
    else:
        alt = f"{t} — Piel genuina Maxipiel León Guanajuato"
    # Máximo 125 caracteres
    return alt[:125]

# Obtener todos los productos (paginado)
all_products = []
url = f'https://{SHOP}/admin/api/2024-01/products.json?limit=250&fields=id,title,images'
while url:
    resp = get(url)
    all_products.extend(resp['products'])
    # Shopify paginación via Link header — simplificado: si hay exactamente 250, hay más
    if len(resp['products']) < 250:
        break
    # Obtener last ID para next page
    last_id = resp['products'][-1]['id']
    url = f'https://{SHOP}/admin/api/2024-01/products.json?limit=250&fields=id,title,images&since_id={last_id}'

print(f"Total productos: {len(all_products)}")

actualizadas = 0
errores = []

for p in all_products:
    pid = p['id']
    title = p['title']
    imgs_sin_alt = [img for img in p['images'] if not img.get('alt')]

    if not imgs_sin_alt:
        continue

    for img in imgs_sin_alt:
        alt = make_alt(title, img.get('position', 1))
        img_url = f'https://{SHOP}/admin/api/2024-01/products/{pid}/images/{img["id"]}.json'
        try:
            put(img_url, {'image': {'id': img['id'], 'alt': alt}})
            actualizadas += 1
        except Exception as e:
            errores.append((pid, img['id'], str(e)))
        time.sleep(0.3)

    print(f"OK: {title} ({len(imgs_sin_alt)} imágenes)")

print(f"\nImágenes actualizadas: {actualizadas}")
print(f"Errores: {len(errores)}")
if errores:
    for e in errores:
        print(f"  ERROR pid={e[0]} img={e[1]}: {e[2]}")
