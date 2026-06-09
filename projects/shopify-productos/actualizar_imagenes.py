# -*- coding: utf-8 -*-
import sys, json, base64, urllib.request, urllib.error
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

TOKEN  = "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"
DOMAIN = "maxipiel.myshopify.com"
PRODUCT_ID = 8504429805668
STEM = "negro72semiliso"
COLOR_NOMBRE = "Negro Semi-liso"

CARPETAS = ["output", "output_v2", "output_v4"]

def api(method, path, data=None):
    url = f"https://{DOMAIN}/admin/api/2024-01/{path}"
    body = json.dumps(data, ensure_ascii=False).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("X-Shopify-Access-Token", TOKEN)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error HTTP:", e.code, e.read().decode("utf-8"))
        raise

# 1. Borrar imagen existente
print("Borrando imagen existente...")
imgs = api("GET", f"products/{PRODUCT_ID}/images.json")["images"]
for img in imgs:
    api("DELETE", f"products/{PRODUCT_ID}/images/{img['id']}.json")
    print(f"  Borrada ID: {img['id']}")

# 2. Subir las 3 imagenes en orden
base = Path(".")
for i, carpeta in enumerate(CARPETAS, 1):
    # manejar nombre con tilde (conac/conac20)
    imagen = base / carpeta / f"{STEM}.jpg"
    if not imagen.exists():
        # intentar con ñ en el nombre
        for f in (base / carpeta).glob("*.jpg"):
            if f.stem.encode("ascii", "ignore").decode() == STEM:
                imagen = f
                break

    if not imagen.exists():
        print(f"  [!] No encontrada: {carpeta}/{STEM}.jpg — saltando")
        continue

    img_b64 = base64.b64encode(imagen.read_bytes()).decode("utf-8")
    resp = api("POST", f"products/{PRODUCT_ID}/images.json", {
        "image": {
            "attachment": img_b64,
            "filename": f"{STEM}_v{i}.jpg",
            "alt": f"Cuero Top Grain {COLOR_NOMBRE} - vista {i}",
            "position": i
        }
    })
    print(f"  [{i}/3] Subida desde {carpeta}/ - Image ID: {resp['image']['id']}")

print("\nListo. Revisa el producto en Shopify.")
