.PHONY: setup sync-submodules infra-up infra-down test lint typecheck

setup:
	uv sync

sync-submodules:
	git submodule update --init --recursive --remote

infra-up:
	docker compose up -d

infra-down:
	docker compose down

test:
	uv run pytest

lint:
	uv run ruff check .

typecheck:
	uv run mypy modules/01-software-architecture/src modules/02-inference-gateway/structured_output_demo.py modules/05-agentops-observability/traced_agent.py
