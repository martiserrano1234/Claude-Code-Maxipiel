from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ─── Colores ────────────────────────────────────────────────
DARK_BG      = HexColor("#0F172A")   # fondo oscuro
ACCENT       = HexColor("#6366F1")   # índigo
ACCENT_LIGHT = HexColor("#818CF8")
SUCCESS      = HexColor("#10B981")   # verde
WARNING      = HexColor("#F59E0B")   # ámbar
SURFACE      = HexColor("#1E293B")   # superficie de cards
BORDER       = HexColor("#334155")   # borde sutil
TEXT_PRIMARY = HexColor("#F1F5F9")   # texto principal
TEXT_MUTED   = HexColor("#94A3B8")   # texto secundario
TAG_BG       = HexColor("#312E81")   # fondo de tags/badges

OUTPUT = os.path.join(os.path.dirname(__file__), "AI_Marketing_Suite_Maxipiel.pdf")

# ─── Fondo de página ────────────────────────────────────────
def draw_background(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.restoreState()

# ─── Documento ──────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=18*mm, leftMargin=18*mm,
    topMargin=14*mm, bottomMargin=14*mm,
    title="AI Marketing Suite — Guia Maxipiel",
    author="Felix Garcia — Maxipiel",
    onFirstPage=draw_background,
    onLaterPages=draw_background,
)

W, H = A4
CONTENT_W = W - 36*mm

styles = getSampleStyleSheet()

# ─── Estilos personalizados ─────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

ST = {
    "cover_title": S("cover_title",
        fontSize=34, textColor=white, fontName="Helvetica-Bold",
        leading=40, alignment=TA_CENTER),
    "cover_sub": S("cover_sub",
        fontSize=13, textColor=ACCENT_LIGHT, fontName="Helvetica",
        leading=18, alignment=TA_CENTER),
    "cover_badge": S("cover_badge",
        fontSize=10, textColor=SUCCESS, fontName="Helvetica-Bold",
        alignment=TA_CENTER),
    "section_label": S("section_label",
        fontSize=8, textColor=ACCENT_LIGHT, fontName="Helvetica-Bold",
        leading=10, spaceAfter=2),
    "section_title": S("section_title",
        fontSize=20, textColor=white, fontName="Helvetica-Bold",
        leading=24, spaceAfter=6),
    "cmd_title": S("cmd_title",
        fontSize=15, textColor=white, fontName="Helvetica-Bold",
        leading=18, spaceAfter=2),
    "cmd_tag": S("cmd_tag",
        fontSize=9, textColor=ACCENT_LIGHT, fontName="Helvetica-Bold",
        leading=11, spaceAfter=8),
    "body": S("body",
        fontSize=9.5, textColor=TEXT_PRIMARY, fontName="Helvetica",
        leading=15, spaceAfter=4, alignment=TA_JUSTIFY),
    "bullet": S("bullet",
        fontSize=9, textColor=TEXT_PRIMARY, fontName="Helvetica",
        leading=14, leftIndent=12, spaceAfter=2,
        bulletIndent=4, bulletText="•"),
    "sub_header": S("sub_header",
        fontSize=10, textColor=ACCENT_LIGHT, fontName="Helvetica-Bold",
        leading=14, spaceBefore=8, spaceAfter=3),
    "code": S("code",
        fontSize=8.5, textColor=SUCCESS, fontName="Courier-Bold",
        leading=13, backColor=SURFACE, leftIndent=8, rightIndent=8,
        borderPadding=(4,4,4,4), spaceAfter=4),
    "muted": S("muted",
        fontSize=8.5, textColor=TEXT_MUTED, fontName="Helvetica",
        leading=12, spaceAfter=2),
    "table_header": S("table_header",
        fontSize=8.5, textColor=white, fontName="Helvetica-Bold",
        leading=11, alignment=TA_CENTER),
    "table_cell": S("table_cell",
        fontSize=8.5, textColor=TEXT_PRIMARY, fontName="Helvetica",
        leading=12, alignment=TA_LEFT),
    "table_cmd": S("table_cmd",
        fontSize=8.5, textColor=SUCCESS, fontName="Courier-Bold",
        leading=12, alignment=TA_LEFT),
    "toc_item": S("toc_item",
        fontSize=10, textColor=TEXT_PRIMARY, fontName="Helvetica",
        leading=16, leftIndent=8),
    "toc_num": S("toc_num",
        fontSize=10, textColor=ACCENT, fontName="Helvetica-Bold",
        leading=16),
    "intro": S("intro",
        fontSize=10.5, textColor=TEXT_PRIMARY, fontName="Helvetica",
        leading=17, spaceAfter=6, alignment=TA_JUSTIFY),
    "highlight_box": S("highlight_box",
        fontSize=9.5, textColor=white, fontName="Helvetica",
        leading=15, alignment=TA_LEFT),
    "footer_text": S("footer_text",
        fontSize=7.5, textColor=TEXT_MUTED, fontName="Helvetica",
        alignment=TA_CENTER),
}

# ─── Flowable: fondo de página ───────────────────────────────
class FullBackground(Flowable):
    def __init__(self, color=DARK_BG):
        super().__init__()
        self.color = color
        self.width = W
        self.height = H
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(-18*mm, -14*mm, W, H, fill=1, stroke=0)

# ─── Flowable: línea decorativa ─────────────────────────────
class DecorLine(Flowable):
    def __init__(self, w=CONTENT_W, color=ACCENT, thickness=1.5):
        super().__init__()
        self.w = w
        self.color = color
        self.thickness = thickness
        self.height = self.thickness + 2
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.w, 0)

# ─── Flowable: card de comando ───────────────────────────────
class CmdCard(Flowable):
    def __init__(self, cmd, tag, color=ACCENT):
        super().__init__()
        self.cmd = cmd
        self.tag = tag
        self.color = color
        self.width = CONTENT_W
        self.height = 48
    def draw(self):
        c = self.canv
        # fondo
        c.setFillColor(SURFACE)
        c.roundRect(0, 0, self.width, self.height, 6, fill=1, stroke=0)
        # barra izquierda
        c.setFillColor(self.color)
        c.roundRect(0, 0, 4, self.height, 2, fill=1, stroke=0)
        c.rect(2, 0, 2, self.height, fill=1, stroke=0)
        # comando
        c.setFillColor(white)
        c.setFont("Courier-Bold", 14)
        c.drawString(14, self.height - 22, self.cmd)
        # tag
        c.setFillColor(self.color)
        tw = c.stringWidth(self.tag, "Helvetica-Bold", 8) + 12
        c.roundRect(14, 6, tw, 14, 3, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(20, 10, self.tag)

# ─── Flowable: separador de sección ─────────────────────────
class SectionDivider(Flowable):
    def __init__(self, num, label):
        super().__init__()
        self.num = num
        self.label = label
        self.width = CONTENT_W
        self.height = 36
    def draw(self):
        c = self.canv
        c.setFillColor(ACCENT)
        c.roundRect(0, 0, 36, 36, 4, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(18, 10, str(self.num))
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(46, 12, self.label)
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.line(46, 11, CONTENT_W, 11)

# ─── Helper: tabla estilo dark ───────────────────────────────
def dark_table(data, col_widths, header=True):
    style = [
        ("BACKGROUND", (0,0), (-1,0), ACCENT if header else SURFACE),
        ("TEXTCOLOR", (0,0), (-1,0), white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 8.5),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [SURFACE, DARK_BG]),
        ("TEXTCOLOR", (0,1), (-1,-1), TEXT_PRIMARY),
        ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
        ("GRID", (0,0), (-1,-1), 0.3, BORDER),
        ("ROWHEIGHT", (0,0), (-1,-1), 16),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ROUNDEDCORNERS", [4]),
    ]
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle(style))
    return t

