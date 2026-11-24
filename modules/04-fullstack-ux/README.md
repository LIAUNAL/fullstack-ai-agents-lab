# Módulo 4: Full-Stack & UX Agéntica (Next.js + SSE + HITL)

## Objetivo
Construir una interfaz web en **Next.js (App Router + TypeScript + Tailwind CSS)** preparada para agentes en producción:
- Consumo de **Server-Sent Events (SSE)** desde `POST http://localhost:8000/chat/stream`.
- Diferenciación visual entre **estado de pensamiento / herramientas** y **respuesta final**.
- **Human-in-the-Loop (HITL)** mediante `ApprovalCard.tsx` para aprobar o rechazar acciones sensibles.

## Ejecución Local
```bash
cd modules/04-fullstack-ux
pnpm install   # o npm install
pnpm dev       # http://localhost:3000
```
