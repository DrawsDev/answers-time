import math
import random

from src.core import *
from src.objects import *
from src.utils import *

BACKGROUND = Color("#000D2C")


class Test(Scene):
    def on_enter(self, **kwargs) -> None:
        width, height = self.app.window.get_mode()
        pattern_surface = graphics.load_surface("res/textures/pattern1.png")

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
        self._fullscreen_key_handler()
        self._objects_process(delta)
        self._graphics_process()

    def _objects_process(self, delta: float) -> None:
        self.scroll.process(delta)
        self.container.process(delta)
        self.label.theme.font_color = rainbow(s=50.0)

    def _graphics_process(self) -> None:
        surface = self.app.window.get_surface()
        self.scroll.draw(surface)
        self.container.draw(surface)
        self._debug_info_process()

    def _debug_info_process(self) -> None:
        wrapper_version = get_wrapper_version().as_text()
        version = self.app.get_version().as_text()
        graphics.print(get_pygame_welcome_message(), 0, 0)
        graphics.print(f"Wrapper v{wrapper_version}", 0, 20)
        graphics.print(f"Answers Time v{version}", 0, 40)
        graphics.print(f"FPS: {self.app.clock.get_framerate()}", 0, 60)
        graphics.print(f"WMP: {mouse.get_position()}", 0, 80)

    def _fullscreen_key_handler(self) -> None:
        if (
            keyboard.is_just_pressed("f11")
            or keyboard.is_just_pressed("return")
            and keyboard.is_modifier_active("alt")
        ):
            if self.app.window.is_fullscreen():
                self.app.window.set_windowed()
            else:
                self.app.window.set_fullscreen()
