# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import datetime
import json


class Booking:
    __slots__ = ('_room_name', '_start', '_end', '_duration', '_start_date', '_end_date', '_start_time', '_end_time')

    def __init__(self, name: str, start: datetime.datetime, end: datetime.datetime):
        self._room_name = name
        if start >= end:
            raise ValueError
        self._start: datetime.datetime = start
        self._end: datetime.datetime = end
        self._duration: int = (end - start).seconds // 60
        self._start_date: str = start.strftime('%Y-%m-%d')
        self._end_date: str = end.strftime('%Y-%m-%d')
        self._start_time: str = start.strftime('%H:%M')
        self._end_time: str = end.strftime('%H:%M')

    @property
    def room_name(self):
        return self._room_name

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, new_start):
        self._start = new_start
        self._duration = (new_start - self._end).seconds // 60
        self._start_time = new_start.strftime('%H:%M')
        self._start_date = new_start.strftime('%Y-%m-%d')

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, new_end):
        self._end = new_end
        self._duration = (self._start - new_end).seconds // 60
        self._end_date = new_end.strftime('%Y-%m-%d')
        self._end_time = new_end.strftime('%H:%M')

    @property
    def duration(self):
        return self._duration

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time


def create_booking(room_name, start, end) -> str:
    print('Начинаем создание бронирования')
    book: Booking = Booking(room_name, start, end)
    try:
        func_res: bool = register_booking(book)
        msg = 'Бронирование создано' if func_res else 'Комната занята'
    except KeyError:
        func_res = False
        msg = 'Комната не найдена'
    finally:
        print('Заканчиваем создание бронирования')
    return json.dumps({
        "created": func_res,
        "msg": msg,
        "booking": {
            "room_name": room_name,
            "start_date": book.start_date,
            "start_time": book.start_time,
            "end_date": book.end_date,
            "end_time": book.end_time,
            "duration": book.duration
        }
    }, indent=2, ensure_ascii=False)


def register_booking(book: Booking):
    """ Это функция пустышка. Реализация не требуется. Я её создал для удобства тестирования."""
    return False


def main():
    result = create_booking(
        "Вагнер",
        datetime.datetime(2022, 9, 1, 14),
        datetime.datetime(2022, 9, 1, 15, 15)
    )
    print(result)
    r = """{
  "created": false,
  "msg": "Комната занята",
  "booking": {
    "room_name": "Вагнер",
    "start_date": "2022-09-01",
    "start_time": "14:00",
    "end_date": "2022-09-01",
    "end_time": "15:15",
    "duration": 75
  }
}"""
    print(r == result)


if __name__ == '__main__':
    main()
