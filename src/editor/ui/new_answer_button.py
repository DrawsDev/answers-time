import pygame
from typing import Tuple
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.base.ui_button import UIButton

class NewAnswerButton(UIButton):
    def __init__(        
        self, 
        game: Game,
        size: Tuple[int, int] = (200, 90),
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        self._new_answer_icon: pygame.Surface = load_asset(SPRITES, "editor_new_answer.png")
        super().__init__(game, size, position, anchor, 2, "#8F8F9E", "#848491", "#747484")

    def _update_image(self) -> None:
        super()._update_image()
        self.image.blit(self._new_answer_icon, self._new_answer_icon.get_rect(center=(self._size[0] / 2, self._size[1] / 2)))
