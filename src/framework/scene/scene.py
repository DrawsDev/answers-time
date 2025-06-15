import pygame

class Scene:
    def __init__(self) -> None:
        pass

    def on_enter(self, *args, **kwargs) -> None:
        pass

    def on_exit(self, *args, **kwargs) -> None:
        pass

    def update(self, delta: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        pass
