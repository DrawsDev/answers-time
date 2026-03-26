import pygame

pygame.font.init()

_font = pygame.Font(size=24)
_color = pygame.Color(255, 255, 255)
_antialias = True


def load_surface(filepath: str) -> pygame.Surface:
    return pygame.image.load(filepath)


def clear(color: pygame.Color = pygame.Color(0, 0, 0)) -> None:
    surface = pygame.display.get_surface()
    surface.fill(color)


def print(text: str, x: int = 0, y: int = 0) -> None:
    surface = pygame.display.get_surface()
    surface.blit(_font.render(text, _antialias, _color), (x, y))
