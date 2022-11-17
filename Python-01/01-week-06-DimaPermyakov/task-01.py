# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import re


class Field(dict):
    def __getitem__(self, key):
        return super(Field, self).__getitem__(self.__get_data(key))

    def __setitem__(self, key, value):
        super(Field, self).__setitem__(self.__get_data(key), value)

    def __delitem__(self, key):
        super(Field, self).__delitem__(self.__get_data(key))

    def __iter__(self):
        for el in self.values():
            yield el

    def __missing__(self, key):
        return None

    def __contains__(self, key):
        return self[self.__get_data(key)] != self.__missing__(1)

    @staticmethod
    def __get_data(data):
        if type(data) == str:
            a = str(re.sub(r'\d+', '', data))
            b = re.findall(r'\d+', data)
            if len(a) != 1 or len(b) == 0:
                raise ValueError

            if not str(*b).isdigit():
                raise ValueError

            else:
                return f'{a}{str(*b)}'.lower()

        elif type(data) == tuple:
            a, b = data
            if type(a) in [str, int] and type(b) in [str, int]:
                if type(a) is str and not a.isdigit() and len(a) != 1:
                    raise ValueError
                elif type(a) is int and a is None:
                    raise ValueError
                if type(b) is str and not b.isdigit() and len(b) != 1:
                    raise ValueError
                elif type(b) is int and b is None:
                    raise ValueError

                return f'{a}{b}'.lower() if type(a) is str and not a.isdigit() else f'{b}{a}'.lower()

            else:
                raise ValueError

        else:
            raise TypeError


def main():
    field = Field()
    print(field["C5"] is None)
    field['a', 1] = 1
    field['b', 1] = 2
    field['c', 1] = 3
    field['d', 1] = 4
    field[1, 'a'] = 1
    field['a', 1] = 2
    field['a', '1'] = 3
    field['1', 'a'] = 4
    field['1a'] = 5
    field['a1'] = 6
    field[1, 'A'] = 7
    field['A', 1] = 8
    field['A', '1'] = 9
    field['1', 'A'] = 10
    field[1, 'A'] = 10
    field['1A'] = 11
    field['A1'] = 12
    print(field)
    print((1, 'a') in field)
    print("A1" in field)
    print(('D', '4') in field)
    for el in field:
        print(el)
    field['F', '123'] = 4
    print(field['F333'] is None)
    print('До удаления: ', *field)
    del field['1', 'a']
    print('После удаления: ', *field)

    # Проверка на выдачу ошибок.
    ERROR_KEY = [
        'AA5',
        'Q2.5',
        '- 6F',
        'A',
        '27',
        'GG'
    ]
    for error_key in ERROR_KEY:
        try:
            field[error_key] = 666
        except ValueError:
            print(f'В field[{error_key}] ошибка ValueError')
        except TypeError:
            print(f'В field[{error_key}] ошибка TypeError')


if __name__ == '__main__':
    main()
