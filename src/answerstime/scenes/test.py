import math
import random

from src.core import *
from src.objects import *
from src.utils import *

BACKGROUND = Color("#a0a0a0")


class Test(Scene):
    def on_enter(self, **kwargs) -> None:
        width, height, _ = self.app.window.get_mode()
        pattern_surface = self.app.graphics.load_surface("res/textures/pattern.png")

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
        self._fps_counter_process()
        self._versions_process()

    def _versions_process(self) -> None:
        version = self.app.version.text
        wrapper_version = self.app.wrapper_version.text
        self.app.graphics.print("Answers Time v" + version, 0, 0)
        self.app.graphics.print("Wrapper v" + wrapper_version, 0, 20)

    def _fps_counter_process(self) -> None:
        framerate = self.app.clock.framerate
        self.app.graphics.print("FPS: " + str(framerate), 0, 40)
