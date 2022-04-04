"""
Терминал
"""
import src.terminal.utils as terminal_helpers

__MESSAGE_ESCAPE = 'До встречи!'
__MESSAGE_PRESS_ANY_KEY = 'Нажмите клавишу ВВОД, чтобы продолжить...'
__MENU_POINT_EXIT = 'Выход'


def __stop(terminal):
    terminal.to_terminal()
    terminal.to_terminal(__MESSAGE_ESCAPE)


def __is_running(is_running, counter, menu_actions):
    return is_running


def run(actions=None, helpers=None, stop_handler=None, check_is_running=None):
    if actions is None:
        actions = ()

    if helpers is None:
        helpers = terminal_helpers

    if stop_handler is None:
        stop_handler = __stop

    if check_is_running is None:
        check_is_running = __is_running

    running = True
    menu_actions = ((__MENU_POINT_EXIT, stop_handler),) + actions
    counter = 0

    while check_is_running(running, counter, menu_actions):
        helpers.print_menu(menu_actions)

        action = helpers.select_action(menu_actions, counter)
        _, handler = action

        handler(helpers)
        counter += 1

        if handler == stop_handler:
            running = False
            continue

        helpers.from_terminal(f'\n{__MESSAGE_PRESS_ANY_KEY}\n')


if __name__ == '__main__':
    run()
