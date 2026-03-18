# Decision Log

Append-only. When a meaningful decision is made, log it here.

Format: [YYYY-MM-DD] DECISION: ... | REASONING: ... | CONTEXT: ...

---

[2026-03-18] DECISION: Conectar API de Mercado Libre a n8n vía OAuth2 | REASONING: Automatizar respuestas a preguntas de clientes en ML para reducir carga manual del equipo | CONTEXT: App creada en developers.mercadolibre.com bajo cuenta de Martín. Credencial OAuth2 "mercado libre" guardada en n8n (Railway). Permisos: Comunicaciones pre y post ventas (lectura y escritura). Workflow de Q&A automático pendiente de construir.

[2026-03-06] DECISION: Configurar MCPs de Google Ads, Meta Ads y n8n en Claude Code | REASONING: Centralizar el acceso a las herramientas de publicidad y automatización desde Claude Code para optimizar campañas sin salir del asistente | CONTEXT: MCPs agregados en `C:\Users\danie\.claude.json`. Google Ads → cuenta Maxipiel ID 6619664178 (bajo manager 4020002227). Meta Ads → cuenta Maxi Piel ID act_10152548466947929. n8n → instancia Railway. El token de Meta expira periódicamente y debe renovarse manualmente.
