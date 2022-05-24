import os
import pytest

#ФУНКЦИИ
def long_separator(count):  # определяем функцию long_separator (рисует count звездочек) count - параметр
    print ('*' * count)   # печатаем строку из count символов "звездочка" (символ, умноженный на count)
    return '*' * count

def print_dir():  # функция выводит на печать содержимое текущей директории
    spisok = os.listdir()
    print(spisok)
    return spisok

def make_dir(name): # функция создает папку в текущей директории (если такой нет)
    if not os.path.exists(name):
        os.mkdir(name) # создать папку в текущей папке, если такой нет
    return name

def del_dir(name): # функция удаляет папку в текущей директории (если такая есть)
    if os.path.exists(name):
        os.rmdir(name) # удалить папку в текущей папке, если такая есть
    return name


# ТЕСТЫ
def test_long_separator():
    assert long_separator(5) == '*****'

def test_print_dir():
    assert 'main.py' in os.listdir()

def test_make_dir():
    assert make_dir('new1') in os.listdir()

