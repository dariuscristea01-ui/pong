# Pong

Clean-architecture scaffold for a Pong game. This repository provides a minimal, modular
Python project layout with clearly separated layers (domain, application, infrastructure)
and adapter placeholders — no gameplay or rendering implementation is included.

**Architecture**
- **Domain:** core entities and value objects ([src/pong/domain/entities.py](src/pong/domain/entities.py)).
- **Application:** ports and orchestration ([src/pong/application/ports.py](src/pong/application/ports.py), [src/pong/application/game_service.py](src/pong/application/game_service.py)).
- **Infrastructure:** adapter placeholders for rendering, input, and timing ([src/pong/infrastructure/rendering/renderer.py](src/pong/infrastructure/rendering/renderer.py), [src/pong/infrastructure/input/keyboard.py](src/pong/infrastructure/input/keyboard.py)).
- **Composition root:** application wiring lives in [src/pong/main.py](src/pong/main.py).

See [docs/architecture.md](docs/architecture.md) for design notes and recommended next steps.

**Getting started (Windows)**

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install the package in editable mode (optional) and run tests:

```powershell
pip install -e .
$env:PYTHONPATH = "src"
.venv\Scripts\python.exe -m unittest discover -s tests
```

**Getting started (POSIX)**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
PYTHONPATH=src python -m unittest discover -s tests
```

**Purpose and scope**

This repository is intended as an architectural starting point for building a Pong
game in Python. It intentionally avoids committing to a specific graphics/input library
and instead provides adapter interfaces and placeholders so you can plug in your
preferred runtime (e.g., Pygame, Arcade, or a custom engine).

**Contributing**

- Open an issue for design proposals or feature requests.
- Prefer adding tests for domain rules and adapters.

**License**

See [LICENSE](LICENSE).