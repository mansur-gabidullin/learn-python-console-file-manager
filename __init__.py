from src import file_manager, quiz, bank
from src.terminal.utils import read_json, save_json

MENU_POINT_QUIZ = 'играть в викторину'
MENU_POINT_BANK = 'мой банковский счет'
JOURNAL_FILE_NAME = 'bank_journal'


def __run_bank():
    bank_journal = read_json(JOURNAL_FILE_NAME)
    bank.run(journal=bank_journal, on_journal_change=lambda journal: save_json(JOURNAL_FILE_NAME, journal))


def run():
    extra_actions = (
        (MENU_POINT_QUIZ, lambda *args: quiz.run()),
        (MENU_POINT_BANK, lambda *args: __run_bank())
    )
    file_manager.run(extra_actions=extra_actions)


if __name__ == '__main__':
    run()
