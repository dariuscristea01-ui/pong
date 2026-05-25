from __future__ import annotations

from dataclasses import dataclass

from ..config import GameConfig
from .ports import ClockPort, InputPort, RendererPort


@dataclass(slots=True)
class GameService:
    """High-level game orchestration.

    This is the place where the main loop, update cadence, and application
    composition will eventually live.
    """

    config: GameConfig
    clock: ClockPort
    input_adapter: InputPort
    renderer: RendererPort

    def run(self) -> None:
        """Start the game loop."""
        raise NotImplementedError("Implement the Pong loop here.")
