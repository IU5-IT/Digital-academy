# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import datetime


def gift_count(budget, month, birthdays):
    counter = 0
    for el in birthdays.values():
        if el.month == month:
            counter += 1
    pass


def main():
    birthdays = {
        "Иванов Иван Иванович": datetime.date(1989, 5, 1),
        "Петров Петр Петрович": datetime.date(1998, 5, 6)
    }
    print(birthdays.values())
    for el in birthdays.values():
        if el.month == 5:
            print('EA')
    # date = datetime.date(1999, 11, 28)

    # gift_count(20000, 5, birthdays)
    # gift_count(budget=20000, month=5, birthdays=birthdays)


if __name__ == '__main__':
    main()
