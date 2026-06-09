# -*- coding: utf-8 -*-
"""
Crea un producto "Cuero Top Grain" por color en Shopify (draft).
Sube la imagen desde output_v5/<color>.jpg
"""
import sys, json, base64, urllib.request, urllib.error
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

TOKEN  = "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"
DOMAIN = "maxipiel.myshopify.com"

# Mapeo filename -> nombre legible del color
COLORES = {
    "azulaqua40":            "Azul Aqua",
    "cafe2":                 "Cafe",
    "cafeoxford20":          "Cafe Oxford",
    "camel6":                "Camel",
    "chedronarena":          "Chedron Arena",
    "chedronterracota10":    "Chedron Terracota",
    "conac20":               "Conac",
    "gris":                  "Gris",
    "grisoxford92":          "Gris Oxford",
    "hueso1":                "Hueso",
    "king_ranch":            "King Ranch",
    "miel30":                "Miel",
    "negro72semiliso":       "Negro Semi-liso",
    "negrofondoazul7":       "Negro Fondo Azul",
    "negrofondogris12":      "Negro Fondo Gris",
    "negrograbadoitaliano10":"Negro Grabado Italiano",
    "plateadoobscuro80":     "Plateado Obscuro",
    "rojoferrari":           "Rojo Ferrari",
    "rojoquemado":           "Rojo Quemado",
    "uva11":                 "Uva",
    "vino":                  "Vino",
    "vinochocolate16":       "Vino Chocolate",
}

DESCRIPCION = """<p>Nuestra piel de grado automotriz ofrece la combinación perfecta entre elegancia y durabilidad extrema. Desarrollada originalmente para cumplir con las rigurosas exigencias de los principales fabricantes de automóviles de lujo.</p>
<ul>
  <li>Piel Top Grain de alta durabilidad</li>
  <li>Ideal para tapicería automotriz y de muebles</li>
  <li>Entregamos en León, Guanajuato</li>
  <li>Envíos a todo México</li>
</ul>"""

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

def crear_producto_color(stem: str, imagen_path: Path):
    nombre_color = COLORES.get(stem, stem.replace("_", " ").title())
    titulo = f"Cuero Top Grain {nombre_color}"
    print(f"Creando: {titulo}...")

    # 1. Crear producto
    producto = api("POST", "products.json", {
        "product": {
            "title": titulo,
            "body_html": DESCRIPCION,
            "vendor": "maxipiel",
            "product_type": "Cuero",
            "tags": f"top grain, {nombre_color.lower()}, piel, tapiceria, automotriz",
            "status": "draft",
            "options": [{"name": "Tamano"}],
            "variants": [
                {"option1": "Medio Cuero",  "price": "1200.00", "inventory_management": "shopify", "inventory_quantity": 100},
                {"option1": "Cuero Entero", "price": "2000.00", "inventory_management": "shopify", "inventory_quantity": 100},
            ]
        }
    })
    product_id = producto["product"]["id"]
    print(f"  Producto creado - ID: {product_id}")

    # 2. Subir imagen en base64
    img_b64 = base64.b64encode(imagen_path.read_bytes()).decode("utf-8")
    img_resp = api("POST", f"products/{product_id}/images.json", {
        "image": {
            "attachment": img_b64,
            "filename": imagen_path.name,
            "alt": f"Cuero Top Grain {nombre_color}"
        }
    })
    print(f"  Imagen subida - ID: {img_resp['image']['id']}")
    print(f"  URL: https://maxipiel.com.mx/products/{producto['product']['handle']}")
    return product_id

if __name__ == "__main__":
    output_v5 = Path("output_v5")

    # PRUEBA: solo negro72semiliso
    stem = "negro72semiliso"
    imagen = output_v5 / f"{stem}.jpg"

    if not imagen.exists():
        print(f"No se encontro: {imagen}")
    else:
        crear_producto_color(stem, imagen)
        print("\nPrueba completada. Revisalo en Shopify como draft.")
