# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

class Calculator:
    last: str | None = None

    def __init__(self):
        self.lst_history = list()

    def sum(self, number_1: int | float, number_2: int | float):
        res = number_1 + number_2
        self.lst_history.append(f'sum({number_1}, {number_2}) == {round(res, 1)}')
        self.set_last(f'sum({number_1}, {number_2}) == {round(res, 1)}')
        return res

    def sub(self, number_1: int | float, number_2: int | float):
        res = number_1 - number_2
        self.lst_history.append(f'sub({number_1}, {number_2}) == {round(res, 1)}')
        self.set_last(f'sub({number_1}, {number_2}) == {round(res, 1)}')
        return res

    def mul(self, number_1: int | float, number_2: int | float):
        res = number_1 * number_2
        self.lst_history.append(f'mul({number_1}, {number_2}) == {round(res, 1)}')
        self.set_last(f'mul({number_1}, {number_2}) == {round(res, 1)}')
        return res

    def div(self, number_1: int | float, number_2: int | float, mod: bool = False):
        res = number_1 % number_2 if mod else number_1 / number_2
        self.lst_history.append(f'div({number_1}, {number_2}) == {round(res, 1)}')
        self.set_last(f'div({number_1}, {number_2}) == {round(res, 1)}')
        return res

    @classmethod
    def set_last(cls, text: str):
        cls.last = text

    def history(self, n):
        return self.lst_history[-n] if len(self.lst_history) != 0 else None

    @classmethod
    def clear(cls):
        cls.last = None


def main():
    pass


if __name__ == '__main__':
    main()
