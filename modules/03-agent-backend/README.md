# Módulo 3: Backend Agéntico con Estado y Protocolo MCP

## Objetivo
Construir un backend asíncrono en producción con **FastAPI**, grafos de estado con **LangGraph** (persistencia por `thread_id` e interrupción Human-in-the-Loop) y herramientas estandarizadas mediante **Model Context Protocol (MCP)**.

## Archivos
- `mcp_server.py`: Servidor MCP oficial (`FastMCP`) con herramientas seguras de solo lectura.
- `graph.py`: Grafo LangGraph (`plan` -> `execute_tools` / `await_approval` -> `respond`) con checkpointer.
- `main.py`: API FastAPI asíncrona con endpoint SSE `POST /chat/stream`.
- `tests/test_agent_backend.py`: Pruebas de integración deterministas sobre el stream SSE.

## Ejecución Local
```bash
# Servidor FastAPI con SSE
uv run uvicorn main:app --app-dir modules/03-agent-backend --reload --port 8000

# Servidor MCP (transporte stdio)
uv run python modules/03-agent-backend/mcp_server.py
```
