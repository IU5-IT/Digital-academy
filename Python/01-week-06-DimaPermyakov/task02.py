# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
from task01 import Field


class Field2(Field):
    def __getattr__(self, key):
        return self[self._get_data(key)]

    def __setattr__(self, key, value):
        try:
            self[self._get_data(key)] = value
        except:
            super().__setattr__(key, value)

    def __delattr__(self, key):
        try:
            del self[self._get_data(key)]
        except:
            super().__delattr__(key)


def main():
    field = Field2()
    field.a1 = 10
    print(field.A1)
    print(field.a1)
    del field.a1
    print(field.a1)
    field = Field2()
    field.abcde = 125
    print(field.abcde)
    print(field.abcde, field.__dict__)


if __name__ == '__main__':
    main()
