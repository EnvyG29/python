from random import randint

# 25. Напишите программу, которая принимает на вход строку, и отслеживает количество повторов каждого символа.

# input_str = input("Слово ")
#
# dict_ = {}
# value = 0
#
# for i in input_str:
#     if i in dict_:
#         dict_[i] += 1
#     else:
#         dict_[i] = 1
# print(dict_)
#

# 27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

#
# input_str = input("Текст ").lower() + " "
#
# value = 1
# set_ = set()
# word = ""
# for i in input_str:
#     if i != " ":
#         word += i
#     else:
#         set_.add(word)
#         word = ""
# print(set_)
#
# print(len(set_))
#

# 1.Создайте список из случайных чисел. Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).

# input_list = [randint(1, 100) for _ in range(10)]
# print(input_list)
# for i in range(len(input_list) - 2, 0, -1):
#     if input_list[i - 1] < input_list[i] > input_list[i + 1]:
#         print(i)
#         break

# 3.Создайте список из случайных чисел. Найдите второй максимум.

input_list = [randint(1, 100) for _ in range(10)]
max1, max2 = input_list[0], input_list[1]
print(input_list)
for i in input_list:
    if i > max1:
        max1 = max2
        max2 = i
    elif i > max2 and i != max1:
        max2 = i
print(max2)
