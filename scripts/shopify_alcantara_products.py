import sys
import os
import base64
import requests

sys.stdout.reconfigure(encoding='utf-8')

SHOP = 'maxipiel.myshopify.com'
TOKEN = 'TU_SHOPIFY_TOKEN'
API_VERSION = '2024-01'
BASE_URL = f'https://{SHOP}/admin/api/{API_VERSION}'
HEADERS = {
    'X-Shopify-Access-Token': TOKEN,
    'Content-Type': 'application/json'
}

IMAGES_DIR = r'C:\Users\danie\Downloads'

COLORS = ['Rojo', 'Negro', 'Cafe', 'Beige', 'Camel', 'Gris', 'Chedron']

# Precio sin IVA: con IVA ya incluido según Felix
# $1,199.99 media hoja | $2,399.99 hoja entera
PRICE_MEDIA = '1199.99'
PRICE_ENTERA = '2399.99'

COLLECTION_HANDLE = 'piel-automotriz'


def encode_image(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')


def get_collection_id():
    r = requests.get(f'{BASE_URL}/custom_collections.json', headers=HEADERS)
    collections = r.json().get('custom_collections', [])
    for c in collections:
        if c['handle'] == COLLECTION_HANDLE:
            return c['id']
    # Intentar smart collections
    r2 = requests.get(f'{BASE_URL}/smart_collections.json', headers=HEADERS)
    for c in r2.json().get('smart_collections', []):
        if c['handle'] == COLLECTION_HANDLE:
            return c['id']
    return None


def create_product(color):
    color_lower = color.lower()
    img_main = os.path.join(IMAGES_DIR, f'Alcantara{color}.png')
    img_sillon = os.path.join(IMAGES_DIR, f'AlcantaraSillon{color}.png')

    if not os.path.exists(img_main):
        print(f'  [!] No encontre imagen: {img_main}')
        return None
    if not os.path.exists(img_sillon):
        print(f'  [!] No encontre imagen: {img_sillon}')
        return None

    payload = {
        'product': {
            'title': f'Alcantara {color} — Piel Automotriz',
            'body_html': (
                f'<p>Tela Alcantara {color} de alta calidad para tapicería automotriz. '
                f'Textura suave, resistente y con acabado premium. '
                f'Disponible en media hoja (250 dcm²) y hoja entera (500 dcm²).</p>'
                f'<ul>'
                f'<li>Color: {color}</li>'
                f'<li>Material: Alcantara</li>'
                f'<li>Uso: Tapicería automotriz</li>'
                f'<li>Presentación: Media hoja 250 dcm² / Hoja entera 500 dcm²</li>'
                f'</ul>'
            ),
            'vendor': 'Maxipiel',
            'product_type': 'Alcantara',
            'tags': f'alcantara, alcantara-{color_lower}, piel-automotriz, tapiceria-automotriz',
            'variants': [
                {
                    'option1': 'Media Hoja',
                    'price': PRICE_MEDIA,
                    'sku': f'ALC-{color.upper()[:3]}-250',
                    'inventory_management': None,
                    'fulfillment_service': 'manual',
                    'requires_shipping': True,
                    'taxable': True,
                },
                {
                    'option1': 'Hoja Entera',
                    'price': PRICE_ENTERA,
                    'sku': f'ALC-{color.upper()[:3]}-500',
                    'inventory_management': None,
                    'fulfillment_service': 'manual',
                    'requires_shipping': True,
                    'taxable': True,
                }
            ],
            'options': [
                {'name': 'Tamaño', 'values': ['Media Hoja', 'Hoja Entera']}
            ],
            'images': [
                {
                    'attachment': encode_image(img_main),
                    'filename': f'Alcantara{color}.png',
                    'position': 1
                },
                {
                    'attachment': encode_image(img_sillon),
                    'filename': f'AlcantaraSillon{color}.png',
                    'position': 2
                }
            ],
            'status': 'active'
        }
    }

    r = requests.post(f'{BASE_URL}/products.json', headers=HEADERS, json=payload)
    if r.status_code == 201:
        product = r.json()['product']
        return product['id']
    else:
        print(f'  [ERROR] {r.status_code}: {r.text[:300]}')
        return None


def add_to_collection(collection_id, product_id):
    payload = {
        'collect': {
            'collection_id': collection_id,
            'product_id': product_id
        }
    }
    r = requests.post(f'{BASE_URL}/collects.json', headers=HEADERS, json=payload)
    return r.status_code == 201


def main():
    print('=== Creando productos Alcantara en Shopify ===')
    print(f'Colores: {", ".join(COLORS)}')
    print()

    collection_id = get_collection_id()
    if collection_id:
        print(f'Coleccion piel-automotriz encontrada (ID: {collection_id})')
    else:
        print('[!] No se encontro la coleccion piel-automotriz — los productos se crearan sin coleccion')
    print()

    created = []
    for color in COLORS:
        print(f'Creando: Alcantara {color}...')
        product_id = create_product(color)
        if product_id:
            print(f'  OK — Product ID: {product_id}')
            if collection_id:
                ok = add_to_collection(collection_id, product_id)
                print(f'  Agregado a coleccion: {"si" if ok else "ERROR"}')
            created.append((color, product_id))
        print()

    print('=== RESUMEN ===')
    print(f'{len(created)}/{len(COLORS)} productos creados exitosamente')
    for color, pid in created:
        print(f'  Alcantara {color} — ID: {pid}')
    print()
    print('Recuerda:')
    print('  - Agrega "Alcantara" como tipo de producto en el filtro de la coleccion si no aparece automatico')
    print('  - Verifica el orden de los productos en la coleccion (cuero top grain primero)')


if __name__ == '__main__':
    main()
