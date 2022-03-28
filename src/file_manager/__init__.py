"""
Главный модуль Консольного файлового менеджера
"""

import src.bank
import src.quiz
import src.terminal
from src.file_manager.actions import get_default_actions

MENU_POINT_QUIZ = 'играть в викторину'
MENU_POINT_BANK = 'мой банковский счет'


def run(terminal=src.terminal, extra_actions=()):
    terminal.run(get_default_actions() + extra_actions)


if __name__ == '__main__':
    run(extra_actions=((MENU_POINT_QUIZ, src.quiz.run), (MENU_POINT_BANK, src.bank.run)))
