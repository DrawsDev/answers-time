import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIResult:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)

        self._create_window()
        self._create_grade_label()
        self._create_info_1_label()
        self._create_info_2_label()
        self._create_info_3_label()
        self._create_info_4_label()
        self._create_back_button()

        self._layout.insert_child(
            self.grade,
            self.info,
            self.info2,
            self.info3,
            self.info4,
            self.back
        )
    
    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._layout.enabled = value

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            surface.blit(self.window, self.window_rect)
            self._layout.draw(surface)

    def _create_window(self) -> None:
        self.window = pygame.Surface((337, 225))
        self.window_rect = self.window.get_rect(center=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2))
        pygame.draw.rect(self.window, Pallete.ATBlue3, ((0, 0), self.window.get_size()), 0, 6)
        pygame.draw.rect(self.window, Pallete.White, ((4, 62 - 4), (329, 163)), 0, 6)

    def _create_grade_label(self) -> None:
        self.grade = TextLabel(
            app=self.app,
            text="0",
            position=(self.window_rect.centerx, self.window_rect.top - GAP - GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=55,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.window_rect.width
        )

    def _create_info_1_label(self) -> None:
        self.info = TextLabel(
            app=self.app,
            text="Отвеченных вопросов: 0 из 0",
            position=(self.window_rect.left + GAP * 2, self.grade.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.Black,
            text_wraplength=self.window_rect.width
        )

    def _create_info_2_label(self) -> None:
        self.info2 = TextLabel(
            app=self.app,
            text="Правильных ответов: 0",
            position=(self.window_rect.left + GAP * 2, self.info.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.Black,
            text_wraplength=self.window_rect.width
        )

    def _create_info_3_label(self) -> None:
        self.info3 = TextLabel(
            app=self.app,
            text="Неправильных ответов: 0",
            position=(self.window_rect.left + GAP * 2, self.info2.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.Black,
            text_wraplength=self.window_rect.width
        )

    def _create_info_4_label(self) -> None:
        self.info4 = TextLabel(
            app=self.app,
            text="Время выполнения тестирования: 00:00:00",
            position=(self.window_rect.left + GAP * 2, self.info3.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.Black,
            text_wraplength=self.window_rect.width
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
            button_icon=load_asset(SPRITES, "exit.png"),
            button_border_radius=6
        )
