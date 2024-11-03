import pygame
import random
from pygame.math import Vector2
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.cursor import Cursor

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

    def on_enter(self) -> None:
        pass

    def update(self, delta: float) -> None:
        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((200, 180, 100))
        super().draw(surface)
