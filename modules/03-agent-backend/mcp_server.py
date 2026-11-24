from mcp.server.fastmcp import FastMCP

mcp = FastMCP("fullstack-agent-lab-tools")

MODULE_DOCS: dict[str, str] = {
    "01-software-architecture": "Arquitectura Hexagonal, contratos Pydantic v2 y puertos Protocol.",
    "02-inference-gateway": "LiteLLM routing/fallbacks, vLLM serving y structured outputs.",
    "03-agent-backend": "FastAPI async, LangGraph con checkpointer y servidor MCP.",
    "04-fullstack-ux": "Next.js App Router, cliente SSE y aprobación Human-in-the-Loop.",
    "05-agentops-observability": "Trazabilidad con Langfuse (@observe) y regresión con Promptfoo.",
}


@mcp.tool()
def get_lab_status() -> dict[str, str]:
    """Consulta el estado general del laboratorio y sus servicios base."""
    return {
        "status": "ready",
        "backend": "fastapi+langgraph",
        "gateway": "litellm",
        "observability": "langfuse",
    }


@mcp.tool()
def list_module_docs(module_name: str = "") -> dict[str, str]:
    """Devuelve la descripción de un módulo específico o de todos los módulos."""
    if module_name and module_name in MODULE_DOCS:
        return {module_name: MODULE_DOCS[module_name]}
    return MODULE_DOCS


if __name__ == "__main__":
    mcp.run()
