import random
import pygame
from src.settings import *
from src.core.game import Game
from src.core.timer import Timer
from src.core.utility import path
from src.components.scene import Scene
from src.components.sprite import *
from src.ui.debug_frame import DebugFrame

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.debug_frame = DebugFrame(game)

        image = pygame.image.load(path(f"{SPRITES}logo.png"))
        image.set_colorkey("Black")

        self.sprite = Sprite(image, (game.surface.width / 2, game.surface.height / 2), Anchor.Center)
        
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.sprite)

        self.timer = Timer(1, True)

    def update(self, delta: float):
        self.debug_frame.update(delta)
        self.sprites.update(delta)

        if self.timer.expired:
            self.sprite.anchor = random.choice(list(Anchor))

    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.debug_frame.draw(surface)
        self.sprites.draw(surface)
    
    def on_enter(self, **kwargs):
        pass
    
    def on_exit(self, **kwargs):
        pass
    