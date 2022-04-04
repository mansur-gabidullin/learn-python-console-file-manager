"""
Главный модуль Консольного файлового менеджера
"""

import src.terminal
from src.file_manager.actions import *


def __get_default_actions():
    return (
        ('просмотр содержимого рабочей директории', view),
        ('посмотреть только папки', lambda *args, **kwargs: view(*args, **kwargs, show_files=False)),
        ('посмотреть только файлы', lambda *args, **kwargs: view(*args, **kwargs, show_directories=False)),
        ('посмотреть содержимое файла', read_file),
        ('создать файл', create_file),
        ('создать папку', create_dir),
        ('удалить (файл/папку)', remove),
        ('копировать (файл/папку)', copy),
        ('просмотр информации об операционной системе',
         lambda *args, **kwargs: info(*args, **kwargs, show_developer=False)),
        ('создатель программы', lambda *args, **kwargs: info(*args, **kwargs, show_platform=False)),
    )


def run(terminal=src.terminal, extra_actions=()):
    terminal.run(__get_default_actions() + extra_actions)


if __name__ == '__main__':
    run()
