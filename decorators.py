# ДЕКОРАТОРЫ
def hello():        # основная функция, которую будем "обертывать" функцией декоратором
    print("Hello")

def other():
    return "other"

def add_separators(f):  # функция декоратор - добавление разделителя (обертка функции f)
    # inner - итоговая фукция с новым поведение
    def inner():
        # поведение до вызова
        print("*" * 10)
        result = f()
        # поведение после вызова
        print("*" * 10)
        return result
    # возвращаем результат новой функции inner
    return inner

new_hello = add_separators(hello)

hello()          # вызываем исходную функцию
new_hello()      # вызываем функцию, обернутую функцией-декоратором

@add_separators  # это аналогично записи:  other = add_separators(other)
def other():
    return "other"

result = other()

print(result)