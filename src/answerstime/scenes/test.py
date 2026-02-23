import math

from src.core import Scene
from src.core.common import *
from src.core.objects import *

BACKGROUND = "#a0a0a0"
SPEED = 500

class Test(Scene):
    def on_enter(self, **kwargs) -> None:
        width, height, _ = self.app.window.get_mode()
        sprite_surface = self.app.graphics.load_surface("res/textures/dev.png")
        pattern_surface = self.app.graphics.load_surface("res/textures/pattern.png")

        self.sprite = Sprite(sprite_surface)
        self.sprite.position = Vector2(width / 2, height / 2)

        self.scroll = ScrollingBackground(pattern_surface)
        self.scroll.angle = 15
        self.scroll.speed = 100

        self.label = Label()
        self.label.anchor = "center"
        self.label.position = Vector2(width / 2, 100)
        self.label.text = "Hello World!"
        self.label.font_filepath = "res/fonts/Ramona-Bold.ttf"
        self.label.font_size = 60
    
    def on_exit(self, **kwargs) -> None:
        pass
    
    def event(self, event: Event) -> None:
        pass

    def process(self, delta: float) -> None:
        self._objects_process(delta)
        self._graphics_process()

    def _objects_process(self, delta: float) -> None:
        self._sprite_process(delta)
        self._label_process(delta)
        self.scroll.process(delta)

    def _graphics_process(self) -> None:
        self.app.graphics.clear(BACKGROUND)
        self.app.graphics.draw(self.scroll)
        self.app.graphics.draw(self.sprite)
        self.app.graphics.draw(self.label)
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
            math.cos(self.app.clock.get_ticks() / 500) * 50,
            math.sin(self.app.clock.get_ticks() / 250) * 25
        )

    def _sprite_process(self, delta: float) -> None:
        velocity = Vector2(
            self.app.keyboard.get_axis("a", "d"),
            self.app.keyboard.get_axis("w", "s")
        )

        if velocity.length() > 0:
            velocity = velocity.normalize()

        self.sprite.position += velocity * SPEED * delta
