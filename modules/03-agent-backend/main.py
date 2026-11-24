import json
from collections.abc import AsyncIterator
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from graph import build_agent_graph
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

app = FastAPI(title="Full-Stack AI Agent Backend", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent_graph = build_agent_graph()


class ChatStreamRequest(BaseModel):
    """Contrato de entrada para iniciar o reanudar una conversación en streaming."""

    thread_id: str = Field(min_length=1, default="default-thread")
    message: str = Field(min_length=1)
    approved: bool | None = None


def _format_sse(event: str, data: dict[str, Any]) -> str:
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


async def _stream_agent_events(payload: ChatStreamRequest) -> AsyncIterator[str]:
    yield _format_sse("status", {"stage": "planning", "thread_id": payload.thread_id})

    initial_state: dict[str, Any] = {
        "messages": [HumanMessage(content=payload.message)],
        "requires_approval": False,
        "approved": payload.approved,
        "tool_output": "",
    }
    config: dict[str, Any] = {"configurable": {"thread_id": payload.thread_id}}
    result = await agent_graph.ainvoke(initial_state, config=config)  # type: ignore[arg-type]

    if result.get("requires_approval") and payload.approved is None:
        yield _format_sse(
            "approval_required",
            {
                "thread_id": payload.thread_id,
                "action": payload.message,
                "reason": "Acción crítica detectada; requiere confirmación Human-in-the-Loop.",
            },
        )
        yield _format_sse("done", {"status": "waiting_approval"})
        return

    yield _format_sse(
        "status",
        {"stage": "tool_execution", "output": result.get("tool_output", "")},
    )

    final_message = str(result["messages"][-1].content) if result.get("messages") else ""
    for word in final_message.split(" "):
        yield _format_sse("token", {"content": f"{word} "})

    yield _format_sse("done", {"status": "completed"})


@app.get("/health")
async def health() -> dict[str, str]:
    """Healthcheck del backend."""
    return {"status": "ok"}


@app.post("/chat/stream")
async def chat_stream(request: ChatStreamRequest) -> StreamingResponse:
    """Endpoint SSE para streaming de estados, HITL y tokens del agente."""
    return StreamingResponse(
        _stream_agent_events(request),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
    )
