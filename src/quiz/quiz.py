import time
import copy
from typing import Union, List, Dict, Any
from src.quiz.question import Question

class Quiz:
    def __init__(
        self,
        title: str = "Quiz title",
        description: str = "",
        author: str = "",
        questions: List[Question] = []
    ) -> None:
        self._title = title
        self._description = description
        self._author = author
        self._questions = copy.deepcopy(questions)
        self._answered_questions = []
        self._question_index = 0
        self._number_of_correct_answers = 0
        self._start_time = 0
        self._duration = 60
        self._ended = False
        self._answers_recived = []
        self._grade_type = 0

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if self._title != value:
            self._title = value

    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str) -> None:
        if self._description != value:
            self._description = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if self._author != value:
            self._author = value

    @property
    def questions(self) -> List[Question]:
        return self._questions
    
    @questions.setter
    def questions(self, value: List[Question]):
        if self._questions != value:
            self._questions = value

    @property
    def question_index(self) -> int:
        return self._question_index
    
    @property
    def answered_questions(self) -> List[int]:
        return self._answered_questions

    @property
    def number_of_correct_answers(self) -> int:
        return self._number_of_correct_answers

    @property
    def start_time(self) -> float:
        self._start_time

    @start_time.setter
    def start_time(self, value: float) -> None:
        if self._start_time != value:
            self._start_time = value

    @property
    def time_left(self) -> float:
        end = self._start_time + self._duration
        left = time.time() - end
        return left if left >= 0 else 0

    @property
    def ended(self) -> bool:
        return self._ended

    def _check_answer(self) -> None:
        correct = 0
        wrong = 0
        question = self._questions[self._question_index]

        for answer in self._answers_recived:
            if type(answer) == int:
                if answer in question.answers:
                    correct += 1
                else:
                    wrong += 1
            elif type(answer) == str:
                if answer.lower().replace(" ", "").replace("\n", "") in [i.lower().replace(" ", "").replace("\n", "") for i in question.options]:
                    correct += 1
                else:
                    wrong += 1
        
        if type(answer) == int:
            if correct == len(question.answers) and wrong == 0:
                self._number_of_correct_answers += 1
        elif type(answer) == str:
            if correct > 0 and wrong == 0:
                self._number_of_correct_answers += 1
        
        self._answered_questions.append(self._question_index)
        self._answers_recived.clear()

    def answer(self, answer: Union[int, str]) -> None:
        if type(answer) == int:
            if answer in self._answers_recived:
                self._answers_recived.remove(answer)
            else:
                self._answers_recived.append(answer)
        elif type(answer) == str:
            self._answers_recived.clear()
            self._answers_recived.append(answer)

    def next_question(self) -> None:
        if self._ended:
            return
        
        if self._question_index == len(self._questions) - 1:
            self._ended = True

        self._check_answer()
        self._question_index += 1

    def get_grade(self) -> float:
        percent = (self._number_of_correct_answers / len(self._questions)) * 100
        if self._grade_type == 0:
            return round(percent)

    def dump(self) -> Dict[str, Any]:
        return {
            "Title": self._title, 
            "Description": self._description, 
            "Author": self._author, 
            "Questions": [question.dump() for question in self._questions]
        }

__all__ = ["Quiz", "Question"]
