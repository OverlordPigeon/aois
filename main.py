from classes import HashTable

if __name__ == "__main__":
    ht = HashTable(capacity=20)

    entries = [
        ('Матрица', 'Прямоугольная таблица чисел'),
        ('Факториал', 'Произведение всех целых чисел от 1 до данного числа'),
        ('Геометрия', 'Раздел математики, изучающий формы и пространственные отношения'),
        ('Тригонометрия', 'Раздел математики, изучающий отношения между углами и сторонами треугольников'),
        ('Комплексное число', 'Число вида a + bi, где a и b — действительные числа, а i — мнимая единица'),
        ('Переменная', 'Символ, обозначающий изменяющуюся величину'),
        ('Вектор', 'Величина, имеющая направление и величину'),
        ('Статистика', 'Наука о сборе, анализе и интерпретации данных'),
        ('Производная', 'Мера изменения функции при изменении её аргумента'),
        ('Линейная алгебра', 'Раздел математики, изучающий векторные пространства и линейные преобразования')
    ]

    for key, value in entries:
        ht.add(key, value)

    print(ht)

    print("Значение для 'линейная алгебра':", ht.get('Линейная алгебра'))
    print("Значение для 'статистика':", ht.get('Статистика'))

    ht.remove('Переменная')
    print(ht)
