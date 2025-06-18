import pygame
from typing import Tuple, Optional
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import PrimitiveButton

class Checkbox(PrimitiveButton):
    def __init__(
        self, 
        app: Application,
        size: Tuple[int, int] = (100, 50),
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        button_border_radius: int = -1
    ) -> None:
        self._value = False
        super().__init__(app, size, position, anchor, z_index, Pallete.ATBlue3, Pallete.ATBlue3, Pallete.ATBlue3, button_border_radius)

    @property
    def value(self) -> bool:
        return self._value
    
    @value.setter
    def value(self, v: bool) -> None:
        self._value = v
        self._update_image()

    def on_mouse_pressed(self):
        super().on_mouse_pressed()
        self.value = not self.value

    def _update_image(self):
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, Pallete.ATBlue3, ((0, 0), self.rect.size), 4, self.button_border_radius)
        if self.value:
            self.image.blit(load_asset(SPRITES, "editor_correct.png"), (17 - 12, 17 - 12))
