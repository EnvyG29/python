import csv


def find_data():
    """поиск информации в справочнике"""
    data_to_see = input("введите данные для поиска ")
    with open('book.csv', 'r', encoding='utf-8') as q:
        tel_book = q.read()
    print(search(tel_book, data_to_see).replace(",", " "))


def search(book: str, info: str) -> str:
    """находит в строке записи по определенному кретерию поиска"""
    book = book.split("\n")
    return "\n".join([post for post in book if info in post])


def add_data():
    """добавляет информацию в справочник"""
    fio = input("введите ФИО ")
    number = input("введите номер телефона ")
    with open("book.csv", "a", encoding='utf=8', newline="") as q:
        wr = csv.writer(q)
        wr.writerow([fio, "|", number])


def show_data():
    """выводит информацию из справочника"""
    with open("book.csv", "r", encoding='utf=8') as q:
        for i in csv.reader(q):
            print(*i)


def del_data():
    """удаление информации из справочника"""
    list_ = []
    with open('book.csv', 'r', encoding='utf-8') as q:
        for i, k in enumerate(csv.reader(q), start=1):
            print(i, *k)
            list_.append(k)
        row_del = int(input("Номер строки "))
        if row_del < 1 or row_del > len(list_):
            print("нет такой строки")
            return
        list_.pop(row_del-1)
    with open('book.csv', 'w', encoding='utf-8', newline='') as q:
        writer = csv.writer(q)
        writer.writerows(list_)


def change():
    """изменение информации из справочника"""
    list_ = []
    with open('book.csv', 'r', encoding='utf-8') as q:
        for i, k in enumerate(csv.reader(q), start=1):
            list_.append(k)
        row_del = int(input("Номер строки "))
        if row_del < 1 or row_del > len(list_):
            print("нет такой строки")
            return
        list_[row_del-1] = [input("ФИО "), "|", input("Номер ")]
    with open('book.csv', 'w', encoding='utf-8', newline='') as q:
        writer = csv.writer(q)
        writer.writerows(list_)
