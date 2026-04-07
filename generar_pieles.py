import os
import sys
import base64
import asyncio
import argparse
from pathlib import Path

# Forzar UTF-8 en Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Cargar .env si existe
_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

from google import genai
from google.genai import types

PROMPT = """You have received exactly two images in this order:
- FIRST image (called "Referencia_imagen1"): a professional studio photo of leather with beautiful natural folds and dramatic lighting. This is ONLY a composition and style reference — do NOT use its color.
- SECOND image: a leather color swatch or sample photo. This is the COLOR MASTER — you must extract the dominant leather color from this image and apply it with 100% fidelity.

Your task: Reproduce the FIRST image exactly — same folds, same composition, same lighting, same shadows, same photographic style — but paint the leather in the EXACT color of the SECOND image.

CRITICAL RULES:
- Leather must fill 100% of the frame — NO white background, NO blank areas, NO gaps anywhere in the image
- The color must be an exact match to the SECOND image's leather tone — same hue, same saturation, same darkness/lightness
- Do NOT lighten or darken the color — reproduce it exactly as seen in the SECOND image
- Do NOT blend with the FIRST image's color — completely replace it
- Ignore background, labels, tags, or rings in the SECOND image — use ONLY the leather color
- Output must look like a real professional studio photograph"""

EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}


def get_mime_type(path: Path) -> str:
    return {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif",
        ".bmp": "image/bmp",
    }.get(path.suffix.lower(), "image/jpeg")


def cargar_referencias(input_dir: Path, nombre: str = "Referencia_imagen1.jpg") -> list:
    """Carga la imagen de referencia de estilo indicada."""
    ref = input_dir / nombre
    if ref.exists():
        mime = get_mime_type(ref)
        return [types.Part.from_bytes(data=ref.read_bytes(), mime_type=mime)]
    return []


async def generar_imagen(client, image_path: Path, output_dir: Path, semaphore: asyncio.Semaphore, referencias: list, color_dir: Path = None) -> bool:
    async with semaphore:
        nombre = image_path.name
        print(f"[...] Generando: {nombre}...")

        for intento in range(2):
            try:
                # Usar imagen de color_dir si existe, si no usar el swatch original
                color_ref_path = None
                if color_dir:
                    candidato = color_dir / (image_path.stem.lower() + ".jpg")
                    if candidato.exists():
                        color_ref_path = candidato

                if color_ref_path:
                    image_bytes = color_ref_path.read_bytes()
                    mime = "image/jpeg"
                    print(f"  >> Color desde: {color_ref_path.name}")
                else:
                    image_bytes = image_path.read_bytes()
                    mime = get_mime_type(image_path)

                contents = referencias + [
                    types.Part.from_bytes(data=image_bytes, mime_type=mime),
                    PROMPT,
                ]

                response = await asyncio.to_thread(
                    client.models.generate_content,
                    model="gemini-3.1-flash-image-preview",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE", "TEXT"],
                    ),
                )

                imagen_bytes = None
                for part in response.candidates[0].content.parts:
                    if part.inline_data and part.inline_data.mime_type.startswith("image/"):
                        imagen_bytes = part.inline_data.data
                        break

                if not imagen_bytes:
                    raise ValueError("La respuesta no contiene imagen")

                output_path = output_dir / (image_path.stem.lower() + ".jpg")
                output_path.write_bytes(imagen_bytes)
                print(f"[OK] Listo: {output_path.name}")
                return True

            except Exception as e:
                if intento == 0:
                    print(f"  [!] Error en {nombre}, reintentando... ({e})")
                    await asyncio.sleep(3)
                else:
                    print(f"  [X] Fallo: {nombre} -- {e}")
                    return False


async def main():
    parser = argparse.ArgumentParser(description="Genera imagenes de piel con Gemini")
    parser.add_argument("--tono", type=str, help="Procesar solo este archivo (ej: vino.JPG)")
    parser.add_argument("--referencia", type=str, default="Referencia_imagen1.jpg", help="Imagen de referencia de estilo (default: Referencia_imagen1.jpg)")
    parser.add_argument("--output", type=str, default="./output_v2", help="Carpeta de salida (default: ./output_v2)")
    parser.add_argument("--color-dir", type=str, default=None, help="Carpeta con imagenes de referencia de color (ej: ./output)")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[X] Variable de entorno GEMINI_API_KEY no encontrada")
        return

    client = genai.Client(api_key=api_key)

    input_dir = Path("./referencias_imagenes")
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    if args.tono:
        archivos = [input_dir / args.tono]
        if not archivos[0].exists():
            print(f"[X] Archivo no encontrado: {archivos[0]}")
            return
    else:
        archivos = [f for f in sorted(input_dir.iterdir())
                    if f.suffix.lower() in EXTENSIONS and not f.stem.lower().startswith("referencia_imagen")]

    if not archivos:
        print("[X] No se encontraron imagenes en ./referencias_imagenes/")
        return

    referencias = cargar_referencias(input_dir, args.referencia)
    if referencias:
        print(f">> Referencia de estilo: {args.referencia}")

    color_dir = Path(args.color_dir) if args.color_dir else None
    if color_dir:
        print(f">> Color desde carpeta: {color_dir}")

    print(f">> {len(archivos)} imagen(es) a procesar\n")

    semaphore = asyncio.Semaphore(1)
    tareas = [generar_imagen(client, f, output_dir, semaphore, referencias, color_dir) for f in archivos]
    resultados = await asyncio.gather(*tareas)

    exitosas = sum(resultados)
    total = len(resultados)
    print(f"\n{'='*40}")
    print(f"Generadas: {exitosas}/{total}")
    if exitosas < total:
        print(f"Errores:   {total - exitosas}/{total}")


if __name__ == "__main__":
    asyncio.run(main())
