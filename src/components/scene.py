import pygame

class Scene:
    def __init__(self) -> None:
        self.sprites = pygame.sprite.Group()
    
    def on_exit(self) -> None: ...

    def on_enter(self) -> None: ...

    def update(self, delta: float) -> None:
        self.sprites.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        self.sprites.draw(surface)
