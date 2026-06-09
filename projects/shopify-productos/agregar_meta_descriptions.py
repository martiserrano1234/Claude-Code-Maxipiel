import urllib.request, json

TOKEN = 'TU_SHOPIFY_TOKEN'
SHOP = 'maxipiel.myshopify.com'

def put(url, payload):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='PUT')
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def get(url):
    req = urllib.request.Request(url)
    req.add_header('X-Shopify-Access-Token', TOKEN)
    with urllib.request.urlopen(req) as r:
        return json.load(r)

# --- Collections con sus meta descriptions ---
# handle -> (title, meta_description)
colecciones = [
    ('piel-automotriz',      'Piel genuina Top Grain para tapicería automotriz. Asientos, puertas, tableros y volantes. Resistente al calor y uso diario. Envíos desde León a todo México en 4-6 días hábiles.'),
    ('piel-para-muebles',    'Cuero genuino para tapicería de muebles: sofás, sillas, cabeceras y sillones. Fácil de limpiar, durable y elegante. Compra por metro desde León, Guanajuato. Envío nacional.'),
    ('piel-para-marroquineria', 'Piel genuina para marroquinería: bolsas, carteras, cinturones y accesorios. Alta flexibilidad y acabado fino. Directo de curtiembres de León, Guanajuato. Envíos a todo México.'),
    ('muestrarios',          'Muestrarios de piel genuina Maxipiel. Conoce los colores y texturas antes de comprar al mayoreo. Ideal para tapiceros que trabajan con clientes. Envío desde León, Guanajuato.'),
    ('accesorios',           'Accesorios y complementos para tapicería en piel genuina. Hilo, pegamento, herrajes y más. Todo lo que necesitas para tu taller en un solo lugar. Envíos a todo México.'),
]

# Obtener todas las smart y custom collections
print("Obteniendo colecciones...")
smart = get(f'https://{SHOP}/admin/api/2024-01/smart_collections.json?limit=250')['smart_collections']
custom = get(f'https://{SHOP}/admin/api/2024-01/custom_collections.json?limit=250')['custom_collections']

handle_map = {}
for c in smart:
    handle_map[c['handle']] = ('smart', c['id'])
for c in custom:
    handle_map[c['handle']] = ('custom', c['id'])

for handle, meta_desc in colecciones:
    if handle not in handle_map:
        print(f"NO ENCONTRADA: {handle}")
        continue
    tipo, cid = handle_map[handle]
    key = 'smart_collection' if tipo == 'smart' else 'custom_collection'
    url = f'https://{SHOP}/admin/api/2024-01/{tipo}_collections/{cid}.json'
    payload = {key: {'id': cid, 'metafields_global_description_tag': meta_desc}}
    try:
        put(url, payload)
        print(f"OK: {handle}")
    except Exception as e:
        print(f"ERROR {handle}: {e}")

# --- Homepage meta description via theme settings ---
# Shopify no expone homepage SEO vía REST directamente; usamos el asset settings_data.json
print("\nActualizando meta description de homepage via theme settings...")
THEME_ID = '144344481892'

asset_url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]=config/settings_data.json'
req = urllib.request.Request(asset_url)
req.add_header('X-Shopify-Access-Token', TOKEN)
with urllib.request.urlopen(req) as r:
    asset_data = json.load(r)

settings_json = json.loads(asset_data['asset']['value'])

# El campo seo está en current -> sections -> (no existe así) — en realidad está en current root
# Shopify usa: settings_data.json > current > seo_meta_description (solo algunos temas)
# Si no existe, lo creamos
current = settings_json.get('current', {})
homepage_desc = 'Cuero genuino para tapiceros en León, Guanajuato. Piel automotriz, para muebles y marroquinería. Directo de curtiembres, sin intermediarios. Envíos a todo México en 4-6 días hábiles.'

if 'seo_meta_description' in current:
    current['seo_meta_description'] = homepage_desc
    settings_json['current'] = current
    # Guardar
    put_url = f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json'
    payload = {'asset': {'key': 'config/settings_data.json', 'value': json.dumps(settings_json, ensure_ascii=False, indent=2)}}
    try:
        put(put_url, payload)
        print("OK: homepage seo_meta_description en settings_data.json")
    except Exception as e:
        print(f"ERROR settings_data: {e}")
else:
    print("NOTA: El tema no tiene seo_meta_description en settings_data.json.")
    print("      La meta description de homepage hay que configurarla manualmente en:")
    print("      Shopify Admin > Online Store > Preferences > Homepage meta description")
    print(f"      Texto a pegar: {homepage_desc}")

print("\nListo.")
