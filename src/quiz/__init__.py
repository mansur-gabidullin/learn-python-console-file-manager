"""
Викторина
"""

from random import sample

people_birthdays = {
    'ivanov': '10.01.1988',
    'petrov': '10.02.1988',
    'sidorov': '10.03.1988',
    'smirnov': '10.04.1988',
    'popov': '10.05.1988',
    'putin': '10.06.1988',
    'agutin': '10.07.1988',
    'lisicin': '10.08.1988',
    'test1': '10.09.1988',
    'test2': '10.10.1988',
}

numbers_text = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвёртое',
    '05': 'пятое',
    '06': 'шестое',
    '07': 'седьмое',
    '08': 'восьмое',
    '09': 'девятое',
    '10': 'десятое',
    '11': 'одинацатое',
    '12': 'двенадцатое',
    '13': 'тринадцатое',
    '14': 'четырнадцатое',
    '15': 'пятнадцатое',
    '16': 'шестнадцатое',
    '17': 'семнадцатое',
    '18': 'восемнадцатое',
    '19': 'девятнадцатое',
    '20': 'двадцатое',
    '21': 'двадцать первое',
    '22': 'двадцать второе',
    '23': 'двадцать третье',
    '24': 'двадцать четвёртое',
    '25': 'двадцать пятое',
    '26': 'двадцать шестое',
    '27': 'двадцать седьмое',
    '28': 'двадцать восьмое',
    '29': 'двадцать девятое',
    '30': 'тридцатое',
}

months_text = {
    '01': 'январь',
    '02': 'февраль',
    '03': 'март',
    '04': 'апрель',
    '05': 'май',
    '06': 'июнь',
    '07': 'июль',
    '08': 'август',
    '09': 'сентябрь',
    '10': 'октябрь',
    '11': 'ноябрь',
    '12': 'декабрь'
}


def run():
    stop_victory = False

    while not stop_victory:
        selected_people = sample(people_birthdays.keys(), 5)
        all_answers_count = 0
        correct_answers_count = 0

        for man in selected_people:
            all_answers_count += 1

            if input(f'Введите дату рождения {man} ') != people_birthdays[man]:
                day, month, year = people_birthdays[man].split('.')
                print(f'{numbers_text[day]} {months_text[month]} {year} года')
            else:
                print('правильно!')
                correct_answers_count += 1

        print('Количество правильных ответов:', correct_answers_count)
        print('Неправильных ответов {:.0%}'.format((all_answers_count - correct_answers_count) / all_answers_count))

        if input('Повторить? да/нет ') != 'да':
            stop_victory = True
