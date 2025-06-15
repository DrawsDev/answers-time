import pygame
from src.framework.enums import *
from src.framework.application import Application
from src.framework.scene import Scene
from src.framework.scene.ui import *

class Tutorial(Scene):
    def __init__(self, app: Application):
        self.app = app
        self.ui_group = pygame.sprite.Group()
        self.label = TextLabel(app, "Нажми Q чтобы вернуться в меню")
        self.label.anchor = Anchor.Center
        self.label.position = [self.app.surface.get_width() / 2, self.app.surface.get_height() / 2]
        self.label.font_align = Align.Center
        self.ui_group.add(self.label)

    def update(self, delta):
        self.ui_group.update(delta)
        if self.app.input.is_key_pressed("q"):
            self.app.change_scene("Menu")

    def draw(self, surface):
        surface.fill("cadetblue1")
        self.ui_group.draw(surface)
