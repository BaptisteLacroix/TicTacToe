import random
import tkinter
from tkinter import messagebox


class Game:
    """
    TODO
    """

    def __init__(self, height, width):
        """
        TODO
        :param height: TODO
        :param width: TODO
        """

        self.name = "Tic tac toe"
        self.window = tkinter.Tk()
        self.window.title(self.name)  # title of the window
        self.window.geometry("600x600")  # size of the window : 450x480
        self.height = height
        self.width = width
        self.grid = Grid(self.window, height, width)
        self.count = 0
        self.winner = False  # variable that may not be used
        self.clicked = True
        self.grid.create_cells(lambda e: self.check_button(e))
        self.grid.display_grid()
        self.botidiot = BotIdiot(self.grid.cells)

    def loop(self, x, y):
        """
        TODO
        :param x: TODO
        :param y: TODO
        :return:
        """

        btn_bot = self.botidiot.bot_is_playing(self.height, self.width)

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:  # if player has clicked 1 time
            self.button_click(x, y)

        elif self.grid.cells[btn_bot[0]][btn_bot[1]]["text"] == "" and self.clicked is False and self.count <= 9:  # the other player play
            self.button_click_bot(btn_bot[0], btn_bot[1])

        else:
            messagebox.showerror(self.name, "Already Pressed")

    def check_button(self, event: tkinter.Event):
        """
        TODO
        :param event: TODO
        :return:
        """
        # print(dir(event))
        for x in range(len(self.grid.cells)):
            for y in range(len(self.grid.cells[x])):
                if event.widget == self.grid.cells[x][y]:
                    self.loop(x, y)

    def button_click(self, x, y):
        """
        method print to the screen the character
        :param y: TODO
        :param x: TODO
        :return:
        """

        self.grid.cells[x][y]["text"] = 'O'
        self.clicked = False  # Change the character for the next move
        self.count += 1
        self.check_if_win("O")  # check if the player 'O' win

    def button_click_bot(self, btnx, btny):
        """
        method print to the screen the character
        :param btny: TODO
        :param btnx: TODO
        :return:
        """

        # TODO : TypeError: can only concatenate str (not "int") to str

        self.grid.cells[btnx][btny]["text"] = 'X'
        self.clicked = True  # Change the character for the next move
        self.count += 1
        self.check_if_win("X")  # check if the player 'X' win

    def check_if_win(self, player):
        """
        This method check if the player win after each stroke
        :param player: is the current character 'X' or 'O'
        :return:
        """

        self.check_row(player)
        self.check_column(player)
        self.check_diagonals(player)
        self.check_draw()

    def check_row(self, player):
        """
        TODO
        :param player: TODO
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[0][1]["text"] == player and \
                self.grid.cells[0][2]["text"] == player or self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[1][2]["text"] == player or \
                self.grid.cells[2][0]["text"] == player and self.grid.cells[2][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + "Win !")
            self.grid.disable_all_buttons()

    def check_column(self, player):
        """
        TODO
        :param player: TODO
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player or self.grid.cells[0][2]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[2][0]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + " Win ! ")
            self.grid.disable_all_buttons()

    def check_diagonals(self, player):
        """
        TODO
        :param player: TODO
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[2][0]["text"] == player or self.grid.cells[0][1]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[2][1]["text"] == player or \
                self.grid.cells[0][2]["text"] == player and self.grid.cells[1][2]["text"] == player and \
                self.grid.cells[2][2]["text"] == player:
            self.winner = True
            messagebox.showinfo(self.name, player + " Win !")
            self.grid.disable_all_buttons()

    def check_draw(self):
        """
        TODO
        :return:
        """

        if self.count >= 9:  # if all cells are filled
            messagebox.showinfo(self.name, " Nobody Won !")  # Alert player !


class Grid:
    """
    TODO
    """

    def __init__(self, window, height, width):
        """
        TODO
        :param window: TODO
        :param height: TODO
        :param width: TODO
        """
        self.window = window
        self.height = height
        self.width = width
        self.cells = []
        self.canvas = tkinter.Canvas(self.window, width=600, height=600, bg='grey', border=0)  # widget canvas

    def create_cells(self, action):
        """
        Method who create the grid
        :return:
        """

        for x in range(self.height):
            self.cells.append([])
            for y in range(self.width):
                btn = tkinter.Button(self.canvas, text="", width=20, height=10)
                btn.bind("<Button-1>", action)
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
        """
        TODO
        :param cells: TODO
        """
        self.cells = cells

    @staticmethod
    def bot_is_playing(x, y):
        """
        TODO
        :param x: TODO
        :param y: TODO
        :return: TODO
        """
        row = random.randint(0, x - 1)
        column = random.randint(0, y - 1)
        return [row, column]


game = Game(3, 3)
game.window.mainloop()
