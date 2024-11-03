import pygame
from pygame.math import Vector2
from src.components.sprite import Sprite

class Player(Sprite):
    def __init__(self, 
                 image: pygame.Surface, 
                 position: pygame.math.Vector2 = [0, 0], 
                 anchor: str = "topleft") -> None:
        super().__init__(image, position, anchor)
        
        self.velocity = Vector2()
        self.speed = 75

    def update(self, delta: float) -> None:
        direction = Vector2(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            direction += Vector2(0, -1)
        if keys[pygame.K_a]:
            direction += Vector2(-1, 0)
        if keys[pygame.K_s]:
            direction += Vector2(0, 1)
        if keys[pygame.K_d]:
            direction += Vector2(1, 0)

        if direction == (0, 0):
            self.velocity = self.velocity.move_towards([0, 0], 5)
        else:
            direction = direction.normalize()
            self.velocity = self.velocity.move_towards((direction * self.speed), 5)

        self.position += self.velocity * delta       
