import os
import pygame
from pygame.math import Vector2
from src.settings import *
from src.core.game import Game
from src.core.utility import path
from src.components.scene import Scene
from src.components.sprite import *
from src.components.cursor import Cursor
from src.components.dialogue import Dialogue
from src.components.line import parse_string
from src.ui.debug_frame import DebugFrame

class Intro(Scene):
    def __init__(self, game: Game) -> None:
        super().__init__()

        self.debug_frame = DebugFrame(game)

        etu_img = pygame.image.load(path(os.path.join(SPRITES, "etu_1.png")))
        etu_img.set_colorkey("Black")
        self.sprite = Sprite(etu_img, (320, 250), Anchor.Center)
        self.sprite.add(self.sprites)

        hand = pygame.image.load(path(os.path.join(SPRITES, "hand_1.png")))
        hand.set_colorkey("Black")
        self.cursor = Cursor(hand, (0, 0))
        self.cursor.add(self.sprites)

        self.dialogue = Dialogue()
        self.test_dialogue_pos = Vector2(640 / 2, 360 / 2)
        self.test_dialogue_index = 0
        self.test_dialogue = [
            # parse_string("<f color=White flash=Grey wobble=True>Привет мир!</f>"),
            # parse_string("<f rgb=True pause=1>Привет! </f><f color=White typing_speed=0.3>Как </f><f color=Lime flash=Orange wobble=True>дела</f><f color=White typing_speed=0.5>?</f>"),
            # parse_string("<f color=Red typing_speed=0.1>Погоди... </f><f angry=1 pause=0.5>ТЫ... </f><f angry=2 pause=0.75>КТО???</f>"),
            parse_string("<f color=Red gradient=Yellow wave=True typing_speed=0>ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ</f>"),
            parse_string("<f color=White speed=0.1>Ладно... </f><f angry=1 pause=0.3>ЛАДНО. </f><f color=White pause=0.5>как </f><f rgb=True pause=0.5>дела</f><f color=White pause=0.5>?</f>"),
            parse_string("<f rgb=True>О! </f><f color=White pause=1>Тут есть некоторые диалоги из </f><f color=Cyan flash=Blue wave=True>Katana ZERO</f>"),
            parse_string("<f color=White typing_speed=0.02>На месте?</f>"),
            parse_string("<f color=Orange typing_speed=0.02>Такого шанса </f><f color=White typing_speed=0.02>второй раз не будет. </f><f color=White typing_speed=0.02 pause=0.3>Действовать нужно </f><f color=Yellow typing_speed=0.02>максимально быстро.</f>"),
            parse_string("<f color=White typing_speed=0.02>Самое главное. </f><f angry=1 pause=0.2>Не должно быть </f><f angry=1 pause=0.5>никаких </f><f angry=1 pause=0.5>свидетелей.</f>"),
            parse_string("<f color=White>Да, </f><f color=White pause=0.3>там что-то про </f><f color=Red wave=True>заговоры, хунту, такое, </f><f color=White pause=0.3>да?</f>"),
            parse_string("<f color=Cyan shake=0.55 typing_speed=0.02>Вроде как дело-то серьёзное... </f><f color=White pause=0.3 typing_speed=0.02>Может, надо </f><f color=Orange typing_speed=0.02>удвоить патрулирование</f><f color=White typing_speed=0.02>?</f>"),
            parse_string("<f color=White>Да ладно, </f><f color=Cyan pause=0.3>что может пойти не так?</f>"),
            parse_string("<f color=#505050 quiet=True speed=0>(Если че их потом дакнули :P)</f>"),
            parse_string("<f color=White>А </f><f rgb=True>всё! </f><f color=White pause=0.5>Больше ничего не скажу.</f>"),
            parse_string("<f angry=1>ы</f>")
        ]

    def update(self, delta: float) -> None:
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_RETURN]:
            if self.dialogue.finished:
                self.test_dialogue_index += 1
                if self.test_dialogue_index > len(self.test_dialogue) - 1:
                    self.test_dialogue_index = 0
            else:
                self.dialogue.skip_typing()
        
        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((180, 180, 180))

        super().draw(surface)

        self.debug_frame.draw(surface)
        self.dialogue.render_lines(self.test_dialogue[self.test_dialogue_index], (self.sprite.position[0], self.sprite.position[1] - self.sprite.image.get_height() / 2), surface)
