from random import randint

# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13...

nw = int(input("Фиббоначи "))


def fibonnachi_recursia(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonnachi_recursia(n - 1) + fibonnachi_recursia(n - 2)


def fibonnachi_for(n):
    first = 0
    second = 1
    if n == first:
        return first
    if n == second:
        return second

    count = 2
    while n != count:
        num = first + second
        first = second
        second = num
        count += 1
    return num


print(fibonnachi_for(nw))

print(fibonnachi_recursia(nw))
print()


# 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


def max_replace_min(input_list: list):
    min_ = max_ = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] > max_:
            max_ = input_list[i]
        if input_list[i] < min_:
            min_ = input_list[i]
    for i in range(len(input_list)):
        if input_list[i] == max_:
            input_list[i] = min_


list_ = [randint(1, 5) for i in range(int(input()))]
print(list_)
list_new = max_replace_min(list_)
print(list_)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def is_num_simple(num):
    if num != 2 and num % 2 == 0:
        return False
    for i in range(3, num // 2 + 1, 2):
        if num % i == 0:
            return False
    return True


print(is_num_simple(int(input("простое "))))

# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

list_ = sorted(set([randint(1, 10) for _ in range(10)]))


def a(list_):
    list_.append(1.9)
    result_temp = []
    result = []

    for i in range(len(list_) - 1):
        if list_[i] == list_[i + 1] - 1:
            result_temp.append(list_[i])
        else:
            if list_[i] not in result_temp:
                result_temp.append(list_[i])
            result.append(result_temp)
            result_temp = []
    print(result)
    result_str = []
    for i in result:
        if len(i) >= 2:
            result_str.append(f"{i[0]}-{i[-1]}")
        else:
            result_str.append(i[0])
    return result_str


print(list_)
print(*a(list_), sep=",")
