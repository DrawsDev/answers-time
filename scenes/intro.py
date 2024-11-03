import pygame
import random
from pygame.math import Vector2
from src.core.game import game
from src.components.scene import Scene
from src.components.sprite import Sprite

class Intro(Scene):
    def __init__(self) -> None:
        super().__init__()

        etu_img = pygame.image.load("assets/images/etu_1.png")
        etu_img.set_colorkey("Black")
        self.sprite = Sprite(etu_img, (250, 250), "center")
        self.sprite.add(self.sprites)

    def update(self, delta: float) -> None:
        super().update(delta)

        self.sprite.position += Vector2(random.randint(-1, 1), random.randint(-1, 1)) 

        global game
        if game != None:
            print(game, "no-none")
        else:
            print(game, "none")
