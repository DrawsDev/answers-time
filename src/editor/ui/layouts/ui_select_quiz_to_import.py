import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.callback import Callback
from src.core.utility import load_asset, asset_path
from src.ui.layout import Layout
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.scroll_frame import ScrollFrame
from src.ui.frame import Frame
from src.ui.explorer_frame import ExplorerFrame
from src.menu.ui.quiz_button import QuizButton
from src.quiz.utility import create_quiz_from_file

GAP = 4

class UISelectQuizToImport:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = False
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_scroll_frame()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.scroll_frame
        )
    
    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._layout.enabled = value
        self.scroll_frame.enabled = value

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._layout.draw(surface)

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            game=self.game,
            text="Импорт из существующего теста",
            position=(self.game.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.game.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            game=self.game,
            color=Pallete.White,
            size=(self.game.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_scroll_frame(self) -> None:
        self.scroll_frame = ScrollFrame(
            game=self.game,
            size=(self.game.surface.get_width() - GAP * 2, 260),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center,
            z_index=-1,
            backcolor=Pallete.Empty,
            scrollbar_width=15
        )

    def create_buttons(self, callback: Callback) -> None:
        self.scroll_frame.remove_child(self.scroll_frame.children)

        files = [file for file in os.listdir(asset_path(QUIZZES)) if file.endswith(".json")]
        for index, value in enumerate(files):
            quiz = create_quiz_from_file(asset_path(QUIZZES, value))
            button = QuizButton(
                game=self.game,
                position=(self.scroll_frame.rect.width / 2, self.scroll_frame.rect.y + (80 + GAP) * index),
                anchor=Anchor.MidTop,
                z_index=1,
                title=quiz.title,
                filename=value
            )
            button.pressed_callback.set((callback, (asset_path(QUIZZES, value),)))
            self.scroll_frame.insert_child(button)

__all__ = ["UISelectQuizToImport"]
