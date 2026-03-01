import math
import random

from src.core import Scene
from src.core.common import *
from src.core.objects import *

BACKGROUND = "#a0a0a0"


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
        self.label.font_filepath = "res/fonts/Baloo-Cyrillic.ttf"
        self.label.font_size = 64

        self.button = Button()
        self.button.anchor = "midbottom"
        self.button.position = Vector2(width / 2, height - 100)
        self.button.text = "random size"
        self.button.font_filepath = "res/fonts/Baloo-Cyrillic.ttf"
        self.button.font_size = 64
        self.button.callback = lambda: self._set_random_font_size()

        self.button2 = Button()
        self.button2.anchor = "midbottom"
        self.button2.position = Vector2(width / 2, height - 130)
        self.button2.text = "nope"
        self.button2.font_filepath = "res/fonts/Baloo-Cyrillic.ttf"
        self.button2.font_size = 48
        self.button2.callback = lambda: print("A")

        self.container = Container()
        self.container.add(self.label, self.button, self.button2)
    
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
        self._label_process(delta)

    def _graphics_process(self) -> None:
        self.app.graphics.clear(BACKGROUND)
        self.app.graphics.draw(self.scroll)
        self.app.graphics.draw(self.container)
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

    def _label_process(self, delta: float) -> None:
        self.label.offset = Vector2(
            math.cos(self.app.clock.get_ticks() / 1000) * 50,
            math.sin(self.app.clock.get_ticks() / 500) * 25
        )

    def _set_random_font_size(self) -> None:
        self.label.font_size = random.randint(16, 128)