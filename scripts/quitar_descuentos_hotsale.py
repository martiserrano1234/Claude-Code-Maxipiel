import requests
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

SHOP = 'maxipiel.myshopify.com'
TOKEN = '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'
API_VERSION = '2024-01'
BASE_URL = f'https://{SHOP}/admin/api/{API_VERSION}'
HEADERS = {
    'X-Shopify-Access-Token': TOKEN,
    'Content-Type': 'application/json'
}

def get_all_products():
    products = []
    url = f'{BASE_URL}/products.json?limit=250'
    while url:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        data = r.json()
        products.extend(data['products'])
        link = r.headers.get('Link', '')
        url = None
        if 'rel="next"' in link:
            for part in link.split(','):
                if 'rel="next"' in part:
                    url = part.split(';')[0].strip().strip('<>')
    return products

def restore_prices():
    products = get_all_products()
    print(f'Total productos encontrados: {len(products)}')

    updated = 0
    skipped = 0

    for product in products:
        variants_to_update = []

        for variant in product['variants']:
            cap = variant.get('compare_at_price')
            price = variant.get('price')

            # Solo tocar variantes que tengan compare_at_price seteado
            if cap and float(cap) > 0:
                variants_to_update.append({
                    'id': variant['id'],
                    'price': cap,           # restaurar precio original
                    'compare_at_price': ''  # limpiar el tachado
                })

        if variants_to_update:
            payload = {
                'product': {
                    'id': product['id'],
                    'variants': variants_to_update
                }
            }
            r = requests.put(f'{BASE_URL}/products/{product["id"]}.json', json=payload, headers=HEADERS)
            if r.status_code == 200:
                print(f'  ✓ {product["title"]} — {len(variants_to_update)} variante(s) restauradas')
                updated += 1
            else:
                print(f'  ✗ ERROR {product["title"]}: {r.status_code} {r.text[:200]}')
            time.sleep(0.5)
        else:
            skipped += 1

    print(f'\nListo. Productos actualizados: {updated} | Sin descuento (no tocados): {skipped}')

restore_prices()
