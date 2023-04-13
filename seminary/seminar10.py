# крестики нолики
# ввод по очереди начинают крестики
# ввод координат клетки
# рисуем текущий статус

def get_game_status(matrix):
    status_list = ["playing", "win", "draw"]
    for i in matrix:
        if len(set(i)) == 1 and set(i).pop() != "-":
            return status_list[1]

    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != "-":
            return status_list[1]

    if matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
        return status_list[1]

    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-":
        return status_list[1]

    for i in range(3):
        if "-" in matrix[i]:
            return status_list[0]
    return status_list[2]


def set_mark(matrix: list, mark: str, x: int, y: int):
    if matrix[x][y] == "-":
        matrix[x][y] = mark
        return True
    return False


field = [["-" for _ in range(3)] for _ in range(3)]

stop = False
while not stop:
    print(*field, sep="\n")
    print("ходит крестик")
    x, y = map(int, input().split())
    while not set_mark(field, "X", x, y):
        print("клетка занята")
        x, y = map(int, input().split())
    if get_game_status(field) == "win" or get_game_status(field) == "draw":
        stop = True
        print(get_game_status(field), "X")
        continue
    print(*field, sep="\n")
    print("ходит нолик")
    x, y = map(int, input().split())
    while not set_mark(field, "O", x, y):
        print("клетка занята")
        x, y = map(int, input().split())
    if get_game_status(field) == "win" or get_game_status(field) == "draw":
        stop = True
        print(get_game_status(field), "O")