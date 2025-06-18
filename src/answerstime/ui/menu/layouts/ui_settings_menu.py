from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *
from src.answerstime.ui import Checkbox
from src.answerstime.utility import *

GAP = 4

class UISettingsMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_frame()
        self._create_fullscreen_label()
        self._create_fullscreen_checkbox()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.frame,
            self.fullscreen_label,
            self.fullscreen_checkbox
        )

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._layout.enabled = value
        if value:
            fullscreen = self.app.settings.get("Fullscreen", True)
            self.fullscreen_checkbox.value = fullscreen

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._layout.draw(surface)

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            app=self.app,
            text="Настройки",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
        )
    
    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Вернуться в меню",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "back.png"),
            button_border_radius=6
        )

    def _create_frame(self) -> None:
        self.frame = Frame(
            app=self.app,
            color=Pallete.ATBlue3,
            size=(340, 140),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
            anchor=Anchor.Center,
            z_index=0,
            border_width=4,
            border_radius=6
        )

    def _create_fullscreen_label(self) -> None:
        self.fullscreen_label = TextLabel(
            app=self.app,
            text="Полноэкранный режим",
            position=(self.app.surface.get_width() / 2 - 30, self.app.surface.get_height() / 2),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_fullscreen_checkbox(self) -> None:
        self.fullscreen_checkbox = Checkbox(
            app=self.app,
            size=(34, 34),
            position=(self.app.surface.get_width() / 2 + 80, self.fullscreen_label.rect.centery),
            anchor=Anchor.MidLeft,
            button_border_radius=6,
            z_index=2
        )
        self.fullscreen_checkbox.pressed_callback.set(self._update_fullscreen_setting)

    def _update_fullscreen_setting(self) -> None:
        self.app.update_setting("Fullscreen", self.fullscreen_checkbox.value)
