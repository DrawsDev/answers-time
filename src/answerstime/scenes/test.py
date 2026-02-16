from src.core import Scene, Vector2
from src.core.objects import ScrollingBackground, Sprite

BACKGROUND = "#a0a0a0"
SPEED = 100

class Test(Scene):
    def on_enter(self, **kwargs) -> None:
        width, height = self.app.window.get_mode()
        sprite_surface = self.app.graphics.load_surface("res/textures/dev.png")
        pattern_surface = self.app.graphics.load_surface("res/textures/pattern.png")

        self.sprite = Sprite(sprite_surface)
        self.sprite.position = Vector2(width / 2, height / 2)

        self.scroll = ScrollingBackground(pattern_surface)
        self.scroll.angle = 15
        self.scroll.speed = 100
    
    def on_exit(self, **kwargs) -> None:
        pass
    
    def process(self, delta: float) -> None:
        self._objects_process(delta)
        self._graphics_process()

    def _objects_process(self, delta: float) -> None:
        self._sprite_process(delta)
        self.scroll.process(delta)

    def _graphics_process(self) -> None:
        self.app.graphics.clear(BACKGROUND)
        self.app.graphics.draw(self.scroll)
        self.app.graphics.draw(self.sprite)
        self._fps_counter_process()

    def _fps_counter_process(self) -> None:
        framerate = self.app.window.get_framerate()
        self.app.graphics.print(str(framerate))

    def _sprite_process(self, delta: float) -> None:
        velocity = Vector2(
            self.app.keyboard.get_axis("a", "d"),
            self.app.keyboard.get_axis("w", "s")
        )

        if velocity.length() > 0:
            velocity = velocity.normalize()

        self.sprite.position += velocity * SPEED * delta
