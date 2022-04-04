from src import file_manager
from src.file_manager.utils import create_file
import tests.moke_terminal_utils as terminal


def test_create_file():
    root_path = terminal.get_root_path()
    file_path = terminal.resolve_file_path('50', root_path=root_path)

    assert not terminal.is_exists(file_path)

    test_actions = (
        ('создать файл', create_file),
    )

    file_manager.run(
        default_actions=test_actions,
        terminal_utils=terminal
    )

    assert terminal.is_exists(file_path)

    terminal.remove('50', root_path=root_path)


def test_file_manager():
    is_called = False

    def set_called():
        nonlocal is_called
        is_called = True

    test_actions = (
        ('custom action', lambda _: set_called()),
    )

    file_manager.run(
        default_actions=test_actions,
        terminal_utils=terminal
    )

    assert is_called
