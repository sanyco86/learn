"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    today = datetime.today()
    str_today = date_to_str(today)
    str_yesterday = date_to_str(today - timedelta(1), '%Y-%b-%d')
    str_thirty_days_ago = date_to_str(today - timedelta(30))

    print('вчера:', str_yesterday)
    print('сегодня:', str_today)
    print('30 дней назад:', str_thirty_days_ago)


def date_to_str(date_obj, date_format='%Y-%m-%d'):
    return date_obj.strftime(date_format)


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
