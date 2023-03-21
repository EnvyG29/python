"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
  Последняя строка содержит число X.
  Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
   Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""
from random import randint, randrange
from time import perf_counter

print("----16----")

list_ = []
list_len = int(input("Колличество чисел "))
for _ in range(list_len):
    list_.append(randint(0, 10_000))
print(list_)

x = int(input("Искомое "))


def count_(check, arr):
    g = 0
    for k in range(len(arr)):
        if arr[k] == check:
            g += 1
    return g


print(f"повторов {x} = ", end="")
start = perf_counter()
count = 0
for i in range(list_len):
    if list_[i] == x:
        count += 1
print(count)
end = perf_counter()
rr = end - start

print(f"повторов {x} = ", end="")
start = perf_counter()
print(count_(x, list_))
end = perf_counter()
ww = end - start

print(f"повторов {x} = ", end="")
start = perf_counter()
print(list_.count(x))
end = perf_counter()
qq = end - start

print(f"готовый метод быстрее кода в {rr / qq}")
print(f"функция быстрее кода вне функции в {rr / ww}")
print(f"готовый метод быстрее функции в {ww / qq}", end='\n\n')

"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

print("----18----")

list_ = []
list_len = int(input("Колличество чисел "))
for _ in range(list_len):
    list_.append(randrange(0, 10_000, 7))
print(list_)
x = int(input("Искомое "))

start = perf_counter()
el = None
delta = abs(x - list_[0])

for i in range(len(list_)):
    if abs(x - list_[i]) < delta:
        delta = abs(x - list_[i])
        delta2 = abs(x - list_[i + 1])
        if delta != delta2:
            el = list_[i]

end = perf_counter()
print(f"дельта =  {el}")
de = end - start

start = perf_counter()
tuple_ = sorted(set(list_))

for i in range(len(tuple_)):
    if x <= tuple_[i]:
        if abs(x - tuple_[i]) > abs(x - tuple_[i - 1]):
            el = tuple_[i - 1]
            break
        else:
            el = tuple_[i]
            break
    else:
        el = tuple_[i]
end = perf_counter()
print(f"sort = {el}")
so = end - start

print(f"через сортировку быстрее, чем через сравнение дельт в {de / so}")

"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
 В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
 F, H, V, W, Y – 4 очка;  K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
  Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
  Й, Ы – 4 очка;  – 5 очков;  – 8 очков;  – 10 очков. 
  Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
  Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
"""

print("----20----")

en_1 = ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R")
en_2 = ("D", "G")
en_3 = ("B", "C", "M", "P")
en_4 = ("F", "H", "V", "W", "Y")
en_5 = ("K",)
en_8 = ("J", "X")
en_10 = ("Q", "Z")

ru_1 = "АВЕИНОРСТ"
ru_2 = "ДКЛМПУ"
ru_3 = "БГЁЬЯ"
ru_4 = "ЙЫ"
ru_5 = "ЖЭХЦЧ"
ru_8 = "ШЭЮ"
ru_10 = "ФЩЪ"

count = 0
word = input("Слово ").upper()
start = perf_counter()
for i in range(len(word)):
    if word[i] in en_1 or word[i] in ru_1:
        count += 1
    elif word[i] in en_2 or word[i] in ru_2:
        count += 2
    elif word[i] in en_3 or word[i] in ru_3:
        count += 3
    elif word[i] in en_4 or word[i] in ru_4:
        count += 4
    elif word[i] in en_5 or word[i] in ru_5:
        count += 5
    elif word[i] in en_8 or word[i] in ru_8:
        count += 8
    elif word[i] in en_10 or word[i] in ru_10:
        count += 10
print(count) if count > 0 else print("word error")
end = perf_counter()
if_ = end - start

start = perf_counter()
dict_ = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
         'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
         'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
         'Y': 4, 'Z': 10, 'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1,
         'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2,
         'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10,
         'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3,
         'Э': 8, 'Ю': 8, 'Я': 3}


def sum_value(word_, values):
    val = 0
    for letter in word_:
        val += values.get(letter, 0)
        # val += values[letter]
    return val


if all(letter.isalpha() for letter in word):
    value = sum_value(word, dict_)
    print("Стоимость слова :", value)
else:
    print("word error")

end = perf_counter()
gpt = end - start
print(f"код написанный GPT с напильником быстрее множества if в {if_ / gpt}")
