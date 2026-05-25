from __future__ import annotations

from dataclasses import dataclass

from ...application.ports import RendererPort
from ...domain.entities import GameState


@dataclass(slots=True)
class RendererAdapter(RendererPort):
    """Concrete rendering adapter placeholder.

    Swap this for the chosen graphics library adapter.
    """

    def clear(self) -> None:
        raise NotImplementedError

    def render(self, state: GameState) -> None:
        raise NotImplementedError

    def present(self) -> None:
        raise NotImplementedError
