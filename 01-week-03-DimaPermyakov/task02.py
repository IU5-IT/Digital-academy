# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

def lists_sum(*args: list, unique: bool = False) -> int:
    return [sum([el for el in set([el for lst_wrapper in args for el in lst_wrapper])]) if unique else sum(
        [sum(el) for el in args])][0]


def task02():
    res1 = lists_sum([1, 1], [1], [1, 2, 3])
    res2 = lists_sum([1, 1, 1], [1, 1], unique=True)
    res3 = lists_sum([1, 1, 1], unique=False)
    return res1, res2, res3


if __name__ == '__main__':
    task02()
