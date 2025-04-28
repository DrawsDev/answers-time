import pygame
from src.settings import SPRITES
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.ui.debug_frame import DebugFrame
from src.core.utility import path

class Menu(Scene):
    def __init__(self, game):
        self.debug_frame = DebugFrame(game)
        
        logo_sprite = pygame.image.load(path(f"{SPRITES}logo.png"))
        logo_sprite.set_colorkey("Black")
        self.logo_sprite = Sprite(logo_sprite, (game.screen.width / 2, game.screen.height / 2), "center")

    def update(self, delta: float):
        self.debug_frame.update(delta)
    
    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.debug_frame.draw(surface)
    
    def on_enter(self, **kwargs):
        pass
    
    def on_exit(self, **kwargs):
        pass
    