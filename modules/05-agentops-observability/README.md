# Módulo 5: AgentOps, Observabilidad y Regresión

## Objetivo
Implementar trazabilidad distribuida con **Langfuse** y pruebas de regresión automáticas con **Promptfoo** para controlar calidad, latencia y formato en sistemas no deterministas.

## Archivos
- `traced_agent.py`: Ejemplo instrumentado con el decorador `@observe()` de Langfuse.
- `promptfooconfig.yaml`: Suite de evaluación con dataset dorado y aserciones de JSON y relevancia.

## Ejecución
```bash
# Ejecutar demo con trazas
uv run python modules/05-agentops-observability/traced_agent.py

# Ejecutar evaluación Promptfoo (requiere Node.js / npx)
npx promptfoo eval -c modules/05-agentops-observability/promptfooconfig.yaml
```
