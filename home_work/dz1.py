# Задача 2:
# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print("----02----")

three_igit_number = 357  # int(input("Введите трехзначное число "))

if 99 < three_igit_number < 999:
    a = three_igit_number // 100
    b = three_igit_number % 100 // 10
    c = three_igit_number % 10
    result = a + b + c
    print(f"{three_igit_number} -> {result} ({a} + {b} + {c})")
else:
    print("ТРЕХЗНАЧНОЕ!!!!!")

print()
# ///////////////////////////////////////////////
# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
print("----04----")

sum_birds = 23  # int(input("Введите количество журавликов "))
if sum_birds % 6 == 0:
    boys = sum_birds // 3
    Katya = boys * 2
    print("{} -> {}  {}  {}".format(sum_birds, boys // 2, Katya, boys // 2))
else:
    print(f'Со значением {sum_birds} данная задача не может быть решена в целых числах.')

# .............вариант под любое число..................
print("----04.5----")
# for sum_birds in range(0, 51, 1):
Petya_and_Serezha = sum_birds // 3 if sum_birds // 3 > 2 else 2
if sum_birds < 4:
    Petya_and_Serezha = 0
Katya = sum_birds - Petya_and_Serezha
boy = Petya_and_Serezha // 2
if sum_birds != boy * 2 + Katya:
    Katya += 1

print("{} -> {}  {}  {}".format(sum_birds, boy, Katya, boy))

print()
# //////////////////////////////////////////////////////////////
# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no
print("----06----")

number = str("534345")  # input("Введит номер билета ")
yes = "yes"
no = "no"

if len(number) == 6:
    number = int(number)
    if (number // 100000 + number // 10000 % 10 + number // 1000 % 10) \
            == (number // 100 % 10 + number // 10 % 10 + number % 10):
        a = True
    else:
        a = False
    print(f"{number} ->  {yes if a else no}")
else:
    print("Номер билета шестизначный")

print()
# //////////////////////////////////////////////////////////
# Задача 8:
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
print("----08----")

row = 10  # int(input("Введите длинну плитки "))
column = 3  # int(input("Введите ширину плитки "))
path = 5  # int(input("Введите количество долек "))
yes = "yes"
no = "no"

a = bool(path % row == 0 or path % column == 0)
print(f"{row} {column} {path} -> {yes if a else no}")

