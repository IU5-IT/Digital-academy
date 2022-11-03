# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import json
import re


def get_popular_name_from_file(filename: str) -> str:
    with open(filename) as f:
        names = [person.split()[0] for person in f.readlines()]
        lst = {el: names.count(el) for el in set(names)}
        max_ind = max([el for el in lst.values()])
        return str(sorted([name for name, count in lst.items() if count == max_ind])).replace("'", '')[1:-1]


def mean_age(json_string):
    res = [el["age"] for el in json.loads(json_string)]
    return json.dumps({"mean_age": sum(res) / len(res)})


def check_string(string) -> bool:
    pattern = re.compile(
        r'(\s*([78])?\s*[-(]*\s*([0-9]{3})\s*[)-]*\s*([0-9]{3})\s*-*\s*([0-9]{2})\s*-*\s*([0-9]{2})\s*$)')
    pattern2 = re.compile(
        r'(\s*(\+\s*7\s*)\s*[-(]*\s*([0-9]{3})\s*[)-]*\s*([0-9]{3})\s*-*\s*([0-9]{2})\s*-*\s*([0-9]{2})\s*$)')
    pattern3 = re.compile(r'\s*[a-z._-]+@([a-z]{2,})\.([a-z]{2,})(\.[a-z]{2,})*$')
    return True if pattern.match(string) else True if pattern2.match(string) else True if pattern3.match(
        string) else False


def main():
    lst = ['abc@abc.ab',
           'abc@abc.ab.ab',
           'a@ab.ab',
           'abc.abc@abc.abc',
           '@abc.abc',
           'abc@abc',
           'abc@abc.a',
           'abc@abc.abc.a',
           'abc@abc.',
           'abc@abc@abc'
           ]



if __name__ == '__main__':
    main()
