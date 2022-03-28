"""
Главный модуль Консольного файлового менеджера
"""

import src.terminal
from src.file_manager.actions import *


def get_default_actions():
    return (
        ('просмотр содержимого рабочей директории', view),
        ('посмотреть только папки', lambda: view(show_files=False)),
        ('посмотреть только файлы', lambda: view(show_directories=False)),
        ('посмотреть содержимое файла', read_file),
        ('создать файл', create_file),
        ('создать папку', create_dir),
        ('удалить (файл/папку)', remove),
        ('копировать (файл/папку)', copy),
        ('просмотр информации об операционной системе', lambda: info(show_developer=False)),
        ('создатель программы', lambda: info(show_platform=False)),
    )


def run(terminal=src.terminal, extra_actions=()):
    terminal.run(get_default_actions() + extra_actions)


if __name__ == '__main__':
    run()
