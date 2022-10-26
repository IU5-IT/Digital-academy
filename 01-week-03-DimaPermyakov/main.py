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
        for el in {lst}:
            sum_res += sum(el)

    return sum_res


def get_balance(name, transactions) -> int:
    """
    Функция, которая возвращает текущий баланс друга с именем name, исходя из списка транзакций transactions.
    Если имя name ни разу не встречается в списке transactions, считаем, что баланс этого друга в общаке равен 0 рублей.
    """
    flag = False
    res = 0
    for el in transactions:
        if name in el.values():
            flag = True
            res += el['amount']
    if not flag:
        transactions.append({'name': name, 'amount': 0})
    return res


def count_debts(names, amount, transactions) -> dict:
    """
    Функция, которая принимает список имен присутствующих на мероприятии друзей names,
    стоимость баранок и чая на человека amount, а также список транзакций в общак transactions.
    Вернуть эта функция должна словарь вида {"имя_друга": 100}, где 100 - это количество денег,
    которое он должен скинуть на мероприятие. Если на балансе друга больше денег, чем требуется на мероприятие,
    то он должен 0 рублей.
    """
    pass


def main():
    transactions = [{"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100},
                    {"name": "Василий", "amount": -300}, ]

    print(get_balance("Василий", transactions))
    count_debts(["Василий", "Петя", "Вова"], 150, transactions)


if __name__ == '__main__':
    main()
