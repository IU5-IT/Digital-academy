# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

def get_balance(name: str, transactions: list) -> int:
    return sum([el['amount'] for el in transactions if el['name'] == name])


def count_debts(names: list, amount: int | float, transactions: list) -> dict:
    return {name: max(amount - get_balance(name, transactions), 0) for name in names}


def task03():
    transactions = [{"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100},
                    {"name": "Василий", "amount": -300}]
    get_balance("Василий", transactions)
    res = count_debts(["Василий", "Петя", "Вова"], 150, transactions)
    return res


if __name__ == '__main__':
    task03()
