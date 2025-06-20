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
        
        self._create_background()
        self._create_window()
        self._create_notification_label()
        self._create_info_label(info)
        self._create_confirm_button()

        self._layout.insert_child(
            self._notification,
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
            surface.blit(self._background)
            surface.blit(self.image, self.rect)
            self._layout.draw(surface)

    def _create_background(self) -> None:
        self._background = pygame.Surface(SURFACE_SIZE)
        self._background.fill(Pallete.ATBlue5)
        self._background.set_alpha(200)

    def _create_window(self) -> None:
        self.image = pygame.Surface((337, 172))
        self.rect = self.image.get_rect(center=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2))
        pygame.draw.rect(self.image, Pallete.ATBlue2, ((0, 0), self.image.get_size()), 0, 6)
        pygame.draw.rect(self.image, Pallete.White, ((4, 52 - 4), (329, 120)), 0, 6)

    def _create_notification_label(self) -> None:
        self._notification = TextLabel(
            app=self.app,
            text="Уведомление",
            position=(self.rect.centerx, self.rect.y + 24),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.rect.width
        )

    def _create_info_label(self, text: str = "") -> None:
        self._info = TextLabel(
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

    def _create_confirm_button(self) -> None:
        self._confirm = TextButton(
            app=self.app,
            text="ОК",
            size=(130, 40),
            position=(self.rect.centerx - 2, self.rect.bottom - 8),
            anchor=Anchor.MidBottom,
            z_index=21,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_border_radius=6,
            button_icon=load_asset(SPRITES, "warn_confirm.png")
        )
        self._confirm.pressed_callback.set(self._confirm_callback)
