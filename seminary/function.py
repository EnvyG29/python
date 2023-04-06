def find_data():
    """поиск информации в справочнике"""
    data_to_see = input("введите данные для поиска ")
    with open('book.txt', 'r', encoding='utf-8') as q:
        tel_book = q.read()
    print(search(tel_book, data_to_see))


def search(book: str, info: str) -> str:
    """находит в строке записи по определенному кретерию поиска"""
    book = book.split("\n")
    return "\n".join([post for post in book if info in post])


def add_data():
    """добавляет информацию в справочник"""
    fio = input("введите ФИО ")
    number = input("введите номер телефоне ")
    with open("book.txt", "a", encoding='utf=8') as q:
        q.write(f'\n{fio} | {number}')


def show_data():
    """выводит информацию из справочника"""
    with open("book.txt", "r", encoding='utf=8') as q:
        print(q.read())
