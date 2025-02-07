import random

from brain_games.engine import game_loop, number_of_questions, welcome

prime_min = 2
prime_max = 100


def play_prime():
    welcome('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_loop(generate_questions())


def generate_questions():
    question_list = []
    for i in range(number_of_questions):
        number = random.randint(prime_min, prime_max)
        answer = isprime(number)
        question = [number, answer]
        question_list.append(question)
    return question_list


def isprime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return 'no'
        return 'yes'