# ─── Helper: box de highlight ────────────────────────────────
def highlight_box(text, color=ACCENT, icon="💡"):
    data = [[Paragraph(f"<b>{icon}</b>  {text}", ST["highlight_box"])]]
    t = Table(data, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("ROUNDEDCORNERS", [5]),
    ]))
    return t

# ─── Helper: bullet list ─────────────────────────────────────
def bullets(items, color=ACCENT_LIGHT):
    result = []
    for item in items:
        p = Paragraph(f"<font color='#{color.hexval()[2:]}'>▸</font>  {item}", ST["bullet"])
        result.append(p)
    return result

def sp(n=6): return Spacer(1, n)

# ════════════════════════════════════════════════════════════
# CONTENIDO
# ════════════════════════════════════════════════════════════
story = []

# ─── PORTADA ────────────────────────────────────────────────
story.append(sp(50))

# Logo / icono visual
logo_data = [["🚀"]]
logo_t = Table(logo_data, colWidths=[80])
logo_t.setStyle(TableStyle([
    ("FONTSIZE", (0,0), (-1,-1), 36),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("BACKGROUND", (0,0), (-1,-1), ACCENT),
    ("ROUNDEDCORNERS", [12]),
    ("LEFTPADDING", (0,0), (-1,-1), 16),
    ("RIGHTPADDING", (0,0), (-1,-1), 16),
    ("TOPPADDING", (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
]))
story.append(Table([[logo_t]], colWidths=[CONTENT_W]))
story.append(sp(20))

story.append(Paragraph("AI Marketing Suite", ST["cover_title"]))
story.append(sp(8))
story.append(Paragraph("Guía completa de funcionalidades para Maxipiel", ST["cover_sub"]))
story.append(sp(24))

# Badges de info
badges = [
    ["15 Skills", "5 Agentes en paralelo", "PDF export ✓", "Claude Code"],
]
bt = Table(badges, colWidths=[CONTENT_W/4]*4)
bt.setStyle(TableStyle([
    ("FONTNAME", (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 9),
    ("TEXTCOLOR", (0,0), (-1,-1), white),
    ("BACKGROUND", (0,0), (-1,-1), SURFACE),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("GRID", (0,0), (-1,-1), 0.5, BORDER),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(bt)
story.append(sp(30))

story.append(DecorLine(color=ACCENT))
story.append(sp(10))
story.append(Paragraph("Maxipiel — León, Guanajuato · 2026", ST["cover_badge"]))
story.append(sp(6))
story.append(Paragraph("Felix Alejandro Garcia Garcia · Developer", ST["muted"]))

story.append(PageBreak())

# ─── ÍNDICE ─────────────────────────────────────────────────
story.append(sp(10))
story.append(Paragraph("CONTENIDO", ST["section_label"]))
story.append(Paragraph("Tabla de contenidos", ST["section_title"]))
story.append(DecorLine())
story.append(sp(12))

toc = [
    ("01", "Cómo funciona el suite"),
    ("02", "Resumen rápido de comandos"),
    ("03", "/market audit — Auditoría completa"),
    ("04", "/market quick — Snapshot rápido"),
    ("05", "/market copy — Análisis y generación de copy"),
    ("06", "/market emails — Secuencias de email"),
    ("07", "/market social — Calendario de redes sociales"),
    ("08", "/market ads — Campañas publicitarias"),
    ("09", "/market funnel — Análisis del embudo de ventas"),
    ("10", "/market competitors — Inteligencia competitiva"),
    ("11", "/market landing — Optimización CRO"),
    ("12", "/market launch — Playbook de lanzamiento"),
    ("13", "/market proposal — Propuesta comercial"),
    ("14", "/market seo — Auditoría SEO"),
    ("15", "/market brand — Voz de marca"),
    ("16", "/market report / report-pdf — Reporte final"),
    ("17", "Flujo recomendado para Maxipiel"),
    ("18", "Limitaciones importantes"),
]

for num, label in toc:
    row = Table(
        [[Paragraph(num, ST["toc_num"]), Paragraph(label, ST["toc_item"])]],
        colWidths=[28, CONTENT_W - 28]
    )
    row.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, BORDER),
    ]))
    story.append(row)

story.append(PageBreak())

# ─── SECCIÓN 1: CÓMO FUNCIONA ───────────────────────────────
story.append(sp(8))
story.append(SectionDivider(1, "Cómo funciona el suite"))
story.append(sp(12))

story.append(Paragraph(
    "El AI Marketing Suite es una colección de 15 skills instaladas directamente en Claude Code. "
    "Se activan con el prefijo <b>/market</b> seguido del comando específico. No requiere salir de la terminal "
    "ni abrir otras herramientas — todo corre dentro de tu entorno de trabajo actual.",
    ST["intro"]))

story.append(Paragraph(
    "Cuando combinas comandos en secuencia, los siguientes automáticamente incorporan los datos "
    "de los análisis anteriores. Por ejemplo, si primero corres <b>/market brand</b> y luego "
    "<b>/market copy</b>, el copy generado usará las guías de voz ya documentadas.",
    ST["intro"]))

story.append(sp(8))
story.append(highlight_box(
    "Todos los outputs se guardan como archivos .md (o .pdf) en el directorio donde estés trabajando. "
    "Asegúrate de estar en la carpeta correcta antes de ejecutar los comandos.",
    color=SURFACE, icon="📁"))

story.append(sp(12))
story.append(Paragraph("Instalación", ST["sub_header"]))
for b in bullets([
    "Repo clonado en: Claude Code Maxipixel/ai-marketing-claude",
    "Skills instaladas en: C:\\Users\\danie\\.claude\\skills\\",
    "Agentes instalados en: C:\\Users\\danie\\.claude\\agents\\",
    "<b>reportlab</b> instalado — soporte completo de exportacion PDF",
]):
    story.append(b)

story.append(PageBreak())

# ─── SECCIÓN 2: RESUMEN RÁPIDO ───────────────────────────────
story.append(sp(8))
story.append(SectionDivider(2, "Resumen rápido de comandos"))
story.append(sp(12))

cmd_table_data = [
    [Paragraph("Comando", ST["table_header"]),
     Paragraph("Qué necesita", ST["table_header"]),
     Paragraph("Output", ST["table_header"])],
    [Paragraph("/market audit <url>", ST["table_cmd"]),
     Paragraph("URL pública accesible", ST["table_cell"]),
     Paragraph("MARKETING-AUDIT.md", ST["table_cell"])],
    [Paragraph("/market quick <url>", ST["table_cmd"]),
     Paragraph("URL pública", ST["table_cell"]),
     Paragraph("Solo en pantalla", ST["table_cell"])],
    [Paragraph("/market copy <url>", ST["table_cmd"]),
     Paragraph("URL o descripción de producto", ST["table_cell"]),
     Paragraph("COPY-SUGGESTIONS.md", ST["table_cell"])],
    [Paragraph("/market emails <tema/url>", ST["table_cmd"]),
     Paragraph("Tema o URL del negocio", ST["table_cell"]),
     Paragraph("EMAIL-SEQUENCES.md", ST["table_cell"])],
    [Paragraph("/market social <tema/url>", ST["table_cmd"]),
     Paragraph("Tema o URL del negocio", ST["table_cell"]),
     Paragraph("SOCIAL-CALENDAR.md", ST["table_cell"])],
    [Paragraph("/market ads <url>", ST["table_cmd"]),
     Paragraph("URL del producto/negocio", ST["table_cell"]),
     Paragraph("AD-CAMPAIGNS.md", ST["table_cell"])],
    [Paragraph("/market funnel <url>", ST["table_cmd"]),
     Paragraph("URL con flujo de compra", ST["table_cell"]),
     Paragraph("FUNNEL-ANALYSIS.md", ST["table_cell"])],
    [Paragraph("/market competitors <url>", ST["table_cmd"]),
     Paragraph("URL propia o de competidor", ST["table_cell"]),
     Paragraph("COMPETITOR-REPORT.md", ST["table_cell"])],
    [Paragraph("/market landing <url>", ST["table_cmd"]),
     Paragraph("URL de landing page", ST["table_cell"]),
     Paragraph("LANDING-CRO.md", ST["table_cell"])],
    [Paragraph("/market launch <descripción>", ST["table_cmd"]),
     Paragraph("Descripción + audiencia + fecha", ST["table_cell"]),
     Paragraph("LAUNCH-PLAYBOOK.md", ST["table_cell"])],
    [Paragraph("/market proposal <cliente>", ST["table_cmd"]),
     Paragraph("Contexto del cliente", ST["table_cell"]),
     Paragraph("CLIENT-PROPOSAL.md", ST["table_cell"])],
    [Paragraph("/market report <url>", ST["table_cmd"]),
     Paragraph("URL (usa datos previos si hay)", ST["table_cell"]),
     Paragraph("MARKETING-REPORT.md", ST["table_cell"])],
    [Paragraph("/market report-pdf <url>", ST["table_cmd"]),
     Paragraph("URL (usa datos previos si hay)", ST["table_cell"]),
     Paragraph("MARKETING-REPORT.pdf", ST["table_cell"])],
    [Paragraph("/market seo <url>", ST["table_cmd"]),
     Paragraph("URL pública", ST["table_cell"]),
     Paragraph("SEO-AUDIT.md", ST["table_cell"])],
    [Paragraph("/market brand <url>", ST["table_cmd"]),
     Paragraph("URL del negocio", ST["table_cell"]),
     Paragraph("BRAND-VOICE.md", ST["table_cell"])],
]
story.append(dark_table(cmd_table_data, [80*mm, 65*mm, 55*mm]))

story.append(PageBreak())

# ════════════════════════════════════════════════════════════
# COMANDOS DETALLADOS
# ════════════════════════════════════════════════════════════

def cmd_section(num, cmd, tag, tag_color, description, needs, does, output_file, maxipiel_tip,
                agents=None, score_table=None, types_table=None, extra_blocks=None):
    items = []
    items.append(sp(8))
    items.append(SectionDivider(num, cmd))
    items.append(sp(10))
    items.append(CmdCard(cmd, tag, tag_color))
    items.append(sp(10))
    items.append(Paragraph(description, ST["intro"]))
    items.append(sp(6))

    items.append(Paragraph("¿Qué necesita?", ST["sub_header"]))
    items += bullets(needs)

    if agents:
        items.append(sp(6))
        items.append(Paragraph("Agentes que lanza en paralelo", ST["sub_header"]))
        items += bullets(agents, color=SUCCESS)

    items.append(sp(6))
    items.append(Paragraph("¿Qué hace?", ST["sub_header"]))
    for d in does:
        items.append(Paragraph(d, ST["body"]))

    if score_table:
        items.append(sp(6))
        items.append(score_table)

    if types_table:
        items.append(sp(6))
        items.append(types_table)

    if extra_blocks:
        for block in extra_blocks:
            items.append(block)

    items.append(sp(6))
    items.append(Paragraph("Archivo de salida", ST["sub_header"]))
    items.append(Paragraph(output_file, ST["code"]))

    items.append(sp(6))
    items.append(highlight_box(f"<b>Para Maxipiel:</b> {maxipiel_tip}", color=TAG_BG, icon="🎯"))
    items.append(sp(4))
    items.append(DecorLine(color=BORDER, thickness=0.5))

    return items

# ─── 03 AUDIT ───────────────────────────────────────────────
story += cmd_section(
    3, "/market audit <url>", "FLAGSHIP · 5 agentes en paralelo", ACCENT,
    "El comando más poderoso del suite. Lanza 5 sub-agentes que trabajan simultáneamente "
    "y combinan sus resultados en un reporte con score 0-100 en 6 dimensiones ponderadas. "
    "Es el punto de partida ideal para cualquier análisis.",
    needs=[
        "Una URL pública accesible (tienda de ML, sitio web de competidor, Amazon, etc.)",
        "No requiere login ni acceso especial — solo que el sitio sea público",
    ],
    agents=[
        "<b>market-content</b> → Calidad del copy, titular, propuesta de valor, prueba social",
        "<b>market-conversion</b> → CTAs, formularios, fricción, experiencia en mobile",
        "<b>market-competitive</b> → Diferenciación vs. competidores del mercado",
        "<b>market-technical</b> → SEO técnico, velocidad, meta tags, alt texts, imágenes",
        "<b>market-strategy</b> → Modelo de negocio, precios, oportunidades de crecimiento",
    ],
    does=[
        "Detecta el tipo de negocio (e-commerce, SaaS, local, agencia, etc.) y ajusta el análisis. "
        "Mapea todas las páginas clave del sitio antes de lanzar los agentes.",
        "Genera un score ponderado en 6 dimensiones con interpretación (A/B/C/D/F). "
        "Clasifica todas las recomendaciones en: Quick Wins (esta semana), "
        "Estratégicas (este mes) e Iniciativas de largo plazo (este trimestre). "
        "Estima el impacto en revenue de cada recomendación.",
    ],
    score_table=dark_table([
        [Paragraph("Dimensión", ST["table_header"]), Paragraph("Peso", ST["table_header"]),
         Paragraph("Score A (85-100)", ST["table_header"])],
        [Paragraph("Contenido y Mensajería", ST["table_cell"]), Paragraph("25%", ST["table_cell"]),
         Paragraph("Copy específico, value prop clara", ST["table_cell"])],
        [Paragraph("Optimización de Conversión", ST["table_cell"]), Paragraph("20%", ST["table_cell"]),
         Paragraph("CTAs fuertes, poco fricción", ST["table_cell"])],
        [Paragraph("SEO y Descubribilidad", ST["table_cell"]), Paragraph("20%", ST["table_cell"]),
         Paragraph("Meta tags, velocidad, mobile", ST["table_cell"])],
        [Paragraph("Posicionamiento Competitivo", ST["table_cell"]), Paragraph("15%", ST["table_cell"]),
         Paragraph("Diferenciación clara vs rivales", ST["table_cell"])],
        [Paragraph("Marca y Confianza", ST["table_cell"]), Paragraph("10%", ST["table_cell"]),
         Paragraph("Consistencia, prueba social", ST["table_cell"])],
        [Paragraph("Crecimiento y Estrategia", ST["table_cell"]), Paragraph("10%", ST["table_cell"]),
         Paragraph("Precios, referidos, retención", ST["table_cell"])],
    ], [75*mm, 25*mm, 100*mm]),
    output_file="MARKETING-AUDIT.md",
    maxipiel_tip="Auditar la tienda de un competidor top en Mercado Libre o tu propia tienda para tener una línea base de mejoras.",
)

story.append(PageBreak())

# ─── 04 QUICK ───────────────────────────────────────────────
story += cmd_section(
    4, "/market quick <url>", "SNAPSHOT · 60 segundos", SUCCESS,
    "Análisis express sin sub-agentes. Ideal para una evaluación rápida antes de decidir "
    "si vale la pena un audit completo. Útil también para comparar múltiples páginas en poco tiempo.",
    needs=["Una URL pública"],
    does=[
        "Evalúa 5 elementos clave: claridad del titular (¿se entiende en 5 segundos?), "
        "fuerza del CTA, propuesta de valor, señales de confianza, y optimización mobile.",
        "El resultado aparece solo en pantalla — máximo 30 líneas con un scorecard rápido, "
        "top 3 fortalezas y top 3 problemas. No genera archivo.",
    ],
    output_file="Solo en pantalla (terminal) — no genera archivo",
    maxipiel_tip="Revisión rápida de páginas de competidores antes de decidir cuál auditar en profundidad.",
)

story.append(PageBreak())

# ─── 05 COPY ────────────────────────────────────────────────
story += cmd_section(
    5, "/market copy <url>", "COPY · Análisis y generación", ACCENT,
    "Analiza el texto de cualquier página y genera alternativas optimizadas con ejemplos "
    "antes/después concretos. Usa fórmulas de copywriting probadas y genera un swipe file completo.",
    needs=[
        "Una URL (ML, Amazon, sitio web propio o de competidor)",
        "También acepta una descripción de producto si no hay URL disponible",
    ],
    does=[
        "Extrae todo el copy existente: H1, subtitular, secciones, botones, meta description. "
        "Detecta el tipo de página y analiza el perfil de voz (formalidad, emoción, complejidad).",
        "Puntúa el copy en 5 dimensiones (0-10 cada una): Claridad, Persuasión, Especificidad, Emoción y Acción. "
        "Genera 10 alternativas de titular usando fórmulas PAS, AIDA, Before-After-Bridge y 4U. "
        "Produce un swipe file con 10 titulares, 5 subtitulares, 5 textos de botón y 3 meta descriptions. "
        "Incluye mínimo 5 pares antes/después con explicación del porqué funciona cada cambio.",
    ],
    extra_blocks=[
        sp(6),
        Paragraph("Fórmulas de copywriting que usa", ST["sub_header"]),
        dark_table([
            [Paragraph("Fórmula", ST["table_header"]), Paragraph("Estructura", ST["table_header"])],
            [Paragraph("PAS", ST["table_cmd"]), Paragraph("Problem → Agitate → Solve", ST["table_cell"])],
            [Paragraph("AIDA", ST["table_cmd"]), Paragraph("Attention → Interest → Desire → Action", ST["table_cell"])],
            [Paragraph("Before-After-Bridge", ST["table_cmd"]), Paragraph("Estado actual → Estado deseado → El producto como puente", ST["table_cell"])],
            [Paragraph("4U", ST["table_cmd"]), Paragraph("Useful + Ultra-specific + Unique + Urgent", ST["table_cell"])],
        ], [30*mm, 130*mm]),
    ],
    output_file="COPY-SUGGESTIONS.md",
    maxipiel_tip="Mejorar copy de listings en ML/Amazon y textos de anuncios de Meta y Google Ads.",
)

story.append(PageBreak())

# ─── 06 EMAILS ──────────────────────────────────────────────
story += cmd_section(
    6, "/market emails <tema o url>", "EMAIL · Secuencias completas", WARNING,
    "Genera secuencias de email completas, listas para pegar en cualquier herramienta "
    "de email marketing. Cada email incluye asunto principal, asunto B para A/B test, "
    "texto de preview, cuerpo completo y CTA.",
    needs=[
        "Un tema: 'tapiceros nuevos', 'seguimiento post-compra', 're-engagement inactivos'",
        "O una URL del negocio para que infiera el contexto automáticamente",
        "Si no especificas el tipo, genera mínimo 2 secuencias diferentes",
    ],
    does=[
        "Selecciona el tipo de secuencia apropiado y genera los emails con timing preciso. "
        "Incluye estrategia de segmentación, plan de A/B testing y benchmarks de la industria.",
    ],
    types_table=dark_table([
        [Paragraph("Tipo", ST["table_header"]), Paragraph("Emails", ST["table_header"]),
         Paragraph("Duración", ST["table_header"]), Paragraph("Objetivo", ST["table_header"])],
        [Paragraph("Bienvenida", ST["table_cell"]), Paragraph("5-7", ST["table_cell"]),
         Paragraph("14 días", ST["table_cell"]), Paragraph("Confianza + presentar producto", ST["table_cell"])],
        [Paragraph("Nurturing", ST["table_cell"]), Paragraph("6-8", ST["table_cell"]),
         Paragraph("~3 semanas", ST["table_cell"]), Paragraph("Educar, romper objeciones", ST["table_cell"])],
        [Paragraph("Lanzamiento", ST["table_cell"]), Paragraph("8-12", ST["table_cell"]),
         Paragraph("1 semana", ST["table_cell"]), Paragraph("Anticipación y ventas", ST["table_cell"])],
        [Paragraph("Re-engagement", ST["table_cell"]), Paragraph("3-4", ST["table_cell"]),
         Paragraph("10 días", ST["table_cell"]), Paragraph("Recuperar inactivos", ST["table_cell"])],
        [Paragraph("Carrito abandonado", ST["table_cell"]), Paragraph("3-4", ST["table_cell"]),
         Paragraph("7 días", ST["table_cell"]), Paragraph("Recuperar ventas perdidas", ST["table_cell"])],
        [Paragraph("Onboarding", ST["table_cell"]), Paragraph("5-7", ST["table_cell"]),
         Paragraph("10 días", ST["table_cell"]), Paragraph("Activar nuevos clientes", ST["table_cell"])],
        [Paragraph("Prospección fría", ST["table_cell"]), Paragraph("3-5", ST["table_cell"]),
         Paragraph("21 días", ST["table_cell"]), Paragraph("Agendar reuniones B2B", ST["table_cell"])],
    ], [40*mm, 22*mm, 30*mm, 108*mm]),
    output_file="EMAIL-SEQUENCES.md",
    maxipiel_tip="Secuencia de nurturing para prospectos de WhatsApp que no cierran, o emails post-compra para fidelizar tapiceros. Conectar con n8n.",
)

story.append(PageBreak())

# ─── 07 SOCIAL ──────────────────────────────────────────────
story += cmd_section(
    7, "/market social <tema o url>", "SOCIAL · Calendario 30 días", SUCCESS,
    "Genera un calendario completo de 30 días de contenido para redes sociales. "
    "Cada post viene listo para publicar: copy completo, descripción del visual, "
    "hashtags por nivel y horario recomendado.",
    needs=[
        "Un tema: 'piel curtida para tapiceros', 'Maxipiel León'",
        "O URL del negocio para que infiera audiencia y voz",
    ],
    does=[
        "Selecciona 2-3 plataformas relevantes (para Maxipiel: Instagram y Facebook principalmente). "
        "Define 5 pilares de contenido con distribución: 40% educativo, 20% behind-the-scenes, "
        "15% prueba social, 15% engagement, 10% promocional.",
        "Por cada día: tipo de contenido, hook de apertura, copy completo, descripción del visual, "
        "hashtags (nicho/mediano/amplio/branded) y horario óptimo. Incluye estrategia de "
        "repurposing 1→10: un contenido convertido en 10 posts diferentes para distintas plataformas.",
    ],
    output_file="SOCIAL-CALENDAR.md",
    maxipiel_tip="30 días de contenido de Instagram/Facebook sobre piel y tapicería generados en minutos, sin tener que pensar qué publicar cada día.",
)

story.append(PageBreak())

# ─── 08 ADS ─────────────────────────────────────────────────
story += cmd_section(
    8, "/market ads <url>", "ADS · Campañas multi-plataforma", ACCENT,
    "Genera campañas publicitarias completas con copy y estructura para Google Ads, "
    "Meta Ads y TikTok. Incluye embudo de retargeting en 3 etapas y recomendaciones "
    "de presupuesto con benchmarks de ROAS.",
    needs=["URL del producto o negocio"],
    does=[
        "<b>Google Ads:</b> 10+ titulares (30 chars c/u) en 7 ángulos distintos, "
        "4 descripciones (90 chars), 10-15 keywords de alta intención por grupo, "
        "lista de keywords negativas, estructura de 3-5 grupos por tema.",
        "<b>Meta Ads:</b> 10 ángulos de copy (dolor, prueba social, antes/después, "
        "objeción, curiosidad, testimonial, comparación, urgencia, cómo hacerlo, directo). "
        "Por ángulo: texto corto + mediano + largo, 5 titulares, 3 descripciones.",
        "<b>TikTok:</b> Script de 30s completo: Hook [0-3s] → Problema [3-10s] → "
        "Solución [10-20s] → Prueba [20-25s] → CTA [25-30s].",
        "<b>Retargeting en 3 etapas:</b> Frío (40% presupuesto, awareness), "
        "Tibio (35%, consideración + casos de estudio), Caliente (25%, conversión + urgencia).",
    ],
    extra_blocks=[
        sp(6),
        Paragraph("Distribución de presupuesto — E-commerce", ST["sub_header"]),
        dark_table([
            [Paragraph("Plataforma", ST["table_header"]), Paragraph("% Recomendado", ST["table_header"]),
             Paragraph("ROAS Bueno", ST["table_header"]), Paragraph("ROAS Excelente", ST["table_header"])],
            [Paragraph("Google Ads", ST["table_cell"]), Paragraph("30%", ST["table_cell"]),
             Paragraph("4:1", ST["table_cell"]), Paragraph("8:1+", ST["table_cell"])],
            [Paragraph("Meta Ads", ST["table_cell"]), Paragraph("40%", ST["table_cell"]),
             Paragraph("4:1", ST["table_cell"]), Paragraph("8:1+", ST["table_cell"])],
            [Paragraph("TikTok", ST["table_cell"]), Paragraph("20%", ST["table_cell"]),
             Paragraph("3:1", ST["table_cell"]), Paragraph("6:1+", ST["table_cell"])],
            [Paragraph("Otros", ST["table_cell"]), Paragraph("10%", ST["table_cell"]),
             Paragraph("—", ST["table_cell"]), Paragraph("—", ST["table_cell"])],
        ], [55*mm, 45*mm, 45*mm, 55*mm]),
    ],
    output_file="AD-CAMPAIGNS.md",
    maxipiel_tip="Genera el copy de tus próximas campañas de Meta y Google Ads enfocado en piel para tapiceros — directo, sin agencia.",
)

story.append(PageBreak())

# ─── 09 FUNNEL ──────────────────────────────────────────────
story += cmd_section(
    9, "/market funnel <url>", "FUNNEL · Análisis de embudo", WARNING,
    "Mapea el camino completo de un visitante desde que llega hasta que compra, "
    "identifica exactamente dónde se pierden los clientes y cuantifica el impacto "
    "económico de cada punto de abandono.",
    needs=[
        "URL con un flujo de compra o contacto (tienda, landing page, formulario)",
    ],
    does=[
        "Detecta el tipo de funnel (e-commerce, lead gen, SaaS, webinar, etc.) y crea un "
        "mapa visual ASCII del recorrido con % de conversión estimado en cada etapa.",
        "Puntúa cada página del funnel en 5 dimensiones (0-10): Claridad, Continuidad, "
        "Motivación, Fricción y Confianza. Calcula el Revenue Per Visitor (RPV) y simula "
        "el impacto económico de cada mejora recomendada.",
        "Prioriza recomendaciones por impacto vs esfuerzo: P1 (esta semana) hasta P5 (cuando haya tiempo). "
        "Mapea secuencias de email apropiadas para cada etapa del funnel.",
    ],
    extra_blocks=[
        sp(6),
        Paragraph("Benchmarks de conversión", ST["sub_header"]),
        dark_table([
            [Paragraph("Tipo de funnel", ST["table_header"]),
             Paragraph("Conversión buena", ST["table_header"]),
             Paragraph("Conversión excelente", ST["table_header"])],
            [Paragraph("Lead gen (formulario)", ST["table_cell"]), Paragraph("3-5%", ST["table_cell"]), Paragraph("10-20%", ST["table_cell"])],
            [Paragraph("E-commerce (visita→compra)", ST["table_cell"]), Paragraph("1-3%", ST["table_cell"]), Paragraph("5-8%", ST["table_cell"])],
            [Paragraph("Carrito → Compra", ST["table_cell"]), Paragraph("50-60%", ST["table_cell"]), Paragraph("70-80%", ST["table_cell"])],
            [Paragraph("Registro de webinar", ST["table_cell"]), Paragraph("20-40%", ST["table_cell"]), Paragraph("55-70%", ST["table_cell"])],
        ], [75*mm, 55*mm, 70*mm]),
    ],
    output_file="FUNNEL-ANALYSIS.md",
    maxipiel_tip="Analizar el flujo de conversación de Sofía para detectar en qué parte del chat se pierden los prospectos y qué mensaje los hace abandonar.",
)

story.append(PageBreak())

# ─── 10 COMPETITORS ─────────────────────────────────────────
story += cmd_section(
    10, "/market competitors <url>", "INTEL · Inteligencia competitiva", ACCENT,
    "Inteligencia competitiva completa. Analiza a tus competidores e identifica qué "
    "copiarles y qué debilidades aprovechar. Incluye SWOT, tácticas robables y "
    "estrategia de diferenciación.",
    needs=[
        "Tu URL propia (para que identifique quiénes son tus competidores automáticamente)",
        "O la URL de un competidor específico que quieras analizar en profundidad",
    ],
    does=[
        "Identifica competidores en 3 niveles: Directos (3-5), Indirectos (2-3) y Aspiracionales (1-2). "
        "Para cada uno analiza: mensajería, precios, features, SEO, redes sociales y reseñas en plataformas externas.",
        "Genera un mapa de posicionamiento visual (precio vs calidad), SWOT individual de cada "
        "competidor y SWOT agregado de tu negocio. Lista de 'tácticas robables' con pasos de "
        "implementación, nivel de esfuerzo e impacto esperado.",
        "Crea plantillas de páginas 'alternativa a [competidor]' para capturar tráfico de alta "
        "intención en buscadores. Incluye 'switching narratives' para atraer clientes que se "
        "quieren ir de la competencia.",
    ],
    output_file="COMPETITOR-REPORT.md",
    maxipiel_tip="Analizar vendedores top de piel en Mercado Libre y Amazon. Descubrir qué les funciona, qué odian sus clientes, y dónde hay huecos sin cubrir.",
)

story.append(PageBreak())

# ─── 11 LANDING ─────────────────────────────────────────────
story += cmd_section(
    11, "/market landing <url>", "CRO · Optimización de landing page", SUCCESS,
    "Análisis CRO (Conversion Rate Optimization) profundo de una landing page específica. "
    "Más enfocado que el audit general — evalúa cada sección con criterios específicos "
    "y genera hipótesis de A/B tests listas para ejecutar.",
    needs=[
        "URL de landing page, página de producto, formulario o página de registro",
    ],
    does=[
        "Evalúa 7 secciones con peso ponderado: Hero (25%), Propuesta de valor (20%), "
        "Prueba social (15%), Features/beneficios (15%), Manejo de objeciones (10%), "
        "CTAs (10%), Footer (5%).",
        "Audita el formulario campo por campo — cada campo extra reduce la conversión ~7%. "
        "Evalúa mobile, estima impacto de velocidad de carga y genera hipótesis de A/B tests. "
        "Incluye predicciones de comportamiento de heatmap sin necesitar datos reales.",
    ],
    extra_blocks=[
        sp(6),
        Paragraph("Benchmarks de conversión por tipo de página", ST["sub_header"]),
        dark_table([
            [Paragraph("Tipo de página", ST["table_header"]),
             Paragraph("Conversión buena", ST["table_header"]),
             Paragraph("Conversión excelente", ST["table_header"])],
            [Paragraph("Captura de lead", ST["table_cell"]), Paragraph("5-10%", ST["table_cell"]), Paragraph("15%+", ST["table_cell"])],
            [Paragraph("Producto e-commerce", ST["table_cell"]), Paragraph("2-4%", ST["table_cell"]), Paragraph("5%+", ST["table_cell"])],
            [Paragraph("Registro de evento/webinar", ST["table_cell"]), Paragraph("20-30%", ST["table_cell"]), Paragraph("40%+", ST["table_cell"])],
            [Paragraph("Consultoría / llamada", ST["table_cell"]), Paragraph("5-10%", ST["table_cell"]), Paragraph("15%+", ST["table_cell"])],
            [Paragraph("Descarga de app", ST["table_cell"]), Paragraph("10-15%", ST["table_cell"]), Paragraph("20%+", ST["table_cell"])],
        ], [80*mm, 55*mm, 65*mm]),
        sp(6),
        highlight_box(
            "Impacto de velocidad de carga: 3s = -20% conversión · 5s = -35% · 8s = -50%+",
            color=SURFACE, icon="⚡"),
    ],
    output_file="LANDING-CRO.md",
    maxipiel_tip="La página donde llegan los clicks de tus anuncios de Google o Meta. Si el ad promete algo y la página no lo refuerza, ahí se pierden las conversiones.",
)

story.append(PageBreak())

# ─── 12 LAUNCH ──────────────────────────────────────────────
story += cmd_section(
    12, "/market launch <descripción>", "LAUNCH · Playbook de lanzamiento", WARNING,
    "Playbook completo de lanzamiento semana a semana para un producto, servicio o "
    "feature nuevo. Incluye emails, posts para redes, coordinación de partners y "
    "dashboard de métricas.",
    needs=[
        "Qué estás lanzando (producto, servicio, feature, promoción)",
        "Audiencia objetivo y tamaño estimado",
        "Fecha de lanzamiento o timeline deseado",
        "Canales disponibles: tamaño de lista de email, seguidores, presupuesto de ads",
        "Precio (si aplica) y si hay clientes actuales para beta testing",
    ],
    does=[
        "<b>Semanas 1-2:</b> Fundación — positioning, landing, analytics, infraestructura.",
        "<b>Semanas 3-4:</b> Construcción de audiencia — contenido, beta testers, outreach.",
        "<b>Semanas 5-6:</b> Intensificación — emails listos, partners briefed, assets finales.",
        "<b>Semana 7 (Lanzamiento):</b> Plan día por día — Lunes soft launch VIPs, Martes anuncio público, "
        "Miércoles push prueba social, Jueves manejo objeciones, Viernes urgencia y cierre.",
        "<b>Semana 8:</b> Post-lanzamiento — encuesta, análisis, transición a precios normales.",
        "Genera 7 emails completos (3 pre-lanzamiento + 4 de lanzamiento), posts para Twitter/LinkedIn/Instagram, "
        "plantilla de press release, swipe copy para partners, y los 10 errores más comunes a evitar.",
    ],
    output_file="LAUNCH-PLAYBOOK.md",
    maxipiel_tip="Lanzamiento de nueva línea de piel, promoción especial de temporada, o nueva versión de Sofía.",
)

story.append(PageBreak())

# ─── 13 PROPOSAL ────────────────────────────────────────────
story += cmd_section(
    13, "/market proposal <cliente>", "PROPOSAL · Propuesta comercial", ACCENT,
    "Genera una propuesta comercial profesional de servicios de marketing lista para "
    "presentar. Si corriste /market audit previamente, usa los datos automáticamente "
    "para una propuesta respaldada por datos.",
    needs=[
        "Nombre del cliente y empresa",
        "Situación de marketing actual y problemas principales",
        "Objetivos (revenue, leads, awareness) y budget si se conoce",
        "Servicios que propones y resultados de auditorías previas (opcionales pero recomendados)",
    ],
    does=[
        "Genera una propuesta de 10 secciones: portada, resumen ejecutivo, análisis de situación, "
        "estrategia en 3 fases (Fundación → Crecimiento → Escala), alcance de trabajo con "
        "entregables específicos, timeline visual, precios en 3 niveles, proyección de ROI, "
        "casos de estudio y próximos pasos.",
        "Aplica psicología de precios: presenta el plan más caro primero (anchoring), "
        "marca el del medio como 'Más popular', y muestra el math de ROI. "
        "Incluye secuencia de seguimiento de 21 días y respuestas a 8 objeciones comunes.",
    ],
    output_file="CLIENT-PROPOSAL.md",
    maxipiel_tip="Propuesta formal para Martín cuando necesites justificar presupuesto de marketing o proponer una nueva estrategia. Se ve como propuesta de agencia.",
)

story.append(PageBreak())

# ─── 14 SEO ─────────────────────────────────────────────────
story += cmd_section(
    14, "/market seo <url>", "SEO · Auditoría técnica y de contenido", SUCCESS,
    "Auditoría completa de SEO técnico y de contenido. Corre automáticamente el "
    "script Python analyze_page.py que extrae meta tags, headings, links, imágenes, "
    "schema, canonical y más.",
    needs=["Una URL pública — el script Python corre automáticamente"],
    does=[
        "<b>On-page SEO:</b> Title tag, meta description, jerarquía H1-H6, alt texts, "
        "links internos/externos y estructura de URL.",
        "<b>E-E-A-T (framework de Google):</b> Experiencia (evidencia directa), Expertise "
        "(credenciales y profundidad), Autoridad (menciones, about page), Confianza (HTTPS, "
        "privacidad, contacto).",
        "<b>Keywords:</b> Identifica keyword primaria, densidad (ideal 1-2%), intención de "
        "búsqueda (informacional/comercial/transaccional/navegacional) y sugiere 5-10 keywords secundarias.",
        "<b>Técnico:</b> Robots.txt, Sitemap.xml, Canonical tags, Core Web Vitals (LCP, FID, CLS), mobile.",
        "<b>Estratégico:</b> Brechas de contenido vs competidores, oportunidades de featured snippets, "
        "schema markup faltante y plan de contenido priorizado por: volumen alto + competencia baja + valor de negocio alto.",
    ],
    output_file="SEO-AUDIT.md",
    maxipiel_tip="Auditar listings de ML y Amazon para mejorar el posicionamiento en búsquedas internas de las plataformas usando las keywords correctas.",
)

story.append(PageBreak())

# ─── 15 BRAND ───────────────────────────────────────────────
story += cmd_section(
    15, "/market brand <url>", "BRAND · Voz y personalidad de marca", ACCENT,
    "Analiza la voz de marca en todos los canales y genera una guía completa de "
    "estilo de comunicación que cualquier redactor puede seguir para escribir "
    "contenido consistente.",
    needs=[
        "URL del negocio (analiza homepage, about, productos, blog y redes si hay links)",
    ],
    does=[
        "Mapea 4 dimensiones de voz (escala 1-10): Formal↔Casual, Serio↔Juguetón, "
        "Técnico↔Simple, Reservado↔Atrevido. Con mapa visual ASCII del espectro.",
        "Identifica el arquetipo de personalidad: La Autoridad (IBM), El Innovador (Tesla), "
        "El Amigo (Mailchimp), El Rebelde (Nike), El Guía (HubSpot).",
        "Genera: vocabulario (palabras que usa / evita / frases características), "
        "tono por contexto (homepage vs email vs error messages), comparación vs competidores, "
        "tabla 'Nuestra voz ES / NO ES', Do's y Don'ts de escritura y 8 ejemplos de copy "
        "en la voz identificada (titular, producto, social, email, botón, error, agradecimiento).",
    ],
    output_file="BRAND-VOICE.md",
    maxipiel_tip="Documenta la voz de Maxipiel para que Sofía (IA de ventas), los anuncios y las redes sociales suenen consistentes. Úsalo como referencia para todo el equipo.",
)

story.append(PageBreak())

# ─── 16 REPORT ──────────────────────────────────────────────
story += cmd_section(
    16, "/market report  ·  /market report-pdf", "REPORT · Reporte compilado completo", WARNING,
    "El compilador del suite. Agrega resultados de todos los análisis anteriores en "
    "un solo reporte profesional con scorecard, deep-dives, comparativa vs competidores, "
    "roadmap 30-60-90 días y estimados de impacto en revenue.",
    needs=[
        "URL del negocio o competidor",
        "Si ya corriste otros comandos antes, los datos se incorporan automáticamente",
        "Si no hay datos previos, hace su propio análisis o te pregunta cómo proceder",
    ],
    does=[
        "Calcula un scorecard en 6 categorías ponderadas. Cada categoría tiene factores "
        "específicos con puntos concretos — no es una evaluación subjetiva.",
        "Por cada categoría: score, qué funciona, qué falla, recomendaciones con impacto en revenue. "
        "Incluye comparación vs competidores (si hay datos de /market competitors), "
        "SEO snapshot checklist visual, action plan con checkboxes y roadmap semanal 30-60-90 días.",
        "<b>/market report-pdf</b> genera el mismo contenido en PDF profesional "
        "listo para presentar (reportlab instalado ✓).",
    ],
    extra_blocks=[
        sp(6),
        Paragraph("Categorías del scorecard", ST["sub_header"]),
        dark_table([
            [Paragraph("Categoría", ST["table_header"]), Paragraph("Peso", ST["table_header"]),
             Paragraph("Factores evaluados", ST["table_header"])],
            [Paragraph("Website y Conversión", ST["table_cell"]), Paragraph("25%", ST["table_cell"]),
             Paragraph("Velocidad, mobile, CTA, prueba social, formularios", ST["table_cell"])],
            [Paragraph("SEO y Orgánico", ST["table_cell"]), Paragraph("20%", ST["table_cell"]),
             Paragraph("Titles, E-E-A-T, técnico, linking, schema", ST["table_cell"])],
            [Paragraph("Contenido y Mensajería", ST["table_cell"]), Paragraph("15%", ST["table_cell"]),
             Paragraph("Voz, calidad, variedad, frecuencia, targeting", ST["table_cell"])],
            [Paragraph("Social Media", ST["table_cell"]), Paragraph("15%", ST["table_cell"]),
             Paragraph("Plataformas, calidad, engagement, consistencia", ST["table_cell"])],
            [Paragraph("Email y Automatización", ST["table_cell"]), Paragraph("15%", ST["table_cell"]),
             Paragraph("Opt-in, diseño, secuencias, segmentación", ST["table_cell"])],
            [Paragraph("Publicidad Pagada", ST["table_cell"]), Paragraph("10%", ST["table_cell"]),
             Paragraph("Estructura, targeting, creative, tracking", ST["table_cell"])],
        ], [65*mm, 22*mm, 113*mm]),
    ],
    output_file="MARKETING-REPORT.md  ·  MARKETING-REPORT.pdf",
    maxipiel_tip="Genera el PDF después de auditar un competidor o la propia tienda y llévalo a la reunión con Martín. Se ve como trabajo de agencia de marketing.",
)

story.append(PageBreak())

# ─── 17 FLUJO RECOMENDADO ───────────────────────────────────
story.append(sp(8))
story.append(SectionDivider(17, "Flujo recomendado para Maxipiel"))
story.append(sp(12))

story.append(Paragraph(
    "Cuando combinas los comandos en secuencia, los siguientes automáticamente incorporan "
    "los datos de los anteriores. Este es el flujo más potente para obtener inteligencia "
    "de marketing completa y accionable:",
    ST["intro"]))

story.append(sp(8))

flow_data = [
    ["Paso", "Comando", "Por qué en este orden"],
    ["1", "/market brand [tu-url]", "Define la voz de Maxipiel primero"],
    ["2", "/market competitors [url-competidor]", "Conoce el mercado y la competencia"],
    ["3", "/market audit [url-competidor]", "Audit profundo del rival más fuerte"],
    ["4", "/market copy [tu-url]", "Mejora tu copy con todo el contexto previo"],
    ["5", "/market ads [tu-url]", "Genera campañas con inteligencia acumulada"],
    ["6", "/market report-pdf [tu-url]", "Reporte final compilado para presentar"],
]

t = Table(flow_data, colWidths=[15*mm, 70*mm, 115*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("TEXTCOLOR", (0,0), (-1,0), white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 8.5),
    ("BACKGROUND", (0,1), (-1,-1), SURFACE),
    ("TEXTCOLOR", (0,1), (-1,-1), TEXT_PRIMARY),
    ("FONTNAME", (0,1), (-1,-1), "Helvetica"),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("TEXTCOLOR", (0,1), (0,-1), ACCENT),
    ("FONTNAME", (1,1), (1,-1), "Courier-Bold"),
    ("TEXTCOLOR", (1,1), (1,-1), SUCCESS),
    ("GRID", (0,0), (-1,-1), 0.3, BORDER),
    ("ROWHEIGHT", (0,0), (-1,-1), 20),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN", (0,0), (0,-1), "CENTER"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1),
     [HexColor("#1E293B"), HexColor("#243044"), HexColor("#1E293B"),
      HexColor("#243044"), HexColor("#1E293B"), HexColor("#243044")]),
]))
story.append(t)

