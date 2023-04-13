import tkinter
from tkinter import Canvas
from random import randrange, choice


class TicTacToe(Canvas):

    def __init__(self, window):
        self.d_p = {0: (0, 0), 1: (1, 0), 2: (2, 0),
                    3: (0, 1), 4: (1, 1), 5: (2, 1),
                    6: (0, 2), 7: (1, 2), 8: (2, 2)}
        super().__init__(window, width=300, height=300, bg='grey80')
        self.turn = 0
        self.state = [None] * 9
        self.bind('<Button-1>', self.click)

    def click(self, event):
        column = event.x // 100
        row = event.y // 100
        index = row * 3 + column

        if self.state[index] is None:
            self.add_x(column, row, index)
            self.get_winner()
            print(self.turn, self.state)
            self.bot_move()

    def bot_move(self):
        d_p = self.d_p
        self.get_winner()
        if self.turn == 1:
            self.bot_turn_1()

        if self.turn == 3:
            self.bot_turn_3()

        if self.turn == 5:
            self.bot_turn_5()

        if self.turn == 7:
            self.bot_turn_7()

    def bot_turn_1(self):
        """первый ход бота"""
        d_p = self.d_p
        if self.state[4] is None:
            self.add_o((1, 1), 4)
            print(self.turn, self.state)
            return
        else:
            i = choice([0, 2, 6, 8])
            self.add_o(d_p[i], i)
            print(self.turn, self.state)
            return

    def bot_turn_3(self):
        """Второй ход бота"""
        d_p = self.d_p
        """если центр бота"""
        if self.state[4] == 'o':
            """диагонали"""
            if self.state[0] == self.state[8] != None or self.state[2] == self.state[6] != None:
                i2 = randrange(1, 7, 2)
                self.add_o(d_p[i2], i2)
                print(self.turn, self.state)
                return

            """противоположные"""
            if self.state[1] == self.state[7] != None:
                i3 = randrange(3, 6, 2)
                self.add_o(d_p[i3], i3)
                print(self.turn, self.state)
                return

            if self.state[3] == self.state[5] != None:
                i3 = randrange(1, 8, 6)
                self.add_o(d_p[i3], i3)
                print(self.turn, self.state)
                return

            """ближние углы"""
            if self.state[0] == self.state[2] != None:
                self.add_o(d_p[1], 1)
                print(self.turn, self.state)
                return

            elif self.state[8] == self.state[6] != None:
                self.add_o(d_p[7], 7)
                print(self.turn, self.state)
                return
            elif self.state[8] == self.state[2] != None:
                self.add_o(d_p[5], 5)
                print(self.turn, self.state)
                return

            elif self.state[0] == self.state[6] != None:
                self.add_o(d_p[3], 3)
                print(self.turn, self.state)
                return

            """парные в рядах"""
            for i in range(1, 8, 6):
                if self.state[i] == self.state[i - 1] != None:
                    self.add_o(d_p[i + 1], i + 1)
                    print(self.turn, self.state)
                    return
                if self.state[i] == self.state[i + 1] != None:
                    self.add_o(d_p[i - 1], i - 1)
                    print(self.turn, self.state)
                    return

            """парные в столбцах"""
            for i in range(3, 6, 2):
                if self.state[i] == self.state[i - 3] != None:
                    self.add_o(d_p[i + 3], i + 3)
                    print(self.turn, self.state)
                    return
                if self.state[i] == self.state[i + 3] != None:
                    self.add_o(d_p[i - 3], i - 3)
                    print(self.turn, self.state)
                    return

            """перехват углов"""
            if self.state[3] == self.state[1] != None:
                self.add_o(d_p[0], 0)
                print(self.turn, self.state)
                return

            elif self.state[1] == self.state[5] != None:
                self.add_o(d_p[2], 2)
                print(self.turn, self.state)
                return
            elif self.state[7] == self.state[5] != None:
                self.add_o(d_p[8], 8)
                print(self.turn, self.state)
                return

            elif self.state[3] == self.state[7] != None:
                self.add_o(d_p[6], 6)
                print(self.turn, self.state)
                return

            """стена напротив угла"""
            if self.state[1] == self.state[6] != None:
                self.add_o(d_p[5], 5)
                print(self.turn, self.state)
                return
            elif self.state[1] == self.state[8] != None:
                self.add_o(d_p[3], 3)
                print(self.turn, self.state)
                return

            elif self.state[3] == self.state[2] != None:
                self.add_o(d_p[7], 7)
                print(self.turn, self.state)
                return
            elif self.state[3] == self.state[8] != None:
                self.add_o(d_p[1], 1)
                print(self.turn, self.state)
                return

            elif self.state[7] == self.state[0] != None:
                self.add_o(d_p[5], 5)
                print(self.turn, self.state)
                return
            elif self.state[7] == self.state[2] != None:
                self.add_o(d_p[3], 3)
                print(self.turn, self.state)
                return

            elif self.state[5] == self.state[0] != None:
                self.add_o(d_p[7], 7)
                print(self.turn, self.state)
                return
            elif self.state[5] == self.state[6] != None:
                self.add_o(d_p[1], 1)
                print(self.turn, self.state)
                return

        else:
            """если центр игрока"""
            for i in range(9):
                if i == 4:
                    continue
                if self.state[4] == self.state[i]:
                    if self.state[8 - i] != 'o':
                        self.add_o(d_p[8 - i], 8 - i)
                        print(self.turn, self.state)
                        return
                    elif self.state[0] == 'o' or self.state[8] == 'o':
                        j = choice([2, 6])
                        self.add_o(d_p[j], j)
                        print(self.turn, self.state)
                        return
                    elif self.state[2] == 'o' or self.state[6] == 'o':
                        j = choice([0, 8])
                        self.add_o(d_p[j], j)
                        print(self.turn, self.state)
                        return

    def bot_turn_5(self):
        d_p = self.d_p
        if self.bot_angles():
            return
        if self.bot_wall():
            return

        for i in range(9):
            if i == 4:
                continue
            """перекрыть центральную пару Х"""
            if self.state[4] == self.state[i] == "x" and self.state[8 - i] != 'o':
                self.add_o(d_p[8 - i], 8 - i)
                self.get_winner()
                print(self.turn, self.state)
                return
            """добавить к центральному О"""
            if self.state[4] == self.state[i] == "o" and self.state[8 - i] == None:
                self.add_o(d_p[8 - i], 8 - i)
                self.get_winner()
                print(self.turn, self.state)
                return
            """если перекрыта диагональ О"""
            if i % 2 == 0 and self.state[i] == self.state[4]:
                j = choice([0, 8]) if 0 < i < 8 else choice([2, 6])
                if self.state[j] == "x":
                    j = abs(j - 8)
                self.add_o(d_p[j], j)
                print(self.turn, self.state)
                return

        """перекрыть парые Х у стены"""
        for i in range(1, 8, 6):
            if self.state[i] == self.state[i - 1] == "x":
                self.add_o(d_p[i + 1], i + 1)
                print(self.turn, self.state)
                return
            if self.state[i] == self.state[i + 1] == "x":
                self.add_o(d_p[i - 1], i - 1)
                print(self.turn, self.state)
                return
        for i in range(3, 6, 2):
            if self.state[i] == self.state[i - 3] == "x":
                self.add_o(d_p[i + 3], i + 3)
                print(self.turn, self.state)
                return
            if self.state[i] == self.state[i + 3] == "x":
                self.add_o(d_p[i - 3], i - 3)
                print(self.turn, self.state)
                return

        """Х треугольником"""
        if self.state[1] == self.state[6] == self.state[8] == "x" or \
                self.state[0] == self.state[2] == self.state[7] == "x":
            i = choice([3, 5])
            self.add_o(d_p[i], i)
            print(self.turn, self.state)
            return
        if self.state[3] == self.state[2] == self.state[8] == "x" or self.state[0] == self.state[5] == self.state[6] == "x":
            i = choice([1, 7])
            self.add_o(d_p[i], i)
            print(self.turn, self.state)
            return

    def bot_turn_7(self):
        """Четвертый ход бота"""
        d_p = self.d_p
        if self.bot_angles():
            return
        if self.bot_wall():
            return

        for i in range(9):
            if i == 4:
                continue
            """перекрыть центральную пару Х"""
            if self.state[4] == self.state[i] == "x" and self.state[8 - i] != 'o':
                self.add_o(d_p[8 - i], 8 - i)
                self.get_winner()
                print(self.turn, self.state)
                return

    def bot_wall(self):
        """добавить О вдоль стены"""
        d_p = self.d_p
        for i in range(1, 8, 6):
            if self.state[i + 1] != "x" and self.state[i] == self.state[i - 1] == "o":
                self.add_o(d_p[i + 1], i + 1)
                self.get_winner()
                print(self.turn, self.state)
                return True
            if self.state[i - 1] != "x" and self.state[i] == self.state[i + 1] == "o":
                self.add_o(d_p[i - 1], i - 1)
                self.get_winner()
                print(self.turn, self.state)
                return True
        for i in range(3, 6, 2):
            if self.state[i + 3] != "x" and self.state[i] == self.state[i - 3] == "o":
                self.add_o(d_p[i + 3], i + 3)
                self.get_winner()
                print(self.turn, self.state)
                return True
            if self.state[i - 3] != "x" and self.state[i] == self.state[i + 3] == "o":
                self.add_o(d_p[i - 3], i - 3)
                self.get_winner()
                print(self.turn, self.state)
                return True
        return False

    def bot_angles(self):
        """близжайшие углы"""
        d_p = self.d_p
        if self.state[0] == self.state[2] == 'o' and self.state[1] == None:
            self.add_o(d_p[1], 1)
            self.get_winner()
            print(self.turn, self.state)
            return True
        if self.state[8] == self.state[2] == 'o' and self.state[5] == None:
            self.add_o(d_p[5], 5)
            self.get_winner()
            print(self.turn, self.state)
            return True
        if self.state[0] == self.state[6] == 'o' and self.state[3] == None:
            self.add_o(d_p[3], 3)
            self.get_winner()
            print(self.turn, self.state)
            return True
        if self.state[6] == self.state[8] == 'o' and self.state[7] == None:
            self.add_o(d_p[7], 7)
            self.get_winner()
            print(self.turn, self.state)
            return True
        return False

    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')

    def add_x(self, row, column, i):
        self.state[i] = "x"
        self.turn += 1
        row *= 100
        column *= 100
        self.create_line(10 + row, 10 + column, 90 + row, 90 + column, width=5, fill='blue')
        self.create_line(10 + row, 90 + column, 90 + row, 10 + column, width=5, fill='blue')

    def add_o(self, rc, i):
        self.state[i] = 'o'
        self.turn += 1
        self.create_oval(10 + rc[0] * 100, 10 + rc[1] * 100, 90 + rc[0] * 100, 90 + rc[1] * 100, width=5, outline='red')

    def finish(self, result):
        self.create_polygon(50, 120, 250, 120, 250, 180, 50, 180, fill='white', outline='grey', width=2)
        if result == "x":
            self.create_text(150, 150, text='You win', font=('Courier', 30))
            return
        elif result == "o":
            self.create_text(150, 150, text='You lose', font=('Courier', 30))
            return
        elif result == "d":
            self.create_text(150, 150, text='draw', font=('Courier', 30))
            return

    def get_winner(self):
        for i in range(0, 7, 3):
            if self.state[i] == self.state[i + 1] == self.state[i + 2] != None:
                self.finish("x") if self.state[i] == "x" else self.finish("o")
                return
        for i in range(3):
            if self.state[i] == self.state[i + 3] == self.state[i + 6] != None:
                self.finish("x") if self.state[i] == "x" else self.finish("o")
                return
        if self.state[0] == self.state[4] == self.state[8] != None or \
                self.state[2] == self.state[4] == self.state[6] != None:
            self.finish("x") if self.state[4] == "x" else self.finish("o")
            return
        if None not in self.state or (self.turn == 8 and self.state.count(None) == 1):
            self.finish("d")
            return
        if self.turn == 7 and (self.state[1] == self.state[3] == self.state[8] == "o" or
                               self.state[1] == self.state[5] == self.state[6] == "o" or
                               self.state[7] == self.state[5] == self.state[0] == "o" or
                               self.state[7] == self.state[3] == self.state[2] == "o"):
            self.finish("d")
            return
        if self.turn == 7 and self.state[4] == "o" and (self.state[0] == self.state[2] == "o" or
                                                        self.state[0] == self.state[6] == "o" or
                                                        self.state[8] == self.state[6] == "o" or
                                                        self.state[8] == self.state[2] == "o" or
                                                        self.state[1] == self.state[3] == "o" or
                                                        self.state[1] == self.state[5] == "o" or
                                                        self.state[7] == self.state[3] == "o" or
                                                        self.state[7] == self.state[5] == "o"):
            self.finish("d")
            return

        return None


window = tkinter.Tk()
game = TicTacToe(window)
game.pack()
game.draw_lines()

window.mainloop()
