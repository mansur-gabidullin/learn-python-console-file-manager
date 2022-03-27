"""
Меню консольного файлового менеджера

Пункты меню:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
"""

from actions import create, copy, remove, view, info, go

FORMAT_PATTERN_MENU_ITEM = '{}. {}'
MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню!'

QUESTION_CHOICE = 'Выберите пункт меню: '

__actions = (
    ('создать папку', create),
    ('удалить (файл/папку)', remove),
    ('копировать (файл/папку)', copy),
    ('просмотр содержимого рабочей директории', view),
    ('посмотреть только папки', lambda: view(show_files=False)),
    ('посмотреть только файлы', lambda: view(show_directories=False)),
    ('просмотр информации об операционной системе', lambda: info(show_developer=False)),
    ('создатель программы', lambda: info(show_platform=False)),
    ('смена рабочей директории', go),
)


def get_actions(additional_actions=()):
    return __actions + additional_actions


def print_menu(actions):
    print()
    for i, action in enumerate(actions, 1):
        print(FORMAT_PATTERN_MENU_ITEM.format(i, action[0]))


def select_action(actions):
    actions_count = len(actions)
    selected_action = None

    print_menu(actions)

    while not selected_action:
        print()
        choice = int(input(QUESTION_CHOICE))

        if 0 < choice <= actions_count:
            selected_action = actions[choice - 1]
        else:
            print(MESSAGE_WRONG_ACTION_CHOICE)

    return selected_action
