# Proyecto — Ventas Amazon Maxipiel

Objetivo: mejorar las ventas en Amazon (cuenta MaxiPiel México).

## Estado

- **2026-06-09:** Análisis inicial de tráfico y conversión por producto (ver `analisis-2026-06-09.md`).
- **Amazon SP-API:** registro de developer EN REVISIÓN (ver `references/sops/seguridad-spapi.md`). Mientras se aprueba, optimización manual de listings.

## Datos crudos

Reportes descargados de Seller Central en `data/`:
- `SalesDashboard-09-06-26.csv` — Panel de ventas (totales)
- `BusinessReport-09-06-26.csv` — Ventas y tráfico por elemento secundario (por ASIN)

## Hallazgos clave (2026-06-09)

1. **Mandil con listados duplicados** — el mismo mandil convierte al 20.93% en la familia de variantes (43 visitas) pero solo al 1.15% en un listado individual que se lleva 262 visitas. Consolidar = mayor oportunidad.
2. **Piel Curtida para Chamarras** — 402 visitas, conversión 0.25% (1 venta). Rehacer listado.
3. **Funda de Asiento** — 428 visitas (la más vista), conversión 1.17%. Optimizar.
4. **Rellenos de boxeo** pierden Buy Box (15kg: 31.6%, 10kg: 25%). Revisar precio.
5. **Campeones:** Zalea de Borrego ($11,685, #1 en ventas) y mandil bueno (20.9% conv). Candidatos para Sponsored Products.

## Pendientes

- [ ] Investigar/consolidar listados duplicados del mandil
- [ ] Rehacer listado "Piel Curtida para Chamarras"
- [ ] Optimizar listado "Funda de Asiento"
- [ ] Revisar precios de rellenos de boxeo (Buy Box)
- [ ] Activar Sponsored Products en Zalea y mandil
- [ ] Revisar por qué solo 7 de 40 listados están activos
