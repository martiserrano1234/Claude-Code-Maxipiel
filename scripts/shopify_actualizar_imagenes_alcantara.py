import sys
import os
import base64
import requests

sys.stdout.reconfigure(encoding='utf-8')

SHOP = 'maxipiel.myshopify.com'
TOKEN = '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'
API_VERSION = '2024-01'
BASE_URL = f'https://{SHOP}/admin/api/{API_VERSION}'
HEADERS = {
    'X-Shopify-Access-Token': TOKEN,
    'Content-Type': 'application/json'
}

IMAGES_DIR = r'C:\Users\danie\Downloads'

PRODUCTS = {
    'Rojo':    8549393137764,
    'Negro':   8549393170532,
    'Cafe':    8549393301604,
    'Beige':   8549393399908,
    'Camel':   8549393530980,
    'Gris':    8549393563748,
    'Chedron': 8549393727588,
}


def encode_image(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')


def delete_existing_images(product_id):
    r = requests.get(f'{BASE_URL}/products/{product_id}/images.json', headers=HEADERS)
    images = r.json().get('images', [])
    for img in images:
        requests.delete(f'{BASE_URL}/products/{product_id}/images/{img["id"]}.json', headers=HEADERS)
    return len(images)


def upload_image(product_id, attachment, filename, position):
    payload = {
        'image': {
            'attachment': attachment,
            'filename': filename,
            'position': position
        }
    }
    r = requests.post(f'{BASE_URL}/products/{product_id}/images.json', headers=HEADERS, json=payload)
    return r.status_code == 200 or r.status_code == 201


def main():
    print('=== Actualizando imagenes Alcantara (sin marca de agua) ===')
    print()

    for color, product_id in PRODUCTS.items():
        print(f'Actualizando: Alcantara {color} (ID: {product_id})...')

        img_main = os.path.join(IMAGES_DIR, f'Alcantara{color}.png')
        img_sillon = os.path.join(IMAGES_DIR, f'AlcantaraSillon{color}.png')

        if not os.path.exists(img_main) or not os.path.exists(img_sillon):
            print(f'  [!] Imagen no encontrada, saltando')
            continue

        deleted = delete_existing_images(product_id)
        print(f'  {deleted} imagenes anteriores eliminadas')

        ok1 = upload_image(product_id, encode_image(img_main), f'Alcantara{color}.png', 1)
        ok2 = upload_image(product_id, encode_image(img_sillon), f'AlcantaraSillon{color}.png', 2)

        if ok1 and ok2:
            print(f'  OK — 2 imagenes subidas')
        else:
            print(f'  [!] Error subiendo imagenes (main:{ok1}, sillon:{ok2})')
        print()

    print('=== LISTO ===')


if __name__ == '__main__':
    main()
