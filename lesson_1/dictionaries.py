# Создайте словарь:
weather = {"city": "Москва", "temperature": 20}

# Выведите на экран значение ключа city
print(weather['city'])

# Уменьшите значение "temperature" на 5
weather['temperature'] -= 5

# Выведите на экран весь словарь
print(weather)

# Проверьте, есть ли в словаре ключ country
print(weather.get("country"))

# Выведите значение по-умолчанию "Россия" для ключа country
print(weather.get("country", "Россия"))

# Добавьте в словарь элемент date со значением "27.05.2019"
weather['date'] = "27.05.2019"

# Выведите на экран длину словаря
print(len(weather))
