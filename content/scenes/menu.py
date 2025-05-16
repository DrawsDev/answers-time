import os
import random
import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import path
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.ui.debug_frame import DebugFrame
from src.ui.base.button import UIButton
from src.ui.label import Label

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.sprites = pygame.sprite.Group()
        self.ui_objects = pygame.sprite.Group()
        self.debug_frame = DebugFrame(game)

        image = pygame.image.load(path(os.path.join(SPRITES, "new_logo.png")))
        image.set_colorkey("Black")

        self.sprite = Sprite(image, (game.surface.get_width() / 2, game.surface.get_height() / 2), Anchor.Center)
        self.sprites.add(self.sprite)

        self.button = UIButton(game, position=[game.surface.get_width() / 2, game.surface.get_height() / 2])
        self.button.anchor = Anchor.Center
        self.ui_objects.add(self.button)

        self.label = Label(game, "Hello World!", [game.surface.get_width() / 2, 50])
        self.label.anchor = Anchor.Center
        self.ui_objects.add(self.label)

    def update(self, delta: float):
        self.debug_frame.update(delta)
        self.ui_objects.update(delta)
        self.sprites.update(delta)

        if self.button.pressed:
            self.sprite.anchor = random.choice(list(Anchor))
            self.label.text = str(self.sprite.anchor.name)
            self.label.color = random.choice(list(pygame.color.THECOLORS.keys()))
            self.label.background_color = random.choice(["BLACK", "DARKGRAY", "WHITE", "BROWN"])
            self.label.fontpath = random.choice([path(os.path.join(FONTS, "Ramona-Bold.ttf")), path(os.path.join(FONTS, "m5x7.ttf")), None])
            self.label.fontsize = random.choice([30, 8, 20])
            self.label.background_padding = random.randint(5, 20)

    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.sprites.draw(surface)
        self.ui_objects.draw(surface)
        self.debug_frame.draw(surface)
