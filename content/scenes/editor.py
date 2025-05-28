from src.core.game import Game
from src.components.scene import Scene

class Editor(Scene):
    def __init__(self, game: Game) -> None:
        self.game = game

__all__ = ["Editor"]
