# Automatización de Preguntas y Respuestas — Mercado Libre

## Objetivo

Automatizar las respuestas a preguntas de clientes en Mercado Libre usando n8n + Claude AI, para que el vendedor no tenga que responder manualmente.

## Estado

**En construcción** — credenciales conectadas, workflow pendiente de armar.

## Contexto

- Los clientes hacen preguntas en las publicaciones de ML antes de comprar
- Actualmente Martín o alguien del equipo responde manualmente
- La API de ML permite leer preguntas sin responder y publicar respuestas

## Flujo planeado

```
Schedule Trigger (cada 15 min)
  → HTTP Request: GET preguntas sin responder (/questions/search?status=UNANSWERED)
  → IF: ¿hay preguntas?
      → HTTP Request: enviar pregunta a Claude
      → HTTP Request: POST respuesta en ML (/answers)
```

## Credenciales configuradas

- **App ML:** creada en developers.mercadolibre.com bajo la cuenta de Martín
- **Credencial n8n:** "mercado libre" — OAuth2 API, conectada y funcional
- **n8n URL:** https://primary-production-dc7a.up.railway.app/

> ⚠️ El client_id y client_secret NO se guardan aquí — están en n8n.

## Endpoints clave

```
# Preguntas sin responder
GET https://api.mercadolibre.com/questions/search?seller_id={ID}&status=UNANSWERED

# Responder pregunta
POST https://api.mercadolibre.com/answers
{ "question_id": 123456, "text": "Tu respuesta aquí" }
```

## Próximo paso

Construir el workflow en n8n con los nodos:
1. Schedule Trigger
2. HTTP Request (obtener preguntas)
3. IF (filtrar si hay preguntas)
4. Claude AI (generar respuesta)
5. HTTP Request (publicar respuesta en ML)
