# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import datetime
from functools import wraps
from inspect import getcallargs


def logging_decorator(lst: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_answer = datetime.datetime.now()
            res = func(*args, **kwargs)
            lst.append({
                'name': func.__name__,
                'arguments': getcallargs(func, *args, **kwargs),
                'call_time': time_answer,
                'result': res
            })
            return res

        return wrapper

    return decorator


logger = []


@logging_decorator(logger)
def test_simple(a, b=2):
    return 127


if __name__ == '__main__':
    test_simple(1, 2)
    print(logger)
