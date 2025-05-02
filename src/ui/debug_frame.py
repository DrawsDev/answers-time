import pygame
from src.settings import *
from src.core.game import Game
from src.core.utility import path

class DebugFrame:
    def __init__(self, game: Game):
        self.font = pygame.font.Font(path(f"{FONTS}Tiny5-Regular.ttf"), 8)
        self.clock = game.clock
    
    def update(self, delta: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        fps = self.clock.get_fps()
        fps_counter = self.font.render("FPS: %.1f" % fps, True, "White")

        surface.blit(fps_counter, (10, 10))
