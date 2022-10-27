# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

def lists_sum(*args: list, unique=False) -> int:
    return \
        [sum([sum(el) for el in args]) if unique else sum([sum(el) for el in list(map(lambda el1: set(el1), args))])][0]


def task02():
    res1 = lists_sum([1, 1], [1], [1, 2, 3])
    res2 = lists_sum([1, 1, 1], [1, 1], unique=True)
    res3 = lists_sum([1, 1, 1], unique=False)
    return res1, res2, res3


if __name__ == '__main__':
    task02()
