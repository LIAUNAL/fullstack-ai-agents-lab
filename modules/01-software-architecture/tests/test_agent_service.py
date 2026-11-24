import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

MODULE_ROOT = Path(__file__).resolve().parents[1]
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from src.adapters.mock_llm import MockLLMAdapter  # noqa: E402
from src.application.agent_service import AgentService  # noqa: E402
from src.domain.models import AgentTaskRequest  # noqa: E402


@pytest.mark.asyncio
async def test_plan_task_safe_goal_does_not_require_approval() -> None:
    mock_llm = MockLLMAdapter(model_name="mock-deterministic")
    service = AgentService(llm=mock_llm)

    request = AgentTaskRequest(
        task_id="task-001",
        goal="Generar documentación técnica del módulo de inferencia",
        max_steps=3,
    )
    response = await service.plan_task(request)

    assert response.task_id == "task-001"
    assert response.model_used == "mock-deterministic"
    assert response.requires_human_approval is False
    assert len(response.steps) == 2
    assert len(mock_llm.calls) == 1


@pytest.mark.asyncio
async def test_plan_task_sensitive_goal_triggers_hitl_flag() -> None:
    service = AgentService(llm=MockLLMAdapter())

    request = AgentTaskRequest(
        task_id="task-002",
        goal="Deploy new inference container to production cluster",
        max_steps=5,
    )
    response = await service.plan_task(request)

    assert response.requires_human_approval is True
    assert response.steps[-1].requires_approval is True


def test_agent_task_request_rejects_short_goal() -> None:
    with pytest.raises(ValidationError):
        AgentTaskRequest(task_id="task-003", goal="hi")
