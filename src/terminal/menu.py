"""
Меню консольного файлового менеджера
"""

FORMAT_PATTERN_MENU_ITEM = '{}. {}'
MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню!'
QUESTION_CHOICE = 'Выберите пункт меню: '


def print_menu(actions):
    print()
    for i, action in enumerate(actions):
        print(FORMAT_PATTERN_MENU_ITEM.format(i, action[0]))


def select_action(actions):
    actions_count = len(actions)
    selected_action = None

    while not selected_action:
        print()
        choice = input(QUESTION_CHOICE)
        choice = int(choice) if choice != '' else 0

        if 0 <= choice < actions_count:
            selected_action = actions[choice]
            continue

        print(MESSAGE_WRONG_ACTION_CHOICE)

    return selected_action
