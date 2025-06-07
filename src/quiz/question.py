import random
from copy import deepcopy
from typing import Dict, List, Any

class Question:
    def __init__(
        self,
        title: str = "Текст вопроса",
        type: int = 0,
        options: List[str] = ["Текст ответа"],
        answers: List[int] = []
    ) -> None:
        self._title = title
        self._type = type
        self._options = deepcopy(options)
        self._answers = deepcopy(answers)
        self._shuffle()

    def _shuffle(self) -> None:
        if self._type == 2:
            return
        while True:
            self._shuffle_options = random.sample(self._options, len(self._options))
            self._shuffle_answers = random.sample(self._answers, len(self._answers))
            if len(self._options) <= 1:
                break
            elif self._type == 4:
                if self._shuffle_options != self._options and self._shuffle_answers != self._answers:
                    break
            elif self._shuffle_options != self._options:
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

    def dump(self) -> Dict[str, Any]:
        return {
            "Title": self._title,
            "Type": self._type,
            "Options": self._options,
            "Answers": self._answers
        }

__all__ = ["Question"]
