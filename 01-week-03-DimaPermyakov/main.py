# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import datetime


def gift_count(budget, month, birthdays):
    counter = list(map(lambda el: el.month, [*birthdays.values()])).count(month)
    people = sorted(
        [f'{name} ({date.day}.{date.month}.{date.year})' for name, date in birthdays.items() if date.month == month])
    text = str(people).replace("'", '')[1:-1]
    return f'Именинники в месяце {counter}: {text}. При бюджете {budget} они получат по {int(budget / counter)} рублей.'


def lists_sum(*args, unique=False) -> int:
    sum_res = 0
    if not unique:
        for el in args:
            sum_res += sum(el)
    else:
        lst = list(map(lambda el1: set(el1), args))
        print(lst)
        for el in lst:
            sum_res += sum(el)

    return sum_res


def main():
    print(lists_sum([1, 1, 1], [1, 1], unique=True) == 1)


if __name__ == '__main__':
    main()
