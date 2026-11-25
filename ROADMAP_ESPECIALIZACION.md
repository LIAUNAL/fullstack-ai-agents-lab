# Roadmap Curricular Unificado — Especialización en Aprendizaje Automático mediante IA (UNAL Manizales · Plan 4356)

Este documento integra el currículo oficial de las **4 asignaturas obligatorias** + la electiva **Principios de Desarrollo de Software con Inteligencia Artificial** con el laboratorio [`fullstack-ai-agents-lab`](README.md), fusionando dos marcos pedagógicos:

1. **Proyecto Hermes 68372 (UNAL – SIUN):** Fortalecer de forma simultánea **Motivación**, **Argumentación (Pensamiento Crítico)** y **Resolución de Problemas**, evitando la *descarga cognitiva* al trabajar con IA mediante andamiaje anclado al dominio y trazabilidad auditable.
2. **Metodología de Diseño Instruccional (Angie / Teacher Training):** Formación ágil para **adultos con poco tiempo** (Andragogía), **Worked Examples** antes del reto autónomo, **ABP + Design Thinking** en 5 fases con **paleta de colores por fase**, cápsulas asíncronas cortas y **evaluación por diagnóstico y mediación** (sin memorización).

---

## 1. Estrategia Pedagógica Fusionada

### 1.1 Ejes Cognitivos (Hermes 68372)
- **Motivación:** Conectar cada unidad con un fallo o reto real de producción (*Full Deployment Engineering*), preservando la autonomía y agencia del estudiante.
- **Argumentación / Pensamiento Crítico:** Exigir justificación de *trade-offs* (costo vs. latencia, local vs. cloud, complejidad vs. mantenibilidad) y auditoría de salidas de IA sin aceptar respuestas no verificables.
- **Resolución de Problemas:** Depurar sistemas rotos, construir desde cero antes de usar librerías y validar cada cambio con pruebas ejecutables.

### 1.2 Ciclo Design Thinking + Paleta de Colores (Angie)
| Fase Design Thinking | Color Guía | Aplicación en el Curso |
| :--- | :--- | :--- |
| **1. Empatizar** | `#00A8E0` | Analizar un caso real roto en producción o aula (brecha disciplinar/operativa). |
| **2. Definir** | `#E9572B` | Formular el reto del módulo y los contratos/criterios de aceptación (*SDD*). |
| **3. Idear** | `#4DB922` | Explorar alternativas arquitectónicas, algoritmos y estrategias de serving/agentes. |
| **4. Prototipar** | `#FF8A00` | Construir el subproyecto en el repositorio con pruebas y trazabilidad. |
| **5. Evaluar** | `#3763A9` | Evaluación estilo Angie (predecir ejecución, detectar bugs, mediar sin descarga cognitiva) + defensa. |

### 1.3 Estructura de la Sesión Semanal (3 horas) + Kit Asíncrono
Todas las asignaturas comparten **48 HAP** oficiales del SIA, distribuidas en **16 semanas = 12 semanas de clase (3 h/sem) + 4 semanas intercaladas de dudas, entregas y evaluación (cadencia 3+1)**:

- **Asíncrono Previo / Consulta Rápida (15–20 min):** Video ≤3 min + Infografía + Mapa mental + 5 Tarjetas de memoria (*Retrieval Practice*) + Worked Example anotado.
- **Bloque 1 · Empatizar + Definir (25 min):** Caso roto real + formulación del reto.
- **Bloque 2 · Cápsula Magistral Corta + Worked Example (35 min):** *(Máximo 60 min expositivos totales).*
- **Pausa Activa (10 min).**
- **Bloque 3 · Idear + Prototipar (80 min):** Taller ABP sobre `fullstack-ai-agents-lab` con tutor IA que da pistas sin entregar la solución.
- **Bloque 4 · Evaluar + Argumentar (30 min):** Diagnóstico de errores, predicción de ejecución no obvia y defensa de *trade-offs*.

---

## 2. Flujo Longitudinal entre las 5 Materias (2 Semestres)

```text
SEMESTRE 1 (Datos, Modelado Clásico y Criterio de Software)
  [OBL 01: Ingeniería de Datos] ──(Dataset versionado + Contratos de datos + Feature Store)──┐
  [OBL 02: Intro al ML]         ──(Línea base clásica + Protocolo validación sin fugas)─────┼──┐
  [ELE: Software con IA]        ──(Hexagonal + SDD + TDD + MCP + CI/CD)────────────────────┼──┼──┐
                                                                                           │  │  │
SEMESTRE 2 (Deep Learning, Serving, Agentes y Gobernanza)                                  ▼  ▼  ▼
  [OBL 03: Redes Neuronales y DL] ──(Modelo profundo / LLM LoRA + Cuantización + Perfil)──────┤
                                                                                              ▼
  [OBL 04: Despliegue y Agentes]  ──(vLLM/LiteLLM + RAG/MCP/LangGraph + SSE/HITL + Langfuse/Promptfoo + Ley 1581/AI Act)
```

---

