# Módulo 2: Despliegue e Inferencia Híbrida (Inference Gateway)

## Objetivo
Dominar el serving de LLMs en producción: cuantización, gestión de memoria con **KV-cache / PagedAttention**, *constrained decoding* hacia esquemas Pydantic y enrutamiento híbrido (local + fallback cloud) con **LiteLLM**.

## Archivos
- `litellm_config.yaml`: Enrutamiento primario a modelo local (`ollama/qwen2.5:7b` o endpoint `vLLM`) con fallback automático a `gpt-4o-mini` / `claude-3-5-sonnet-20241022`.
- `Dockerfile.vllm`: Imagen lista para servir modelos Hugging Face en GPU con API compatible con OpenAI.
- `structured_output_demo.py`: Demostración de extracción estricta validada con Pydantic v2.

## Conceptos Clave de Serving
- **Cuantización (AWQ / GPTQ / GGUF / FP8):** Reduce VRAM y aumenta throughput sacrificando mínima precisión.
- **KV-Cache y PagedAttention (vLLM):** Evita recomputar atención en tokens previos y elimina fragmentación de memoria bajo alta concurrencia.
- **Métricas de Benchmarking:**
  - **TTFT (Time to First Token):** Latencia percibida por el usuario antes del primer token.
  - **TPOT (Time Per Output Token):** Velocidad de generación continua.
  - **Throughput (tokens/s):** Capacidad agregada del servidor bajo múltiples peticiones simultáneas.
