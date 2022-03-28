from src import file_manager, quiz, bank

MENU_POINT_QUIZ = 'играть в викторину'
MENU_POINT_BANK = 'мой банковский счет'


def run():
    file_manager.run(extra_actions=((MENU_POINT_QUIZ, quiz.run), (MENU_POINT_BANK, bank.run)))


if __name__ == '__main__':
    run()
