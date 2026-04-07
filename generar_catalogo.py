import sys
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, HRFlowable, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import io

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# ---------- Nombres limpios ----------
NOMBRES = {
    "azulaqua40":             "Azul Aqua",
    "cafe2":                  "Cafe",
    "cafeoxford20":           "Cafe Oxford",
    "camel6":                 "Camel",
    "chedronarena":           "Chedron Arena",
    "chedronterracota10":     "Chedron Terracota",
    "cona20":                 "Conac",
    "coñac20":                "Conac",
    "gris":                   "Gris",
    "grisoscuro":             "Gris Oscuro",
    "grisoxford92":           "Gris Oxford",
    "hueso1":                 "Hueso",
    "king_ranch":             "King Ranch",
    "miel30":                 "Miel",
    "negro72semiliso":        "Negro Semi Liso",
    "negrofondoazul7":        "Negro Fondo Azul",
    "negrofondogris12":       "Negro Fondo Gris",
    "negrograbadoitaliano10": "Negro Grabado Italiano",
    "plateadoobscuro80":      "Plateado Obscuro",
    "rojoferrari":            "Rojo Ferrari",
    "rojoladrillo42":         "Rojo Ladrillo",
    "rojoquemado":            "Rojo Quemado",
    "uva11":                  "Uva",
    "vino":                   "Vino",
    "vinochocolate16":        "Vino Chocolate",
}

LOGO_PATH = Path("./referencias_imagenes/logo_maxipiel.jpeg")

def nombre_limpio(stem):
    return NOMBRES.get(stem, stem.replace("_", " ").title())

def preparar_imagen(path: Path, size_px: int) -> io.BytesIO:
    img = Image.open(path).convert("RGB")
    w, h = img.size
    lado = min(w, h)
    left = (w - lado) // 2
    top  = (h - lado) // 2
    img  = img.crop((left, top, left + lado, top + lado))
    img  = img.resize((size_px, size_px), Image.LANCZOS)
    buf  = io.BytesIO()
    img.save(buf, format="JPEG", quality=92)
    buf.seek(0)
    return buf

def preparar_logo(path: Path, alto_pt: float) -> io.BytesIO:
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    ancho_pt = alto_pt * (w / h)
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=92)
    buf.seek(0)
    return buf, ancho_pt

def main():
    input_dir  = Path("./output_v5")
    output_pdf = Path("./Catalogo_Maxipiel.pdf")

    archivos = sorted([f for f in input_dir.iterdir() if f.suffix.lower() in {".jpg", ".jpeg", ".png"}])
    if not archivos:
        print("[X] No se encontraron imagenes en output_v5/")
        return

    W, H   = A4
    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        leftMargin=15*mm, rightMargin=15*mm,
        topMargin=15*mm,  bottomMargin=15*mm,
    )

    col_w  = (W - 30*mm) / 2
    img_pt = col_w - 10*mm

    # ---------- Estilos ----------
    sub_style = ParagraphStyle(
        "sub",
        fontName="Helvetica",
        fontSize=10,
        textColor=colors.HexColor("#555555"),
        alignment=TA_CENTER,
        spaceAfter=0,
    )
    nombre_style = ParagraphStyle(
        "nombre",
        fontName="Helvetica-Bold",
        fontSize=9,
        textColor=colors.HexColor("#1a1a1a"),
        alignment=TA_CENTER,
        spaceBefore=2.5*mm,
        spaceAfter=0,
    )

    # ---------- Story ----------
    story = []

    # Header: logo + texto centrados
    logo_alto = 18*mm
    if LOGO_PATH.exists():
        logo_buf, logo_ancho = preparar_logo(LOGO_PATH, logo_alto)
        logo_img = RLImage(logo_buf, width=logo_ancho, height=logo_alto)
        header_data = [[logo_img, Paragraph("<b>Maxipiel S.A. de C.V.</b><br/>Catalogo de Pieles para Tapiceria", sub_style)]]
        header_tabla = Table(
            header_data,
            colWidths=[logo_ancho + 4*mm, W - 30*mm - logo_ancho - 4*mm],
        )
        header_tabla.setStyle(TableStyle([
            ("ALIGN",   (0, 0), (0, 0), "RIGHT"),
            ("ALIGN",   (1, 0), (1, 0), "LEFT"),
            ("VALIGN",  (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 3*mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3*mm),
        ]))
        story.append(header_tabla)
    else:
        story.append(Paragraph("MAXIPIEL", sub_style))

    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#bbbbbb")))
    story.append(Spacer(1, 5*mm))

    # ---------- Grid de tonos ----------
    filas = []
    for i in range(0, len(archivos), 2):
        fila_imgs    = []
        fila_nombres = []
        for j in range(2):
            if i + j < len(archivos):
                f       = archivos[i + j]
                buf     = preparar_imagen(f, 600)
                rl_img  = RLImage(buf, width=img_pt, height=img_pt)
                nombre  = nombre_limpio(f.stem)
                fila_imgs.append(rl_img)
                fila_nombres.append(Paragraph(nombre, nombre_style))
            else:
                fila_imgs.append("")
                fila_nombres.append("")
        filas.append(fila_imgs)
        filas.append(fila_nombres)

    tabla = Table(
        filas,
        colWidths=[col_w, col_w],
        rowHeights=None,
    )
    tabla.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5*mm),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5*mm),
    ]))
    story.append(tabla)

    # ---------- Footer ----------
    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(colors.HexColor("#aaaaaa"))
        canvas.drawCentredString(W / 2, 9*mm, "Maxipiel  |  Pieles de calidad para tapiceria  |  Leon, Guanajuato")
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"[OK] PDF generado: {output_pdf}")

if __name__ == "__main__":
    main()
