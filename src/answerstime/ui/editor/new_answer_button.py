import pygame
from typing import Tuple
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import PrimitiveButton

class NewAnswerButton(PrimitiveButton):
    def __init__(        
        self, 
        app: Application,
        size: Tuple[int, int] = (200, 90),
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        self._new_answer_icon: pygame.Surface = load_asset(SPRITES, "editor_new_answer.png")
        super().__init__(app, size, position, anchor, 2, "#8F8F9E", "#848491", "#747484")

    def _update_image(self) -> None:
        super()._update_image()
        self.image.blit(self._new_answer_icon, self._new_answer_icon.get_rect(center=(self._size[0] / 2, self._size[1] / 2)))
