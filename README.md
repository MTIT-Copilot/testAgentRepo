# Agent Lab (Demo Project for Coding Agents)

A small, intentionally imperfect Python project designed to **exercise coding agents** (GitHub Copilot Coding Agent, etc.).
Use the included issue templates in `docs/SCENARIOS.md` to run realistic tasks: refactors, tests, bug fixes, docs, and hygiene.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
pytest -q
```

## Structure
```
agent-lab/
  src/agentlab/
  tests/
  .github/workflows/ci.yml
  pyproject.toml
  requirements.txt
```
