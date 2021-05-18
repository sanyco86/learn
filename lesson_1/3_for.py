"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    school_book = [
        {'school_class': '4А', 'scores': [3,4,4,5,3]},
        {'school_class': '4Б', 'scores': [3,4,4,5,4]},
        {'school_class': '4В', 'scores': [3,4,4,5,5]},
        {'school_class': '5А', 'scores': [3,4,3,5,2]},
        {'school_class': '5Б', 'scores': [3,5,4,5,2]},
        {'school_class': '5В', 'scores': [3,4,2,5,3]},
        {'school_class': '6А', 'scores': [3,4,4,2,2]},
        {'school_class': '6Б', 'scores': [3,4,4,3,2]},
        {'school_class': '6В', 'scores': [3,4,4,5,5]},
    ]

    scores = []

    for klass in school_book:
        for item in klass['scores']:
            scores.append(item)

        print(f"{klass['school_class']}: {sum(klass['scores']) / len(klass['scores'])}")

    print(f"Total: {sum(scores) / len(scores)}")

if __name__ == "__main__":
    main()
