import json
from typing import Dict, List
from src.answerstime.quiz import Quiz
from src.answerstime.question import Question

def validate_quiz_from_file(filepath: str) -> bool:
    if not filepath.endswith(".json"):
        return False
    with open(filepath, "r", encoding="utf-8") as file:
        quiz_data = json.load(file)
        if type(quiz_data) == dict:
            quiz_title = quiz_data.get("Title") != None
            quiz_description = quiz_data.get("Description") != None
            quiz_author = quiz_data.get("Author") != None
            quiz_questions = quiz_data.get("Questions") != None
            if not (quiz_title and quiz_description and quiz_author and quiz_questions):
                return False
        else:
            return False
    return True

def validate_question_from_dict(quesiton_dict: Dict) -> bool:
    title = quesiton_dict.get("Title") is not None
    type = quesiton_dict.get("Type") is not None
    options = quesiton_dict.get("Options") is not None
    answers = quesiton_dict.get("Answers") is not None
    return title and type and options and answers

def create_questions_from_dict(question_dict: Dict) -> List[Question]:
    questions = []
    for question_data in question_dict:
        if not validate_question_from_dict(question_data):
            continue
        questions.append(Question(
            question_data.get("Title"),
            question_data.get("Type"),
            question_data.get("Options"),
            question_data.get("Answers"),
            question_data.get("Tip") or "Подсказка не указана."
        ))
    return questions

def create_quiz_from_file(filepath: str) -> Quiz:
    if not validate_quiz_from_file(filepath):
        return Quiz()
    with open(filepath, "r", encoding="utf-8") as file:
        quiz_data: dict = json.load(file)
        return Quiz(
            quiz_data.get("Title"),
            quiz_data.get("Description"),
            quiz_data.get("Author"),
            create_questions_from_dict(quiz_data.get("Questions"))
        )    