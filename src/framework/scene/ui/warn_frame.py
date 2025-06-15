import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.callback import *
from src.framework.scene.ui import *

class WarnFrame(Primitive):
    def __init__(
        self, 
        app: Application, 
        warn1: str = "Warn 1", 
        warn2: str = "Warn 2",
        confirm_callback: CallbackType = None,
        deny_callback: CallbackType = None
    ) -> None:
        super().__init__(app, SURFACE_SIZE, z_index=20)
        self._active = False
        self._enabled = False
        self._layout = Layout(False)
        self._confirm_callback = Callback(confirm_callback)
        self._deny_callback = Callback(deny_callback)
        self._warn1 = self._create_warn_1_label(warn1)
        self._warn2 = self._create_warn_2_label(warn2)
        self._confirm = self._create_confirm_button()
        self._deny = self._create_deny_button()
        self._layout.insert_child(self._warn1, self._warn2, self._confirm, self._deny)

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        if self._enabled != value:
            self._enabled = value
            self._active = value
            self._layout.enabled = value

    @property
    def confirm_callback(self) -> Callback:
        return self._confirm_callback

    @property
    def deny_callback(self) -> Callback:
        return self._deny_callback

    @property
    def warn1(self) -> str:
        return self._warn1.text
    
    @warn1.setter
    def warn1(self, value: str) -> None:
        if self._warn1.text != value:
            self._warn1.text = value

    @property
    def warn2(self) -> str:
        return self._warn2.text
    
    @warn2.setter
    def warn2(self, value: str) -> None:
        if self._warn2.text != value:
            self._warn2.text = value

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            surface.fill("black")
            self._layout.draw(surface)

    def _create_warn_1_label(self, text: str = "") -> TextLabel:
        warn = TextLabel(
            app=self.app,
            text=text,
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 - 20),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self._size[0]
        )
        return warn

    def _create_warn_2_label(self, text: str = "") -> TextLabel:
        warn = TextLabel(
            app=self.app,
            text=text,
            position=(self._warn1.rect.centerx, self._warn1.rect.bottom + 10),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="red",
            text_wraplength=self._size[0]
        )
        return warn

    def _create_confirm_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="Да",
            size=(130, 40),
            position=(self._warn2.rect.centerx - 2, self._warn2.rect.bottom + 10),
            anchor=Anchor.TopRight,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "warn_confirm.png")
        )
        button.pressed_callback.set(self._confirm_callback)
        return button

    def _create_deny_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="Нет",
            size=(130, 40),
            position=(self._warn2.rect.centerx + 2, self._warn2.rect.bottom + 10),
            anchor=Anchor.TopLeft,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "warn_deny.png")
        )
        button.pressed_callback.set(self._deny_callback)
        return button
