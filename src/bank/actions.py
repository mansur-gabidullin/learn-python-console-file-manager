"""
Функционал консольного файлового менеджера
"""

__QUESTION_CHOICE = 'Выберите пункт меню: '
__QUESTION_REFILL_AMOUNT = 'Введите сумму на сколько пополнить счет: '
__QUESTION_PURCHASE_COST = 'Введите сумму покупки: '
__QUESTION_PURCHASE_NAME = 'Введите название покупки: '
__MESSAGE_REFILL_ACTION = 'пополнение'
__MESSAGE_PURCHASE = 'покупка'
__MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню'
__MESSAGE_REMAINING_AMOUNT = 'Денег не хватает!'
__FORMAT_PATTERN_LOG_HISTORY = '{:+.2f}: {}'
__FORMAT_PATTERN_LOG_PURCHASE = '{}: {}'
__FORMAT_PATTERN_MENU_ITEM = '{}. {}'


def __get_amount(journal):
    return sum((i[0] for i in journal))


def refill(terminal, journal):
    terminal.to_terminal()
    refill_amount = float(terminal.from_terminal(__QUESTION_REFILL_AMOUNT))
    journal.append((refill_amount, __MESSAGE_REFILL_ACTION))


def purchase(terminal, journal):
    terminal.to_terminal()
    remaining_amount = __get_amount(journal)

    if remaining_amount == 0:
        terminal.to_terminal(__MESSAGE_REMAINING_AMOUNT)
        return

    cost = float(terminal.from_terminal(__QUESTION_PURCHASE_COST))

    if cost > remaining_amount:
        terminal.to_terminal()
        terminal.to_terminal(__MESSAGE_REMAINING_AMOUNT)
        return

    terminal.to_terminal()
    purchase_name = terminal.from_terminal(__QUESTION_PURCHASE_NAME)
    journal.append((-cost, __FORMAT_PATTERN_LOG_PURCHASE.format(__MESSAGE_PURCHASE, purchase_name)))


def history(terminal, journal):
    terminal.to_terminal()
    remaining_amount = __get_amount(journal)

    for amount, description in journal:
        terminal.to_terminal(__FORMAT_PATTERN_LOG_HISTORY.format(amount, description))

    terminal.to_terminal('_' * 25)
    terminal.to_terminal(remaining_amount)
