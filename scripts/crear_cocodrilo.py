import sys, json, base64, time, os, requests
sys.stdout.reconfigure(encoding='utf-8')

TOKEN = "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"
STORE = "maxipiel.myshopify.com"
API = f"https://{STORE}/admin/api/2024-01"
H = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}
IMGS = "C:/Users/danie/Downloads"

COLORS = ["Negro", "Rojo", "Cafe", "Hueso", "Gris"]
SIZES  = ["Medio Cuero", "Cuero Entero"]
PRECIO_MEDIO  = "1375.00"
PRECIO_ENTERO = "2750.00"

# Mapeo de color → archivos (encontrados en la carpeta)
IMG_FILES = {
    "Negro": ["cocodrilograbadanegra.png",   "cocodrilograbadonegrohoja.png"],
    "Rojo":  ["cocodrilograbadarojo.png",    "cocodrilograbadorojohoja.png"],
    "Cafe":  ["cocodrilograbadacafe.png",    "cocodrilograbadocafehoja.png"],
    "Hueso": ["cocodrilograbadahueso.png",   "cocodrilograbadohuesohoja.png"],
    "Gris":  ["cocodrilograbadogris.png",    "cocodrilograbadogrishoja.png"],
}

def api(method, path, body=None):
    r = requests.request(method, f"{API}/{path}", headers=H, json=body, timeout=120)
    if r.status_code >= 400:
        print(f"  ERROR {r.status_code}: {r.text[:300]}")
        return None
    return r.json()

def b64(fname):
    with open(os.path.join(IMGS, fname), "rb") as f:
        return base64.b64encode(f.read()).decode()

# ── 1. Crear producto ──────────────────────────────────────────────────────────
print("Creando producto...")
desc = """<h2>Piel Grabada de Cocodrilo — Textura Premium para Tapicería</h2>
<p>Cuero con grabado de cocodrilo de alta definición. Textura firme, acabado elegante y resistente al uso diario. Disponible en <strong>5 colores</strong>: Negro, Rojo, Café, Hueso y Gris.</p>
<p>Selecciona el color y el tamaño que necesitas directamente en la página.</p>
<ul>
  <li><strong>Medio Cuero (media hoja)</strong> — aprox. 250 dm². Ideal para un asiento, una silla o proyectos chicos.</li>
  <li><strong>Cuero Entero (hoja completa)</strong> — aprox. 500 dm². Para sofás, sillones o proyectos grandes.</li>
</ul>"""

product_data = {
    "product": {
        "title": "Piel Grabada de Cocodrilo",
        "body_html": desc,
        "product_type": "Piel",
        "tags": "cocodrilo, grabado, piel, tapicería, hot sale",
        "options": [
            {"name": "Tamaño",  "values": SIZES},
            {"name": "Color",   "values": COLORS},
        ],
        "variants": [
            {
                "option1": size,
                "option2": color,
                "price": PRECIO_MEDIO if size == "Medio Cuero" else PRECIO_ENTERO,
                "inventory_management": None,
                "fulfillment_service": "manual",
                "requires_shipping": True,
                "taxable": True,
            }
            for size in SIZES
            for color in COLORS
        ],
        "status": "active",
    }
}

r = api("POST", "products.json", product_data)
if not r:
    sys.exit("No se pudo crear el producto")

prod = r["product"]
pid = prod["id"]
print(f"  Producto creado: ID {pid} | {prod['title']}")

# Mapear variantes por (size, color)
variant_map = {}  # (size, color) → variant_id
for v in prod["variants"]:
    variant_map[(v["option1"], v["option2"])] = v["id"]
    print(f"  Variante: {v['option1']} / {v['option2']} → ID:{v['id']} | ${v['price']}")

# ── 2. Subir imágenes y asociar ────────────────────────────────────────────────
print("\nSubiendo imágenes...")
for color in COLORS:
    files = IMG_FILES[color]
    # IDs de variantes de este color (ambos tamaños)
    color_variant_ids = [variant_map[(s, color)] for s in SIZES if (s, color) in variant_map]
    print(f"\n  {color}: variantes {color_variant_ids}")

    for fname in files:
        fpath = os.path.join(IMGS, fname)
        if not os.path.exists(fpath):
            print(f"    ✗ No encontrado: {fname}")
            continue

        for attempt in range(3):
            r = api("POST", f"products/{pid}/images.json", {
                "image": {
                    "attachment": b64(fname),
                    "filename": fname,
                    "variant_ids": color_variant_ids,
                }
            })
            if r and "image" in r:
                img = r["image"]
                print(f"    ✓ {fname} → img ID:{img['id']} | variantes:{img['variant_ids']}")
                break
            print(f"    Reintentando ({attempt+1}/3)...")
            time.sleep(2)
        time.sleep(1.5)

print(f"\nLISTO — Producto ID: {pid}")
print(f"URL admin: https://{STORE}/admin/products/{pid}")
