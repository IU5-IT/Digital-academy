# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

import datetime


def gift_count(budget: [int, float], month: int, birthdays: dict) -> str:
    counter = [date.month for date in birthdays.values()].count(month)
    people = sorted(
        [f'{name} ({date.day}.{date.month}.{date.year})' for name, date in birthdays.items() if date.month == month])
    text = str(people).replace("'", '')[1:-1]
    return f'Именинники в месяце {counter}: {text}. При бюджете {budget} они получат по {int(budget / counter)} рублей.'


def task01():
    birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
    gift_count(20000, 5, birthdays)
    res = gift_count(budget=20000, month=5, birthdays=birthdays)
    return res


if __name__ == '__main__':
    task01()
