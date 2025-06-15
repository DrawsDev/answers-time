import os
import json
import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import asset_path, load_asset
from src.framework.callback import Callback
from src.framework.explorer import Explorer
from src.framework.scene.ui import *
# TODO: КОСТЫЛЬ \/\/\/
from src.answerstime.quiz.utility import validate_quiz_from_file

class ExplorerFrame(Primitive):
    def __init__(self, app: Application, behavior: int = 0) -> None:
        super().__init__(app, SURFACE_SIZE, (0, 0), "topleft", 10)
        self._enabled = False
        self._explorer = Explorer()
        self._warn = WarnFrame(app, "«Файл» уже существует.", "Вы хотите заменить его?")
        self._layout = Layout(True)
        self._title = self._create_title_label()
        self._line = self._create_title_line()
        self._home = self._create_home_button()
        self._history_back = self._create_history_back_button()
        self._history_fore = self._create_history_fore_button()
        self._back = self._create_back_button()
        self._cancel = self._create_cancel_button()
        self._select = self._create_select_button()
        self._scroll = self._create_scroll_frame()
        self._layout.insert_child(
            self._title,
            self._line,
            self._home,
            self._history_back,
            self._history_fore,
            self._back,
            self._cancel,
            self._select,
            self._scroll
        )
        self._close_callback: Callback = Callback()
        
        self._behavior = behavior # TODO: КОСТЫЛЬ, ИЗБАВИТЬСЯ <===============
        self._path = ""
    
    @property
    def enabled(self) -> bool:
        return self._active
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        if self._enabled != value:
            self._enabled = value
            self._active = value
            if value:
                self._create_files_buttons()
            else:
                self._scroll.remove_child(self._scroll.children)

    @property
    def close_callback(self) -> Callback:
        return self._close_callback

    def _copy_and_close(self, source_path: str, destination_path: str) -> None:
        self._return()
        self._explorer.copy(source_path, destination_path)
        self._close()

    def _return(self) -> None:
        self._layout.enabled = True
        self._warn.enabled = False

    def _import_file(self, path: str, filename: str) -> None:
        if self._behavior == 0:
            if not validate_quiz_from_file(os.path.join(path, filename)):
                return
            if os.path.exists(asset_path(QUIZZES, filename)):
                self._layout.enabled = False
                self._warn.enabled = True
                self._warn.warn1 = f"«{filename}» уже существует."
                self._warn.confirm_callback.set((self._copy_and_close, (os.path.join(path, filename), asset_path(QUIZZES))))
                self._warn.deny_callback.set(self._return)
                return
            self._copy_and_close(os.path.join(path, filename), asset_path(QUIZZES))
        elif self._behavior == 1:
            self._path = os.path.join(path, filename)
            self._close()

    def move_to(self, path: str) -> None:
        self._explorer.move_to(path)
        self._back.text = self._explorer.current_path
        self._scroll.remove_child(self._scroll.children)
        self._create_files_buttons()

    def move_up(self) -> None:
        self._explorer.move_up()
        self._back.text = self._explorer.current_path
        self._scroll.remove_child(self._scroll.children)
        self._create_files_buttons()

    def move_home(self) -> None:
        self._explorer.move_home()
        self._back.text = self._explorer.current_path
        self._scroll.remove_child(self._scroll.children)
        self._create_files_buttons()

    def move_history_backward(self) -> None:
        self._explorer.move_history_backward()
        self._back.text = self._explorer.current_path
        self._scroll.remove_child(self._scroll.children)
        self._create_files_buttons()

    def move_history_forward(self) -> None:
        self._explorer.move_history_forward()
        self._back.text = self._explorer.current_path
        self._scroll.remove_child(self._scroll.children)
        self._create_files_buttons()

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)
            self._warn.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            surface.fill("black")
            self._layout.draw(surface)
            self._warn.draw(surface)
        else:
            self._active = False

    def _close(self) -> None:
        if self._enabled:
            self._enabled = False
            self._close_callback()

    def _create_files_buttons(self) -> None:
        for index, file in enumerate(self._explorer.list_content(target_extension=".json")):
            button = TextButton(
                app=self.app,
                text=file[0],
                size=(self._scroll.rect.width, 20),
                position=(self._scroll.rect.x, self._scroll.rect.y + 20 * index),
                anchor=Anchor.TopLeft,
                z_index=11,
                font_align=Align.Left,
                button_color=(0, 0, 0, 0),
                button_hover_color="#64646E",
                button_press_color="#000000",
                button_icon=load_asset(SPRITES, "explorer_dir.png") if file[1] == "dir" else load_asset(SPRITES, "explorer_quiz.png")
            )

            if file[1] == "dir":
                button.pressed_callback.set((self.move_to, (file[0],)))
            elif file[1] == "file":
                button.pressed_callback.set((self._import_file, (self._explorer.current_path, file[0])))

            self._scroll.insert_child(button)

    def _create_scroll_frame(self) -> ScrollFrame:
        scroll = ScrollFrame(
            app=self.app,
            size=(640 - 4, 276),
            position=(2, self._home.rect.bottom + 2),
            anchor=Anchor.TopLeft
        )
        scroll.enabled = True
        scroll.scrollbar_width = 15
        return scroll

    def _create_cancel_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="Отмена",
            size=(320 - 2, 30),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - 2),
            anchor=Anchor.BottomRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000"
        )
        button.pressed_callback = self._close
        return button

    def _create_select_button(self) -> TextButton:
        return TextButton(
            app=self.app,
            text="Выбрать",
            size=(320 - 2, 30),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - 2),
            anchor=Anchor.BottomLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000"
        )

    def _create_title_label(self) -> TextLabel:
        return TextLabel(
            app=self.app,
            text="ПРОВОДНИК",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color="#3CA4FF",
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        return Frame(
            app=self.app,
            color="#3CA4FF",
            size=(self.app.surface.get_width() - 10, 2),
            position=(self._title.rect.centerx, self._title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_home_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2, self._line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "explorer_home.png")
        )
        button.pressed_callback = self.move_home
        return button

    def _create_history_back_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2 + 30 + 2, self._line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "explorer_backward.png")
        )
        button.pressed_callback = self.move_history_backward
        return button

    def _create_history_fore_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2 + 30 + 2 + 30 + 2, self._line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "explorer_forward.png")
        )
        button.pressed_callback = self.move_history_forward
        return button

    def _create_back_button(self) -> TextButton:
        button = TextButton(
            app=self.app,
            text=self._explorer.current_path,
            size=(540, 30),
            position=(2, self._line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_align=Align.Left,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "explorer_up.png")
        )
        button.pressed_callback = self.move_up
        return button

__all__ = ["ExplorerFrame"]
