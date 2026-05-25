# Architecture

## Goals

- Keep game rules isolated from I/O.
- Keep rendering, input, and timing behind adapters.
- Keep the composition root in `src/pong/main.py`.

## Layers

- `domain`: entities, value objects, and rules.
- `application`: orchestration and ports.
- `infrastructure`: adapters for rendering, input, and timing.
- `docs`: high-level design notes and future decisions.

## Recommended next additions

- Choose the graphics library adapter.
- Add a real input adapter.
- Add tests for domain rules.
