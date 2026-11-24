from src.domain.models import (
    AgentPlanStep,
    AgentTaskRequest,
    AgentTaskResponse,
    LLMMessage,
)
from src.ports.llm_port import LLMPort

SENSITIVE_KEYWORDS: tuple[str, ...] = ("delete", "drop", "deploy", "production", "transfer")


class AgentService:
    """Caso de uso principal que orquesta la planificación con autonomía acotada."""

    def __init__(self, llm: LLMPort) -> None:
        self._llm = llm

    async def plan_task(self, request: AgentTaskRequest) -> AgentTaskResponse:
        """Construye un plan acotado y marca si requiere aprobación humana."""
        messages = [
            LLMMessage(
                role="system",
                content="Eres un arquitecto de software. Responde con un resumen conciso del plan.",
            ),
            LLMMessage(role="user", content=request.goal),
        ]
        llm_response = await self._llm.generate(messages, temperature=0.0)

        is_sensitive = any(kw in request.goal.lower() for kw in SENSITIVE_KEYWORDS)
        steps = [
            AgentPlanStep(
                step_number=1,
                action="Analizar requisitos y validar contratos de entrada",
                requires_approval=False,
            ),
            AgentPlanStep(
                step_number=2,
                action=f"Ejecutar objetivo: {request.goal}",
                requires_approval=is_sensitive,
            ),
        ][: request.max_steps]

        return AgentTaskResponse(
            task_id=request.task_id,
            summary=llm_response.content,
            steps=steps,
            requires_human_approval=any(step.requires_approval for step in steps),
            model_used=llm_response.model_name,
        )
