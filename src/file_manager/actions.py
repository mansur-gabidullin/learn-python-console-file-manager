"""
Функционал консольного файлового менеджера
"""


def __create():
    print('create')


def __remove():
    print('remove')


def __copy():
    print('copy')


def __view(show_directories=True, show_files=True):
    print('show_di')


def __info(show_platform=True, show_developer=True):
    print('show_pl')


def __go():
    print('go')


def get_default_actions():
    return (
        ('создать папку', __create),
        ('удалить (файл/папку)', __remove),
        ('копировать (файл/папку)', __copy),
        ('просмотр содержимого рабочей директории', __view),
        ('посмотреть только папки', lambda: __view(show_files=False)),
        ('посмотреть только файлы', lambda: __view(show_directories=False)),
        ('просмотр информации об операционной системе', lambda: __info(show_developer=False)),
        ('создатель программы', lambda: __info(show_platform=False)),
        ('смена рабочей директории', __go),
    )
