"""
Банк
"""

import src.terminal
from src.bank.actions import *

__DESCRIPTION_REFILL = 'пополнение счета'
__DESCRIPTION_PURCHASE = 'покупка'
__DESCRIPTION_HISTORY = 'история покупок'
__DESCRIPTION_OPEN = 'открытие счета'
__INITIAL_AMOUNT = 0


def __get_default_actions():
    return (
        (__DESCRIPTION_REFILL, refill),
        (__DESCRIPTION_PURCHASE, purchase),
        (__DESCRIPTION_HISTORY, history),
    )


def __wrap(fn, *wrapper_args, **wrapper_kwargs):
    """Даёт возможность вызвать функцию с заранее определёнными параметрами"""
    return lambda *args, **kwargs: fn(*args, *wrapper_args, **kwargs, **wrapper_kwargs)


def __inject_journal_to_actions(initial_actions, journal):
    return tuple((description, __wrap(handler, journal)) for description, handler in initial_actions)


def run(terminal=src.terminal, extra_actions=(), journal=None):
    if journal is None:
        journal = [(__INITIAL_AMOUNT, __DESCRIPTION_OPEN)]

    terminal.run(__inject_journal_to_actions(__get_default_actions() + extra_actions, journal))


if __name__ == '__main__':
    run()
