# Módulo 1: Arquitectura de Software y SDLC para Agentes

## Objetivo
Aplicar **Arquitectura Hexagonal (Ports & Adapters)** y **autonomía acotada** para desacoplar la lógica de negocio de los frameworks y proveedores LLM.

## Estructura
- `src/domain/models.py`: Entidades y contratos estrictos con **Pydantic v2**.
- `src/ports/llm_port.py`: Interfaz `Protocol` que define el contrato del proveedor LLM.
- `src/adapters/mock_llm.py`: Adaptador determinista para pruebas sin llamadas externas.
- `src/application/agent_service.py`: Caso de uso que aplica límites de autonomía (`max_steps`, acciones sensibles).
- `tests/test_agent_service.py`: Suite de pruebas unitarias deterministas con `pytest`.

## Principios Clave
1. **El dominio no importa SDKs de LLMs** (`openai`, `litellm`, `langgraph` viven en `adapters/`).
2. **Inversión de dependencias:** `AgentService` depende de `LLMPort` (`Protocol`), nunca de una implementación concreta.
3. **Autonomía acotada:** Toda acción con palabras clave sensibles o exceso de pasos queda marcada para aprobación humana.
