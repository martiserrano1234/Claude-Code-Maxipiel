# -*- coding: utf-8 -*-
"""
Duplica Cuero Top Grain Oxblood para los 22 colores.
Sube 3 imagenes por producto: output/, output_v2/, output_v4/
Status: draft
"""
import sys, json, base64, urllib.request, urllib.error, time
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

TOKEN  = "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"
DOMAIN = "maxipiel.myshopify.com"

BODY_HTML = """<p>Nuestra piel de grado automotriz ofrece la combinación perfecta entre elegancia y durabilidad extrema. Desarrollada originalmente para cumplir con las rigurosas exigencias de los principales fabricantes de equipo original (OEM), esta piel destaca por su consistencia de grano y una resistencia superior al desgaste, los rayos UV y las manchas. Es un material de alta gama, con un tacto firme pero flexible, ideal para quienes buscan la calidad táctica y visual que solo se encuentra en los interiores de vehículos de prestigio.</p>"""

# filename stem -> nombre legible
COLORES = {
    "azulaqua40":             "Azul Aqua",
    "cafe2":                  "Cafe",
    "cafeoxford20":           "Cafe Oxford",
    "camel6":                 "Camel",
    "chedronarena":           "Chedron Arena",
    "chedronterracota10":     "Chedron Terracota",
    "conac20":                "Conac",
    "gris":                   "Gris",
    "grisoxford92":           "Gris Oxford",
    "hueso1":                 "Hueso",
    "king_ranch":             "King Ranch",
    "miel30":                 "Miel",
    "negro72semiliso":        "Negro Semi-liso",
    "negrofondoazul7":        "Negro Fondo Azul",
    "negrofondogris12":       "Negro Fondo Gris",
    "negrograbadoitaliano10": "Negro Grabado Italiano",
    "plateadoobscuro80":      "Plateado Obscuro",
    "rojoferrari":            "Rojo Ferrari",
    "rojoquemado":            "Rojo Quemado",
    "uva11":                  "Uva",
    "vino":                   "Vino",
    "vinochocolate16":        "Vino Chocolate",
}

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
        msg = e.read().decode("utf-8")
        print(f"  Error HTTP {e.code}: {msg}")
        raise

def buscar_imagen(carpeta: str, stem: str) -> Path | None:
    """Busca la imagen en la carpeta, manejando nombres con caracteres especiales."""
    base = Path(carpeta)
    # intento directo
    p = base / f"{stem}.jpg"
    if p.exists():
        return p
    # buscar ignorando caracteres especiales (ej: conac20 == coñac20)
    stem_ascii = stem.encode("ascii", "ignore").decode()
    for f in base.glob("*.jpg"):
        if f.stem.encode("ascii", "ignore").decode() == stem_ascii:
            return f
    return None

def crear_producto(stem: str, nombre_color: str) -> bool:
    titulo = f"Cuero Top Grain {nombre_color}"
    print(f"\n[{stem}] Creando: {titulo}")

    # 1. Crear producto sin imagenes
    resp = api("POST", "products.json", {
        "product": {
            "title": titulo,
            "body_html": BODY_HTML,
            "vendor": "maxipiel",
            "product_type": "Cuero",
            "tags": "std",
            "status": "draft",
            "options": [{"name": "Tamano"}],
            "variants": [
                {"option1": "Medio Cuero",  "price": "1200.00",
                 "inventory_management": "shopify", "inventory_quantity": 100},
                {"option1": "Cuero Entero", "price": "2000.00",
                 "inventory_management": "shopify", "inventory_quantity": 100},
            ]
        }
    })
    product_id = resp["product"]["id"]
    print(f"  Producto ID: {product_id}")

    # 2. Subir 3 imagenes
    subidas = 0
    for pos, carpeta in enumerate(CARPETAS, 1):
        img_path = buscar_imagen(carpeta, stem)
        if not img_path:
            print(f"  [{pos}/3] No encontrada en {carpeta}/ — saltando")
            continue
        img_b64 = base64.b64encode(img_path.read_bytes()).decode("utf-8")
        img_resp = api("POST", f"products/{product_id}/images.json", {
            "image": {
                "attachment": img_b64,
                "filename": f"{stem}_v{pos}.jpg",
                "alt": f"Cuero Top Grain {nombre_color}",
                "position": pos
            }
        })
        print(f"  [{pos}/3] Imagen subida desde {carpeta}/ - ID: {img_resp['image']['id']}")
        subidas += 1
        time.sleep(0.3)  # pequeña pausa para no saturar la API

    print(f"  Listo: {subidas}/3 imagenes subidas")
    return True

# Ejecutar
base_dir = Path(".")
ok, errores = 0, []

for stem, nombre in COLORES.items():
    try:
        crear_producto(stem, nombre)
        ok += 1
        time.sleep(0.5)
    except Exception as e:
        print(f"  [X] Error en {stem}: {e}")
        errores.append(stem)

print(f"\n{'='*45}")
print(f"Creados: {ok}/{len(COLORES)}")
if errores:
    print(f"Con errores: {errores}")
