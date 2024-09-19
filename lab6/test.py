import pytest
from classes import HashTable

@pytest.fixture
def empty_hash_table():
    return HashTable(capacity=10)

@pytest.fixture
def hash_table():
    ht = HashTable(capacity=10)
    ht.add('Матрица', 'Прямоугольная таблица чисел')
    ht.add('Факториал', 'Произведение всех целых чисел от 1 до данного числа')
    ht.add('Геометрия', 'Раздел математики, изучающий формы и пространственные отношения')
    ht.add('Тригонометрия', 'Раздел математики, изучающий отношения между углами и сторонами треугольников')
    ht.add('Комплексное число', 'Число вида a + bi, где a и b — действительные числа, а i — мнимая единица')
    return ht

def test_add(empty_hash_table):
    empty_hash_table.add('яблоко', 'фрукт')
    assert empty_hash_table.get('яблоко') == 'фрукт'

def test_get(hash_table):
    assert hash_table.get('Матрица') == 'Прямоугольная таблица чисел'
    assert hash_table.get('Комплексное число') == 'Число вида a + bi, где a и b — действительные числа, а i — мнимая единица'

def test_update(hash_table):
    hash_table.add('Матрица', 'Обновленное определение')
    assert hash_table.get('Матрица') == 'Обновленное определение'

def test_remove(hash_table):
    hash_table.remove('Факториал')
    with pytest.raises(KeyError):
        hash_table.get('Факториал')

def test_collision(empty_hash_table):
    empty_hash_table.add('яблоко', 'фрукт')
    empty_hash_table.add('апельсин', 'фрукт')
    empty_hash_table.add('банан', 'фрукт')
    empty_hash_table.add('груша', 'фрукт')
    empty_hash_table.add('персик', 'фрукт')

    assert empty_hash_table.get('яблоко') == 'фрукт'
    assert empty_hash_table.get('апельсин') == 'фрукт'
    assert empty_hash_table.get('банан') == 'фрукт'
    assert empty_hash_table.get('груша') == 'фрукт'
    assert empty_hash_table.get('персик') == 'фрукт'

def test_key_not_found(empty_hash_table):
    with pytest.raises(KeyError):
        empty_hash_table.get('несуществующий_ключ')

if __name__ == "__main__":
    pytest.main()
