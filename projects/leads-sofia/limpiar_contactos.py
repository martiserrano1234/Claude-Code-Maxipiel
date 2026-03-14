"""
Limpieza y normalización de contactos de Sofía para Meta Ads, Google Ads y n8n.
Convierte los números de WhatsApp al formato E.164 (+52XXXXXXXXXX).

Uso: python limpiar_contactos.py
"""

import csv
import re
import os

INPUT_FILE = "contactos.csv"
OUT_META = "leads_meta.csv"
OUT_GOOGLE = "leads_google.csv"
OUT_WHATSAPP = "leads_whatsapp.csv"
OUT_REPORTE = "reporte_limpieza.txt"


def normalizar_numero(numero_raw):
    """
    Convierte un número de WhatsApp al formato E.164.

    Casos que maneja:
    - 521XXXXXXXXXX  → +52XXXXXXXXXX  (México móvil con "1" de WhatsApp)
    - 52XXXXXXXXXX   → +52XXXXXXXXXX  (México ya sin "1")
    - 1XXXXXXXXXX    → +1XXXXXXXXXX   (EE.UU./Canadá)
    - Otros          → se devuelven tal cual con "+" para revisión

    Retorna: (numero_e164, pais, valido)
    """
    # Quitar todo lo que no sea dígito
    digits = re.sub(r"\D", "", str(numero_raw))

    if not digits:
        return None, "desconocido", False

    # México: empieza con 521 + 10 dígitos = 13 dígitos en total
    # Ej: 5214776460439 → +524776460439
    if digits.startswith("521") and len(digits) == 13:
        normalizado = "+52" + digits[3:]
        return normalizado, "MX", True

    # México: empieza con 52 + 10 dígitos = 12 dígitos
    # Ej: 5214776460 → ya está bien (si tiene 12 dígitos)
    if digits.startswith("52") and len(digits) == 12:
        normalizado = "+" + digits
        return normalizado, "MX", True

    # EE.UU./Canadá: empieza con 1 + 10 dígitos = 11 dígitos
    if digits.startswith("1") and len(digits) == 11:
        normalizado = "+" + digits
        return normalizado, "US", True

    # Colombia: empieza con 57 + 10 dígitos = 12 dígitos
    if digits.startswith("57") and len(digits) == 12:
        normalizado = "+" + digits
        return normalizado, "CO", True

    # Número corto o sin código de país identificable
    if len(digits) <= 10:
        # Asumir México si son 10 dígitos
        if len(digits) == 10:
            normalizado = "+52" + digits
            return normalizado, "MX_asumido", True
        return None, "corto", False

    # Otros: devolver con + para revisión manual
    return "+" + digits, "otro", False


def nombre_limpio(nombre_raw):
    """Limpia el nombre removiendo emojis y caracteres problemáticos."""
    # Quitar emojis y caracteres no ASCII básicos
    nombre = re.sub(r"[^\w\s\.\,\-\@áéíóúÁÉÍÓÚñÑüÜ]", "", str(nombre_raw), flags=re.UNICODE)
    nombre = nombre.strip()
    # Si queda vacío, usar placeholder
    return nombre if nombre else "Cliente"


def es_nombre_util(nombre):
    """Retorna True si el nombre parece un nombre real (no solo símbolos o números)."""
    nombre_clean = re.sub(r"\d", "", nombre).strip()
    return len(nombre_clean) >= 2


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, INPUT_FILE)

    contadores = {
        "total": 0,
        "MX": 0,
        "MX_asumido": 0,
        "US": 0,
        "CO": 0,
        "otro": 0,
        "invalido": 0,
        "duplicados": 0,
    }

    leads_meta = []
    leads_google = []
    leads_whatsapp = []
    numeros_vistos = set()

    with open(input_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            contadores["total"] += 1
            numero_raw = row.get("Numero", "").strip()
            nombre_raw = row.get("Nombre", "").strip()

            numero_e164, pais, valido = normalizar_numero(numero_raw)
            nombre = nombre_limpio(nombre_raw)

            if not valido or not numero_e164:
                contadores["invalido"] += 1
                continue

            # Deduplicar
            if numero_e164 in numeros_vistos:
                contadores["duplicados"] += 1
                continue
            numeros_vistos.add(numero_e164)

            contadores[pais] = contadores.get(pais, 0) + 1

            # Para Meta Ads: solo el número sin "+" (Meta lo acepta así o con +)
            leads_meta.append({"phone": numero_e164})

            # Para Google Ads: E.164 con "+"
            leads_google.append({"Phone Number": numero_e164})

            # Para WhatsApp/n8n: número sin "+" (formato que usa WhatsApp) + nombre
            numero_wa = numero_e164.replace("+", "")
            leads_whatsapp.append({
                "numero": numero_wa,
                "nombre": nombre if es_nombre_util(nombre) else "Cliente",
                "pais": pais,
            })

    # Guardar archivos
    def guardar_csv(filepath, datos, fieldnames):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datos)

    guardar_csv(os.path.join(script_dir, OUT_META), leads_meta, ["phone"])
    guardar_csv(os.path.join(script_dir, OUT_GOOGLE), leads_google, ["Phone Number"])
    guardar_csv(os.path.join(script_dir, OUT_WHATSAPP), leads_whatsapp, ["numero", "nombre", "pais"])

    # Reporte
    reporte = f"""
=== REPORTE DE LIMPIEZA DE CONTACTOS SOFÍA ===

Total de filas en CSV original:  {contadores['total']}
Números inválidos/muy cortos:     {contadores['invalido']}
Duplicados eliminados:            {contadores['duplicados']}

--- Leads válidos por país ---
México (formato 521...):   {contadores.get('MX', 0)}
México (asumido 10 dígitos): {contadores.get('MX_asumido', 0)}
EE.UU. / Canadá:           {contadores.get('US', 0)}
Colombia:                  {contadores.get('CO', 0)}
Otros:                     {contadores.get('otro', 0)}

--- Archivos generados ---
{OUT_META}       → {len(leads_meta)} contactos (para Meta Ads)
{OUT_GOOGLE}     → {len(leads_google)} contactos (para Google Ads Customer Match)
{OUT_WHATSAPP}   → {len(leads_whatsapp)} contactos (para broadcast WhatsApp/n8n)

==============================================
"""
    print(reporte)
    with open(os.path.join(script_dir, OUT_REPORTE), "w", encoding="utf-8") as f:
        f.write(reporte)

    print(f"✅ Archivos guardados en: {script_dir}")


if __name__ == "__main__":
    main()
