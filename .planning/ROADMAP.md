# Roadmap: Motor de Comisión Maxipiel

## Overview

Programa de crecimiento en cinco fases que mueve la comisión de Sebastián en los canales que la generan (Sofía/ventas directas, Amazon y Shopify), usando Google Ads como fuente de demanda que alimenta dos de ellos. Arrancamos con la palanca más rápida y el fundamento de medición: recuperar el flujo de conversaciones hacia Sofía y dejar el clic-a-WhatsApp como conversión confiable en Google Ads ("primero medir"). Con la medición lista, escalamos Google Ads — la mina de oro — porque Google → WhatsApp → Sofía y Google → Shopify son rutas directas a comisión ("luego escalar"). Después exprimimos margen y ticket en Amazon y Shopify, reactivamos a los clientes que ya compraron, y cerramos con el tablero de atribución que dice qué campaña trae qué comisión. Todo opera sobre las herramientas ya conectadas (Meta Ads, Google Ads, n8n, Shopify Admin API, Amazon Ads). Mercado Libre queda fuera de foco, nunca se toca el flujo interno de Sofía en n8n, y todo cambio de gasto en anuncios se propone a Martín antes de gastar.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Recuperar el flujo hacia Sofía y medir el clic-a-WhatsApp** - Restaurar las conversaciones perdidas, sumar una campaña de mayoreo y dejar el clic-a-WhatsApp como conversión confiable (fundamento para escalar)
- [ ] **Phase 2: Google Ads, la mina de oro** - Escalar Search (clic-a-WhatsApp → Sofía) y llevar tráfico calificado a Shopify con Shopping/PMax
- [ ] **Phase 3: Subir margen y ticket en Amazon y Shopify** - Optimizar ACOS, mezcla de producto y conversión/ticket en las dos tiendas
- [ ] **Phase 4: Reactivar clientes que dejaron de comprar** - Recompra dirigida a clientes inactivos de Sofía y Shopify
- [ ] **Phase 5: Atribuir la comisión por canal** - Tablero que muestra qué campaña trae qué venta y qué comisión

## Phase Details

### Phase 1: Recuperar el flujo hacia Sofía y medir el clic-a-WhatsApp
**Goal**: Devolver a Sofía el volumen de conversaciones que perdió en sep 2026, empezar a traerle compradores de volumen, y dejar el clic-a-WhatsApp como conversión sólida en Google Ads — el fundamento para escalar con datos. Sin tocar el flujo de n8n.
**Depends on**: Nothing (first phase)
**Requirements**: SOFIA-01, SOFIA-02, MEAS-01
**Success Criteria** (what must be TRUE):
  1. Las conversaciones que llegan a Sofía vuelven a ~300/quincena (recuperando la caída de ~123), con propuesta de reasignación de presupuesto de la campaña de Mensajes aprobada por Martín antes de gastar
  2. Hay una campaña Meta de "proyecto/mayoreo" activa dirigida a Mensajes que auto-filtra al comprador chico y le manda conversaciones identificables a Sofía, sin cambios en su flujo interno de n8n
  3. El clic-a-WhatsApp queda como conversión medible y confiable en Google Ads (los 2 pasos pendientes del disparador instalado el 2026-08-05 quedan cerrados)
  4. Se puede leer en Google Ads cuántos clic-a-WhatsApp genera cada campaña, dejando lista la base para escalar la inversión con datos
**Plans**: 01-A (MEAS-01, wave 1), 01-B (SOFIA-01, wave 1), 01-C (SOFIA-02, wave 2)

### Phase 2: Google Ads, la mina de oro
**Goal**: Exprimir Google Ads como fuente de demanda hacia los dos canales que pagan comisión: escalar Search que manda clic-a-WhatsApp a Sofía y llevar tráfico calificado a la tienda Shopify con Shopping/Performance Max — apoyándose en la conversión ya medible de la Phase 1.
**Depends on**: Phase 1 (necesita el clic-a-WhatsApp medible para escalar con datos)
**Requirements**: GADS-01, GADS-02
**Success Criteria** (what must be TRUE):
  1. Las campañas de Search que mandan clic-a-WhatsApp escalan con presupuesto propuesto y aprobado por Martín: suben los términos que cierran y se pausan los que no
  2. Sofía recibe más conversaciones atribuibles a Google Ads, medibles vía la conversión de clic-a-WhatsApp de la Phase 1
  3. Existe al menos una campaña de Google (Shopping o Performance Max) activa que lleva tráfico calificado a la tienda Shopify
  4. Se puede leer el costo por clic-a-WhatsApp y el tráfico a Shopify por campaña para decidir dónde meter más presupuesto
**Plans**: TBD

### Phase 3: Subir margen y ticket en Amazon y Shopify
**Goal**: Sacar más margen y más ticket de los dos canales de tienda: bajar ACOS y mejorar mezcla en Amazon, y convertir mejor + subir el ticket en Shopify sin quemar presupuesto.
**Depends on**: Phase 2
**Requirements**: AMZN-01, AMZN-02, SHOP-01, SHOP-02
**Success Criteria** (what must be TRUE):
  1. El margen mensual de Amazon supera los $30k (base del bono de Sebastián) con ACOS bajo control en las 6 campañas AUTO
  2. La mezcla de Amazon empuja productos de mayor margen y/o bundles, no solo el producto ancla
  3. La tasa de conversión del tráfico de Shopify sube y se deja de pagar por visitas que no cierran
  4. El ticket promedio de Shopify sube vía bundles o precio por volumen ("lleva más piel")
**Plans**: TBD
**UI hint**: yes

### Phase 4: Reactivar clientes que dejaron de comprar
**Goal**: Traer de vuelta ingresos que ya existían: clientes que compraron una vez y no volvieron, con recompra dirigida por canal.
**Depends on**: Phase 3
**Requirements**: SOFIA-03, SHOP-03
**Success Criteria** (what must be TRUE):
  1. Existe un segmento identificado de clientes inactivos de Sofía y de Shopify (compraron y no volvieron)
  2. Se envía mensajería de reactivación por WhatsApp a inactivos de Sofía y genera nuevas conversaciones/ventas, sin tocar el flujo interno de n8n
  3. Se activa recompra dirigida a clientes existentes de Shopify (email/anuncio/mensaje) que produce pedidos repetidos medibles
**Plans**: TBD

### Phase 5: Atribuir la comisión por canal
**Goal**: Saber, con números confiables, qué campaña trae qué venta y qué comisión, para decidir dónde invertir — cerrando el ciclo de medición que arrancó en la Phase 1.
**Depends on**: Phase 4
**Requirements**: MEAS-02
**Success Criteria** (what must be TRUE):
  1. Existe un tablero de atribución que muestra ventas/comisión por canal (Amazon, Sofía, Shopify)
  2. Se puede leer qué campaña específica (Google Ads, Meta, etc.) aporta a la comisión de Sebastián
  3. El tablero sirve para decidir dónde subir o bajar presupuesto, con la propuesta de gasto aprobada por Martín antes de mover dinero
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Recuperar el flujo hacia Sofía y medir el clic-a-WhatsApp | 0/TBD | Not started | - |
| 2. Google Ads, la mina de oro | 0/TBD | Not started | - |
| 3. Subir margen y ticket en Amazon y Shopify | 0/TBD | Not started | - |
| 4. Reactivar clientes que dejaron de comprar | 0/TBD | Not started | - |
| 5. Atribuir la comisión por canal | 0/TBD | Not started | - |
