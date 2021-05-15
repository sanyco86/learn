# Создайте функцию get_summ(one, two, delimiter='&'),
# которая принимает два параметра, приводит их к строке
# и отдает объединенными через разделитель delimiter

# Вызовите функцию, передав в нее два аргумента "Learn" и "python",
# положите результат в переменную и выведите ее значение на экран

# Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_sum(one, two, delimiter='&'):
    lst = [str(one), str(two)]
    return delimiter.join(lst)


join_str = get_sum("Learn", "python")

print(join_str.upper())
