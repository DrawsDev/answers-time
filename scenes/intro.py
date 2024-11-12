import os
import math
import random
import pygame
from src.core.timer import Timer
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.cursor import Cursor
from src.components.dialogue import Dialogue, Line
from src.components.label import Label, FontParams

class Intro(Scene):
    def __init__(self) -> None:
        super().__init__()

        etu_img = pygame.image.load("assets/images/etu_1.png")
        etu_img.set_colorkey("Black")
        self.sprite = Sprite(etu_img, (250, 250), "center")
        self.sprite.add(self.sprites)

        etu_img2 = pygame.image.load("assets/images/etu_0.png")
        etu_img2.set_colorkey("Black")
        self.player = Player(etu_img2, (30, 30), "center")
        self.player.add(self.sprites)

        hand = pygame.image.load("content/images/hand_1.png")
        hand.set_colorkey("Black")
        self.player = Cursor(hand, (0, 0), "topleft")
        self.player.add(self.sprites)       

        self.fontparams = FontParams()
        self.fontparams.size += 10
        self.fontparams.fontpath = os.path.join("content", "fonts", "Ramona-Bold.ttf")
        self.fontparams.color = (255, 0, 200)
        self.fontparams.align = 1
        self.fontparams.wraplength = 0

        self.label = Label("Hello World!", self.fontparams, (100, 100), "center")
        self.label.add(self.sprites)

        self.dialogue = Dialogue()
        self.current_dialogue = 0
        self.test_dialogue = [Line("Привет!", rgb=True, pause=1, speed=2), Line("Как дела?"), Line("ЧЕЕЕ...", shake=True, shake_amplitude=1, color=(255, 0, 0))]
        self.text_dialogue2 = [Line("Ты", shake=True, color=(255, 0, 0)), Line("Кто", shake=True, color=(255, 0, 0)), Line("???", shake=True, color=(255, 0, 0))]
        self.text_dialogue3 = [Line("ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ", rgb=True)]

    def update(self, delta: float) -> None:
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_RETURN]:
            self.current_dialogue += 1
            if self.current_dialogue > 2:
                self.current_dialogue = 0

        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((180, 180, 180))

        if self.current_dialogue == 0:
            self.dialogue.render_lines(self.test_dialogue, surface)
        elif self.current_dialogue == 1:  
            self.dialogue.render_lines(self.text_dialogue2, surface)
        elif self.current_dialogue == 2:  
            self.dialogue.render_lines(self.text_dialogue3, surface)

        super().draw(surface)
