import random
from copy import deepcopy
from typing import Dict, List, Any

class Question:
    def __init__(
        self,
        title: str = "Текст вопроса",
        type: int = 0,
        options: List[str] = ["Текст ответа"],
        answers: List[int] = [],
        tip: str = "Подсказка не указана."
    ) -> None:
        self._title = title
        self._type = type
        self._options = deepcopy(options)
        self._answers = deepcopy(answers)
        self._tip = tip
        self._shuffle()

    def _shuffle(self) -> None:
        if self._type in (0, 1, 3):
            while True:
                self._shuffle_options = random.sample(self._options, len(self._options))
                if len(self._options) <= 1:
                    break
                if all(v == self._options[0] for v in self._options):
                    break
                if self._shuffle_options != self._options:
                    break
        elif self._type == 2:
            return
        elif self._type == 4:
            while True:
                self._shuffle_options = random.sample(self._options, len(self._options))
                self._shuffle_answers = random.sample(self._answers, len(self._answers))
                if len(self._options) <= 1:
                    break
                if all(v == self._options[0] for v in self._options):
                    break
                if all(v == self._answers[0] for v in self._answers):
                    break
                if self._shuffle_options != self._options and self._shuffle_answers != self._answers:
                    break

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if self._title != value:
            self._title = value

    @property
    def type(self) -> int:
        return self._type

    @type.setter
    def type(self, value: int) -> None:
        if self._type != value:
            self._type = value

    @property
    def options(self) -> List[str]:
        return self._options

    @options.setter
    def options(self, value: List[str]) -> None:
        if self._options != value:
            self._options = value

    @property
    def shuffle_options(self) -> List[str]:
        return self._shuffle_options

    @shuffle_options.setter
    def shuffle_options(self, value: List[str]) -> None:
        if self._shuffle_options != value:
            self._shuffle_options = value    

    @property
    def shuffle_answers(self) -> List[str]:
        return self._shuffle_answers

    @shuffle_answers.setter
    def shuffle_answers(self, value: List[str]) -> None:
        if self._shuffle_answers != value:
            self._shuffle_answers = value   

    @property
    def answers(self) -> List[int]:
        return self._answers

    @answers.setter
    def answers(self, value: List[int]) -> None:
        if self._answers != value:
            self._answers = value

    @property
    def tip(self) -> str:
        return self._tip

    @tip.setter
    def tip(self, value: str) -> None:
        if self._tip != value:
            self._tip = value

    def dump(self) -> Dict[str, Any]:
        return {
            "Title": self._title,
            "Type": self._type,
            "Options": self._options,
            "Answers": self._answers,
            "Tip": self._tip
        }

__all__ = ["Question"]
