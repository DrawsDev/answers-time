import os
import random
import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.timer import Timer
from src.core.utility import path
from src.components.scene import Scene
from src.components.sprite import *
from src.ui.debug_frame import DebugFrame
from src.ui.base.button import UIButton

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.sprites = pygame.sprite.Group()
        self.ui_objects = pygame.sprite.Group()
        self.debug_frame = DebugFrame(game)

        image = pygame.image.load(path(os.path.join(SPRITES, "logo.png")))
        image.set_colorkey("Black")

        self.sprite = Sprite(image, (game.surface.get_width() / 2, game.surface.get_height() / 2), Anchor.Center)
        self.sprites.add(self.sprite)

        self.button = UIButton(game, position=[game.surface.get_width() / 2, game.surface.get_height() / 2])
        self.button.anchor = Anchor.Center
        self.ui_objects.add(self.button)

        self.timer = Timer(1, True)

    def update(self, delta: float):
        self.debug_frame.update(delta)
        self.ui_objects.update(delta)
        self.sprites.update(delta)

        if self.timer.expired:
            self.sprite.anchor = random.choice(list(Anchor))

    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.sprites.draw(surface)
        self.ui_objects.draw(surface)
        self.debug_frame.draw(surface)
