import sys, json, base64, time, os
import requests
sys.stdout.reconfigure(encoding='utf-8')

TOKEN = "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"
STORE = "maxipiel.myshopify.com"
API = f"https://{STORE}/admin/api/2024-01"
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}
IMAGES_DIR = "C:/Users/danie/Downloads"

PRODUCTS = [
    # Cafe: variantes ya creadas, solo falta subir imágenes
    {"id": 8504430788708, "color": "cafe",  "img_color": "cafe",  "only_images": True,
     "perforada_variant_ids": [48473740968036, 48473741000804],
     "lisa_variant_ids": [48218214269028, 48218214301796]},
    {"id": 8504431542372, "color": "rojo",  "img_color": "rojo",  "only_images": False},
    {"id": 8504431050852, "color": "gris",  "img_color": "gris",  "only_images": False},
    {"id": 8504431149156, "color": "hueso", "img_color": "hueso", "only_images": False},
    {"id": 8504431312996, "color": "negro", "img_color": "negro", "only_images": False},
]

PRECIO_PERFORADA_MEDIO  = "1625.00"
PRECIO_PERFORADA_ENTERO = "3250.00"

def api(method, path, body=None):
    url = f"{API}/{path}"
    try:
        r = requests.request(method, url, headers=HEADERS, json=body, timeout=120)
        if r.status_code >= 400:
            print(f"  ERROR {r.status_code}: {r.text[:300]}")
            return None
        return r.json()
    except Exception as e:
        print(f"  EXCEPTION: {e}")
        return None

def load_image_b64(filename):
    path = os.path.join(IMAGES_DIR, filename)
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def upload_image(pid, fname, ic, variant_ids, retries=3):
    fpath = os.path.join(IMAGES_DIR, fname)
    if not os.path.exists(fpath):
        print(f"    No encontrado: {fname}")
        return None
    b64 = load_image_b64(fname)
    for attempt in range(retries):
        r = api("POST", f"products/{pid}/images.json", {
            "image": {"attachment": b64, "filename": fname, "variant_ids": variant_ids}
        })
        if r and "image" in r:
            return r["image"]["id"]
        print(f"    Reintentando ({attempt+1}/{retries})...")
        time.sleep(2)
    return None

for prod in PRODUCTS:
    pid = prod["id"]
    color = prod["color"]
    ic = prod["img_color"]
    only_images = prod.get("only_images", False)
    print(f"\n{'='*60}")
    print(f"Procesando: {color.upper()} (ID: {pid}){' [solo imágenes]' if only_images else ''}")

    if only_images:
        perforada_variant_ids = prod["perforada_variant_ids"]
        lisa_variant_ids = prod["lisa_variant_ids"]
        # Asociar imágenes existentes con lisa
        p2 = api("GET", f"products/{pid}.json?fields=images")
        existing_image_ids = [img["id"] for img in p2["product"]["images"]] if p2 else []
        print(f"  Asociando {len(existing_image_ids)} imágenes existentes con Piel Lisa...")
        for img_id in existing_image_ids:
            r = api("PUT", f"products/{pid}/images/{img_id}.json", {
                "image": {"id": img_id, "variant_ids": lisa_variant_ids}
            })
            if r: print(f"    Imagen {img_id} → Lisa OK")
            time.sleep(0.3)
    else:
        # 1. Obtener producto actual
        p = api("GET", f"products/{pid}.json?fields=id,title,options,variants,images")
        if not p:
            print("  No se pudo obtener el producto, saltando...")
            continue
        product = p["product"]
        print(f"  Título: {product['title']}")

        opt_tamano = next((o for o in product["options"] if "tama" in o["name"].lower()), product["options"][0])
        opt_color  = next((o for o in product["options"] if o["id"] != opt_tamano["id"]), None)
        tipo_opt_num = opt_color["position"] if opt_color else 2
        opt_key = f"option{tipo_opt_num}"
        tamano_opt_key = f"option{opt_tamano['position']}"

        # 2. Renombrar opción
        if opt_color and opt_color["name"].lower() != "tipo":
            print(f"  Renombrando '{opt_color['name']}' → 'Tipo'...")
            r = api("PUT", f"products/{pid}.json", {"product": {"id": pid, "options": [
                {"id": opt_tamano["id"], "name": opt_tamano["name"]},
                {"id": opt_color["id"], "name": "Tipo"}
            ]}})
            if r: print("  OK")
            time.sleep(0.5)

        # 3. Variantes existentes → Piel Lisa
        print(f"  Actualizando variantes → 'Piel Lisa'...")
        for v in product["variants"]:
            if v.get(opt_key, "").lower() != "piel lisa":
                r = api("PUT", f"variants/{v['id']}.json", {"variant": {"id": v["id"], opt_key: "Piel Lisa"}})
                if r: print(f"    {v['id']} OK")
                time.sleep(0.3)

        # 4. Crear variantes Piel Perforada
        print(f"  Creando variantes Piel Perforada...")
        perforada_variant_ids = []
        for i, tamano in enumerate(opt_tamano["values"]):
            precio = PRECIO_PERFORADA_MEDIO if i == 0 else PRECIO_PERFORADA_ENTERO
            r = api("POST", f"products/{pid}/variants.json", {"variant": {
                tamano_opt_key: tamano, opt_key: "Piel Perforada",
                "price": precio, "inventory_management": None,
                "fulfillment_service": "manual", "requires_shipping": True, "taxable": True,
            }})
            if r and "variant" in r:
                vid = r["variant"]["id"]
                perforada_variant_ids.append(vid)
                print(f"    {tamano} / Piel Perforada → ID:{vid} | ${precio}")
            time.sleep(0.5)

        # 5. Obtener variantes lisa e imágenes actuales
        p2 = api("GET", f"products/{pid}.json?fields=variants,images")
        all_variants = p2["product"]["variants"] if p2 else []
        lisa_variant_ids = [v["id"] for v in all_variants if v.get(opt_key) == "Piel Lisa"]
        existing_image_ids = [img["id"] for img in p2["product"]["images"]] if p2 else []

        print(f"  Variantes Lisa: {lisa_variant_ids}")
        print(f"  Variantes Perforada: {perforada_variant_ids}")

        # 6. Asociar imágenes existentes con Piel Lisa
        print(f"  Asociando imágenes existentes con Piel Lisa...")
        for img_id in existing_image_ids:
            r = api("PUT", f"products/{pid}/images/{img_id}.json", {
                "image": {"id": img_id, "variant_ids": lisa_variant_ids}
            })
            if r: print(f"    {img_id} → Lisa OK")
            time.sleep(0.3)

    # 7. Subir imágenes Perforada (aplica a todos)
    print(f"  Subiendo imágenes perforada...")
    uploaded_img_ids = []
    for fname in [f"perforada{ic}.png", f"perforadaasiento{ic}.png"]:
        img_id = upload_image(pid, fname, ic, perforada_variant_ids)
        if img_id:
            uploaded_img_ids.append(img_id)
            print(f"    {fname} → ID:{img_id} OK")
        time.sleep(1.5)

    print(f"  COMPLETADO — Lisa:{lisa_variant_ids} | Perforada:{perforada_variant_ids} | Imgs:{uploaded_img_ids}")
    time.sleep(1)

print("\n\nTODO COMPLETADO")
