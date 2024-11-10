import math
import random
import re
import pygame
from pygame.math import Vector2
from src.core.utility import clamp
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.cursor import Cursor
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
        self.label = Label("Hello World!", self.fontparams, (100, 100), "center")
        self.label.add(self.sprites)

        self.font = pygame.font.Font(None, 24)


    def renderCharacter(self, char, color):
        return self.font.render(char, True, color)


    def clamp(self, v, _min, _max):
        return max(_min, min(v, _max))

    def renderText(self, text: str, surface: pygame.Surface):
        r_size = self.font.size(text)
        ix = 640 / 2 - r_size[0] / 2
        iy = 360 / 2 - r_size[1] / 2

        w_acc = 0
        sector = 360 / 64

        step = (pygame.time.get_ticks() / 1000.0) * 4.0

        mode = 0

        for index, char in enumerate(text):
            # Выбор "режима"
            if text[index:index+5] == "[rgb:":
                mode = 1
            elif text[index:index+7] == "[shake:":
                mode = 2
            elif text[index:index+1] == "]":
                mode = 0

            # Отрисовка на основе выбранного "Режима"
            if mode == 0:
                r_char = self.renderCharacter(char, (0, 0, 0)) 
                x = ix
                y = iy
            elif mode == 1:
                hue = (step * 32 + sector + index) % 360
                r_char = self.renderCharacter(char, pygame.Color.from_hsva(hue, 100, 100))
                x = ix + 1 * math.cos(step + sector * index)
                y = iy + 2 * math.sin(step + sector * index)
            elif mode == 2:
                r_char = self.renderCharacter(char, (255, 0, 100))
                x = ix + random.uniform(-1, 1)
                y = iy + random.uniform(-1, 1)             
            
            surface.blit(r_char, (x + w_acc, y))
            w_acc += r_char.get_size()[0] 

    def on_enter(self) -> None:
        pass

    def update(self, delta: float) -> None:
        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((180, 180, 180))
        self.renderText("Привет, [rgb:а ты кто]? Мы [shake:знакомы]? [rgb:Чеее...] лл.", surface)
        super().draw(surface)
