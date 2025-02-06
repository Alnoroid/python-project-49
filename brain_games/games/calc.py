import random

from brain_games.engine import game_loop, number_of_questions, welcome

rand_min = 1
rand_max = 10


def play_calc():
    welcome('Answer "yes" if the number is even, otherwise answer "no".')
    game_loop(generate_questions())


def generate_questions():
    question_list = []
    for i in range(number_of_questions):
        number1 = random.randint(rand_min, rand_max)
        number2 = random.randint(rand_min, rand_max)
        operator = random.choice(['+', '-', '*'])
        resulting_string = f'{number1} {operator} {number2}'
        answer = correct_answer(number1, number2, operator)
        question = [resulting_string, answer]
        question_list.append(question)
    return question_list


def correct_answer(number1, number2, operator):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2