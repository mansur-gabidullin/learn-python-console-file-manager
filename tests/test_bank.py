import src.bank as bank
import tests.moke_terminal_utils as terminal_utils
from src.bank.utils import get_amount, refill, purchase


def __get_initial_journal():
    return [(100, 'Открытие тестового счёта с начальной суммой равная 100')]


def test_bank_refill():
    test_journal = __get_initial_journal()
    terminal = terminal_utils

    refill(terminal, test_journal)

    assert get_amount(test_journal) == 150.0


def test_bank_purchase():
    test_journal = __get_initial_journal()
    terminal = terminal_utils

    purchase(terminal, test_journal)

    assert get_amount(test_journal) == 50.0


def test_bank_journal():
    test_journal = __get_initial_journal()

    test_actions = (
        ('пополнить 50', lambda terminal, journal, _: journal.append((50, 'пришла зарплата'))),
        ('купить на 30', lambda terminal, journal, _: journal.append((-30, 'купил яблоки'))),
    )

    bank.run(
        default_actions=test_actions,
        journal=test_journal,
        terminal_utils=terminal_utils
    )

    assert get_amount(test_journal) == 120
