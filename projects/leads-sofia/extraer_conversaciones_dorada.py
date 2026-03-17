"""
Extrae mensajes de clientes de la Lista Dorada desde Chatwoot.
Busca cada número, obtiene sus conversaciones y guarda los mensajes entrantes.
Output: conversaciones_dorada.json
"""

import csv
import json
import time
import requests

CHATWOOT_URL = "https://chatwoot-production-77a5.up.railway.app"
ACCOUNT_ID = 2
TOKEN = "tDNe9Ugf3Ahtw2v3VhxSe1G3"
HEADERS = {"api_access_token": TOKEN}

def normalizar_telefono(tel):
    """Limpia el número: solo dígitos, quita +, espacios, guiones."""
    tel = str(tel).strip().replace("+", "").replace("-", "").replace(" ", "")
    # Si empieza con 521 y tiene 13 dígitos, quitar el 1
    if tel.startswith("521") and len(tel) == 13:
        tel = "52" + tel[3:]
    return tel

def buscar_contacto(telefono):
    """Busca un contacto en Chatwoot por número de teléfono.
    Prueba varias variantes: +521XXXXXXXX, +52XXXXXXXX, solo los 10 dígitos.
    """
    ultimos10 = telefono[-10:]
    variantes = [
        f"+521{ultimos10}",
        f"+52{ultimos10}",
        ultimos10,
        telefono,
    ]
    for variante in variantes:
        try:
            r = requests.get(
                f"{CHATWOOT_URL}/api/v1/accounts/{ACCOUNT_ID}/contacts/search",
                headers=HEADERS,
                params={"q": variante, "page": 1},
                timeout=10
            )
            data = r.json()
            contactos = data.get("payload", [])
            # Coincidencia por últimos 10 dígitos
            for c in contactos:
                phone = str(c.get("phone_number", "")).replace("+", "").replace("-", "").replace(" ", "")
                if phone[-10:] == ultimos10:
                    return c
            time.sleep(0.1)
        except Exception as e:
            print(f"  ERROR buscando {variante}: {e}")
    return None

def obtener_conversaciones(contact_id):
    """Obtiene todas las conversaciones de un contacto (con mensajes incluidos)."""
    try:
        r = requests.get(
            f"{CHATWOOT_URL}/api/v1/accounts/{ACCOUNT_ID}/contacts/{contact_id}/conversations",
            headers=HEADERS,
            timeout=10
        )
        data = r.json()
        payload = data.get("payload", [])
        # payload es una lista de conversaciones
        if isinstance(payload, list):
            return payload
        # Por si acaso viene como dict con 'conversations'
        if isinstance(payload, dict):
            return payload.get("conversations", [])
        return []
    except Exception as e:
        print(f"  ERROR obteniendo conversaciones: {e}")
        return []

def main():
    resultados = []

    with open("Lista dorada clientes - Hoja 1.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        clientes = list(reader)

    print(f"Total clientes en lista dorada: {len(clientes)}")
    print("=" * 60)

    for cliente in clientes:
        telefono_raw = cliente.get("Telefono", "").strip()
        nombre = cliente.get("Nombre", "sin nombre").strip()
        empresa = cliente.get("Empresa", "").strip()

        if not telefono_raw:
            continue

        telefono = normalizar_telefono(telefono_raw)
        print(f"\nBuscando: {nombre} ({telefono_raw} -> {telefono})")

        contacto = buscar_contacto(telefono)
        if not contacto:
            print(f"  NO encontrado en Chatwoot")
            resultados.append({
                "telefono": telefono_raw,
                "nombre": nombre,
                "empresa": empresa,
                "encontrado": False,
                "conversaciones": []
            })
            time.sleep(0.3)
            continue

        contact_id = contacto["id"]
        print(f"  OK Encontrado - ID: {contact_id}")

        conversaciones = obtener_conversaciones(contact_id)
        print(f"  Conversaciones: {len(conversaciones)}")

        convs_data = []
        for conv in conversaciones:
            conv_id = conv["id"]
            # Usar endpoint /messages para obtener el historial completo
            try:
                r_msgs = requests.get(
                    f"{CHATWOOT_URL}/api/v1/accounts/{ACCOUNT_ID}/conversations/{conv_id}/messages",
                    headers=HEADERS,
                    timeout=10
                )
                mensajes = r_msgs.json().get("payload", [])
            except Exception as e:
                print(f"    ERROR mensajes conv {conv_id}: {e}")
                mensajes = []

            # Solo mensajes entrantes del cliente (message_type == 0) con contenido
            mensajes_cliente = [
                m.get("content", "")
                for m in mensajes
                if m.get("message_type") == 0 and m.get("content")
            ]

            if mensajes_cliente:
                convs_data.append({
                    "conv_id": conv_id,
                    "mensajes_cliente": mensajes_cliente
                })
                print(f"    Conv {conv_id}: {len(mensajes_cliente)} mensajes del cliente")

            time.sleep(0.2)

        resultados.append({
            "telefono": telefono_raw,
            "nombre": nombre,
            "empresa": empresa,
            "encontrado": True,
            "contact_id": contact_id,
            "conversaciones": convs_data
        })

        time.sleep(0.3)

    # Guardar JSON completo
    with open("conversaciones_dorada.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    # Resumen
    encontrados = [r for r in resultados if r["encontrado"]]
    con_mensajes = [r for r in encontrados if any(c["mensajes_cliente"] for c in r["conversaciones"])]

    print("\n" + "=" * 60)
    print(f"Encontrados en Chatwoot: {len(encontrados)}/{len(resultados)}")
    print(f"Con mensajes extraidos: {len(con_mensajes)}")
    print(f"Guardado en: conversaciones_dorada.json")

if __name__ == "__main__":
    main()
