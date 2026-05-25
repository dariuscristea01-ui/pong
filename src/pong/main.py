"""Application composition root for Pong."""

from .config import GameConfig
from .application.game_service import GameService
from .infrastructure.input.keyboard import KeyboardInputAdapter
from .infrastructure.rendering.renderer import RendererAdapter
from .infrastructure.timing.clock import SystemClock


def build_application() -> GameService:
    """Wire the application together.

    This module is intentionally a composition root only.
    """
    config = GameConfig()
    clock = SystemClock()
    input_adapter = KeyboardInputAdapter()
    renderer = RendererAdapter()
    return GameService(
        config=config,
        clock=clock,
        input_adapter=input_adapter,
        renderer=renderer,
    )


def main() -> None:
    """Entry point for the game."""
    application = build_application()
    try:
        application.run()
    except NotImplementedError as exc:
        raise SystemExit(str(exc)) from exc
