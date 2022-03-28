"""
Вспомогательные функции-утилиты
"""
import os

MESSAGE_EMPTY_ANSWER = 'Вы ничего не указали'
MESSAGE_NOT_FOUND = 'Файл или папка не найдены по указанному пути.'


def wrap(fn, *args, **kwargs):
    """Даёт возможность вызвать функцию с заранее определёнными параметрами"""
    return lambda: fn(*args, **kwargs)


def ask_user(question, empty_warning=MESSAGE_EMPTY_ANSWER):
    answer = input(question)

    if answer.strip() == '':
        print(empty_warning)
        return ''

    return answer


def ask_paths(question_from, question_to, root_path, not_found_warning=MESSAGE_NOT_FOUND):
    path_from = ask_user(question_from)
    no_result = (None, None, False, False)

    if not path_from:
        return no_result

    path_to = ask_user(question_to)

    if not path_to:
        return no_result

    path_from = os.path.join(root_path, path_from)
    path_to = os.path.join(root_path, path_to)

    is_file = os.path.isfile(path_from)
    is_dir = os.path.isdir(path_from)

    if not is_file and not is_dir:
        print(not_found_warning)
        return no_result

    return path_from, path_to, is_file, is_dir
