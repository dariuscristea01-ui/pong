from __future__ import annotations

from dataclasses import dataclass

from ...application.ports import InputPort
from ...domain.entities import Ball, GameState, Paddle, Scoreboard
from ...domain.value_objects import Vector2


@dataclass(slots=True)
class KeyboardInputAdapter(InputPort):
    """Keyboard input adapter placeholder."""

    def read_state(self) -> GameState:
        raise NotImplementedError
