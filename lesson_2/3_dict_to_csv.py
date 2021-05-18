"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    user_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 28, 'job': 'Programmer'},
        {'name': 'Петя', 'age': 30, 'job': 'Manager'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]

    with open('tmp/export.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, user_list[0].keys(), delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
