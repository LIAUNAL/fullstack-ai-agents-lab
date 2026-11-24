from typing import Annotated, Literal, TypedDict

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

CRITICAL_KEYWORDS: tuple[str, ...] = ("delete", "drop", "deploy", "production", "transfer")


class AgentState(TypedDict):
    """Estado persistido del grafo LangGraph por thread_id."""

    messages: Annotated[list[BaseMessage], add_messages]
    requires_approval: bool
    approved: bool | None
    tool_output: str


def plan_node(state: AgentState) -> dict[str, object]:
    """Evalúa la intención del usuario y determina si requiere aprobación HITL."""
    last_message = state["messages"][-1].content if state["messages"] else ""
    text = str(last_message).lower()
    needs_hitl = any(kw in text for kw in CRITICAL_KEYWORDS)
    return {
        "requires_approval": needs_hitl,
        "approved": None if needs_hitl else True,
    }


def tool_node(state: AgentState) -> dict[str, object]:
    """Simula la ejecución segura de herramientas MCP tras validar permisos."""
    if state.get("requires_approval") and state.get("approved") is False:
        return {"tool_output": "Acción rechazada por el operador humano."}
    return {"tool_output": "MCP[get_lab_status]: status=ready, gateway=litellm"}


def response_node(state: AgentState) -> dict[str, object]:
    """Construye la respuesta final del agente."""
    user_text = ""
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_text = str(msg.content)
            break

    tool_info = state.get("tool_output", "")
    reply = f"Procesado: '{user_text}'. Resultado de herramientas: {tool_info}"
    return {"messages": [AIMessage(content=reply)]}


def route_after_plan(state: AgentState) -> Literal["tool_node", "response_node"]:
    """Enruta al nodo de herramientas o finaliza si espera aprobación."""
    if state.get("requires_approval") and state.get("approved") is None:
        return "response_node"
    return "tool_node"


def build_agent_graph():
    """Compila el grafo LangGraph con checkpointer en memoria (o Postgres en prod)."""
    builder = StateGraph(AgentState)
    builder.add_node("plan_node", plan_node)
    builder.add_node("tool_node", tool_node)
    builder.add_node("response_node", response_node)

    builder.add_edge(START, "plan_node")
    builder.add_conditional_edges("plan_node", route_after_plan)
    builder.add_edge("tool_node", "response_node")
    builder.add_edge("response_node", END)

    return builder.compile(checkpointer=MemorySaver())
