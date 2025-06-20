import pygame
from typing import Tuple
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class MatchingAnswer(Primitive):
    def __init__(        
        self, 
        app: Application,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        super().__init__(app, (150, 185), position, anchor, 1)
        self._create_move_1_button()
        self._create_move_2_button()
        self._create_text_1_label()
        self._create_text_2_label()
        self._create_icon_1_label()
        self._create_icon_2_label()
        self._layout: Layout = Layout(False)
        self._layout.insert_child(self.move_1, self.move_2)
        self._update_image()

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._layout.enabled:
            self._layout.update(delta)
        else:
            self.text_1.update(delta)
            self.text_2.update(delta)
            self.icon_1.update(delta)
            self.icon_2.update(delta)
    
    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        if self._layout.enabled:
            self._layout.draw(surface)
        else:
            self.text_1.draw(surface)
            self.text_2.draw(surface)
            self.icon_1.draw(surface)
            self.icon_2.draw(surface)
            # surface.blit(self.icon_1.image, self.icon_1.rect)
            # surface.blit(self.icon_2.image, self.icon_2.rect)
            surface.blit(self.text_1.image, self.text_1.rect)
            surface.blit(self.text_2.image, self.text_2.rect)

    def on_mouse_enter(self) -> None:
        self._layout.enabled = True

    def on_mouse_leave(self) -> None:
        self._layout.enabled = False

    def change_number(self, value: int = 1, index: int = 0) -> None:
        nums = ("editor_one.png", "editor_two.png", "editor_three.png")
        if 0 < value < 4:
            if index == 0:
                self.icon_1.image_path = asset_path(SPRITES, nums[value - 1])
            if index == 1:
                self.icon_2.image_path = asset_path(SPRITES, nums[value - 1])

    def _update_image(self):
        super()._update_image()
        pygame.draw.rect(self.image, Pallete.White, ((0, 0), self.size), 0, 6)
        pygame.draw.rect(self.image, Pallete.ATBlue1, (0, 0, self.rect.width, 80), 0, -1, 6, 6)
        pygame.draw.polygon(self.image, Pallete.ATBlue1, [(0, 80), (self.rect.width / 2, 110), (self.rect.width, 80)])
    
    def _create_move_1_button(self) -> None:
        self.move_1 = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(self.rect.centerx, self.rect.centery - self.rect.height / 4),
            anchor=Anchor.Center,
            z_index=3,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "editor_prev.png"),
            button_border_radius=6
        )

    def _create_move_2_button(self) -> None:
        self.move_2 = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(self.rect.centerx, self.rect.centery + self.rect.height / 4),
            anchor=Anchor.Center,
            z_index=3,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "editor_prev.png"),
            button_border_radius=6
        )

    def _create_text_1_label(self) -> None:
        self.text_1 = TextLabel(
            app=self.app,
            text="test",
            position=(self.rect.centerx, self.rect.centery - self.rect.height / 4),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.ATBlue5,
            text_wraplength=self.rect.width
        )

    def _create_text_2_label(self) -> None:
        self.text_2 = TextLabel(
            app=self.app,
            text="test",
            position=(self.rect.centerx, self.rect.centery + self.rect.height / 4),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.ATBlue5,
            text_wraplength=self.rect.width
        )

    def _create_icon_1_label(self) -> None:
        self.icon_1 = ImageLabel(
            app=self.app,
            path=None,
            position=self.rect.topright,
            anchor=Anchor.TopRight,
            z_index=1
        )

    def _create_icon_2_label(self) -> None:
        self.icon_2 = ImageLabel(
            app=self.app,
            path=None,
            position=(self.rect.right, self.rect.centery),
            anchor=Anchor.TopRight,
            z_index=1
        )
