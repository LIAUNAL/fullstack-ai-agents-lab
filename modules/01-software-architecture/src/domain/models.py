from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class LLMMessage(BaseModel):
    """Mensaje inmutable intercambiado con un proveedor LLM."""

    model_config = ConfigDict(frozen=True)

    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)


class LLMResponse(BaseModel):
    """Respuesta normalizada desde cualquier adaptador LLM."""

    model_config = ConfigDict(frozen=True)

    content: str = Field(min_length=1)
    model_name: str = Field(min_length=1)
    tokens_used: int = Field(ge=0)


class AgentTaskRequest(BaseModel):
    """Contrato de entrada para solicitar una tarea al agente."""

    model_config = ConfigDict(frozen=True)

    task_id: str = Field(min_length=1)
    goal: str = Field(min_length=3, max_length=2000)
    max_steps: int = Field(default=3, ge=1, le=10)


class AgentPlanStep(BaseModel):
    """Paso individual dentro del plan generado por el agente."""

    model_config = ConfigDict(frozen=True)

    step_number: int = Field(ge=1)
    action: str = Field(min_length=1)
    requires_approval: bool = False


class AgentTaskResponse(BaseModel):
    """Contrato de salida estructurado del servicio agéntico."""

    model_config = ConfigDict(frozen=True)

    task_id: str
    summary: str
    steps: list[AgentPlanStep]
    requires_human_approval: bool
    model_used: str