## 3. Acoplamiento por Módulos (`12 + 4` semanas por materia)

### Materia 1: `OBL 01` — Fundamentos de Ingeniería de Datos y Big Data (`SIA 18368`)
- **Módulos acoplados:** `references/Made-With-ML` (data validation & lineage), contratos Pydantic v2 (`M1`), `Postgres/pgvector` (`docker-compose.yml`).
- **Bloques (12+4):**
  - `S1–S3 → S4`: Arquitecturas de datos (Warehouse/Lakehouse), formatos (Parquet/Avro) y calidad/contratos → **Hito 1 (S4)**.
  - `S5–S7 → S8`: SQL analítico, modelado dimensional y bases NoSQL → **Hito 2 (S8)**.
  - `S9–S11 → S12`: Pipelines batch/stream, Spark e idempotencia/orquestación → **Hito 3 (S12)**.
  - `S13–S15 → S16`: Versionado/linaje, Feature Store, deriva de datos y Ley 1581/2012 → **Hito 4 (S16)**.

### Materia 2: `OBL 02` — Introducción al Aprendizaje de Máquina (`SIA 18371`)
- **Módulos acoplados:** `references/Made-With-ML` (pipelines reproducibles, validación sin *data leakage*, métricas).
- **Bloques (12+4):**
  - `S1–S3 → S4`: Fundamentos matemáticos/optimización y riesgo empírico → **Hito 1 (S4)**.
  - `S5–S7 → S8`: Modelos supervisados (lineales, SVM/kernels, árboles/boosting) → **Hito 2 (S8)**.
  - `S9–S11 → S12`: No supervisados (clustering, GMM/EM, PCA/UMAP) y regularización/CV → **Hito 3 (S12)**.
  - `S13–S15 → S16`: Métricas (F1, ROC/PR-AUC, RMSE), desbalanceo e interpretabilidad → **Hito 4 (S16)**.

### Materia 3: `ELE` — Principios de Desarrollo de Software con IA (3 Créditos)
- **Módulos acoplados:** `M1: 01-software-architecture`, `M3` (MCP), `.github/workflows/agent-ci.yml`.
- **Bloques (12+4):**
  - `S1–S3 → S4`: Deuda técnica con IA, Arquitectura Hexagonal (`M1`) y **SDD** (specs ejecutables) → **Hito 1 (S4)**.
  - `S5–S7 → S8`: **TDD** (rojo-verde-refactor), pirámide de pruebas, dobles/mocks (`MockLLMAdapter`) y propiedades → **Hito 2 (S8)**.
  - `S9–S11 → S12`: Agentes de codificación, ingeniería de contexto, protocolo **MCP** (`M3`) y cuándo no usar agente → **Hito 3 (S12)**.
  - `S13–S15 → S16`: Revisión asistida, análisis estático (`ruff`, `mypy`), CI/CD y métricas **DORA** → **Hito 4 (S16)**.

### Materia 4: `OBL 03` — Redes Neuronales y Aprendizaje Profundo (`SIA 18373`)
- **Módulos acoplados:** `M2: 02-inference-gateway` (puente en cuantización y costo), `M3` (embeddings/atención), `Made-With-ML`.
- **Bloques (12+4):**
  - `S1–S3 → S4`: MLP desde cero vs. PyTorch, CNNs/ResNet y RNN/LSTM/GRU → **Hito 1 (S4)**.
  - `S5–S7 → S8`: Atención (Q/K/V), Transformers y fundamentos de LLMs (tokens, embeddings, scaling) → **Hito 2 (S8)**.
  - `S9–S11 → S12`: Ajuste fino eficiente (**LoRA/QLoRA**), **cuantización** y entrenamiento distribuido/precisión mixta → **Hito 3 (S12)**.
  - `S13–S15 → S16`: Reproducibilidad, perfilado de cómputo y comparativa modelo compacto vs. LLM → **Hito 4 (S16)**.

### Materia 5: `OBL 04` — Despliegue de Modelos y Agentes Inteligentes (`SIA 18375`)
- **Módulos acoplados:** `M2: 02-inference-gateway`, `M3: 03-agent-backend`, `M4: 04-fullstack-ux`, `M5: 05-agentops-observability`, `capstone/`.
- **Bloques (12+4):**
  - `S1–S3 → S4`: MLOps, *model registry*, estrategias canary/shadow/A-B y contenerización Docker → **Hito 1 (S4)**.
  - `S5–S7 → S8`: Optimización de inferencia (`vLLM`, cuantización, `ONNX`/edge) y gateway híbrido (`LiteLLM`) → **Hito 2 (S8)**.
  - `S9–S11 → S12`: `pgvector` + RAG / Agentic RAG, `LangGraph` + `MCP`, multiagente y UX `SSE` + `HITL` → **Hito 3 (S12)**.
  - `S13–S15 → S16`: Evaluación (`Promptfoo`), observabilidad (`Langfuse`), deriva, seguridad y regulación (Ley 1581, UE 2024/1689, ISO 42001) → **Hito 4 (S16)**.
