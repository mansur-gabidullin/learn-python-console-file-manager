"""
Терминал
"""
from src.terminal.menu import *

MESSAGE_ESCAPE = 'До встречи!'
MESSAGE_PRESS_ANY_KEY = 'Нажмите клавишу ВВОД, чтобы продолжить...'
MENU_POINT_EXIT = 'Выход'


def __stop():
    print()
    print(MESSAGE_ESCAPE)


def run(actions=()):
    running = True
    menu_actions = actions + ((MENU_POINT_EXIT, __stop),)

    while running:
        print_menu(menu_actions)

        action = select_action(menu_actions)
        _, handler = action

        handler()

        if handler == __stop:
            running = False
            continue

        input(f'\n{MESSAGE_PRESS_ANY_KEY}\n')


if __name__ == '__main__':
    run()
