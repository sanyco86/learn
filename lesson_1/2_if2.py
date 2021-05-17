"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def compare(str_1, str_2):
    if not isinstance(str_1, str) or not isinstance(str_2, str) :
        return 0
    elif str_1 == str_2:
        return 1
    elif str_1 != str_2 and len(str_1) > len(str_2):
        return 2
    elif str_1 != str_2 and str_2 == 'learn':
        return 3

def main():
    print('Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0')
    print(compare(1, 2))
    print(compare(1, 'qwerty'))
    print(compare('qwerty', 2))

    print('Если строки одинаковые, вернуть 1')
    print(compare('qwerty', 'qwerty'))

    print('Если строки разные и первая длиннее, вернуть 2')
    print(compare('qwerty big len', 'qwerty'))

    print('Если строки разные и вторая строка \'learn\', возвращает 3')
    print(compare('abc', 'learn'))

if __name__ == "__main__":
    main()
