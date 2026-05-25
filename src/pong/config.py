from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GameConfig:
    """Static configuration for the Pong application."""

    window_width: int = 800
    window_height: int = 600
    target_fps: int = 60
    paddle_width: int = 16
    paddle_height: int = 96
    ball_size: int = 16
