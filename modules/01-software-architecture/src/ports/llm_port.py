from typing import Protocol

from src.domain.models import LLMMessage, LLMResponse


class LLMPort(Protocol):
    """Puerto de salida para cualquier proveedor o gateway de inferencia LLM."""

    async def generate(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Genera una respuesta determinista o estocástica a partir de mensajes."""
        ...
