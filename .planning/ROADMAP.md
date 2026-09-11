# Roadmap: Motor de Comisión Maxipiel

## Overview

Programa de crecimiento en cuatro fases que mueve la comisión de Sebastián en los tres canales que la generan (Sofía/ventas directas, Amazon y Shopify). Arrancamos recuperando y ampliando el flujo de conversaciones que alimentan a Sofía — la palanca más rápida —, luego exprimimos margen y ticket en Amazon y Shopify, después reactivamos a los clientes que ya compraron, y cerramos dejando la medición y atribución por canal para saber qué campaña trae qué comisión. Todo opera sobre las herramientas ya conectadas (Meta Ads, Google Ads, n8n, Shopify Admin API, Amazon Ads). Mercado Libre queda fuera de foco y nunca se toca el flujo interno de Sofía en n8n.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Recuperar y ampliar el flujo hacia Sofía** - Restaurar las conversaciones perdidas y sumar una campaña de mayoreo que alimente a Sofía
- [ ] **Phase 2: Subir margen y ticket en Amazon y Shopify** - Optimizar ACOS, mezcla de producto y conversión/ticket en las dos tiendas
- [ ] **Phase 3: Reactivar clientes que dejaron de comprar** - Recompra dirigida a clientes inactivos de Sofía y Shopify
- [ ] **Phase 4: Medir y atribuir la comisión por canal** - Clic-a-WhatsApp como conversión confiable y tablero de atribución

## Phase Details

### Phase 1: Recuperar y ampliar el flujo hacia Sofía
**Goal**: Devolver a Sofía el volumen de conversaciones que perdió en sep 2026 y, además, empezar a traerle compradores de volumen — todo desde la campaña de Mensajes, sin tocar el flujo de n8n.
**Depends on**: Nothing (first phase)
**Requirements**: SOFIA-01, SOFIA-02
**Success Criteria** (what must be TRUE):
  1. Las conversaciones que llegan a Sofía vuelven a ~300/quincena (recuperando la caída de ~123)
  2. Existe una propuesta de reasignación de presupuesto de la campaña de Mensajes aprobada por Martín antes de gastar
  3. Hay una campaña Meta de "proyecto/mayoreo" activa dirigida a Mensajes que auto-filtra al comprador chico
  4. Sofía recibe conversaciones de compradores de volumen identificables (proyecto/mayoreo), sin cambios en su flujo interno de n8n
**Plans**: TBD

### Phase 2: Subir margen y ticket en Amazon y Shopify
**Goal**: Sacar más margen y más ticket de los dos canales de tienda: bajar ACOS y mejorar mezcla en Amazon, y convertir mejor + subir el ticket en Shopify sin quemar presupuesto.
**Depends on**: Phase 1
**Requirements**: AMZN-01, AMZN-02, SHOP-01, SHOP-02
**Success Criteria** (what must be TRUE):
  1. El margen mensual de Amazon supera los $30k (base del bono de Sebastián) con ACOS bajo control en las 6 campañas AUTO
  2. La mezcla de Amazon empuja productos de mayor margen y/o bundles, no solo el producto ancla
  3. La tasa de conversión del tráfico de Shopify sube y se deja de pagar por visitas que no cierran
  4. El ticket promedio de Shopify sube vía bundles o precio por volumen ("lleva más piel")
**Plans**: TBD
**UI hint**: yes

### Phase 3: Reactivar clientes que dejaron de comprar
**Goal**: Traer de vuelta ingresos que ya existían: clientes que compraron una vez y no volvieron, con recompra dirigida por canal.
**Depends on**: Phase 2
**Requirements**: SOFIA-03, SHOP-03
**Success Criteria** (what must be TRUE):
  1. Existe un segmento identificado de clientes inactivos de Sofía y de Shopify (compraron y no volvieron)
  2. Se envía mensajería de reactivación por WhatsApp a inactivos de Sofía y genera nuevas conversaciones/ventas
  3. Se activa recompra dirigida a clientes existentes de Shopify (email/anuncio/mensaje) que produce pedidos repetidos medibles
**Plans**: TBD

### Phase 4: Medir y atribuir la comisión por canal
**Goal**: Saber, con números confiables, qué campaña trae qué venta y qué comisión — empezando por dejar el clic-a-WhatsApp como conversión sólida.
**Depends on**: Phase 3
**Requirements**: MEAS-01, MEAS-02
**Success Criteria** (what must be TRUE):
  1. El clic-a-WhatsApp queda como conversión medible y confiable en Google Ads (los 2 pasos pendientes cerrados)
  2. Existe un tablero de atribución que muestra ventas/comisión por canal (Amazon, Sofía, Shopify)
  3. Se puede leer qué campaña específica aporta a la comisión de Sebastián para decidir dónde invertir
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Recuperar y ampliar el flujo hacia Sofía | 0/TBD | Not started | - |
| 2. Subir margen y ticket en Amazon y Shopify | 0/TBD | Not started | - |
| 3. Reactivar clientes que dejaron de comprar | 0/TBD | Not started | - |
| 4. Medir y atribuir la comisión por canal | 0/TBD | Not started | - |
