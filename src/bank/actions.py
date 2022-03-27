"""
Функционал консольного файлового менеджера
"""
from src.utils import wrap

DESCRIPTION_REFILL = 'пополнение счета'
DESCRIPTION_PURCHASE = 'покупка'
DESCRIPTION_HISTORY = 'история покупок'
QUESTION_CHOICE = 'Выберите пункт меню: '
QUESTION_REFILL_AMOUNT = 'Введите сумму на сколько пополнить счет: '
QUESTION_PURCHASE_COST = 'Введите сумму покупки: '
QUESTION_PURCHASE_NAME = 'Введите название покупки: '
MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню'
MESSAGE_REMAINING_AMOUNT = 'Денег не хватает!'
FORMAT_PATTERN_LOG_HISTORY = '{:+.2f}: {}'
FORMAT_PATTERN_LOG_PURCHASE = '{}: {}'
FORMAT_PATTERN_MENU_ITEM = '{}. {}'


def __get_amount(journal):
    return sum((i[0] for i in journal))


def __refill(journal):
    print()
    refill_amount = float(input(QUESTION_REFILL_AMOUNT))
    journal.append((refill_amount, DESCRIPTION_REFILL))


def __purchase(journal):
    print()
    remaining_amount = __get_amount(journal)

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
    journal.append((-cost, FORMAT_PATTERN_LOG_PURCHASE.format(DESCRIPTION_PURCHASE, purchase_name)))


def __history(journal):
    print()
    remaining_amount = __get_amount(journal)

    for amount, description in journal:
        print(FORMAT_PATTERN_LOG_HISTORY.format(amount, description))

    print('_' * 25)
    print(remaining_amount)


def get_default_actions():
    return (
        (DESCRIPTION_REFILL, __refill),
        (DESCRIPTION_PURCHASE, __purchase),
        (DESCRIPTION_HISTORY, __history),
    )


def inject_log_to_actions(actions, journal):
    return tuple((description, wrap(handler, journal)) for description, handler in actions)
