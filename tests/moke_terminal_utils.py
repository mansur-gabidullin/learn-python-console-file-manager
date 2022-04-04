from src.terminal.utils import *


def get_root_path():
    import os
    return os.path.join(os.getcwd(), 'test_data')


def check_is_running(running, counter, actions):
    return counter < len(actions)


def select_action(actions, counter):
    return actions[counter]


def print_menu(*args, **kwargs):
    pass


def to_terminal(*args, **kwargs):
    pass


def from_terminal(*args, **kwargs):
    return '50'


def ask_user(*args, **kwargs):
    return from_terminal()
