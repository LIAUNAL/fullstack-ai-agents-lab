import sys
from pathlib import Path

import pytest
from httpx import ASGITransport, AsyncClient

MODULE_ROOT = Path(__file__).resolve().parents[1]
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from main import app  # noqa: E402


@pytest.mark.asyncio
async def test_health_endpoint() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_chat_stream_safe_request() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/chat/stream",
            json={"thread_id": "t-safe", "message": "Consultar estado del laboratorio"},
        )
    assert response.status_code == 200
    assert "event: status" in response.text
    assert "event: token" in response.text
    assert '"status": "completed"' in response.text


@pytest.mark.asyncio
async def test_chat_stream_critical_request_triggers_hitl() -> None:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/chat/stream",
            json={"thread_id": "t-hitl", "message": "Deploy model to production"},
        )
    assert response.status_code == 200
    assert "event: approval_required" in response.text
    assert '"status": "waiting_approval"' in response.text
