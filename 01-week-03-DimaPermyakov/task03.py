# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

def get_balance(name, transactions) -> int:
    return sum([dict_el['amount'] for dict_el in list(filter(lambda el: el['name'] == name, transactions))])


def count_debts(names, amount, transactions) -> dict:
    return {name: 0 if get_balance(name, transactions) > amount else amount - get_balance(name, transactions) for name
            in names}


def task03():
    transactions = [{"name": "Василий", "amount": 500}, {"name": "Петя", "amount": 100},
                           {"name": "Василий", "amount": -300}, ]
    get_balance("Василий", transactions)
    res = count_debts(["Василий", "Петя", "Вова"], 150, transactions)
    return res


if __name__ == '__main__':
    task03()
