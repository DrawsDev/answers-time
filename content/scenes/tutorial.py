import pygame
from src.enums import Anchor
from src.core.game import Game
from src.components.scene import Scene
from src.ui.text_label import TextLabel

class Tutorial(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.ui_group = pygame.sprite.Group()
        self.label = TextLabel(game, "Нажми Q чтобы вернуться в меню")
        self.label.anchor = Anchor.Center
        self.label.align = pygame.FONT_CENTER
        self.label.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() / 2]
        self.ui_group.add(self.label)

    def update(self, delta):
        self.ui_group.update(delta)
        if self.game.input.is_key_pressed("q"):
            self.game.change_scene("Menu")

    def draw(self, surface):
        surface.fill("cadetblue1")
        self.ui_group.draw(surface)

__all__ = ["Tutorial"]
