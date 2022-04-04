"""
Терминал
"""
import src.terminal.helpers as terminal_helpers

__MESSAGE_ESCAPE = 'До встречи!'
__MESSAGE_PRESS_ANY_KEY = 'Нажмите клавишу ВВОД, чтобы продолжить...'
__MENU_POINT_EXIT = 'Выход'


def __stop(terminal):
    terminal.to_terminal()
    terminal.to_terminal(__MESSAGE_ESCAPE)


def run(actions=(), terminal=terminal_helpers):
    running = True
    menu_actions = ((__MENU_POINT_EXIT, __stop),) + actions

    while running:
        terminal.print_menu(menu_actions)

        action = terminal.select_action(menu_actions)
        _, handler = action

        handler(terminal)

        if handler == __stop:
            running = False
            continue

        helpers.from_terminal(f'\n{__MESSAGE_PRESS_ANY_KEY}\n')


if __name__ == '__main__':
    run()
