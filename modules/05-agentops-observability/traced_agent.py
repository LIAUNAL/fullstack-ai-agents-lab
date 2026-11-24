import json
import os

from langfuse import get_client, observe


@observe(name="retrieve-architecture-context")
def retrieve_context(query: str) -> list[str]:
    """Simula la recuperación de contexto técnico para el agente."""
    return [
        f"Contexto relevante para '{query}':",
        "Usa Arquitectura Hexagonal (Ports & Adapters) para aislar el dominio del LLM.",
    ]


@observe(name="generate-agent-answer", as_type="generation")
def synthesize_answer(query: str, context: list[str]) -> dict[str, str]:
    """Genera una respuesta estructurada y registra metadatos en Langfuse."""
    if os.getenv("LANGFUSE_PUBLIC_KEY"):
        get_client().update_current_generation(
            model="mock-agent-v1",
            metadata={"query_length": len(query)},
        )
    return {
        "query": query,
        "answer": " ".join(context),
        "status": "ok",
    }


@observe(name="agent-pipeline")
def run_traced_pipeline(query: str) -> dict[str, str]:
    """Pipeline completo instrumentado con spans anidados."""
    ctx = retrieve_context(query)
    return synthesize_answer(query, ctx)


if __name__ == "__main__":
    if not os.getenv("LANGFUSE_PUBLIC_KEY"):
        print("Aviso: LANGFUSE_PUBLIC_KEY no definida; ejecutando en modo local sin envío remoto.")
    output = run_traced_pipeline("¿Cómo desacoplar LangGraph del dominio?")
    print(json.dumps(output, indent=2, ensure_ascii=False))
