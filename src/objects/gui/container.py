from typing import Iterable, List, Optional, Tuple, Union

import pygame

from src.core.graphics import Drawable
from src.objects.gui import Element


class Container(Drawable):
    def __init__(self) -> None:
        self._elements: List[Element] = []
        self._captured: Optional[Element] = None

    def add(self, *elements: Union[Element, Iterable[Element]]) -> None:
        for element in elements:
            if isinstance(element, Element):
                if not self.has(element):
                    self._elements.append(element)
            else:
                try: # yeah
                    self.add(*element)
                except:
                    pass

    def remove(self, *elements: Union[Element, Iterable[Element]]) -> None:
        for element in elements:
            if isinstance(element, Element):
                if self.has(element):
                    self._elements.remove(element)
            else:
                try: # nah..
                    self.remove(*element)
                except:
                    pass

    def clear(self) -> None:
        self._elements.clear()

    def has(self, element: Element) -> bool:
        return element in self._elements

    def find_element_at_point(self, point: Tuple[int, int]) -> Optional[Element]:
        for element in reversed(self._elements):
            if element.has_point(point):
                return element

    def get_captured(self) -> Optional[Element]:
        return self._captured

    def get_children(self) -> List[Element]:
        return self._elements

    def draw(self, surface: pygame.Surface) -> None:
        for element in self._elements:
            element.draw(surface)

    def event(self, event: pygame.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            element = self.find_element_at_point(event.pos)
            if not self._captured and element:
                self._captured = element
                self._captured.event(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self._captured:
                self._captured.event(event)
                self._captured = None

    def process(self, delta: float) -> None:
        for element in self._elements:
            element.process(delta)
            if element != self._captured:
                element.hovered = False

        point = pygame.mouse.get_pos()
        element = self.find_element_at_point(point)
        if element:
            element.hovered = True
