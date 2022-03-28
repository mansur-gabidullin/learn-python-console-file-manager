"""
Функционал консольного файлового менеджера
"""
from src.utils import wrap

QUESTION_CHOICE = 'Выберите пункт меню: '
QUESTION_REFILL_AMOUNT = 'Введите сумму на сколько пополнить счет: '
QUESTION_PURCHASE_COST = 'Введите сумму покупки: '
QUESTION_PURCHASE_NAME = 'Введите название покупки: '
MESSAGE_REFILL_ACTION = 'пополнение'
MESSAGE_PURCHASE = 'покупка'
MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню'
MESSAGE_REMAINING_AMOUNT = 'Денег не хватает!'
FORMAT_PATTERN_LOG_HISTORY = '{:+.2f}: {}'
FORMAT_PATTERN_LOG_PURCHASE = '{}: {}'
FORMAT_PATTERN_MENU_ITEM = '{}. {}'


def get_amount(journal):
    return sum((i[0] for i in journal))


def refill(journal):
    print()
    refill_amount = float(input(QUESTION_REFILL_AMOUNT))
    journal.append((refill_amount, MESSAGE_REFILL_ACTION))


def purchase(journal):
    print()
    remaining_amount = get_amount(journal)

    if remaining_amount == 0:
        print(MESSAGE_REMAINING_AMOUNT)
        return

    cost = float(input(QUESTION_PURCHASE_COST))

    if cost > remaining_amount:
        print()
        print(MESSAGE_REMAINING_AMOUNT)
        return

    print()
    purchase_name = input(QUESTION_PURCHASE_NAME)
    journal.append((-cost, FORMAT_PATTERN_LOG_PURCHASE.format(MESSAGE_PURCHASE, purchase_name)))


def history(journal):
    print()
    remaining_amount = get_amount(journal)

    for amount, description in journal:
        print(FORMAT_PATTERN_LOG_HISTORY.format(amount, description))

    print('_' * 25)
    print(remaining_amount)


def inject_log_to_actions(actions, journal):
    return tuple((description, wrap(handler, journal)) for description, handler in actions)
