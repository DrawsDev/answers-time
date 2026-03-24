from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from src.core.application import Application


class Graphics:
    def __init__(self, app: "Application") -> None:
        self._app = app
        self._font = pygame.Font(size=24)
        self._color = pygame.Color(255, 255, 255)
        self._antialias = True

    @staticmethod
    def load_surface(filepath: str) -> pygame.Surface:
        return pygame.image.load(filepath)

    def clear(self, color: pygame.Color = pygame.Color(0, 0, 0)) -> None:
        self._app.window.get_surface().fill(color)

    def print(self, text: str, x: int = 0, y: int = 0) -> None:
        text_surface = self._font.render(text, self._antialias, self._color)
        self._app.window.get_surface().blit(text_surface, (x, y))
