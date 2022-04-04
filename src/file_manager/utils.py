"""
Функционал консольного файлового менеджера
"""

__DEVELOPER = 'Мансур Габидуллин'


def view(terminal, show_directories=True, show_files=True):
    content = terminal.get_list_dir(show_directories=show_directories, show_files=show_files)
    terminal.to_terminal(tuple(content))


def create_file(terminal):
    name = terminal.ask_user('Укажите имя файла: ')

    if not name:
        return

    content = terminal.ask_user('Укажите содержимое файла: ')

    if not content:
        return

    terminal.save(name, content, root_path=terminal.get_root_path())


def read_file(terminal):
    name = terminal.ask_user('Укажите имя файла: ')

    if not name:
        return

    root_path = terminal.get_root_path()

    content = terminal.read(name, root_path=root_path)

    if content is None:
        terminal.to_terminal('Файл не найден!')
        return

    terminal.to_terminal(content)


def create_dir(terminal):
    name = terminal.ask_user('Укажите имя папки: ')

    if not name:
        return

    terminal.make_dir(name, root_path=terminal.get_root_path())


def remove(terminal):
    name = terminal.ask_user('Укажите название папки или файла: ')

    if not name:
        return

    root_path = terminal.get_root_path()

    is_dir = terminal.isdir(terminal.resolve_path(name, root_path=root_path))
    is_file = terminal.isfile(terminal.resolve_file_path(name, root_path=root_path))

    if not is_file and not is_dir:
        terminal.to_terminal('Файл или папка не найдены по указанному пути.')
        return

    if is_file:
        terminal.remove(name, root_path=root_path)
        return

    if len(terminal.listdir(name, root_path=root_path)) == 0:
        terminal.rmdir(name, root_path=root_path)
        return

    answer = terminal.ask_user('Папка не пустая. Вы уверены что хотите удалить папку и всё её содержимое? (да/НЕТ): ')
    answer = answer.strip().lower()

    if answer == 'да' or answer == 'yes':
        terminal.rmtree(name, root_path=root_path)


def copy(terminal):
    root_path = terminal.get_root_path()
    is_file_copying = False

    name_from = terminal.ask_user('Укажите название папки или файла, для копирования: ')

    if not name_from:
        return

    path_from = terminal.resolve_path(name_from, root_path=root_path)

    if not terminal.isdir(path_from):
        path_from = terminal.resolve_file_path(name_from, root_path=root_path)

    if terminal.isfile(path_from):
        is_file_copying = True

    if not path_from:
        return

    name_to = terminal.ask_user('Укажите название, куда вы хотите скопировать: ')

    if not name_to:
        return

    if is_file_copying:
        path_to = terminal.resolve_file_path(name_to, root_path=root_path)
    else:
        path_to = terminal.resolve_path(name_to, root_path=root_path)

    if not path_to:
        return

    if is_file_copying:
        terminal.copy2(path_from, path_to)
        return

    terminal.copytree(path_from, path_to)


def info(terminal, show_platform=True, show_developer=True):
    if show_platform:
        terminal.to_terminal(terminal.get_platform())

    if show_developer:
        terminal.to_terminal(__DEVELOPER)
