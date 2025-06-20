import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.callback import *
from src.framework.scene.ui import *

class Warning(Primitive):
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
        
        self._create_background()
        self._create_window()
        self._create_warning_label()
        self._warn1 = self._create_warn_1_label(warn1)
        self._warn2 = self._create_warn_2_label(warn2)
        self._create_confirm_button()
        self._create_deny_button()
        
        self._layout.insert_child(
            self._warning, 
            self._warn1, 
            self._warn2, 
            self._confirm, 
            self._deny
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
            surface.blit(self._background)
            surface.blit(self.image, self.rect)
            self._layout.draw(surface)

    def _create_background(self) -> None:
        self._background = pygame.Surface(SURFACE_SIZE)
        self._background.fill(Pallete.ATRed5)
        self._background.set_alpha(200)

    def _create_window(self) -> None:
        self.image = pygame.Surface((337, 215))
        self.rect = self.image.get_rect(center=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2))
        pygame.draw.rect(self.image, Pallete.ATRed3, ((0, 0), self.image.get_size()), 0, 6)
        pygame.draw.rect(self.image, Pallete.White, ((4, 52 - 4), (329, 163)), 0, 6)

    def _create_warning_label(self) -> None:
        self._warning = TextLabel(
            app=self.app,
            text="Предупреждение",
            position=(self.rect.centerx, self.rect.y + 26),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.rect.width
        )

    def _create_warn_1_label(self, text: str = "") -> TextLabel:
        warn = TextLabel(
            app=self.app,
            text=text,
            position=(self.rect.centerx, self.rect.y + 52),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.Black,
            text_wraplength=self.rect.width
        )
        return warn

    def _create_warn_2_label(self, text: str = "") -> TextLabel:
        warn = TextLabel(
            app=self.app,
            text=text,
            position=(self._warn1.rect.centerx, self._warn1.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.ATRed3,
            text_wraplength=self.rect.width
        )
        return warn

    def _create_confirm_button(self) -> None:
        self._confirm = TextButton(
            app=self.app,
            text="Да",
            size=(130, 40),
            position=(self.rect.centerx - 2, self.rect.bottom - 8),
            anchor=Anchor.BottomRight,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATRed3,
            button_hover_color=Pallete.ATRed2,
            button_press_color=Pallete.ATRed4,
            button_border_radius=6,
            button_icon=load_asset(SPRITES, "warn_confirm.png")
        )
        self._confirm.pressed_callback.set(self._confirm_callback)

    def _create_deny_button(self) -> None:
        self._deny = TextButton(
            app=self.app,
            text="Нет",
            size=(130, 40),
            position=(self.rect.centerx + 2, self.rect.bottom - 8),
            anchor=Anchor.BottomLeft,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.LightGray3,
            button_hover_color=Pallete.LightGray2,
            button_press_color=Pallete.LightGray4,
            button_border_radius=5,
            button_icon=load_asset(SPRITES, "warn_deny.png")
        )
        self._deny.pressed_callback.set(self._deny_callback)
