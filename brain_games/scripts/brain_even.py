import random

import prompt

from brain_games.cli import welcome_user

number_of_questions = 3


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(number_of_questions):
        is_correct = question()
        if is_correct:
            print('Correct!')
        else:
            print(f"Let's try again, {user_name}")
            exit(0)
    print(f'Congratulations, {user_name}')


def question():
    is_correct = False
    number = random.randint(1, 20)
    print('Question: {}.'.format(number))
    answer = prompt.string('Your answer: ')
    good_answer = correct_answer(number)
    if answer == good_answer:
        is_correct = True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{good_answer}'.")
    return is_correct


def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == "__main__":
    main()