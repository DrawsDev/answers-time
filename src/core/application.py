import sys
import pygame
from .window import Window
from .keyboard import Keyboard
from .mouse import Mouse

pygame.init()

class Application:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.window = Window(title, width, height)
        self.keyboard = Keyboard()
        self.mouse = Mouse()

    def run(self) -> None:
        while not self.window.is_should_close():
            self.process()
        self.quit()

    def quit(self) -> None:
        sys.exit(0)
        pygame.quit()

    def process(self) -> None:
        self.window.process()
