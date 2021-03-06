"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def get_educational_institution(input_age):
    try:
        age = int(input_age)

        if age <= 0:
            return 'Вы еще не родились'
        elif age > 60:
            return 'Вы пенсионер'
        elif age > 23:
            return 'Вы работаете'
        elif age > 17:
            return 'Вы студент'
        elif age > 7:
            return 'Вы школьник'
        elif age > 3:
            return 'Вы дошкольник'
        else:
            return 'Вы мледенец'
    except(TypeError, ValueError):
        return 'Не верный тип данных'


def main():
    age = input('Сколько Вам лет?:')
    educational_institution = get_educational_institution(age)

    print(educational_institution)


if __name__ == "__main__":
    main()
