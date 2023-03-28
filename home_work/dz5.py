from random import randint


# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по " общим буквам ".

print("---3*--")


def rand_word(lang, h):
    eng = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",
           12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u",
           22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}
    ru = {1: "а", 2: "б", 3: "в", 4: "г", 5: "д", 6: "е", 7: "ё", 8: "ж", 9: "з", 10: "и", 11: "й",
          12: "к", 13: "л", 14: "м", 15: "н", 16: "о", 17: "п", 18: "р", 19: "с", 20: "т", 21: "у",
          22: "ф", 23: "х", 24: "ц", 25: "ч", 26: "ш", 27: "щ", 28: "ъ", 29: "ы", 30: "ь", 31: "э", 32: "ю", 33: "я"}
    if lang == "ru":
        dict_, letters = ru, 33
    if lang == "eng":
        dict_, letters = eng, 26
    q = 0
    word = ""
    while q < h:
        word += dict_[randint(1, letters)]
        q += 1
    return word


# lan = input("ru - русские буквы, eng - английские: ")
# n = int(input("минимальная длина псевдо-слова "))
# m = int(input("максимальная длина псевдо-слова "))
# list_input = list(set([rand_word(lan, randint(n, m)) for i in range(int(input("Длина списка "))+1)]))


list_input = ["et", "te", "tea", "tan", "wate", "ate", "nat", "tawe", "bat", "awet", "rteqr", "qwer", "eat", "batt"]

list_input.sort(key=lambda x: len(x))
print(list_input)

def sort_group(list_):
    list_temp = [[list_[0]]]
    q = 0
    for i in range(1, len(list_)):
        if len(list_[i - 1]) != len(list_[i]):
            list_temp.append([])
            q += 1
        list_temp[q].append(list_[i])

    list_result = [[] for _ in range(len(list_temp))]

    for i in range(len(list_temp)):
        for q in range(len(list_temp[i])):
            if len(list_temp[i]) >= 1:
                list_result[i].append([])
                list_result[i][q].append(list_temp[i].pop(0))
            elif list_temp[i] != []:
                list_result[i].append(list_temp[i].pop(0))
            k = 0
            while k < (len(list_temp[i])):
                if sorted(list_result[i][q][0]) == sorted(list_temp[i][k]):
                    list_result[i][q].append(list_temp[i].pop(k))
                else:
                    k += 1


    return list_result


print(sort_group(list_input))

# вариант chatGPT, я в печале(((

groups = {}
# проходим по каждому слову
for word in list_input:
    # создаем ключ на основе отсортированных букв
    key = ''.join(sorted(word))
    # добавляем слово в список соответствующей группы
    groups.setdefault(key, []).append(word)
# выводим списки групп
print(list(groups.values()))


def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in word_dict:
            word_dict[(frozenset(word), len(word))] = [word]
        else:
            word_dict[(frozenset(word), len(word))].append(word)
    res_list = []
    for value in word_dict.values():
        res_list.append(value)
    return res_list


prepod = group_letter(list_input)

print(prepod)

# Дана строка (возможно, пустая), состоящая из букв A-Z:
#
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
#
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
#
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений

print("\n\n---6---")


def RLE_1(str_):
    if str_ == "":
        return ""
    list_ = [str_[0], 1]
    n = 1
    for i in range(1, len(str_)):
        if str_[i-1] == str_[i]:
            list_[n] += 1
        else:
            if list_[n] == 1:
                list_.pop(n)
                n -= 1
            else:
                list_[n] = str(list_[n])
            list_.append(str_[i])
            list_.append(1)
            n += 2

    list_[-1] = str(list_[-1])
    if list_[-1] == "1":
        list_.pop(-1)
    list_result = "".join(list_)

    return list_result


def RLE_2(str_):
    if str_ == "":
        return ""
    list_ = [str_[0]]
    count = 1
    for i in range(1, len(str_)):
        if str_[i-1] == str_[i]:
            count += 1
            if i == len(str_)-1:
                list_.append(str(count))
        else:
            if count > 1:
                list_.append(str(count))
            list_.append(str_[i])
            count = 1

    list_result = "".join(list_)

    return list_result


letters = input("Набор букв ").upper()
rle_1 = RLE_1(letters)

rle_2 = RLE_2(letters)

print(rle_1)
print(rle_2)
