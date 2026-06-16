# SOP — Seguridad para Amazon SP-API

_Creado: 2026-06-09_

Este documento respalda los compromisos de seguridad que se marcaron como "Sí" en el registro de developer de Amazon (Data Protection Policy). **Hay que cumplirlos de verdad** — no son trámite, son obligación al manejar datos de la API de Amazon.

## Contexto

- Cuenta de seller: **MaxiPiel** (México)
- Registro de developer: **Desarrollador privado** (uso interno, sin PII)
- Correo del developer / casos de Amazon: `Maxipielmercadotecnia@gmail.com`
- Permisos solicitados: Listing de producto, Precios, Información del colaborador comercial, Finanzas y contabilidad, Seguimiento de pedidos e inventario (todos **sin PII**)

## Checklist de seguridad (cumplir antes de operar)

- [ ] **MFA activado** en la cuenta de Amazon Seller Central
- [ ] **MFA activado** en n8n (donde vivirán las credenciales)
- [ ] **Contraseñas fuertes** (mínimo 12 caracteres, con símbolos) en ambas cuentas
- [ ] **Antivirus + firewall activos** en la máquina que opera (Windows Defender basta)
- [ ] **Credenciales cifradas** — NUNCA en texto plano en el repo git
- [ ] Rotación de credenciales al menos **una vez al año**

## ⚠️ Regla de oro: credenciales fuera del repo

El `LWA Client Secret` y el `Refresh Token` **JAMÁS** se guardan en este repositorio git ni en ningún archivo en texto plano. Van:

1. En las **credenciales cifradas de n8n**, o
2. En **variables de entorno** del servidor

Si por error se suben al repo, se consideran comprometidas → revocar y regenerar de inmediato.

## Plan de respuesta a incidentes (mínimo viable)

Amazon exige un plan con revisiones cada 6 meses y notificación en 24h. El nuestro:

1. **Detección:** si se sospecha que una credencial (Refresh Token / Secret) se filtró o hubo acceso no autorizado.
2. **Contención inmediata:** revocar la autorización en Seller Central → Develop Apps, y regenerar credenciales.
3. **Notificación:** avisar a `security@amazon.com` dentro de las **24 horas** posteriores a la detección.
4. **Responsables:** Felix (técnico) y Sebastián (supervisor). Escalar a Martín si hay impacto en la operación.
5. **Revisión:** revisar este plan cada **6 meses** (próxima: 2026-12-09).

## Estado del registro

- 2026-06-09: Perfil de developer enviado → **en revisión por Amazon**. Pendiente de aprobación para poder crear el "cliente de aplicación" y obtener credenciales.
