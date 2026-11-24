# Arquitectura del Proyecto Integrador (Capstone - Semana 12)

> Plantilla de diseño arquitectónico para el sistema End-to-End. Completa cada sección antes de escribir código en producción.

## 1. Contexto del Sistema
- **Problema a resolver:** *(Describe el flujo de negocio, usuarios objetivo y SLA esperado).*
- **Autonomía acotada:** *(Define qué acciones puede ejecutar el agente de forma autónoma y cuáles requieren aprobación Human-in-the-Loop).*
- **Actores y sistemas externos:** *(Usuario final, APIs internas, servidores MCP, proveedores LLM).*

## 2. Diagrama de Contenedores
```text
[Next.js Web UI (SSE + HITL)]
          |
          v  (HTTP/SSE)
[FastAPI + LangGraph Backend] ---> [MCP Servers (Tools)]
          |             |
          v             v
[LiteLLM Gateway]   [PostgreSQL + pgvector (Checkpoints & RAG)]
     |      |
     v      v
[vLLM/Ollama] [Cloud LLM Fallback]
          |
          v
[Langfuse (Traces & Scores)]
```

## 3. Componentes Internos (Arquitectura Hexagonal)
- **Domain (`domain/`):** Entidades inmutables, invariantes de negocio y contratos Pydantic v2.
- **Ports (`ports/`):** Interfaces `Protocol` para LLM, memoria vectorial, herramientas MCP y repositorio de estado.
- **Application (`application/`):** Casos de uso y grafo LangGraph con nodos deterministas e interrupciones HITL.
- **Adapters (`adapters/`):** Implementaciones concretas (LiteLLM, PostgresSaver, FastAPI SSE, MCP Client).

## 4. Contratos de Datos y Streaming
- **Entrada (`POST /chat/stream`):** `thread_id`, `user_id`, `message`, `metadata`.
- **Eventos SSE:**
  - `status`: progreso de nodos (`planning`, `tool_call`, `waiting_approval`).
  - `approval_required`: payload de acción sensible para confirmación del usuario.
  - `token`: fragmento incremental de respuesta.
  - `done` / `error`: cierre de stream con `trace_id` de Langfuse.

## 5. Estrategia de Evaluación y AgentOps
- **Pruebas unitarias deterministas:** Cobertura del dominio y casos de uso con mocks (`pytest`).
- **Regresión de prompts y formatos:** Dataset dorado en `promptfooconfig.yaml` ejecutado en CI/CD.
- **Métricas en producción (Langfuse):** Latencia p95, costo por conversación, tasa de fallback y tasa de aprobación HITL.
