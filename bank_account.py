# отрабатываем приемы записи-чтения файла

# ОПРЕДЕЛЕНИЯ ПЕРЕМЕННЫХ И ФУНКЦИИ
import json
import os.path

def bank():
    remains = 0  # обнуляем остаток денег на счету
    history = []  # в данном списке храним историю покупок
    if os.path.exists('file_remains.txt'): # если такой файл существует
        f = open('file_remains.txt', 'r')
        remains = int(f.read()) # счмтываем из файла остаток денег на счете
        f.close()
    if os.path.exists('file_history.json'): # если такой файл существует
        with open('file_history.json', 'r') as f:
            history = json.load(f) # считываем из файла историю покупок

    while True:
        print()                        # печатаем пустую строку (для удобства восприятия)
        print('У Вас на счету: ', remains)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print("У Вас на счету: ", remains)
            remains = remains + int(input("Введите сумму пополнения счета: "))
            print("У Вас на счету: ", remains)
        elif choice == '2':
            name = input("Введите Наименование товара: ") # вводим наименование
            summa = int(input("Введите Стоимость товара: "))
            if remains - summa < 0:  # если остаток на счете меньше суммы покупки
                print("Не хватает денег. Пополните счет")
            else:                    # если денег на счете хватает для осуществления покупки
                remains = remains - summa  # уменьшаем остаток на сумму покупки
                print("Покупка произведена. Остаток денег на Счете: ", remains)
                history.append((name, summa)) # добавляем запись в историю покупок
                print(history)
        elif choice == '3':
            print("История Ваших покупок: ")  # вывод истории покупок
            print(history)
        elif choice == '4':
            f = open('file_remains.txt', 'w')
            f.write(str(remains)) # записываем в виде текста остаток денег
            f.close()
            with open('file_history.json', 'w') as f:
                json.dump(history, f) # записываем в виде текста историю покупок
            break                             # выход из программы
        else:
            print('Неверный пункт меню')

# ИСПОЛНЯЕМАЯ ЧАСТЬ ПРОГРАММЫ:
if __name__ == '__main__':
    bank() # вызываемфункциюю bank()
