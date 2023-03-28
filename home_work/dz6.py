from random import randint

"""Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

num1 = int(input("первый элемент "))
step = int(input("разность "))
numbers = int(input("число элементов "))


def ariph_progress(n1, s, n):
    list_ = [i for i in range(n1, n * s+1, s)]
    return list_


print(ariph_progress(num1, step, numbers))

"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
 (т.е. не меньше заданного минимума и не больше заданного максимума)"""

list_ = [randint(-100, 100) for i in range(randint(10, 20+1))]
mi = int(input("минимум "))
ma = int(input("максимум "))
print(*list(enumerate(list_)), sep=' ')


def find_indexs(arr: list, min, max):
    list_result = []
    for i in range(len(arr)):
        if min < arr[i] < max:
            list_result.append(i)
    return list_result


print(find_indexs(list_, mi, ma))

