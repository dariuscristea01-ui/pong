from dataclasses import dataclass, field

from .value_objects import Vector2


@dataclass(slots=True)
class Paddle:
    position: Vector2
    velocity: Vector2 = field(default_factory=lambda: Vector2(0.0, 0.0))


@dataclass(slots=True)
class Ball:
    position: Vector2
    velocity: Vector2


@dataclass(slots=True)
class Scoreboard:
    left_player: int = 0
    right_player: int = 0


@dataclass(slots=True)
class GameState:
    ball: Ball
    left_paddle: Paddle
    right_paddle: Paddle
    score: Scoreboard
