import pytest

# filter() - фильтрует последовательность с помощью заданного алгоритма (фильтрующей функции)
numbers = [1, 2, 4, 5, 7, 8, 10, 11]    # список чисел

def filter_odd_num(in_num): # фильтрующая функция (для четных->True, для нечетных->False)
    if(in_num % 2) == 0:
        return True
    else:
        return False

out_filter = filter(filter_odd_num, numbers) # Применение filter() - оставляем ТОЛЬКО четные числа
print(list(out_filter))

# ТЕСТ для функции filter:
def test_filter():          # тестирующая функция проверяет функцию filter
    assert list(filter(filter_odd_num, [1, 2, 4, 5, 7, 8, 10, 11])) == [2, 4, 8, 10]

# map() - преобразует последовательность с помощью заданного алгоритма (преобразующей функции)
lambda_function = lambda x: x**2    # возводим в квадрат
print(lambda_function(5))
result = map(lambda_function, (1, 2, 3, 4, 5, 6, 7, 8, 9)) # возводим последовательность в квадрат
print(list(result))

# ТЕСТ для функции map:
def test_map():          # тестирующая функция проверяет функцию map
    assert list(map(lambda_function, (1, 2, 3, 4, 5, 6, 7, 8, 9))) == [1, 4, 9, 16, 25, 36, 49, 64, 81]

# sorted() - сортирует последовательность (по возрастанию, по убыванию, по ключу)
l1=[1, 4, 5, 2, 456, 12]
print(sorted(l1))   # Вывод:[1, 2, 4, 5, 12, 456]

# ТЕСТ для функции sorted:
def test_sorted():          # тестирующая функция проверяет функцию sorted
    assert sorted([1, 4, 5, 2, 456, 12]) == [1, 2, 4, 5, 12, 456]


# ТЕСТЫ ДЛЯ МАТЕМАТИЧЕСКИХ ФУНКЦИЙ
import math  # импортируем, чтобы работали математические функции (pi, sqrt,...)

def test_pi():    # тестирующая функция проверяет функцию pi
    assert round(math.pi, 5) == 3.14159  # округляем, чтобы сравнить с 3.14159

def test_sqrt():
    assert math.sqrt(4) == 2  # квадратный корень

def test_pow():
    assert math.pow(2, 3) == 8  # возведение числа в степень

def test_hypot():
    assert math.hypot(5, 5) ==7.0710678118654755 # вычисление гипотенузы
