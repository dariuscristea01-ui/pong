from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from ...application.ports import ClockPort


@dataclass(slots=True)
class SystemClock(ClockPort):
    """System time adapter."""

    def now(self) -> float:
        return perf_counter()
