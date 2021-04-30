import random
import tkinter
from tkinter import messagebox

"""

TODO : besoins de remettre la cellule à zero au moment du restart, il faut faire commmencer le bot en premier en hard
TODO : Et le faire jouer sans devoir avoir à appuyer.

"""


class Game:
    """
    Class used to create the game
    """

    def __init__(self, height, width):
        """
        Game initialization
        :param height: number of lines
        :param width: number of columns
        """

        self.name = "Tic tac toe"
        self.window = tkinter.Tk()
        self.window.title(self.name)  # title of the window
        self.window.geometry("600x600")  # size of the window : 600x600
        self.my_menu = tkinter.Menu(self.window)
        self.window.config(menu=self.my_menu)
        options = tkinter.Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Options", menu=options)
        options.add_command(label="Player VS Player", command=self.choice_player_vs_player)
        options.add_command(label="Player VS Bot Idiot", command=self.choice_player_vs_bot_idiot)
        options.add_command(label="Player VS Bot Hard", command=self.choice_player_vs_bot_hard)
        options.add_command(label="Restart Game", command=self.restart)
        self.height = height
        self.width = width
        self.grid = Grid(self.window, height, width)
        self.choice = ""
        self.count = 0
        self.winner = False
        self.clicked = True
        self.grid.create_cells(lambda e: self.check_button(e, self.choice))
        self.grid.display_grid()
        self.botidiot = Bot(self.grid.cells)

    def restart(self):
        """
        Method which restart the game
        :return:
        """
        self.count = 0
        self.clicked = True
        self.grid.create_cells(lambda e: self.check_button(e, self.choice))
        self.grid.display_grid()

    def choice_player_vs_player(self):
        """
        Method used to update the value of choice
        :return:
        """
        self.choice = 1

    def choice_player_vs_bot_idiot(self):
        """
        Method used to update the value of choice
        :return:
        """
        self.choice = 2

    def choice_player_vs_bot_hard(self):
        """
        Method used to update the value of choice
        :return:
        """
        self.choice = 3
        messagebox.showinfo(self.name, "Im working on this bot. They are some bugs im sorry ! "
                                       "\nIm doing my best to resolve them.")

    def player_vs_bot_idiot(self, x, y):
        """
        Method that allows a player to play against a bot
        :param x: line number
        :param y: column number
        :return:
        """

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:
            # if player has clicked 1 time
            self.menu_player_vs_bot_idiot(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

        btn_bot = self.botidiot.bot_idiot_is_playing(self.height, self.width)

        if self.grid.cells[btn_bot[0]][btn_bot[1]]["text"] == "" and self.clicked is False and self.count <= 9:
            # the other player play
            self.menu_player_vs_bot_idiot(x, y, btn_bot[0], btn_bot[1])
            self.grid.cells[btn_bot[0]][btn_bot[1]].config(state=tkinter.DISABLED)

    def player_vs_bot_hard(self, x, y):
        """
        Method that allows a player to play against a bot
        :param x: line number
        :param y: column number
        :return:
        """

        btn_bot = self.botidiot.bot_hard_is_playing(self.height, self.width)
        print(self.grid.cells)

        if self.grid.cells[btn_bot[0]][btn_bot[1]]["text"] == "" and self.clicked is False and self.count <= 9:
            # the other player play
            self.menu_player_vs_bot_hard(x, y, btn_bot[0], btn_bot[1])
            self.grid.cells[btn_bot[0]][btn_bot[1]].config(state=tkinter.DISABLED)

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:
            # if player has clicked 1 time
            self.menu_player_vs_bot_hard(x, y, btn_bot[0], btn_bot[1])
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

    def player_vs_player(self, x, y):
        """
        Method which allows a player to be played against another player
        :param x: line number
        :param y: column number
        :return:
        """

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:
            # if player has clicked 1 time
            self.menu_player_vs_player(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

        elif self.grid.cells[x][y]["text"] == "" and self.clicked is False and self.count <= 9:
            # the other player play
            self.menu_player_vs_player(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

    def check_button(self, event: tkinter.Event, choice):
        """
        Method which makes it possible to check that the pressed button is the correct one and that the button is
        well pressable
        # print(dir(event))
        :param choice: parameter that lets you know if you throw against a player or against a bot
        :param event: parameter which takes in parameter the pressed button
        :return:
        """

        # print(event.widget)
        if choice == 1:
            self.choice1(event)
        elif choice == 2:
            self.choice2(event)
        elif choice == 3:
            self.choice3(event)

    def choice1(self, event: tkinter.Event):
        for x in range(len(self.grid.cells)):
            for y in range(len(self.grid.cells[x])):
                if event.widget == self.grid.cells[x][y] and event.widget["state"] == "normal":
                    self.player_vs_player(x, y)

    def choice2(self, event: tkinter.Event):
        for x in range(len(self.grid.cells)):
            for y in range(len(self.grid.cells[x])):
                if event.widget == self.grid.cells[x][y] and event.widget["state"] == "normal":
                    self.player_vs_bot_idiot(x, y)

    def choice3(self, event: tkinter.Event):
        for x in range(len(self.grid.cells)):
            for y in range(len(self.grid.cells[x])):
                if event.widget == self.grid.cells[x][y] and event.widget["state"] == "normal":
                    self.player_vs_bot_hard(x, y)

    def menu_player_vs_player(self, x, y):
        """
        method print to the screen the character
        :param y: column number
        :param x: line number
        :return:
        """

        if self.clicked is True:
            self.grid.cells[x][y]["text"] = "O"
            self.clicked = False  # Change the character for the next move
            self.count += 1
            self.check_if_win("O")  # check if the player 'O' win

        elif self.clicked is False:
            self.grid.cells[x][y]["text"] = "X"
            self.clicked = True  # Change the character for the next move
            self.count += 1
            self.check_if_win("X")  # check if the player 'O' win

    def menu_player_vs_bot_idiot(self, x, y, btnx=None, btny=None):
        """
        method print to the screen the character
        :param x: line number
        :param y: column number
        :param btnx: line number
        :param btny: column number
        :return:
        """

        if self.clicked is True:
            self.grid.cells[x][y]["text"] = "O"
            self.clicked = False  # Change the character for the next move
            self.count += 1
            self.check_if_win("O")  # check if the player 'O' win

        elif self.clicked is False:
            self.grid.cells[btnx][btny]["text"] = 'X'
            self.clicked = True  # Change the character for the next move
            self.count += 1
            self.check_if_win("X")  # check if the player 'X' win

    def menu_player_vs_bot_hard(self, x, y, btnx, btny):
        """
        method print to the screen the character
        :param x: line number
        :param y: column number
        :param btnx: line number
        :param btny: column number
        :return:
        """

        if self.clicked is True:
            self.grid.cells[x][y]["text"] = "O"
            self.clicked = False  # Change the character for the next move
            self.count += 1
            self.check_if_win("O")  # check if the player 'O' win

        elif self.clicked is False:
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
        method which checks for each row if the player wins
        :param player: Current player's pawn
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[0][1]["text"] == player and \
                self.grid.cells[0][2]["text"] == player or self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[1][2]["text"] == player or \
                self.grid.cells[2][0]["text"] == player and self.grid.cells[2][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player:
            messagebox.showinfo(self.name, player + " Win !")
            self.winner = True
            self.grid.disable_all_buttons()

    def check_diagonals(self, player):
        """
        method which checks for each column if the player wins
        :param player: Current player's pawn
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player or self.grid.cells[0][2]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[2][0]["text"] == player:
            messagebox.showinfo(self.name, player + " Win ! ")
            self.winner = True
            self.grid.disable_all_buttons()

    def check_column(self, player):
        """
        method which checks for each diagonal if the player wins
        :param player: Current player's pawn
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][0]["text"] == player and \
                self.grid.cells[2][0]["text"] == player or self.grid.cells[0][1]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[2][1]["text"] == player or \
                self.grid.cells[0][2]["text"] == player and self.grid.cells[1][2]["text"] == player and \
                self.grid.cells[2][2]["text"] == player:
            messagebox.showinfo(self.name, player + " Win !")
            self.winner = True
            self.grid.disable_all_buttons()

    def check_draw(self):
        """
        method that checks if there is an equality
        :return:
        """

        if self.count == 9 and self.winner is False:  # if all cells are filled
            messagebox.showinfo(self.name, " Nobody Won !")  # Alert player !
            self.grid.disable_all_buttons()


class Grid:

    def __init__(self, window, height, width):
        """
        Initializes the button grid
        :param window: window parameter
        :param height: number of lines
        :param width: number of columns
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

        self.cells = []

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


class Bot:

    def __init__(self, cells):
        """
        silly bot initialization
        :param cells: list containing buttons
        """
        self.cells = cells

    @staticmethod
    def bot_idiot_is_playing(x, y):
        """
        Method that randomly chooses row is column
        :param x: number of lines
        :param y: number of columns
        :return: the coordinates of the pawn
        """
        row = random.randint(0, x - 1)
        column = random.randint(0, y - 1)
        return [row, column]

    def bot_hard_is_playing(self, x, y):
        """
        TODO
        :param x: TODO
        :param y: TODO
        :return: TODO
        """

        row = self.check_row()
        print("row : ", row)
        column = self.check_column()
        print("column : ", column)
        diagonal = self.check_diagonals()
        print("diagonal : ", diagonal, "\n")

        if row is None and column is None and diagonal is None:
            row = random.randint(0, x - 1)
            column = random.randint(0, y - 1)
            return [row, column]

        elif row is not None:
            return row

        elif column is not None:
            return column

        elif diagonal is not None:
            return diagonal

    def check_row(self):
        """
        method which checks for each row if the player wins
        :return: TODO
        """

        row0 = self.row0()
        print("row0 : ", row0)
        row1 = self.row1()
        print("row1 : ", row1)
        row2 = self.row2()
        print("row2 : ", row2)
        if row0 is True:
            return row0[1]
        elif row1 is True:
            return row1[1]
        elif row2 is True:
            return row2[1]
        else:
            return None

    def row0(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][0]["text"] == "X" and self.cells[0][1]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[0][1]["text"] == "O":
            return True, [0, 2]
        elif self.cells[0][0]["text"] == "X" and self.cells[0][2]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[0][2]["text"] == "O":
            return True, [0, 1]
        elif self.cells[0][1]["text"] == "X" and self.cells[0][2]["text"] == "X" or self.cells[0][1]["text"] == "O" and \
                self.cells[0][2]["text"] == "O":
            return True, [0, 0]

    def row1(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[1][0]["text"] == "X" and self.cells[1][1]["text"] == "X" or self.cells[1][0]["text"] == "O" and \
                self.cells[1][1]["text"] == "O":
            return True, [1, 2]
        elif self.cells[1][0]["text"] == "X" and self.cells[1][2]["text"] == "X" or self.cells[1][0]["text"] == "O" and \
                self.cells[1][2]["text"] == "O":
            return True, [1, 1]
        elif self.cells[1][1]["text"] == "X" and self.cells[1][2]["text"] == "X" or self.cells[1][1]["text"] == "O" and \
                self.cells[1][2]["text"] == "O":
            return True, [1, 0]

    def row2(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[2][0]["text"] == "X" and self.cells[2][1]["text"] == "X" or self.cells[2][0]["text"] == "O" and \
                self.cells[2][1]["text"] == "O":
            return True, [2, 2]
        elif self.cells[2][0]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[2][0]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [2, 1]
        elif self.cells[2][1]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[2][1]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [2, 0]

    def check_column(self):
        """
        method which checks for each column if the player wins
        :return: TODO
        """

        column0 = self.column0()
        print("column0 : ", column0)
        column1 = self.column1()
        print("column1 : ", column1)
        column2 = self.column2()
        print("column2 : ", column2)
        if column0 is True:
            return column0[1]
        elif column1 is True:
            return column1[1]
        elif column2 is True:
            return column2[1]
        else:
            return None

    def column0(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][0]["text"] == "X" and self.cells[1][0]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[1][0]["text"] == "O":
            return True, [2, 0]
        elif self.cells[0][0]["text"] == "X" and self.cells[2][0]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[2][0]["text"] == "O":
            return True, [1, 0]
        elif self.cells[1][0]["text"] == "X" and self.cells[2][0]["text"] == "X" or self.cells[1][0]["text"] == "O" and \
                self.cells[2][0]["text"] == "O":
            return True, [0, 0]

    def column1(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][1]["text"] == "X" and self.cells[1][1]["text"] == "X" or self.cells[0][1]["text"] == "O" and \
                self.cells[1][1]["text"] == "O":
            return True, [2, 1]
        elif self.cells[0][1]["text"] == "X" and self.cells[2][1]["text"] == "X" or self.cells[0][1]["text"] == "O" and \
                self.cells[2][1]["text"] == "O":
            return True, [1, 1]
        elif self.cells[1][1]["text"] == "X" and self.cells[2][1]["text"] == "X" or self.cells[1][1]["text"] == "O" and \
                self.cells[2][1]["text"] == "O":
            return True, [0, 1]

    def column2(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][2]["text"] == "X" and self.cells[1][2]["text"] == "X" or self.cells[0][2]["text"] == "O" and \
                self.cells[1][2]["text"] == "O":
            return True, [2, 2]
        elif self.cells[0][2]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[0][2]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [1, 2]
        elif self.cells[1][2]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[1][2]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [2, 0]

    def check_diagonals(self):
        """
        method which checks for each column if the player wins
        :return: TODO
        """

        diagonal0 = self.diagonal0()
        print("diagonal0 : ", diagonal0)
        diagonal1 = self.diagonal1()
        print("diagonal1 : ", diagonal1)
        if diagonal0 is True:
            return diagonal0[1]
        elif diagonal1 is True:
            return diagonal1[1]
        else:
            return None

    def diagonal0(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][2]["text"] == "X" and self.cells[1][1]["text"] == "X" or self.cells[0][2]["text"] == "O" and \
                self.cells[1][1]["text"] == "O":
            return True, [2, 0]
        elif self.cells[0][2]["text"] == "X" and self.cells[2][0]["text"] == "X" or self.cells[0][2]["text"] == "O" and \
                self.cells[2][0]["text"] == "O":
            return True, [1, 1]
        elif self.cells[1][1]["text"] == "X" and self.cells[2][0]["text"] == "X" or self.cells[1][1]["text"] == "O" and \
                self.cells[2][0]["text"] == "O":
            return True, [0, 2]

    def diagonal1(self):
        """
        TODO
        :return: TODO
        """

        if self.cells[0][0]["text"] == "X" and self.cells[1][1]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[1][1]["text"] == "O":
            return True, [2, 2]
        elif self.cells[0][0]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[0][0]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [1, 1]
        elif self.cells[1][1]["text"] == "X" and self.cells[2][2]["text"] == "X" or self.cells[1][1]["text"] == "O" and \
                self.cells[2][2]["text"] == "O":
            return True, [0, 0]


game = Game(3, 3)
game.window.mainloop()
