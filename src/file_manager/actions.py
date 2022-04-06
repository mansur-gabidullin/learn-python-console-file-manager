"""
Функционал консольного файлового менеджера
"""

import os
import shutil
import sys

from src.utils import ask_user, ask_paths

ROOT_PATH = os.path.normpath(
    os.path.join(
        os.path.commonpath([
            os.getcwd(),
            os.path.normpath(os.path.join(__file__, '../../../'))
        ]),
        'data'
    )
)

DEVELOPER = 'Мансур Габидуллин'

ignored_files = ['README.md', '.gitignore']


def view(show_directories=True, show_files=True):
    content = filter(
        lambda file: file not in ignored_files,
        os.listdir(ROOT_PATH)
    )

    if not show_directories:
        content = filter(
            lambda file: not os.path.isdir(os.path.join(ROOT_PATH, file)),
            content
        )

    if not show_files:
        content = filter(
            lambda file: not os.path.isfile(os.path.join(ROOT_PATH, file)),
            content
        )

    print(tuple(content))


def create_file():
    name = ask_user('Укажите имя файла: ')

    if not name:
        return

    content = ask_user('Укажите содержимое файла: ')

    with open(os.path.join(ROOT_PATH, f'{name}.txt'), 'x') as f:
        f.write(content)


def read_file():
    name = ask_user('Укажите имя файла: ')

    if not name:
        return

    with open(os.path.join(ROOT_PATH, name), 'r') as f:
        print(f.read())


def create_dir():
    name = ask_user('Укажите имя папки: ')

    if not name:
        return

    directory = os.path.join(ROOT_PATH, name)

    if not os.path.exists(directory):
        os.makedirs(directory)


def remove():
    path = ask_user('Укажите путь к папке или файлу: ')

    if not path:
        return

    path = os.path.join(ROOT_PATH, path)

    is_file = os.path.isfile(path)
    is_dir = os.path.isdir(path)

    if not is_file and not is_dir:
        print('Файл или папка не найдены по указанному пути.')
        return

    if is_file:
        os.remove(path)
        return

    if len(os.listdir(path)) == 0:
        os.rmdir(path)
        return

    answer = ask_user('Папка не пустая. Вы уверены что хотите удалить папку и всё её содержимое? (да/НЕТ)')

    if answer.strip().lower() == 'да':
        shutil.rmtree(path)


def copy():
    path_from, path_to, is_file, is_dir = ask_paths(
        'Укажите путь к папке или файлу, для копирования: ',
        'Укажите путь, куда вы хотите скопировать: ',
        root_path=ROOT_PATH
    )

    if not is_file and not is_dir:
        return

    if is_file:
        shutil.copy2(path_from, path_to)
        return

    shutil.copytree(path_from, path_to)


def info(show_platform=True, show_developer=True):
    if show_platform:
        print(sys.platform)

    if show_developer:
        print(DEVELOPER)
