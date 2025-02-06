import random

from brain_games.engine import game_loop, number_of_questions, welcome

prog_len_min = 5
prog_len_max = 10
prog_step_min = 3
prog_step_max = 5
prog_start_min = 1
prog_start_max = 50
hidden_symbol = '..'


def play_progression():
    welcome('What number is missing in the progression?')
    game_loop(generate_questions())


def generate_questions():
    question_list = []
    for i in range(number_of_questions):
        prog_len = random.randint(prog_len_min, prog_len_max)
        hidden_element = random.randint(0, prog_len)
        prog_step = random.randint(prog_step_min, prog_step_max)
        prog_start = random.randint(prog_start_min, prog_start_max)
        progression = []
        question = [progression, 0]
        for j in range(prog_len):
            if j == hidden_element:
                question[1] = prog_start
                progression.append(hidden_symbol)
            else:
                progression.append(str(prog_start))
            prog_start = prog_start + prog_step
        question_list.append([' '.join(question[0]), question[1]])
    return question_list