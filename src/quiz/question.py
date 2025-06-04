from copy import deepcopy
from typing import Dict, List, Any

class Question:
    def __init__(
        self,
        title: str = "Question text",
        type: int = 0,
        options: List[str] = ["Answer"],
        answers: List[int] = [1]
    ) -> None:
        self._title = title
        self._type = type
        self._options = deepcopy(options)
        self._answers = deepcopy(answers)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if self._title != value:
            self._title = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
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
