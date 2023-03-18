# from time import perf_counter
# from random import randint
#
# some_list = [randint(1, 1000000) for _ in range(1000000)]
#
# start = perf_counter()
# print(100234 in some_list)
# end = perf_counter()
# first_time = end - start
#
# some_set = set(some_list)
#
# start = perf_counter()
# print(40 in some_set)
# end = perf_counter()
# second_time = end - start
# print(first_time / second_time)

# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# spisok = []
# list_len = int(input("длина списка "))
# for i in range(list_len):
#     spisok.append(int(input(f"{i+1} = ")))
# spisok = set(spisok)
# print(f"уникальных чисел {len(spisok)}")

# 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# spisok = []
# list_len = int(input("длина списка "))
# for i in range(list_len):
#     spisok.append(int(input(f"{i + 1} = ")))
# k = int(input("Введите К "))
# while k > len(spisok):
#     k = k - len(spisok)
# spisok = spisok[-k:] + spisok[:-k]
# print(spisok)

# 21. Напишите программу для печати всех уникальных значений в словаре.

# dict_ = {}
# dict_len = int(input("Длина словаря "))
# for _ in range(dict_len):
#     input_key = input("ключ ")
#     input_value = input("значение ")
#     dict_[input_key] = input_value
#
# print(set(dict_.values()))

# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
    print(input_list)
count = 0
for i in range(list_len - 1):
    if input_list[i] < input_list[i + 1]:
        count += 1
print(f"Количество элементов массива, больших предыдущего : {count}")