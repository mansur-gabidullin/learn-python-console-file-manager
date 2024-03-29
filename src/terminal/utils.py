"""
Вспомогательные функции-утилиты
"""
import json
import os as __os
import shutil as __shutil
import sys as __sys

__MESSAGE_EMPTY_ANSWER = 'Вы ничего не указали'
__MESSAGE_NOT_FOUND = 'Файл или папка не найдены по указанному пути.'
__MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню!'
__QUESTION_CHOICE = 'Выберите пункт меню: '
__FORMAT_PATTERN_MENU_ITEM = '{}. {}'
__FORMAT_TEXT_FILE_NAME = '{}.txt'
__FORMAT_JSON_FILE_NAME = '{}.json'

__ignored_files = ['README.md', '.gitignore']

__ROOT_PATH = __os.path.normpath(__os.path.join(__file__, '../../../data'))


def check_is_running(running, counter, actions):
    return running


def get_root_path():
    return __ROOT_PATH


def get_platform():
    return __sys.platform


def resolve_path(name='', root_path=get_root_path()):
    return __os.path.join(root_path, name)


def resolve_file_path(name='', root_path=get_root_path()):
    return resolve_path(__FORMAT_TEXT_FILE_NAME.format(name), root_path)


def resolve_json_file_path(name='', root_path=get_root_path()):
    return resolve_path(__FORMAT_JSON_FILE_NAME.format(name), root_path)


def listdir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return __os.listdir(path)


def isfile(path=''):
    return __os.path.isfile(path)


def isdir(path=''):
    return __os.path.isdir(path)


def is_exists(path):
    return __os.path.exists(path)


def make_dir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)

    if not is_exists(path):
        __os.makedirs(path)


def remove(name='', root_path=get_root_path()):
    path = resolve_file_path(name, root_path=root_path)
    remove_file(path)


def remove_file(path):
    if not is_exists(path):
        to_terminal(__MESSAGE_NOT_FOUND)
        return

    __os.remove(path)


def rmdir(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return __os.rmdir(path)


def rmtree(name='', root_path=get_root_path()):
    path = resolve_path(name, root_path=root_path)
    return __shutil.rmtree(path)


def copy2(path_from, path_to):
    return __shutil.copy2(path_from, path_to)


def copytree(path_from, path_to):
    return __shutil.copytree(path_from, path_to)


def get_list_dir(show_directories=True, show_files=True, root_path=get_root_path()):
    list_dir = filter(
        lambda file: file not in __ignored_files,
        __os.listdir(root_path)
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
    return read_file(path)


def read_json(name, root_path=get_root_path()):
    path = resolve_json_file_path(name, root_path=root_path)

    if not is_exists(path):
        return

    with open(path, 'rt', encoding='utf-8') as f:
        return json.load(f)


def read_file(path):
    if not is_exists(path):
        return

    with open(path, 'rt', encoding='utf-8') as f:
        return f.read()


def save(name, content, root_path=get_root_path()):
    path = resolve_file_path(name, root_path=root_path)
    save_file(path, content)


def save_json(name, content, root_path=get_root_path()):
    path = resolve_json_file_path(name, root_path=root_path)

    with open(path, 'wt', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False)


def save_file(path, content):
    with open(path, 'wt', encoding='utf-8') as f:
        f.write(content)


def print_menu(actions):
    to_terminal()
    for i, action in enumerate(actions):
        to_terminal(__FORMAT_PATTERN_MENU_ITEM.format(i, action[0]))


def select_action(actions, counter):
    actions_count = len(actions)
    selected_action = None

    while not selected_action:
        to_terminal()
        answer = ask_user(__QUESTION_CHOICE)

        try:
            choice = int(answer) if answer != '' else 0

            if choice < 0 or choice >= actions_count:
                raise IndexError(__MESSAGE_WRONG_ACTION_CHOICE)
        except (IndexError, ValueError):
            to_terminal(__MESSAGE_WRONG_ACTION_CHOICE)
        else:
            selected_action = actions[choice]

    return selected_action


def ask_user(question, default=None, empty_warning=__MESSAGE_EMPTY_ANSWER, transform=lambda _: _):
    answer = from_terminal(question)
    result = None

    try:
        if answer.strip() == '':
            if default:
                raise ValueError(empty_warning)
            to_terminal(empty_warning)
            result = transform('')
        result = transform(answer)
    except ValueError:
        result = default
    except Exception:
        result = ''
    finally:
        return result
