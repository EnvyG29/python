from random import randint
from time import perf_counter

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


print("----22----")
n = int(input("длина списка1 "))
m = int(input("длина списка2 "))
set1 = set([randint(-10000, 10000) for _ in range(n)])
set2 = set([randint(-10000, 10000) for _ in range(m)])

start = perf_counter()
list_unit = []
list1 = sorted(set1)
list2 = sorted(set2)

for i in range(len(list1)):
    for k in range(len(list2)):
        if list1[i] == list2[k]:
            list_unit.append(list1[i])
            break
end = perf_counter()
code = end - start

print(list_unit)

start = perf_counter()
list_intersection = sorted(set1.intersection(set2))
end = perf_counter()
intersection = end - start

print(list_intersection)

print(f".intersection() быстрее for в {code / intersection} раз\n\n")  # при 50_000_000 с break в 25й строке разница 7_500 : 1, без - 17_500 : 1

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


print("----24----")

garden_bed = int(input("длина глядки: "))
berry_on_shrub = [randint(1, 100_000) for _ in range(garden_bed)]

start = perf_counter()
max_sum, sum_ = berry_on_shrub[-2] + berry_on_shrub[-1] + berry_on_shrub[0], 0

for i in range(garden_bed - 1):
    sum_ = berry_on_shrub[i - 1] + berry_on_shrub[i] + berry_on_shrub[i + 1]
    if sum_ > max_sum:
        max_sum = sum_
end = perf_counter()
if_ = end - start
print(max_sum)

start = perf_counter()
list_ = []
for i in range(garden_bed - 1):
    sum_ = berry_on_shrub[i - 1] + berry_on_shrub[i] + berry_on_shrub[i + 1]
    list_.append(sum_)
list_.append(berry_on_shrub[-2] + berry_on_shrub[-1] + berry_on_shrub[0])
max_list = max(list_)
end = perf_counter()
etalon = end - start

print(max_list)

some_list = berry_on_shrub
start = perf_counter()
summa = 0
max_sum = 0
penultimate_sum = 0
ultimate_sum = 0
length = len(some_list)
for i in range(len(some_list) - 2):
    penultimate_sum = some_list[length - 2] + some_list[length - 1] + some_list[0]
    ultimate_sum = some_list[length - 1] + some_list[0] + some_list[1]
    summa = some_list[i] + some_list[i + 1] + some_list[i + 2]
    if summa > max_sum:
        max_sum = summa
    if penultimate_sum > max_sum:
        max_sum = penultimate_sum
    if ultimate_sum > max_sum:
        max_sum = ultimate_sum

end = perf_counter()
print(f"Максимальное количество ягод: {max_sum}")

another = end - start

print(f"another/if_ {another / if_}")  # 2.75
print(f"etalon / if_ {etalon / if_}")  # 1.3
print(f"another/ max_ {another / etalon}")  # 2.2
