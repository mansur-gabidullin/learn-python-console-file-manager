"""
Вспомогательные функции-утилиты
"""

import os
import shutil
import sys

__MESSAGE_EMPTY_ANSWER = 'Вы ничего не указали'
__MESSAGE_NOT_FOUND = 'Файл или папка не найдены по указанному пути.'
__MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню!'
__QUESTION_CHOICE = 'Выберите пункт меню: '
__FORMAT_PATTERN_MENU_ITEM = '{}. {}'
__FORMAT_FILE_NAME = '{}.txt'

__ignored_files = ['README.md', '.gitignore']

__ROOT_PATH = os.path.normpath(
    os.path.join(
        os.path.commonpath([
            os.getcwd(),
            os.path.normpath(os.path.join(__file__, '../../../'))
        ]),
        'data'
    )
)


def get_root_path():
    return __ROOT_PATH


def get_platform():
    return sys.platform


def resolve_path(name='', root_path=get_root_path()):
    return os.path.join(root_path, name)


def resolve_file_path(name='', root_path=get_root_path()):
    return resolve_path(__FORMAT_FILE_NAME.format(name), root_path)


def listdir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return os.listdir(path)


def isfile(path=''):
    return os.path.isfile(path)


def isdir(path=''):
    return os.path.isdir(path)


def is_exists(path):
    return os.path.exists(path)


def make_dir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)

    if not is_exists(path):
        os.makedirs(path)


def remove(name='', root_path=get_root_path()):
    path = resolve_file_path(name, root_path=root_path)

    if not is_exists(path):
        to_terminal(__MESSAGE_NOT_FOUND)
        return

    os.remove(path)


def rmdir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return os.rmdir(path)


def rmtree(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return shutil.rmtree(path)


def copy2(path_from, path_to):
    return shutil.copy2(path_from, path_to)


def copytree(path_from, path_to):
    return shutil.copytree(path_from, path_to)


def get_list_dir(show_directories=True, show_files=True, root_path=get_root_path()):
    list_dir = filter(
        lambda file: file not in __ignored_files,
        os.listdir(root_path)
    )

    if not show_directories:
        list_dir = filter(
            lambda name: not isdir(resolve_path(name, root_path=root_path)),
            list_dir
        )

    if not show_files:
        list_dir = filter(
            lambda name: not isfile(resolve_path(name, root_path=root_path)),
            list_dir
        )

    return tuple(list_dir)


def to_terminal(*args, **kwargs):
    return print(*args, **kwargs)


def from_terminal(*args, **kwargs):
    return input(*args, **kwargs)


def read(name, root_path=get_root_path()):
    path = resolve_file_path(name, root_path=root_path)

    if not is_exists(path):
        return ''

    with open(path, 'r') as f:
        return f.read()


def save(name, content, root_path=get_root_path()):
    path = resolve_file_path(name, root_path=root_path)

    with open(path, 'x') as f:
        f.write(content)


def print_menu(actions):
    to_terminal()
    for i, action in enumerate(actions):
        to_terminal(__FORMAT_PATTERN_MENU_ITEM.format(i, action[0]))


def select_action(actions):
    actions_count = len(actions)
    selected_action = None

    while not selected_action:
        to_terminal()
        choice = from_terminal(__QUESTION_CHOICE)
        choice = int(choice) if choice != '' else 0

        if 0 <= choice < actions_count:
            selected_action = actions[choice]
            continue

        to_terminal(__MESSAGE_WRONG_ACTION_CHOICE)

    return selected_action


def ask_user(question, empty_warning=__MESSAGE_EMPTY_ANSWER):
    answer = from_terminal(question)

    if answer.strip() == '':
        to_terminal(empty_warning)
        return ''

    return answer
