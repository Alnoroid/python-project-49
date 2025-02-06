import random

from brain_games.engine import game_loop, number_of_questions, welcome

rand_min = 2
rand_max = 10
gcd = [2, 3, 5]

def play_gcd():
    welcome('Find the greatest common divisor of given numbers.')
    game_loop(generate_questions())

def generate_questions():
    question_list = []
    for i in range(number_of_questions):
        g = random.choice(gcd)
        a = random.randint(rand_min, rand_max)
        b = random.randint(rand_min, rand_max)
        while calculate_gcd(a, b) != 1:
            a = random.randint(rand_min, rand_max)
            b = random.randint(rand_min, rand_max)
        x = g * a
        y = g * b
        resulting_string = f'{x} {y}'
        question = [resulting_string, g]
        question_list.append(question)
    return question_list

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a