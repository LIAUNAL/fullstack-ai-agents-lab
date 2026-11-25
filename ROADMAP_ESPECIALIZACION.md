# Roadmap Curricular — Especialización en Aprendizaje Automático mediante IA (UNAL Manizales · Plan 4356)

Este documento articula el plan de estudios de la Especialización con el laboratorio [`LIAUNAL/fullstack-ai-agents-lab`](README.md), integrando un enfoque de **Aprendizaje Profundo Verificable** (motivación, argumentación crítica y resolución de problemas sin descarga cognitiva) con **diseño instruccional ágil para adultos** (Andragogía, *Worked Examples*, ABP y *Design Thinking*).

---

## 1. Estrategia Pedagógica Base

### 1.1 Dimensiones del Aprendizaje Profundo
- **Motivación intrínseca:** Conectar cada unidad con retos reales de ingeniería y despliegue (*Full Deployment Engineering*), preservando la autonomía del estudiante.
- **Argumentación y Pensamiento Crítico:** Defender *trade-offs* arquitectónicos (costo vs. latencia, local vs. cloud, complejidad vs. mantenibilidad) con evidencia empírica y trazas auditables, sin aceptar salidas de IA sin verificación.
- **Resolución de Problemas:** Construir e instrumentar sistemas desde cero antes de abstraer con librerías, depurar fallos reales y validar cada cambio con pruebas ejecutables.

### 1.2 Ciclo Design Thinking + Paleta de Colores Guía
| Fase Design Thinking | Color Guía | Aplicación en el Curso |
| :--- | :--- | :--- |
| **1. Empatizar** | `#00A8E0` | Analizar un caso real roto en producción o entorno de datos/modelos. |
| **2. Definir** | `#E9572B` | Formular el reto del módulo y sus criterios de aceptación (*SDD*). |
| **3. Idear** | `#4DB922` | Explorar alternativas de modelado, arquitectura, serving y agentes. |
| **4. Prototipar** | `#FF8A00` | Implementar el subproyecto en el repositorio con pruebas y trazabilidad. |
| **5. Evaluar** | `#3763A9` | Diagnóstico de fallos, predicción de ejecución no obvia y defensa de *trade-offs*. |

### 1.3 Formato Semanal Ágil (`12 + 4` semanas · 48 HAP)
Cada asignatura del path se organiza en **16 semanas**: **12 semanas de clase (3 h/sem)** + **4 semanas intercaladas** de resolución de dudas, entregas y sustentación (**cadencia 3+1**: `S1–S3→S4`, `S5–S7→S8`, `S9–S11→S12`, `S13–S15→S16`):

- **Material Asíncrono Corto (15–20 min):** Video ≤3 min, infografía, mapa mental, 5 tarjetas de memoria (*Retrieval Practice*) y *Worked Example* anotado.
- **Sesión Semanal de 3 horas (180 min):**
  - *Empatizar + Definir* (25 min): caso roto real y formulación del reto.
  - *Cápsula Magistral + Worked Example* (35 min — máx. 60 min expositivos totales).
  - *Pausa Activa* (10 min).
  - *Idear + Prototipar (ABP)* (80 min): trabajo práctico guiado por pistas sin entregar la solución final.
  - *Evaluar + Argumentar* (30 min): evaluación por diagnóstico (sin memorización) y defensa breve de decisiones.

---

## 2. Distribución por Semestres y Relación con el Path

### Primer Semestre
1. **Fundamentos de Ingeniería de Datos y Big Data** *(OBL · SIA 18368 · En el path)*
   - **Relación con el path:** Base de datos, contratos de esquema, linaje y almacenamiento (`Postgres + pgvector`, `Made-With-ML`). Entrega datasets versionados y confiables para el resto del programa.
   - **Bloques `12+4`:** `S1–S3→S4` (Arquitecturas Lakehouse, Parquet/Avro, contratos de calidad) · `S5–S7→S8` (SQL analítico, modelado dimensional y NoSQL) · `S9–S11→S12` (Pipelines batch/stream, Spark e idempotencia) · `S13–S15→S16` (Versionado/linaje, Feature Store, deriva y Ley 1581/2012).
2. **Redes Neuronales y Aprendizaje Profundo** *(OBL · SIA 18373 · En el path)*
   - **Relación con el path:** Profundiza en arquitecturas neuronales, Transformers, fundamentos de LLMs, ajuste fino eficiente (`LoRA/QLoRA`), cuantización y perfilado de cómputo (`M2` y `M3` del laboratorio).
   - **Bloques `12+4`:** `S1–S3→S4` (MLP desde cero, CNNs/ResNet, RNN/LSTM/GRU) · `S5–S7→S8` (Atención Q/K/V, Transformers y LLMs) · `S9–S11→S12` (LoRA, cuantización y entrenamiento distribuido) · `S13–S15→S16` (Reproducibilidad, perfilado y comparativa modelo compacto vs. LLM).
3. **Despliegue de Modelos y Agentes Inteligentes** *(OBL · SIA 18375 · En el path)*
   - **Relación con el path:** Núcleo de producción Full-Stack del laboratorio (`M2: vLLM/LiteLLM`, `M3: FastAPI/LangGraph/MCP`, `M4: Next.js SSE/HITL`, `M5: Langfuse/Promptfoo`, `capstone/`).
   - **Bloques `12+4`:** `S1–S3→S4` (MLOps, *model registry*, canary/shadow y Docker) · `S5–S7→S8` (vLLM, cuantización, ONNX/edge y gateway híbrido LiteLLM) · `S9–S11→S12` (RAG/`pgvector`, LangGraph, MCP, multiagente y UX SSE/HITL) · `S13–S15→S16` (Promptfoo, Langfuse, deriva, seguridad y regulación Ley 1581 / UE 2024/1689 / ISO 42001).
4. **Electiva General** *(Fuera del path)*
   - Complemento electivo del semestre según intereses del estudiante.

### Segundo Semestre
1. **Introducción al Aprendizaje de Máquina** *(OBL · SIA 18371 · En el path)*
   - **Relación con el path:** Consolida rigor estadístico, modelos clásicos supervisados/no supervisados, prevención de *data leakage*, validación cruzada, métricas e interpretabilidad (`references/Made-With-ML`).
   - **Bloques `12+4`:** `S1–S3→S4` (Fundamentos matemáticos, optimización y riesgo empírico) · `S5–S7→S8` (Supervisados: lineales, SVM/kernels, árboles/boosting) · `S9–S11→S12` (No supervisados: clustering, PCA/UMAP y regularización/CV) · `S13–S15→S16` (Métricas F1/PR-AUC/RMSE, desbalanceo e interpretabilidad).
2. **Principios de Desarrollo de Software con IA y Agentes** *(ELE · 3 Créditos · En el path)*
   - **Relación con el path:** Cierra el ciclo de ingeniería de software (`M1: 01-software-architecture`, `M3: MCP`, `.github/workflows/agent-ci.yml`): Arquitectura Hexagonal, **SDD** (especificaciones ejecutables), **TDD**, ingeniería de contexto y métricas **DORA**.
   - **Bloques `12+4`:** `S1–S3→S4` (Deuda técnica con IA, Arquitectura Hexagonal y SDD) · `S5–S7→S8` (TDD, pirámide de pruebas y dobles/mocks) · `S9–S11→S12` (Agentes de código, ingeniería de contexto y protocolo MCP) · `S13–S15→S16` (Revisión asistida, análisis estático `ruff`/`mypy`, CI/CD y métricas DORA).
3. **Dos Electivas** *(Fuera del path)*
   - Profundización electiva libre para completar los créditos del segundo semestre.
