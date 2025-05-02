import pygame
from src.settings import *
from src.core.game import Game
from src.core.utility import path
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.ui.debug_frame import DebugFrame

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.debug_frame = DebugFrame(game)

    def update(self, delta: float):
        self.debug_frame.update(delta)
    
    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.debug_frame.draw(surface)
    
    def on_enter(self, **kwargs):
        pass
    
    def on_exit(self, **kwargs):
        pass
    