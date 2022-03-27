"""
Главный модуль Консольного файлового менеджера
"""
import src.bank
import src.quiz

from menu import *

MESSAGE_ESCAPE = 'До встречи!'
MESSAGE_PRESS_ANY_KEY = 'Нажмите любою клавишу, чтобы продолжить...'


def __stop():
    print()
    print(MESSAGE_ESCAPE)


def run(quiz, bank):
    """Консольный файловый менеджер"""
    running = True

    additional_actions = (
        ('играть в викторину', quiz.run),
        ('мой банковский счет', bank.run),
        ('выход', __stop),
    )

    actions = get_actions(additional_actions)

    while running:
        _, handler = select_action(actions)
        handler()

        if handler == __stop:
            running = False

        input(f'\n{MESSAGE_PRESS_ANY_KEY}\n')


if __name__ == '__main__':
    run(quiz=src.quiz, bank=src.bank)
