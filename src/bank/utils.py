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
__MESSAGE_ENTERED_AMOUNT_MUST_BE_GREATER_THEN_ZERO = 'Вводимая сумма должна быть больше нуля!'
__FORMAT_PATTERN_LOG_HISTORY = '{:+.2f}: {}'
__FORMAT_PATTERN_LOG_PURCHASE = '{}: {}'
__FORMAT_PATTERN_MENU_ITEM = '{}. {}'


def get_amount(journal):
    return sum((i[0] for i in journal))


def refill(terminal, journal, on_journal_change=lambda _: None):
    terminal.to_terminal()
    answer = terminal.ask_user(__QUESTION_REFILL_AMOUNT)

    if not answer:
        return

    refill_amount = float(answer)

    if refill_amount <= 0:
        terminal.to_terminal(__MESSAGE_ENTERED_AMOUNT_MUST_BE_GREATER_THEN_ZERO)
        return

    journal.append((refill_amount, __MESSAGE_REFILL_ACTION))
    on_journal_change(journal)


def purchase(terminal, journal, on_journal_change=lambda _: None):
    terminal.to_terminal()
    remaining_amount = get_amount(journal)

    if remaining_amount == 0:
        terminal.to_terminal(__MESSAGE_REMAINING_AMOUNT)
        return

    cost = terminal.ask_user(__QUESTION_PURCHASE_COST, default=0, transform=float)

    if cost > remaining_amount:
        terminal.to_terminal()
        terminal.to_terminal(__MESSAGE_REMAINING_AMOUNT)
        return

    terminal.to_terminal()
    purchase_name = terminal.ask_user(__QUESTION_PURCHASE_NAME)
    journal.append((-cost, __FORMAT_PATTERN_LOG_PURCHASE.format(__MESSAGE_PURCHASE, purchase_name)))
    on_journal_change(journal)


def history(terminal, journal, on_journal_change=lambda _: None):
    terminal.to_terminal()
    remaining_amount = get_amount(journal)

    for amount, description in journal:
        terminal.to_terminal(__FORMAT_PATTERN_LOG_HISTORY.format(amount, description))

    terminal.to_terminal('_' * 25)
    terminal.to_terminal(remaining_amount)
