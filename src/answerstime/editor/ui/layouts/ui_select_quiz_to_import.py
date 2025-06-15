import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.callback import Callback
from src.framework.utility import *
from src.framework.scene.ui import *
from src.answerstime.menu.ui import QuizButton
from src.answerstime.quiz import create_quiz_from_file

GAP = 4

class UISelectQuizToImport:
    def __init__(self, app: Application) -> None:
        self.app = app
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
            app=self.app,
            text="Импорт из существующего теста",
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
            text="Назад",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
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
            app=self.app,
            size=(self.app.surface.get_width() - GAP * 2, 260),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
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
                app=self.app,
                position=(self.scroll_frame.rect.width / 2, self.scroll_frame.rect.y + (80 + GAP) * index),
                anchor=Anchor.MidTop,
                z_index=1,
                title=quiz.title,
                filename=value
            )
            button.pressed_callback.set((callback, (asset_path(QUIZZES, value),)))
            self.scroll_frame.insert_child(button)
