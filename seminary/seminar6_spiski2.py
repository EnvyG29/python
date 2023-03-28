from random import randint

"""39. Даны два массива чисел. Требуется вывести те элементы первого массива
 (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
 Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
 Затем число M - количество элементов во втором массиве. Затем элементы второго массива"""

#
#
# list_B = [int(input(f"{i + 1} число ")) for i in range(int(input("Длина спискаB ")))]
#
#
# def cross_list(l_A, l_B):
#     set_B = set(l_B)
#     result = []
#     for i in l_A:
#         if i not in set_B:
#             result.append(i)
#
#     return result
#
# print((cross_list(list_A, list_B)))

"""Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество 
элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится 
число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из 
целых чисел."""

# list_A = [int(input(f"{i + 1} число ")) for i in range(int(input("Длина спискаA ")))]
#
# def count_correct_max(arr: list):
#     count = 0
#     for i in range(1, len(arr) - 1):
#         if arr[i - 1] < arr[i] > arr[i+1]:
#             count += 1
#     return count
# print(count_correct_max(list_A))


"""Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках."""

# list_A = [randint(1, 10) for i in range(50_000_000)]
#
# print(list_A)
#
# def count_couple(l_a: list):
#     """описание функции test"""
#     sum_ = 0
#     set_l = set(l_a)
#     for i in set_l:
#         sum_ += l_a.count(i) // 2
#     return sum_
#
# def dict_cople(l_a: list):
#     count = 0
#     dict_ = {}
#     for i in l_a:
#         if i in dict_:
#             dict_[i] += 1
#         else:
#             dict_[i] = 1
#     for i in dict_.values():
#         count += i // 2
#     return count
#
# from time import perf_counter
# st = perf_counter()
# count_couple(list_A)
# en = perf_counter()
# co = en - st
# st = perf_counter()
# dict_cople(list_A)
# en = perf_counter()
# di = en - st
# print(co/di)
# print()

"""Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
Программа получает на вход одно натуральное число k, не превосходящее 105.
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает)."""


def sum_of_divisors(input_number: int):
    sum_result = 0
    for i in range(1, input_number // 2 + 1):
        if input_number % i == 0:
            sum_result += i
    return sum_result


def friendly_numbers(input_num: int):
    find = set()
    for i in range(1, input_num + 1):  # i = 220
        sum_temp_number = sum_of_divisors(i)  # 284
        sum2 = sum_of_divisors(sum_temp_number)
        if sum2 == i and sum_temp_number != i and i not in find and sum_temp_number not in find:
            print(i, sum_temp_number)
            find.add(i)


input_k = int(input("Введите число k: "))
friendly_numbers(input_k)

