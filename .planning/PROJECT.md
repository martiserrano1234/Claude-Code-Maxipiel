# Motor de Comisión Maxipiel

## What This Is

Programa multi-fase para maximizar **clientes nuevos** y **ventas/margen** en los tres canales donde Sebastián percibe comisión: Amazon, ventas directas cerradas por Sofía (Chatwoot/WhatsApp) y la tienda Shopify propia. Maxipiel vende piel/cuero a tapiceros, con entregas locales en León, Gto. y envíos nacionales. El objetivo es un sistema de crecimiento operado sobre las herramientas ya conectadas (Meta Ads, Google Ads, n8n, Shopify Admin API, Amazon SP-API/Ads), no un producto de software nuevo.

## Core Value

Cada fase debe mover, de forma medible, la aguja de la **comisión de Sebastián** — o más clientes nuevos, o más ticket/margen — en Amazon, Sofía o Shopify. Si una acción no impacta uno de esos tres canales, no entra.

## Requirements

### Validated

(Ninguno aún — se validan al ejecutar y medir)

### Active

- [ ] Recuperar el flujo de conversaciones que alimentan a Sofía (cayó ~60% en sep 2026 al desviarse presupuesto a tráfico Shopify sin chats)
- [ ] Atraer clientes de venta grande / mayoreo (campaña Meta específica de "proyecto/volumen" que auto-filtra al comprador chico)
- [ ] Subir el margen de Amazon por encima de $30k/mes (base del bono de Sebastián), optimizando ACOS de Amazon Ads y mezcla de productos
- [ ] Convertir mejor el tráfico de Shopify (recuperación de carrito, ticket promedio, recompra) sin quemar presupuesto en visitas que no cierran
- [ ] Medir de punta a punta: clic-a-WhatsApp como conversión (Google Ads) y atribución por canal para saber qué campaña trae qué comisión
- [ ] Reactivar clientes que ya compraron y dejaron de comprar (recompra dirigida por canal)

### Out of Scope

- **Mercado Libre como foco de crecimiento** — no genera comisión para Sebastián; se mantiene operando pero no recibe esfuerzo del roadmap (puede alimentar otros canales de forma oportunista)
- **Modificar el flujo de Sofía en n8n** — se rompe; Felix la actualiza a mano. Solo se permiten mejoras de mensajería, targeting y campañas que la alimenten, nunca el flujo interno
- **Construir un producto/plataforma de software nuevo** — este programa opera sobre las herramientas existentes

## Context

- **Negocio:** venta de piel/cuero a tapiceros; entregas en León Gto + envíos nacionales por paquetería.
- **Canales de venta:** Amazon, Mercado Libre, ventas directas (Sofía vía Chatwoot/WhatsApp), tienda Shopify propia (piel + mandiles).
- **Herramientas conectadas (API/MCP):** Meta Ads (act_10152548466947929), Google Ads (6619664178), n8n, Shopify Admin API, Amazon SP-API (en revisión) y Amazon Ads (~$2,000/mes, 6 campañas AUTO).
- **Hallazgo reciente (sep 2026):** la campaña de Mensajes que alimenta a Sofía pasó de ~314 a ~123 conversaciones/quincena tras desviarse presupuesto a una campaña de tráfico a Shopify que generó 0 chats. Recuperar ese flujo es la palanca más rápida.
- **Comisión de Sebastián:** bono documentado = 10% del margen de Amazon arriba de $30k/mes (corte mensual día 28); además percibe comisión sobre ventas directas (Sofía) y tienda Shopify.
- **El "código" de este proyecto** son automatizaciones (n8n), scripts de campañas (PowerShell/API), contenido y configuración de anuncios — no una app.

## Constraints

- **Restricción dura**: NO tocar el flujo de Sofía en n8n — se rompe; Felix la edita a mano.
- **Foco de comisión**: priorizar Amazon (margen), Sofía (ventas directas) y Shopify. Mercado Libre fuera de foco.
- **Presupuesto**: los cambios de gasto en anuncios los aprueba Martín (jefe). Diseñar y proponer antes de gastar.
- **Idioma/tono**: español, casual de colega en lo interno; amigable y vendedor en lo externo (dirigido a tapiceros).
- **Norte doble**: balancear cantidad de clientes nuevos con tamaño/margen del ticket.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Enfocar el roadmap solo en Amazon, Sofía y Shopify | Son los canales donde Sebastián cobra comisión | — Pending |
| Dejar Mercado Libre fuera de foco | No genera comisión | — Pending |
| Saltar la investigación de dominio de 4 agentes de GSD | Está diseñada para software; tenemos el contexto de negocio ya | — Pending |
| Granularidad "coarse" (fases amplias) | Es un plan de estrategia de crecimiento, no de código fino | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-09-10 after initialization*
