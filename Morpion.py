import random
import tkinter
from tkinter import messagebox


class Game:

    def __init__(self, height, width):
        self.name = "Tic tac toe"
        self.window = tkinter.Tk()
        self.window.title(self.name)  # title of the window
        self.window.geometry("600x600")  # size of the window : 450x480
        self.grid = Grid(self.window, height, width)
        self.count = 0
        self.winner = False
        self.clicked = True
        self.grid.create_cells()
        self.grid.display_grid()
        self.botidiot = BotIdiot(self.grid.cells)

    def loop(self, x, y):

        btn = self.botidiot.bot_is_playing()
        print(btn)
        print(self.grid.cells[btn[0]][btn[1]][btn["text"]] == "")

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True:  # if player has clicked 1 time
            self.button_click(x, y)

        elif self.grid.cells[btn[0]][btn[1]][btn["text"]] == "" and self.clicked is False:  # the other player play
            self.button_click_bot(btn)

        else:
            messagebox.showerror(self.name, "Already Pressed")

    def button_click(self, x, y):
        """
        method print to the screen the character
        :param x: TODO
        :param y: TODO
        :return:
        """

        self.grid.cells[x][y]["text"] = 'O'
        self.clicked = False  # Change the character for the next move
        self.count += 1
        self.check_if_win("O")  # check if the player 'O' win

    def button_click_bot(self, btn):
        """
        method print to the screen the character
        :param btn: TODO
        :return:
        """

        self.grid.cells[btn[0]][btn[1]][btn["text"]] = 'X'
        self.clicked = True  # Change the character for the next move
        self.count += 1
        self.check_if_win("X")  # check if the player 'X' win

    def check_if_win(self, player):
        """
        This method check if the player win after each stroke
        :param player: is the current character
        :return:
        """

        self.check_row(player)
        self.check_column(player)
        self.check_diagonals(player)
        self.check_draw()

    def check_row(self, player):

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[0][1]["text"] == player and \
                self.grid.cells[0][2]["text"] == player or self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[1][2]["text"] == player or \
                self.grid.cells[2][0]["text"] == player and self.grid.cells[2][1]["text"] == player and self.grid.cells[
            2][2]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + "Win !")
            self.grid.disable_all_buttons()

    def check_column(self, player):

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player or self.grid.cells[0][2]["text"] == player and self.grid.cells[
            1][1]["text"] == player and self.grid.cells[2][0]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + " Win ! ")
            self.grid.disable_all_buttons()

    def check_diagonals(self, player):

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[2][0]["text"] == player or self.grid.cells[0][1]["text"] == player and self.grid.cells[
            1][1]["text"] == player and self.grid.cells[2][1]["text"] == player or self.grid.cells[0][2]["text"] == \
                player and self.grid.cells[1][2]["text"] == player and self.grid.cells[2][2]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + " Win !")
            self.grid.disable_all_buttons()

    def check_draw(self):

        if self.count >= 9:  # if all cells are filled
            messagebox.showinfo(self.name, " Nobody Won !")  # Alert player !


class Grid:

    def __init__(self, window, height, width):
        self.window = window
        self.height = height
        self.width = width
        self.cells = []
        self.canvas = tkinter.Canvas(self.window, width=600, height=600, bg='grey', border=0)  # widget canvas

    def create_cells(self):
        """
        Method who create the grid
        :return:
        """

        for x in range(self.height):
            self.cells.append([])
            for y in range(self.width):
                btn = tkinter.Button(self.canvas, text="", width=20, height=10,
                                     command=lambda: check_clicked(x, y))
                print(x, y)
                btn.grid(row=x, column=y)
                self.cells[x].append(btn)

    def disable_all_buttons(self):
        """
        Method that disable all the buttons of the grid
        :return:
        """

        for x in range(self.height):
            for y in range(self.width):
                self.cells[x][y].config(state=tkinter.DISABLED)

    def display_grid(self):
        """
        Method who display the grid to the screen
        :return:
        """

        self.canvas.pack()


class BotIdiot:

    def __init__(self, cells):
        self.cells = cells

    def bot_is_playing(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        # print(row, column)
        # print(self.cells[row][column])
        return self.cells[row][column]


def check_clicked(x, y):
    game.loop(x, y)


game = Game(3, 3)
game.window.mainloop()
