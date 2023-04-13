"""ИНН физика состоит из 12 цифр и последние 2 из них - контрольные.
Нужно реализовать "продакшн реди" ф-ю проверяющую валидность ИНН.
Контрольные цифры (n_11 и n_12) вычисляются по алгоритму:
Контрольное число n есть остаток от деления на 11 суммы из цифр номера,
умноженных на соответствующие коэффициенты.
Если остаток есть 10, то n = 0.

Коэффициенты для n_11 - 7, 2, 4, 10, 3, 5, 9, 4, 6, 8
Коэффициенты для n_12 - 3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8

Примеры: 100000000074, 100010000002, 100010010032, 969944000024
ИНН считается валидным, если контрольные цифры соответствуют алгоритму."""


inn_ = input("проверка ИНН ")


def check_inn(inn):
    inn = [int(i) for i in inn]
    n_11 = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    n_12 = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)

    n11 = 0
    n12 = 0

    for i in range(len(n_11)):
        n11 += inn[i] * n_11[i]
        n12 += inn[i] * n_12[i]
    n12 += inn[-2] * n_12[-1]

    n11 %= 11
    n12 %= 11

    if n11 == 10:
        n11 = 0
    if n12 == 10:
        n12 = 0
    if n11 == inn[-2] and n12 == inn[-1]:
        return True
    return False


def check_inn_GPT(in_n):
    if len(in_n) != 12:
        return False
    inn = [int(i) for i in in_n]
    n_11n = sum(inn[i] * [7, 2, 4, 10, 3, 5, 9, 4, 6, 8][i] for i in range(10)) % 11
    n_12n = sum(inn[i] * [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8][i] for i in range(11)) % 11
    if n_11n == 10:
        n_11n = 0
    if n_12n == 10:
        n_12n = 0
    return int(inn[-2]) == n_11n and int(inn[-1]) == n_12n

"""задача 2"""
# result = []
#
# stop = False
# separator_letter = input("Введите символ: ")
# while not stop:
#     input_str = input("введите строку: ")
#     if input_str == "ВЕЧЕР":
#         stop = True
#     part_list = input_str.split(separator_letter)
#     if len(part_list) > 1:
#         result.append(part_list[1])
#
# print(*set(result), sep="\n")

