"""
Sube las fotos de Sofía a Higgsfield y guarda las URLs permanentes.
"""
import os
import requests
import higgsfield_client

os.environ["HF_API_KEY"] = "fbafc015-82d8-441d-b94a-914c7abfad8c"
os.environ["HF_API_SECRET"] = "7d78231a8014dacf04cbca58a1139563e0dd3b5c7ddb070161e3e62bfb7a7baa"

DRIVE_URLS = [
    "https://drive.google.com/uc?export=download&id=1cXq32t6IYYAKH_15u8rxTO0os8DdF_NJ",
    "https://drive.google.com/uc?export=download&id=18wVmD4H_Yw6xCkQ1zOxfQX9jW9cMWli-",
    "https://drive.google.com/uc?export=download&id=1BYCZvdhPWs77nbA_UdRH25pMSNHnEs8W",
    "https://drive.google.com/uc?export=download&id=17oOs1Ie3KocYi6ATsTwaV0qMjsyKLTAC",
    "https://drive.google.com/uc?export=download&id=1gG-NTsGK5pT0Hu4sk7-N-m8cK6MzVr_l",
    "https://drive.google.com/uc?export=download&id=1M7agiJeeR7Ql6f4g_42bJeH6ZYlfafov",
    "https://drive.google.com/uc?export=download&id=1hJA7PxwJVPDOgFtxM_mxLUNjkzs7_wgg",
    "https://drive.google.com/uc?export=download&id=1kE6VTgLQeQxcsSaIu78fcwSP0CCbZm_p",
    "https://drive.google.com/uc?export=download&id=1WWzh8KrYvnF8JWOfVRBUgSiZ_Xq9bsaK",
    "https://drive.google.com/uc?export=download&id=17m697z8ZLAu8TTk4n_qi6FyUHFrVQptO",
    "https://drive.google.com/uc?export=download&id=10qS7raXvUq2S1wBlQvMOA8Z2yghuNESU",
    "https://drive.google.com/uc?export=download&id=1eJc-AZVEllENUiN9pvhjVLFhTgXI8VIz",
]

def download_image(url, index):
    session = requests.Session()
    response = session.get(url, stream=True, allow_redirects=True)
    # Maneja confirmación de Drive para archivos grandes
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            params = {"confirm": value, "id": url.split("id=")[1]}
            response = session.get("https://drive.google.com/uc", params=params, stream=True)
    content_type = response.headers.get("Content-Type", "image/jpeg")
    if "html" in content_type:
        print(f"  [!] Imagen {index+1} requiere acceso — asegúrate de que el archivo es público")
        return None, None
    return response.content, content_type.split(";")[0]

def main():
    print("Subiendo fotos de Sofía a Higgsfield...\n")
    uploaded_urls = []

    for i, drive_url in enumerate(DRIVE_URLS):
        print(f"[{i+1}/{len(DRIVE_URLS)}] Descargando desde Drive...")
        data, content_type = download_image(drive_url, i)
        if data is None:
            continue
        print(f"  Descargada ({len(data)/1024:.1f} KB) — subiendo a Higgsfield...")
        try:
            hf_url = higgsfield_client.upload(data, content_type or "image/jpeg")
            print(f"  OK: {hf_url}")
            uploaded_urls.append(hf_url)
        except Exception as e:
            print(f"  ERROR: {e}")

    print(f"\n{'='*60}")
    print(f"Subidas exitosas: {len(uploaded_urls)}/{len(DRIVE_URLS)}")
    print(f"{'='*60}")
    print("\nURLs permanentes de Sofía en Higgsfield:\n")
    for i, url in enumerate(uploaded_urls):
        print(f"{i+1}. {url}")

    # Guarda las URLs en un archivo
    with open("scripts/sofia_higgsfield_urls.txt", "w") as f:
        f.write("# URLs permanentes de Sofía en Higgsfield\n")
        f.write("# Usar estas URLs como image_url en los prompts de generación\n\n")
        for url in uploaded_urls:
            f.write(url + "\n")
    print("\nURLs guardadas en: scripts/sofia_higgsfield_urls.txt")

if __name__ == "__main__":
    main()