story.append(sp(12))
story.append(highlight_box(
    "Cuando los outputs de un comando (.md) están en el directorio activo, "
    "los comandos siguientes los detectan automáticamente y los incorporan. "
    "No necesitas hacer nada extra — el sistema lo hace solo.",
    color=TAG_BG, icon="⚡"))

story.append(PageBreak())

# ─── 18 LIMITACIONES ────────────────────────────────────────
story.append(sp(8))
story.append(SectionDivider(18, "Limitaciones importantes"))
story.append(sp(12))

lims = [
    ("<b>URLs públicas:</b>",
     "Funciona mejor con sitios completamente accesibles. Mercado Libre y Amazon "
     "a veces limitan el scraping — el análisis puede ser parcial o limitado."),
    ("<b>Scores son orientativos:</b>",
     "Generados por IA, no son métricas absolutas. Úsalos para priorizar acciones, "
     "no para reportar como datos duros a terceros."),
    ("<b>Sin datos internos de competidores:</b>",
     "Solo analiza lo que está visible en su sitio público. No puede acceder a sus "
     "ventas reales, CTR de anuncios, ni métricas internas."),
    ("<b>Directorio activo:</b>",
     "Los archivos .md se guardan donde estés trabajando. Asegúrate de estar en la "
     "carpeta correcta antes de ejecutar los comandos."),
    ("<b>PDF (reportlab):</b>",
     "Ya instalado ✓. Si hay problemas con /market report-pdf, verificar que Python "
     "3.13 sea el intérprete activo del sistema."),
]

for title, desc in lims:
    data = [[Paragraph(title, ST["sub_header"]), Paragraph(desc, ST["body"])]]
    t = Table(data, colWidths=[45*mm, CONTENT_W - 50*mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, BORDER),
    ]))
    story.append(t)

story.append(sp(16))
story.append(DecorLine(color=ACCENT))
story.append(sp(10))
story.append(Paragraph(
    "AI Marketing Suite · Guía Maxipiel · Generado 2026-03-09 · Felix Garcia",
    ST["footer_text"]))
story.append(Paragraph(
    "Repo: github.com/zubair-trabzada/ai-marketing-claude · Instalado en Claude Code",
    ST["footer_text"]))

# ─── BUILD ──────────────────────────────────────────────────
doc.build(story)
print(f"PDF generado: {OUTPUT}")
