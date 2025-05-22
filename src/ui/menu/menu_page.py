from typing import Tuple
from src.enums import Anchor, TextAlign
from src.core.game import Game
from src.ui.text_label import TextLabel
from src.ui.frame import Frame

ATBLUE = "#3CA4FF"

class MenuPage:
    def __init__(self, game: Game, title: str):
        self.game = game
        self._create(title)

    @property
    def children(self) -> Tuple[Frame, TextLabel, Frame]:
        return tuple([self.frame, self.title, self.line])

    def _create(self, title: str) -> None:
        # Фрейм
        self.frame = Frame(self.game, self.game.surface.get_size())
        self.frame.transparency = 225
        # Заголовок
        self.title = TextLabel(self.game, title, [self.game.surface.get_width() / 2, 0])
        self.title.align = TextAlign.Center
        self.title.anchor = Anchor.MidTop
        self.title.color = ATBLUE
        # Линия под заголовком
        self.line = Frame(self.game, [self.game.surface.get_width() - 10, 2])
        self.line.color = ATBLUE
        self.line.anchor = Anchor.Center
        self.line.position = [self.game.surface.get_width() / 2, self.title.image.get_height()]

__all__ = ["Menu"]
