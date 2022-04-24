from src import file_manager, quiz, bank

MENU_POINT_QUIZ = 'играть в викторину'
MENU_POINT_BANK = 'мой банковский счет'


def run():
    extra_actions = ((MENU_POINT_QUIZ, lambda *args: quiz.run()), (MENU_POINT_BANK, lambda *args: bank.run()))
    file_manager.run(extra_actions=extra_actions)


if __name__ == '__main__':
    run()
