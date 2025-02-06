import random

from brain_games.engine import game_loop, number_of_questions, welcome

rand_min = 1
rand_max = 10


def play_gcd():
    welcome('Find the greatest common divisor of given numbers.')