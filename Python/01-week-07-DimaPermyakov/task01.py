# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import time


def time_decorator(func):
    def wrapper():
        st = time.time()
        res = func()
        print(int(time.time() - st))
        return res

    return wrapper


@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25


if __name__ == '__main__':
    result = sleep_1_sec()
    print(result)
