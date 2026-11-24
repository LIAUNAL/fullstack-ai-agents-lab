from src.domain.models import LLMMessage, LLMResponse


class MockLLMAdapter:
    """Adaptador determinista en memoria para pruebas unitarias y desarrollo offline."""

    def __init__(self, model_name: str = "mock-llm-v1") -> None:
        self._model_name = model_name
        self.calls: list[list[LLMMessage]] = []

    async def generate(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.0,
    ) -> LLMResponse:
        self.calls.append(messages)
        user_goal = next((m.content for m in reversed(messages) if m.role == "user"), "")
        summary = f"Plan generado para: {user_goal[:80]}"
        return LLMResponse(
            content=summary,
            model_name=self._model_name,
            tokens_used=max(1, len(summary.split())),
        )
