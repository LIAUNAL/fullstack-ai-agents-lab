# Capstone TODO & Criterios de Aceptación (Semana 12)

## Infraestructura y SDLC
- [ ] `.env` configurado a partir de `.env.example` sin credenciales en Git.
- [ ] `make infra-up` levanta `postgres` (pgvector), `redis`, `litellm` y `langfuse` en estado `healthy`.
- [ ] Pipeline CI (`agent-ci.yml`) en verde: `docker compose config --quiet`, `ruff check .`, `pyright` y `pytest`.

## Backend, Inferencia y Arquitectura
- [ ] Dominio desacoplado de frameworks mediante puertos (`Protocol`) y contratos Pydantic v2.
- [ ] Enrutamiento híbrido en LiteLLM: modelo local primario (`vLLM` / `Ollama`) con fallback automático a cloud.
- [ ] Servidor MCP exponiendo al menos 2 herramientas seguras con validación de parámetros.
- [ ] Grafo LangGraph persistiendo estado por `thread_id` en PostgreSQL y soportando interrupción HITL.
- [ ] Endpoint `POST /chat/stream` emitiendo eventos SSE tipados.

## Frontend Full-Stack y UX Agéntica
- [ ] Interfaz Next.js consumiendo el stream SSE en tiempo real.
- [ ] Diferenciación visual entre estado de pensamiento/herramientas y respuesta final.
- [ ] Tarjeta de aprobación Human-in-the-Loop funcional (`Aprobar` / `Rechazar`) que reanuda el grafo.

## Observabilidad y Evaluación (AgentOps)
- [ ] Trazas completas en Langfuse (spans por nodo, herramienta y llamada LLM).
- [ ] Suite de regresión en Promptfoo con mínimo 10 casos dorados y aserciones de esquema JSON.
- [ ] Documentación final completada en `capstone/ARCHITECTURE.md`.
