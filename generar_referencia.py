import os, sys, asyncio
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

_env_file = Path(__file__).parent / ".env"
if _env_file.exists():
    for line in _env_file.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

from google import genai
from google.genai import types

PROMPT_V4 = """Generate a photorealistic premium leather studio photograph with the following creative direction:

CONCEPT: An extreme close-up of premium leather that fills the ENTIRE frame with no background visible anywhere — 100% leather from edge to edge.

COMPOSITION:
- Leather fills every single pixel of the image — zero background, zero gaps
- Large, sweeping organic folds that flow naturally across the entire frame
- Folds create a beautiful diagonal flow from one corner to the opposite corner
- Multiple layers of leather depth visible through overlapping folds
- The composition feels rich, full, and immersive

LIGHTING:
- Dramatic professional studio lighting: powerful key light from upper-left
- Bold sweeping highlight across the top surfaces of the folds
- Deep cinematic shadows falling hard into the fold creases
- Strong contrast between bright highlights and dark shadows — editorial quality
- The leather has a refined satin sheen that catches the studio light beautifully
- Lighting feels like a high-end fashion or automotive leather catalog

TEXTURE:
- Ultra fine pebble grain (nappa style) — sharply visible across all highlighted surfaces
- Flawless surface, no scratches, no marks, no imperfections
- Grain detail is crisp and beautiful in the highlights, melts into shadow in the creases

COLOR: Warm neutral cream/ivory/beige — base image for color grading

TECHNICAL:
- Cream/ivory/beige leather color as base
- Photorealistic — indistinguishable from a real luxury studio photograph
- Tack sharp across the entire frame
- NO background visible anywhere
- NO watermarks, NO logos, NO text
- Horizontal 16:9 format
- Luxury Italian leather catalog quality"""

PROMPT_V5 = """Generate a photorealistic premium leather catalog swatch photograph, styled exactly like a professional upholstery leather sample catalog (similar to high-end European leather catalogs).

CONCEPT: An extreme macro close-up of premium leather that fills 100% of the frame — shot from directly above (flat lay), showing the surface texture in maximum detail.

COMPOSITION:
- Camera is positioned directly overhead — perfectly flat, top-down angle
- Leather fills every single pixel — zero background, zero gaps
- The leather surface is flat with very subtle, gentle draping or natural relaxed folds — not dramatic, just organic
- Feels like a leather swatch laid flat for catalog photography

LIGHTING:
- Soft, even studio lighting — large softbox diffused light from above-left
- Minimal hard shadows — gentle, soft shadow lines only on natural folds
- Even illumination across the entire surface so texture is visible everywhere
- No deep dark shadows — this is catalog/sample card lighting, not editorial
- Light sheen that reveals the grain without overexposing

TEXTURE:
- Ultra-fine pebble grain (nappa upholstery style) — razor sharp and crisp across the entire frame
- Grain is the hero — every pore and texture detail clearly visible
- Flawless surface — no scratches, no marks
- Surface feels touchable and real

COLOR: Warm neutral cream/ivory/beige — base image for color transfer

TECHNICAL:
- Cream/ivory/beige leather as base color
- Photorealistic — indistinguishable from a real product catalog photo
- Tack sharp across 100% of the frame
- Square format (1:1)
- NO background, NO text, NO logos, NO watermarks
- Professional upholstery leather catalog quality — like Mendele, Boxmark, or Wollsdorf"""

async def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", type=int, default=4, help="Version de referencia a generar (4 o 5)")
    args = parser.parse_args()

    prompt = PROMPT_V5 if args.version == 5 else PROMPT_V4
    salida = Path(f"referencias_imagenes/Referencia_imagen{args.version}.jpg")

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    print(f"[...] Generando Referencia_imagen{args.version}...")

    response = await asyncio.to_thread(
        client.models.generate_content,
        model="gemini-3.1-flash-image-preview",
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            salida.write_bytes(part.inline_data.data)
            print(f"[OK] Guardada en: {salida}")
            return

    print("[X] No se genero imagen")

if __name__ == "__main__":
    asyncio.run(main())
