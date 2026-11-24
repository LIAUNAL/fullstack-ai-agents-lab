# Full-Stack AI Agents Lab (`amalvarezme/fullstack-ai-agents-lab`)

Laboratorio y plantilla de ingeniería **Full-Stack para Sistemas con Agentes de IA en Producción**. Diseñado para dar el salto desde bases de Machine Learning, agentes y programación hacia **arquitectura de software, despliegue de modelos (Serving), MLOps/AgentOps y ciclo de vida de software (SDLC)**.

---

## Visión General del Programa (12 Semanas · 6 Módulos)

Este repositorio combina:
1. **Repositorios de referencia open-source** forkeados en `amalvarezme` y enlazados como **Git Submodules** en [`references/`](references/) (sin contaminar el historial).
2. **Módulos prácticos desde cero** en [`modules/`](modules/) que cubren las brechas de producción: Arquitectura Hexagonal, LiteLLM/vLLM, FastAPI + LangGraph + MCP, Next.js con SSE/HITL y Langfuse + Promptfoo.
3. **Infraestructura local reproducible** con Docker Compose (`pgvector`, Redis, LiteLLM Gateway, Langfuse), gestión de dependencias con `uv` y CI/CD en GitHub Actions.

---

## Tabla de Trazabilidad Curricular

| Semanas | Módulo | Qué revisar en `references/` | Qué construir en `modules/` / `capstone/` |
| :--- | :--- | :--- | :--- |
| **1–2** | **Módulo 1: Arquitectura de Software y SDLC** | [`references/Made-With-ML`](references/Made-With-ML) (diseño modular, testing, reproducibilidad) | [`modules/01-software-architecture`](modules/01-software-architecture) (Arquitectura Hexagonal, contratos Pydantic v2, `Protocol` ports, tests deterministas) |
| **3–4** | **Módulo 2: Despliegue e Inferencia (Serving)** | [`references/llm-zoomcamp`](references/llm-zoomcamp) (contenedores, evaluación y despliegue) | [`modules/02-inference-gateway`](modules/02-inference-gateway) (LiteLLM routing/fallbacks, `Dockerfile.vllm`, structured outputs, benchmarking) |
| **5–7** | **Módulo 3: Backend y Agentes con Estado** | [`references/GenAI_Agents`](references/GenAI_Agents) y [`references/ai-agents-for-beginners`](references/ai-agents-for-beginners) (grafos, memoria, tool calling) | [`modules/03-agent-backend`](modules/03-agent-backend) (FastAPI async, LangGraph con checkpointer Postgres, servidor MCP, SSE) |
| **8–9** | **Módulo 4: Full-Stack y UX Agéntica** | — | [`modules/04-fullstack-ux`](modules/04-fullstack-ux) (Next.js + TypeScript + Tailwind, cliente SSE, confirmación Human-in-the-Loop) |
| **10–11** | **Módulo 5: MLOps, AgentOps y CI/CD** | [`references/Made-With-ML`](references/Made-With-ML) (CI/CD) y [`references/llm-zoomcamp`](references/llm-zoomcamp) (evaluación) | [`modules/05-agentops-observability`](modules/05-agentops-observability) (trazabilidad Langfuse `@observe()`, regresión con Promptfoo) |
| **12** | **Módulo 6: Proyecto Integrador (Capstone)** | Todos los anteriores | [`capstone/`](capstone/) (`ARCHITECTURE.md` + `TODO.md` End-to-End) |

---

## Guía de Estudio por Fork (`references/`)

- **`references/Made-With-ML`**: Foco en cómo estructurar proyectos Python como paquetes reales, configuración tipada, pruebas unitarias/de datos y pipelines reproducibles.
- **`references/llm-zoomcamp`**: Foco en pipelines RAG, bases vectoriales, contenerización y métricas de evaluación.
- **`references/GenAI_Agents`**: Catálogo de patrones agénticos avanzados (multi-agente, reflexión, planificación, memoria).
- **`references/ai-agents-for-beginners`**: Fundamentos claros de tool calling, diseño de agentes y patrones base.

### Recursos Complementarios Recomendados (MLOps, Serving y Full-Stack)

- **MLOps & SDLC**: [`DataTalksClub/mlops-zoomcamp`](https://github.com/DataTalksClub/mlops-zoomcamp) · [`fmind/mlops-coding-course`](https://github.com/fmind/mlops-coding-course)
- **Serving & vLLM**: Curso gratuito *Fast & Efficient LLM Inference with vLLM* (DeepLearning.AI) · [`hadi-technology/vllm-mlops`](https://github.com/hadi-technology/vllm-mlops)
- **Full-Stack Templates**: [`TekkenSteve/fastapi_langgraph_template`](https://github.com/TekkenSteve/fastapi_langgraph_template) · [`vstorm-co/full-stack-ai-agent-template`](https://github.com/vstorm-co/full-stack-ai-agent-template)

---

## Inicio Rápido y Comandos del `Makefile`

```bash
# 1. Clonar con submódulos o sincronizarlos
make sync-submodules

# 2. Configurar variables de entorno
cp .env.example .env

# 3. Instalar dependencias Python con uv
make setup

# 4. Levantar infraestructura local (Postgres+pgvector, Redis, LiteLLM, Langfuse)
make infra-up

# 5. Ejecutar calidad de código y tests
make lint
make test

# 6. Apagar infraestructura
make infra-down
```

---

## Estructura del Repositorio

```text
fullstack-ai-agents-lab/
├── README.md
├── Makefile
├── pyproject.toml
├── docker-compose.yml
├── .env.example
├── .gitignore
├── .github/workflows/agent-ci.yml
├── references/
│   ├── Made-With-ML/
│   ├── llm-zoomcamp/
│   ├── GenAI_Agents/
│   └── ai-agents-for-beginners/
├── modules/
│   ├── 01-software-architecture/
│   ├── 02-inference-gateway/
│   ├── 03-agent-backend/
│   ├── 04-fullstack-ux/
│   └── 05-agentops-observability/
└── capstone/
    ├── ARCHITECTURE.md
    └── TODO.md
```
