import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene import Scene
from src.framework.scene.ui import *
from src.answerstime.ui import Background

class Tutorial(Scene):
    def __init__(self, app: Application):
        self.app = app
        self.background = Background(load_asset(SPRITES, "quiz_background.png"), 0, 10)
        self.ui_group = pygame.sprite.Group()
        self.label = TextLabel(app, "Нажми Q чтобы вернуться в меню")
        self.label.anchor = Anchor.Center
        self.label.position = [self.app.surface.get_width() / 2, self.app.surface.get_height() / 2]
        self.label.font_align = Align.Center
        self.ui_group.add(self.label)

    def update(self, delta):
        self.background.update(delta)
        self.ui_group.update(delta)
        if self.app.input.is_key_pressed("q"):
            self.app.change_scene("Menu")

    def draw(self, surface):
        surface.fill(Pallete.ATBlue5)
        self.background.draw(surface)
        self.ui_group.draw(surface)
