"""
Главный модуль Консольного файлового менеджера
"""

import src.terminal
import src.file_manager.utils as utils


def __get_default_actions():
    return (
        ('просмотр содержимого рабочей директории', utils.view),
        ('посмотреть только папки', lambda *args, **kwargs: utils.view(*args, **kwargs, show_files=False)),
        ('посмотреть только файлы', lambda *args, **kwargs: utils.view(*args, **kwargs, show_directories=False)),
        ('посмотреть содержимое файла', utils.read_file),
        ('создать файл', utils.create_file),
        ('создать папку', utils.create_dir),
        ('удалить (файл/папку)', utils.remove),
        ('копировать (файл/папку)', utils.copy),
        ('просмотр информации об операционной системе',
         lambda *args, **kwargs: utils.info(*args, **kwargs, show_developer=False)),
        ('создатель программы', lambda *args, **kwargs: utils.info(*args, **kwargs, show_platform=False)),
    )


def run(
        extra_actions=None,
        default_actions=None,
        terminal=None,
        terminal_utils=None,
        check_is_running=None
):
    if default_actions is None:
        default_actions = __get_default_actions()

    if extra_actions is None:
        extra_actions = ()

    if terminal is None:
        terminal = src.terminal

    terminal.run(default_actions + extra_actions, utils=terminal_utils, check_is_running=check_is_running)


if __name__ == '__main__':
    run()
