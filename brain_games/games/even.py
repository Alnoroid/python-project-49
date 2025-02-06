import random

from brain_games.engine import game_loop, number_of_questions, welcome

rand_min = 1
rand_max = 100


def play_even():
    welcome('Answer "yes" if the number is even, otherwise answer "no".')
    game_loop(generate_questions())


def generate_questions():
    question_list = []
    for i in range(number_of_questions):
        number = random.randint(rand_min, rand_max)
        answer = correct_answer(number)
        question = [number, answer]
        question_list.append(question)
    return question_list


def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'