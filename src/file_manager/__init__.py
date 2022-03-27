"""
Главный модуль Консольного файлового менеджера
"""

import src.bank
import src.quiz
import src.terminal
from src.file_manager.actions import get_default_actions

MENU_POINT_QUIZ = 'играть в викторину'
MENU_POINT_BANK = 'мой банковский счет'


def run(terminal=src.terminal, default_actions=get_default_actions(), quiz=src.quiz, bank=src.bank):
    additional_actions = ()

    if quiz:
        additional_actions += ((MENU_POINT_QUIZ, quiz.run),)

    if bank:
        additional_actions += ((MENU_POINT_BANK, bank.run),)

    terminal.run(default_actions + additional_actions)


if __name__ == '__main__':
    run()
