"""
Transfiere el tono/color de las imagenes en output/ a las imagenes en output_v2/
conservando la composicion de output_v2/.

Uso:
    python transferir_color.py                    # procesa todas
    python transferir_color.py --tono negro72semiliso.jpg  # solo una
"""
import sys
import argparse
import numpy as np
from pathlib import Path
from PIL import Image, ImageEnhance

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


def transferir_color_lab(composicion: np.ndarray, color_ref: np.ndarray) -> np.ndarray:
    """
    Aplica el tono de color_ref a composicion usando transferencia en espacio LAB.
    Ambas entradas deben ser arrays RGB float32 en rango [0, 1].
    """
    def rgb_a_lab(img):
        # RGB -> XYZ (iluminante D65)
        mask = img > 0.04045
        img_lin = np.where(mask, ((img + 0.055) / 1.055) ** 2.4, img / 12.92)
        M = np.array([
            [0.4124564, 0.3575761, 0.1804375],
            [0.2126729, 0.7151522, 0.0721750],
            [0.0193339, 0.1191920, 0.9503041]
        ])
        xyz = img_lin @ M.T
        # XYZ -> LAB
        xyz /= np.array([0.95047, 1.00000, 1.08883])
        eps, kappa = 0.008856, 903.3
        f = np.where(xyz > eps, xyz ** (1/3), (kappa * xyz + 16) / 116)
        L = 116 * f[..., 1] - 16
        a = 500 * (f[..., 0] - f[..., 1])
        b = 200 * (f[..., 1] - f[..., 2])
        return np.stack([L, a, b], axis=-1)

    def lab_a_rgb(lab):
        L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
        fy = (L + 16) / 116
        fx = a / 500 + fy
        fz = fy - b / 200
        eps = 0.008856
        x = np.where(fx**3 > eps, fx**3, (116*fx - 16) / 903.3)
        y = np.where(L > (eps * 903.3), ((L + 16)/116)**3, L / 903.3)
        z = np.where(fz**3 > eps, fz**3, (116*fz - 16) / 903.3)
        xyz = np.stack([x, y, z], axis=-1) * np.array([0.95047, 1.00000, 1.08883])
        M_inv = np.array([
            [ 3.2404542, -1.5371385, -0.4985314],
            [-0.9692660,  1.8760108,  0.0415560],
            [ 0.0556434, -0.2040259,  1.0572252]
        ])
        rgb_lin = xyz @ M_inv.T
        rgb_lin = np.clip(rgb_lin, 0, None)
        mask = rgb_lin > 0.0031308
        rgb = np.where(mask, 1.055 * rgb_lin**(1/2.4) - 0.055, 12.92 * rgb_lin)
        return np.clip(rgb, 0, 1)

    lab_comp = rgb_a_lab(composicion)
    lab_ref  = rgb_a_lab(color_ref)

    # Solo transferir los canales de color (a y b), preservar luminancia (L) intacta
    for c in range(1, 3):  # 0=L (brillo), 1=a (verde-rojo), 2=b (azul-amarillo)
        media_comp = lab_comp[..., c].mean()
        std_comp   = lab_comp[..., c].std() + 1e-6
        media_ref  = lab_ref[..., c].mean()
        std_ref    = lab_ref[..., c].std() + 1e-6

        lab_comp[..., c] = (lab_comp[..., c] - media_comp) * (std_ref / std_comp) + media_ref

    return lab_a_rgb(lab_comp)


def procesar(comp_path: Path, ref_path: Path, output_path: Path,
             brillo: float = 1.0, contraste: float = 1.0, saturacion: float = 1.0):
    comp_img = Image.open(comp_path).convert("RGB")
    ref_img  = Image.open(ref_path).convert("RGB").resize(comp_img.size, Image.LANCZOS)

    comp_arr = np.array(comp_img).astype(np.float32) / 255.0
    ref_arr  = np.array(ref_img).astype(np.float32) / 255.0

    resultado = transferir_color_lab(comp_arr, ref_arr)
    resultado = (resultado * 255).clip(0, 255).astype(np.uint8)

    img = Image.fromarray(resultado)
    if brillo != 1.0:
        img = ImageEnhance.Brightness(img).enhance(brillo)
    if contraste != 1.0:
        img = ImageEnhance.Contrast(img).enhance(contraste)
    if saturacion != 1.0:
        img = ImageEnhance.Color(img).enhance(saturacion)

    img.save(output_path, "JPEG", quality=95)
    print(f"[OK] {output_path.name}")


def main():
    parser = argparse.ArgumentParser(description="Transfiere color de output/ a output_v2/")
    parser.add_argument("--tono", type=str, help="Procesar solo este archivo (ej: negro72semiliso.jpg)")
    parser.add_argument("--base", type=str, default=None, help="Usar una sola imagen como composicion base (ej: referencias_imagenes/Referencia_imagen3.jpeg)")
    parser.add_argument("--composicion-dir", type=str, default="./output_v2", help="Carpeta con imagenes de composicion")
    parser.add_argument("--color-dir",       type=str, default="./output",    help="Carpeta con imagenes de referencia de color")
    parser.add_argument("--output-dir",      type=str, default="./output_v3", help="Carpeta de salida")
    parser.add_argument("--brillo",     type=float, default=1.0, help="Factor de brillo (ej: 1.3 = +30%%)")
    parser.add_argument("--contraste",  type=float, default=1.0, help="Factor de contraste (ej: 1.2 = +20%%)")
    parser.add_argument("--saturacion", type=float, default=1.0, help="Factor de saturacion (ej: 1.2 = +20%%)")
    args = parser.parse_args()

    color_dir  = Path(args.color_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    # Modo base unica: aplica todos los colores de color-dir a una sola imagen
    if args.base:
        base_path = Path(args.base)
        if not base_path.exists():
            print(f"[X] Imagen base no encontrada: {base_path}")
            return
        archivos_color = sorted(color_dir.glob("*.jpg"))
        if args.tono:
            archivos_color = [color_dir / args.tono]
        total, ok = 0, 0
        for ref_path in archivos_color:
            total += 1
            try:
                procesar(base_path, ref_path, output_dir / ref_path.name, args.brillo, args.contraste, args.saturacion)
                ok += 1
            except Exception as e:
                print(f"[X] Error en {ref_path.name}: {e}")
        print(f"\n{'='*40}")
        print(f"Procesadas: {ok}/{total}")
        return

    comp_dir = Path(args.composicion_dir)
    if args.tono:
        archivos = [comp_dir / args.tono]
    else:
        archivos = sorted(comp_dir.glob("*.jpg"))

    total, ok = 0, 0
    for comp_path in archivos:
        ref_path = color_dir / comp_path.name
        if not ref_path.exists():
            print(f"[!] Sin referencia de color para {comp_path.name}, saltando")
            continue
        total += 1
        try:
            procesar(comp_path, ref_path, output_dir / comp_path.name, args.brillo, args.contraste, args.saturacion)
            ok += 1
        except Exception as e:
            print(f"[X] Error en {comp_path.name}: {e}")

    print(f"\n{'='*40}")
    print(f"Procesadas: {ok}/{total}")


if __name__ == "__main__":
    main()
