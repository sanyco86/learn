"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import re
import requests

def download_dropbox_file():
    url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1'
    response = requests.get(url, allow_redirects=True)
    open('tmp/referat.txt', 'wb').write(response.content)


def main():
    try:
        with open('tmp/referat.txt', 'r', encoding='utf-8') as file:
            data = file.read()

        print('длина строки:', len(data))
        print('количество слов:', len(re.findall(r'[-А-Яа-я]+', data)))

        with open('tmp/referat2.txt', 'w', encoding='utf-8') as f:
            f.write(data.replace('.', '!'))
    except FileNotFoundError:
        print('File Not Found Error')


if __name__ == "__main__":
    download_dropbox_file()
    main()
