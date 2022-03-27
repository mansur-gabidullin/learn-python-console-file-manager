"""
Банк
"""

import src.terminal
from src.bank.actions import get_default_actions, inject_log_to_actions

DESCRIPTION_OPEN = 'открытие счета'
INITIAL_AMOUNT = 0


def run(terminal=src.terminal, default_actions=get_default_actions(), journal=None):
    if journal is None:
        journal = [(INITIAL_AMOUNT, DESCRIPTION_OPEN)]

    terminal.run(inject_log_to_actions(default_actions, journal))


if __name__ == '__main__':
    run()
