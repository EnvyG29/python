"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных"""

import function as fu

while True:
    print('\n1:вывод\n2:ввод\n3:поиск\n4:удалить\n5:изменить строку\nномер команды', end=" ")
    mode = input()
    print()
    if mode == "1":
        fu.show_data()
    elif mode == "2":
        fu.add_data()
    elif mode == "3":
        fu.find_data()
    elif mode == "4":
        fu.del_data()
    elif mode == "5":
        fu.change()
    else:
        print("\nневерная команда\n")
