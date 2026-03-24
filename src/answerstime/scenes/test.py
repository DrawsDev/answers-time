import math
import random

from src.core import *
from src.objects import *
from src.utils import *

BACKGROUND = Color("#a0a0a0")


class Test(Scene):
    def on_enter(self, **kwargs) -> None:
        width, height = self.app.window.get_mode()
        pattern_surface = self.app.graphics.load_surface("res/textures/pattern1.png")

        self.scroll = ScrollingBackground()
        self.scroll.pattern = pattern_surface
        self.scroll.angle = 15
        self.scroll.speed = 100

        self.label = Label()
        self.label.anchor = "center"
        self.label.position = Vector2(width / 2, height / 2)
        self.label.text = "Hello World!"
        self.label.theme.font.filepath = "res/fonts/Baloo-Cyrillic.ttf"
        self.label.theme.font.size = 64

        self.button = Button()
        self.button.anchor = "midbottom"
        self.button.position = Vector2(width / 2, height - 100)
        self.button.text = "Button"
        self.button.theme.font.filepath = "res/fonts/Baloo-Cyrillic.ttf"
        self.button.theme.font.size = 64
        self.button.theme.box_style.corner_radius = 8

        self.container = Container()
        self.container.add(self.label, self.button)
    
    def on_exit(self, **kwargs) -> None:
        pass
    
    def event(self, event: Event) -> None:
        self.container.event(event)

    def process(self, delta: float) -> None:
        self._objects_process(delta)
        self._graphics_process()

    def _objects_process(self, delta: float) -> None:
        self.scroll.process(delta)
        self.container.process(delta)

    def _graphics_process(self) -> None:
        self.app.graphics.clear(BACKGROUND)
        self.app.graphics.draw(self.scroll)
        self.app.graphics.draw(self.container)
        self.label.theme.font_color = rainbow(s=50.0)
        self._debug_info_process()

    def _debug_info_process(self) -> None:
        wrapper_version = self.app.get_wrapper_version().as_text()
        version = self.app.get_version().as_text()
        self.app.graphics.print(f"Wrapper v{wrapper_version}", 0, 0)
        self.app.graphics.print(f"Answers Time v{version}", 0, 20)
        self.app.graphics.print(f"FPS: {self.app.clock.framerate}", 0, 40)
        self.app.graphics.print(f"MP: {self.app.mouse.get_position()}", 0, 60)
