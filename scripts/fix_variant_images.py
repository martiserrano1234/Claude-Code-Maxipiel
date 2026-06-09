import sys, json, time
import requests
sys.stdout.reconfigure(encoding='utf-8')

TOKEN = "TU_SHOPIFY_TOKEN"
STORE = "maxipiel.myshopify.com"
API = f"https://{STORE}/admin/api/2024-01"
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

PRODUCT_IDS = [8504430788708, 8504431542372, 8504431050852, 8504431149156, 8504431312996]

def api(method, path, body=None):
    url = f"{API}/{path}"
    r = requests.request(method, url, headers=HEADERS, json=body, timeout=60)
    if r.status_code >= 400:
        print(f"  ERROR {r.status_code}: {r.text[:200]}")
        return None
    return r.json()

for pid in PRODUCT_IDS:
    p = api("GET", f"products/{pid}.json?fields=id,title,images,variants")
    if not p: continue
    product = p["product"]
    print(f"\n{product['title']} (ID:{pid})")

    # Clasificar variantes por tipo
    lisa_ids = [v["id"] for v in product["variants"] if "piel lisa" in v["title"].lower()]
    perf_ids = [v["id"] for v in product["variants"] if "piel perforada" in v["title"].lower()]
    print(f"  Lisa: {lisa_ids}")
    print(f"  Perforada: {perf_ids}")

    for img in product["images"]:
        iid = img["id"]
        current = img["variant_ids"]
        src = img["src"]

        # Determinar a qué tipo pertenece esta imagen
        is_perf_img = "perforada" in src.lower()

        # Determinar target variant_ids
        if is_perf_img:
            target = perf_ids
            label = "perforada"
        else:
            target = lisa_ids
            label = "lisa"

        if set(current) == set(target):
            print(f"  Img {iid} ({label}) — ya OK")
            continue

        r = api("PUT", f"products/{pid}/images/{iid}.json", {
            "image": {"id": iid, "variant_ids": target}
        })
        if r:
            print(f"  Img {iid} ({label}) → {target} OK")
        time.sleep(0.3)

print("\nTODO LISTO")
