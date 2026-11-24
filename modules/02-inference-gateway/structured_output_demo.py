import asyncio
import json
import os
from typing import Literal

import litellm
from pydantic import BaseModel, Field


class DeploymentRiskAssessment(BaseModel):
    """Esquema estricto para evaluar riesgos de despliegue mediante structured output."""

    service_name: str = Field(description="Nombre del servicio evaluado")
    risk_level: Literal["low", "medium", "high"]
    requires_rollback_plan: bool
    checks: list[str] = Field(min_length=1)


async def extract_risk_assessment(prompt: str) -> DeploymentRiskAssessment:
    """Ejecuta una llamada con response_format estructurado y valida con Pydantic v2."""
    model = os.getenv("DEMO_LLM_MODEL", "openai/gpt-4o-mini")
    response = await litellm.acompletion(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Extrae una evaluación de riesgo de despliegue en formato JSON estricto."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        response_format=DeploymentRiskAssessment,
        temperature=0.0,
    )
    raw_content = response.choices[0].message.content  # type: ignore[union-attr]
    if not raw_content:
        raise ValueError("El modelo devolvió una respuesta vacía.")
    return DeploymentRiskAssessment.model_validate(json.loads(raw_content))


if __name__ == "__main__":
    sample_prompt = (
        "Vamos a desplegar el servicio inference-gateway con vLLM en GPU "
        "y cambiar el enrutamiento de tráfico al 100%."
    )
    if not os.getenv("OPENAI_API_KEY"):
        offline_demo = DeploymentRiskAssessment(
            service_name="inference-gateway",
            risk_level="high",
            requires_rollback_plan=True,
            checks=["Verificar VRAM disponible", "Validar healthcheck /v1/models"],
        )
        print("Modo offline (sin OPENAI_API_KEY):", offline_demo.model_dump_json(indent=2))
    else:
        result = asyncio.run(extract_risk_assessment(sample_prompt))
        print(result.model_dump_json(indent=2))
