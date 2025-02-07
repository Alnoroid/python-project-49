import prompt

from brain_games.cli import welcome_user

number_of_questions = 3

user_name = welcome_user()


def welcome(message):
    print(message)


def ask_question(question):
    print('Question: ' + str(question))


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def compare_answer(answer, correct_answer):
    is_correct = False
    if str(answer) == str(correct_answer):
        is_correct = True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
    return is_correct


def game_loop(questions):
    for i in range(len(questions)):
        question, correct_answer = questions[i]
        ask_question(question)
        answer = get_answer()
        is_correct = compare_answer(answer, correct_answer)
        if is_correct:
            print('Correct!')
        else:
            lose()
    win()


def win():
    print(f'Congratulations, {user_name}!')


def lose():
    print(f"Let's try again, {user_name}")
    exit(0)