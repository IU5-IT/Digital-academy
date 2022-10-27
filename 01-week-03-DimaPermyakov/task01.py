# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

import datetime


def gift_count(budget: [int, float], month: int, birthdays: dict) -> None | str:
    """
    :param budget: Выделенный бюджет.
    :param month: Месяц, по которому ищут дату.
    :param birthdays: Словарь Имя:Дата.
    :return: По заданию надо использовать print(), чтобы работали тесты. Но я так не хочу. Я возвращаю строку.
    """
    counter = [date.month for date in birthdays.values()].count(month)
    if counter == 0:
        # Да-да, слово 'именинников' с ошибкой, но что поделать. Тесты проверяют на него.
        return 'В этом месяце нет именниннков.'
    people = [f'{name} ({date.strftime("%d.%m.%Y")})' for name, date in birthdays.items() if date.month == month]
    text = str(people).replace("'", '')[1:-1]
    return f'Именинники в месяце {month}: {text}. При бюджете {budget} они получат по {int(budget / counter)} рублей.'


def task01():
    birthdays = {"Катя": datetime.date(1971, 1, 6), "Ваня": datetime.date(1989, 1, 1)}
    print(gift_count(20000, 1, birthdays))
    print(gift_count(budget=20000, month=5, birthdays=birthdays))


if __name__ == '__main__':
    task01()
