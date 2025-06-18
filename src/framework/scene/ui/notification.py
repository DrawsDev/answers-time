import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.callback import *
from src.framework.scene.ui import *

class Notification(Primitive):
    def __init__(
        self, 
        app: Application, 
        info: str = "Info",
        confirm_callback: CallbackType = None
    ) -> None:
        super().__init__(app, SURFACE_SIZE, z_index=20)
        self._active = False
        self._enabled = False
        self._layout = Layout(False)
        self._confirm_callback = Callback(confirm_callback)
        self._create_info_label(info)
        self._create_title_line()
        self._create_title_label()
        self._create_confirm_button()
        self._layout.insert_child(
            self._title,
            self._title_line,
            self._info,
            self._confirm
        )

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
    def info_text(self) -> str:
        return self._info.text
    
    @info_text.setter
    def info_text(self, value: str) -> None:
        if self._info.text != value:
            self._info.text = value

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            surface.fill("black")
            self._layout.draw(surface)

    def _create_title_label(self) -> TextLabel:
        self._title = TextLabel(
            app=self.app,
            text="Уведомление",
            position=(self._title_line.rect.centerx, self._title_line.rect.top),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self._title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() / 2, 2),
            position=(self._info.rect.centerx, self._info.rect.top - 4),
            anchor=Anchor.MidBottom
        )

    def _create_info_label(self, text: str = "") -> TextLabel:
        self._info = TextLabel(
            app=self.app,
            text=text,
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self._size[0]
        )

    def _create_confirm_button(self) -> TextButton:
        self._confirm = TextButton(
            app=self.app,
            text="ОК",
            size=(130, 40),
            position=(self._info.rect.centerx, self._info.rect.bottom + 10),
            anchor=Anchor.MidTop,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "warn_confirm.png")
        )
        self._confirm.pressed_callback.set(self._confirm_callback)
