"""
Банк
"""

import src.terminal
from src.bank.actions import *

DESCRIPTION_REFILL = 'пополнение счета'
DESCRIPTION_PURCHASE = 'покупка'
DESCRIPTION_HISTORY = 'история покупок'
DESCRIPTION_OPEN = 'открытие счета'
INITIAL_AMOUNT = 0


def get_default_actions():
    return (
        (DESCRIPTION_REFILL, refill),
        (DESCRIPTION_PURCHASE, purchase),
        (DESCRIPTION_HISTORY, history),
    )


def run(terminal=src.terminal, default_actions=get_default_actions(), journal=None):
    if journal is None:
        journal = [(INITIAL_AMOUNT, DESCRIPTION_OPEN)]

    terminal.run(inject_log_to_actions(default_actions, journal))


if __name__ == '__main__':
    run()
