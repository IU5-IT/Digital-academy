# Copyright 2022 Dmitriy <dimapermyakov55@gmail.com>
from tasks import *


def main():
    print(task1())
    print(task2())
    print(task3())

    for el in task4():
        print(el)

    print(task6())
    print(task7())

    for key, value in task8().items():
        print(f'{key}: {value}')

    print(task9())


if __name__ == '__main__':
    main()
