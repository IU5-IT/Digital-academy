# Copyright 2022 Dmitriy <dimapermyakov55@gmail.com>

from datetime import date, timedelta
from typing import Any, Generator


def task1() -> str:
    """
    :return: Строку "привет".
    """
    num = input()
    if num == 'привет' or num == 'здравствуйте':
        return 'привет'


def task2() -> int:
    """
    :return: Сумма чётных чисел.
    """
    sum_result = 0
    while True:
        num = input()
        if num == '':
            break

        if int(num) % 2 == 0:
            sum_result += int(num)

    return sum_result


def task3() -> str:
    """
    Заменяет пробелы звездочкой. Если встречается подряд
    несколько пробелов, то заменяет одним знаком "*", пробелы в начале и конце строки удаляются.
    :return: Какая-нибудь*строка*типа*этой*.
    """
    return '*'.join((' '.join(input().split())).split())


def task4() -> Generator[str, Any, None]:
    """
    Формат ввода:
    Раз два три четыре пять
    а

    Формат вывода:
    Раз
    два

    :return: Генератор слов.
    """
    full_text = input().split()
    substring = input().lower()
    return (el for el in full_text if substring in el.lower())


def task6() -> str:
    """
    С клавиатуры подается 5 чисел, разделенных концом строки.
    Нужно вывести их на экран от большего к меньшему, также разделяя их концом строки.
    :return: Строка.
    """
    text = ''
    for i in range(5):
        text += input()
        text += '\n'
    text = text[:-1].split('\n')

    # Можно в одну строчку сделать, но, полагаю, это не очень хорошая идея)).
    numbers = list(map(lambda num: int(num), text))
    numbers = '\n'.join(map(lambda num: str(num), sorted(numbers, reverse=True)))

    return numbers


def task7() -> str:
    """
    С клавиатуры строка, содержащая произвольное количество слов через запятую и пробел.
    Слова могут повторяться. Нужно вывести на экран все уникальные слова в алфавитном порядке,
    также через пробел и запятую.
    :return: строку.
    """
    return ', '.join(sorted(list(set(map(lambda word: word.lower(), input().split(', '))))))


def task8() -> dict:
    """
    С клавиатуры вводятся слова через запятую с пробелом. Выведите на экран три наиболее часто встречаемых слова,
    вместе с количеством этих слов. Количество должно быть отделено от слова двоеточием и пробелом.
    Каждая пара слово-количество должна быть выведена на отдельной строчке. Для простоты гарантируется,
    что в строке нет слов с одинаковой встречаемостью.
    :return: Словарь с самыми повторяющимися.
    """
    lst = input().lower().split(', ')
    set_lst = set(lst)
    dict_word = {el: lst.count(el) for el in set_lst}
    values = sorted(dict_word.values(), reverse=True)
    values = values[:3]
    return {key: val for el in values for key, val in dict_word.items() if el == val}


def task9() -> str:
    """
    С клавиатуры вводится дата в формате DD-MM-YYYY.
    Нужно вывести дату начала недели, к которой относится введенная дата (дата понедельника недели),
    в таком же формате.
    :return: Дату начала недели.
    """
    day, month, year = list(map(int, input().split('-')))
    user_date = date(year, month, day)
    week_day = user_date.strftime("%A")

    while week_day != 'Monday':
        user_date -= timedelta(days=1)
        week_day = user_date.strftime('%A')

    return f'{"0" + str(user_date.day) if user_date.day < 10 else user_date.day}-' \
           f'{"0" + str(user_date.month) if user_date.month < 10 else user_date.month}-{user_date.year}'


def main():
    pass


if __name__ == '__main__':
    main()
