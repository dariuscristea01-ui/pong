from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol

from ..domain.entities import GameState


class InputPort(Protocol):
    def read_state(self) -> GameState:
        """Translate external input into game state intent."""


class RendererPort(ABC):
    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def render(self, state: GameState) -> None:
        raise NotImplementedError

    @abstractmethod
    def present(self) -> None:
        raise NotImplementedError


class ClockPort(Protocol):
    def now(self) -> float:
        """Return the current time in seconds."""
