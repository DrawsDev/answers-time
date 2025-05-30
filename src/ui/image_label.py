from typing import Tuple
from src.enums import Anchor
from src.core.game import Game
from src.ui.base.ui_image import UIImage

class ImageLabel(UIImage):
    def __init__(
        self, 
        game: Game, 
        path: str, 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft
    ) -> None:
        super().__init__(game, path, position, anchor)

__all__ = ["ImageLabel"]
