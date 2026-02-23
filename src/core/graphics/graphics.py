from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from src.core.application import Application
    from src.core.graphics import Drawable

class Graphics:
    def __init__(self, app: "Application") -> None:
        self._app = app
        self._font = pygame.Font(size=24)
        self._color = "white"
        self._antialias = True

    @staticmethod
    def load_surface(filepath: str) -> pygame.Surface:
        return pygame.image.load(filepath)

    def clear(self, color: pygame.Color = "black") -> None:
        surface = self._app.window.get_surface()
        surface.fill(color)

    def print(self, text: str, x: int = 0, y: int = 0) -> None:
        surface = self._app.window.get_surface()
        text_surface = self._font.render(text, self._antialias, self._color)
        surface.blit(text_surface, (x, y))

    def draw(self, drawable: "Drawable") -> None:
        surface = self._app.window.get_surface()
        drawable.draw(surface)