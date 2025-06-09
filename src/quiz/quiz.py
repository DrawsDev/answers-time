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
        self._shuffle_questions = copy.deepcopy(questions)
        self._answered_questions = []
        self._question_index = 0
        self._number_of_correct_answers = 0
        self._start_time = 0
        self._duration = 600
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
            self._questions = copy.deepcopy(value)

    @property
    def shuffle_questions(self) -> List[Question]:
        return self._shuffle_questions
    
    @shuffle_questions.setter
    def shuffle_questions(self, value: List[Question]):
        if self._shuffle_questions != value:
            self._shuffle_questions = copy.deepcopy(value)

    @property
    def question_index(self) -> int:
        return self._question_index
    
    @property
    def options(self) -> List[str]:
        return [v.shuffle_options[i] for i, v in enumerate(self.questions)]

    @property
    def answered_questions(self) -> List[int]:
        return self._answered_questions

    @property
    def answers_recived(self) -> List[Union[int, str]]:
        return self._answers_recived

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
        left = end - time.time()
        return left if left >= 0 else 0

    @property
    def ended(self) -> bool:
        return self._ended

    def _check_answer(self) -> None:
        correct = 0
        wrong = 0
        question = self._questions[self._question_index]

        if question.type == 0 and len(self._answers_recived) > 0:
            recived_answer = self._answers_recived[0]
            recived_option = question.shuffle_options[recived_answer]
            index = question.options.index(recived_option)
            
            if index in question.answers:
                self._number_of_correct_answers += 1
        elif question.type == 1 and len(self._answers_recived) > 0:
            for recived_answer in self._answers_recived:
                recived_option = question.shuffle_options[recived_answer]
                index = question.options.index(recived_option)
                
                if index in question.answers:
                    correct += 1
                else:
                    wrong += 1
            if correct == len(question.answers) and wrong == 0:
                self._number_of_correct_answers += 1
        elif question.type == 2 and len(self._answers_recived) > 0:
            recived_answer = str(self._answers_recived[0])
            recived_answer = recived_answer.lower().replace(" ", "").replace("\n", "")
            options = [i.lower().replace(" ", "").replace("\n", "") for i in question.options]
            if recived_answer in options:
                self._number_of_correct_answers += 1
        elif question.type == 3:
            for i, v in enumerate(question.shuffle_options):
                if question.options[i] == question.shuffle_options[i]:
                    correct += 1
                else:
                    wrong += 1
            if correct == len(question.options) and wrong == 0:
                self._number_of_correct_answers += 1
        elif question.type == 4:
            shuffle_options = question.shuffle_options
            shuffle_answers = question.shuffle_answers

            for i, v in enumerate(question.options):
                i_option = shuffle_options.index(v)

                if shuffle_answers[i_option] == question.answers[i]:
                    correct += 1
                else:
                    wrong += 1
            if correct == len(question.options) and wrong == 0:
                self._number_of_correct_answers += 1
        else:
            return
            
        self._answered_questions.append(self._question_index)
        self._answers_recived.clear()

    def is_answered(self) -> bool:
        question = self._questions[self._question_index]
        if question.type in (0, 1, 2) and len(self._answers_recived) > 0:
            return True
        elif question.type in (3, 4):
            return True
        return False

    def answer(self, answer: Union[int, str], a = None) -> None:
        question = self._questions[self._question_index]
        if question.type == 0:
            if answer in self._answers_recived:
                self._answers_recived.remove(answer)
            else:
                self._answers_recived.clear()
                self._answers_recived.append(answer)
        elif question.type == 1:
            if answer in self._answers_recived:
                self._answers_recived.remove(answer)
            else:
                self._answers_recived.append(answer)
        elif question.type == 2:
            if not answer in self._answers_recived:
                self._answers_recived.clear()
                self._answers_recived.append(answer)
        elif question.type == 3:
            if answer == 0:
                new_options = question.shuffle_options[1:] + [question.shuffle_options[0]]
            else:
                new_options = question.shuffle_options.copy()
                new_options[answer], new_options[answer - 1] = new_options[answer - 1], new_options[answer]
            question.shuffle_options = new_options
        elif question.type == 4:
            if a == 0:
                if answer == 0:
                    new_options = question.shuffle_options[1:] + [question.shuffle_options[0]]
                else:
                    new_options = question.shuffle_options.copy()
                    new_options[answer], new_options[answer - 1] = new_options[answer - 1], new_options[answer]
                question.shuffle_options = new_options
            elif a == 1:
                if answer == 0:
                    new_options = question.shuffle_answers[1:] + [question.shuffle_answers[0]]
                else:
                    new_options = question.shuffle_answers.copy()
                    new_options[answer], new_options[answer - 1] = new_options[answer - 1], new_options[answer]
                question.shuffle_answers = new_options

    def skip_question(self) -> None:
        if self._ended:
            return
        
        if len(self._answered_questions) >= len(self._questions) - 1:
            return
        
        question = self._questions[self._question_index]
        index = self._questions.index(question)
        self._questions = self._questions[:index] + self._questions[index+1:] + [self._questions[index]]
        self._answers_recived.clear()

    def next_question(self) -> None:
        if self._ended:
            return
        
        if self._question_index == len(self._questions) - 1:
            self._ended = True

        self._check_answer()
        self._question_index += 1

    def get_question_number(self) -> int:
        current_index = self._question_index
        current_question = self._questions[current_index]
        for i, q in enumerate(self._shuffle_questions):
            if q.title == current_question.title:
                return i + 1
        return 1

    def get_grade(self) -> float:
        percent = (self._number_of_correct_answers / len(self._questions)) * 100
        if self._grade_type == 0:
            return round(percent)

    def start(self) -> None:
        self._start_time = time.time()

    def stop(self) -> None:
        self._ended = True

    def dump(self) -> Dict[str, Any]:
        return {
            "Title": self._title, 
            "Description": self._description, 
            "Author": self._author, 
            "Questions": [question.dump() for question in self._questions]
        }

__all__ = ["Quiz", "Question"]
