import os
import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import asset_path, load_asset
from src.framework.callback import Callback
from src.framework.explorer import Explorer
from src.framework.scene.ui import *

class ExplorerFrame(Primitive):
    def __init__(self, app: Application) -> None:
        super().__init__(app, SURFACE_SIZE, (0, 0), "topleft", 10)
        self._enabled = False
        self._explorer = Explorer()
        self._layout = Layout(True)
        self._create_title_label()
        self._create_title_line()
        self._create_cancel_button()
        self._create_confirm_button()
        self._create_file_textbox()
        self._create_home_button()
        self._create_history_back_button()
        self._create_history_fore_button()
        self._create_back_button()
        self._create_scroll_frame()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.home,
            self.history_back,
            self.history_fore,
            self.back,
            self.confirm,
            self.cancel,
            self.file_textbox,
            self.scroll
        )
        self._confirm_callback: Callback = Callback()
        self._cancel_callback: Callback = Callback()
        self._behavior = 0
    
    @property
    def enabled(self) -> bool:
        return self._active
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._active = value
        if value:
            self._create_file_lines()
        else:
            self.scroll.remove_child(self.scroll.children)

    @property
    def confirm_callback(self) -> Callback:
        return self._confirm_callback
    
    @property
    def cancel_callback(self) -> Callback:
        return self._cancel_callback

    def copy(self, source_path: str, destination_path: str) -> None:
        self._explorer.copy(source_path, destination_path)

    def open(self, behavior: int) -> None:
        if behavior == 0: # Импорт файла
            self.confirm.text = "Выбрать"
            self.file_textbox.text = ""
            self.file_textbox.textinput_enabled = False
            self.confirm.pressed_callback.set()
            self._behavior = behavior
            self.enabled = True
        elif behavior == 1: # Экспорт файла
            self.confirm.text = "Сохранить"
            self.file_textbox.text = ""
            self.file_textbox.textinput_enabled = True
            self.confirm.pressed_callback.set(self._export_confirm)
            self._behavior = behavior
            self.enabled = True

    def move_to(self, path: str) -> None:
        self._explorer.move_to(path)
        self.back.text = self._explorer.current_path
        self.scroll.remove_child(self.scroll.children)
        self._create_file_lines()

    def move_up(self) -> None:
        self._explorer.move_up()
        self.back.text = self._explorer.current_path
        self.scroll.remove_child(self.scroll.children)
        self._create_file_lines()

    def move_home(self) -> None:
        self._explorer.move_home()
        self.back.text = self._explorer.current_path
        self.scroll.remove_child(self.scroll.children)
        self._create_file_lines()

    def move_history_backward(self) -> None:
        self._explorer.move_history_backward()
        self.back.text = self._explorer.current_path
        self.scroll.remove_child(self.scroll.children)
        self._create_file_lines()

    def move_history_forward(self) -> None:
        self._explorer.move_history_forward()
        self.back.text = self._explorer.current_path
        self.scroll.remove_child(self.scroll.children)
        self._create_file_lines()

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._layout.draw(surface)
        else:
            self._active = False

    def _cancel(self) -> None:
        self._enabled = False
        self._cancel_callback()

    def _confirm(self, path: str, filename: str) -> None:
        self._enabled = False
        self._confirm_callback(path, filename)

    def _export_confirm(self) -> None:
        if len(self.file_textbox.text) > 0:
            self._enabled = False
            self._confirm_callback(self._explorer.current_path)

    def _select_file(self, path: str, filename: str) -> None:
        if self._behavior == 0:
            filepath = os.path.join(path, filename)
            self.file_textbox.text = filepath
            self.confirm.pressed_callback.set((self._confirm, (path, filename)))

    def _create_file_lines(self) -> None:
        if self._behavior == 0:
            target = ".json"
        elif self._behavior == 1:
            target = ".NOPE"

        for index, file in enumerate(self._explorer.list_content(target_extension=target)):
            button = TextButton(
                app=self.app,
                text=file[0],
                size=(self.scroll.rect.width, 20),
                position=(self.scroll.rect.x, self.scroll.rect.y + 20 * index),
                anchor=Anchor.TopLeft,
                z_index=11,
                font_align=Align.Left,
                text_color=Pallete.White,
                button_color=Pallete.Black,
                button_hover_color=Pallete.Gray1,
                button_press_color=Pallete.Gray3,
                button_icon=load_asset(SPRITES, "explorer_dir.png") if file[1] == "dir" else load_asset(SPRITES, "explorer_quiz.png")
            )

            if file[1] == "dir":
                button.pressed_callback.set((self.move_to, (file[0],)))
            elif file[1] == "file":
                if self._behavior == 0:
                    button.pressed_callback.set((self._select_file, (self._explorer.current_path, file[0])))
        
            self.scroll.insert_child(button)

    def _create_title_label(self) -> None:
        self.title = TextLabel(
            app=self.app,
            text="Проводник",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> None:
        self.title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_scroll_frame(self) -> ScrollFrame:
        self.scroll = ScrollFrame(
            app=self.app,
            size=(640 - 4, 268),
            position=(2, self.home.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            scrollbar_width=15,
            backcolor=Pallete.Empty
        )
        self.scroll.enabled = True

    def _create_cancel_button(self) -> None:
        self.cancel = TextButton(
            app=self.app,
            text="Отмена",
            size=(130, 30),
            position=(self.app.surface.get_width() - 2, self.app.surface.get_height() - 2),
            anchor=Anchor.BottomRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3
        )
        self.cancel.pressed_callback = self._cancel

    def _create_confirm_button(self) -> None:
        self.confirm = TextButton(
            app=self.app,
            text="Выбрать",
            size=(130, 30),
            position=(self.cancel.rect.left - 2, self.app.surface.get_height() - 2),
            anchor=Anchor.BottomRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3
        )

    def _create_file_textbox(self) -> None:
        self.file_textbox = TextBox(
            app=self.app,
            text="",
            placeholder="Имя файла",
            size=(372, 30),
            position=(2, self.app.surface.get_height() - 2),
            anchor=Anchor.BottomLeft,
            z_index=10,
        )
        self.file_textbox.textinput_enabled = False

    def _create_home_button(self) -> TextButton:
        self.home = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2, self.title_line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "explorer_home.png")
        )
        self.home.pressed_callback = self.move_home

    def _create_history_back_button(self) -> TextButton:
        self.history_back = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2 + 30 + 2, self.title_line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "explorer_backward.png")
        )
        self.history_back.pressed_callback = self.move_history_backward

    def _create_history_fore_button(self) -> TextButton:
        self.history_fore = TextButton(
            app=self.app,
            text="",
            size=(30, 30),
            position=(2 + 540 + 2 + 30 + 2 + 30 + 2, self.title_line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "explorer_forward.png")
        )
        self.history_fore.pressed_callback = self.move_history_forward

    def _create_back_button(self) -> TextButton:
        self.back = TextButton(
            app=self.app,
            text=self._explorer.current_path,
            size=(540, 30),
            position=(2, self.title_line.rect.bottom + 2),
            anchor=Anchor.TopLeft,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "explorer_up.png")
        )
        self.back.pressed_callback = self.move_up
