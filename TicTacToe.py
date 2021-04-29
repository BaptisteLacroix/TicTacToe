import random
import tkinter
from tkinter import messagebox


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
        self.window.geometry("600x600")  # size of the window : 450x480
        self.my_menu = tkinter.Menu(self.window)
        self.window.config(menu=self.my_menu)
        options = tkinter.Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Options", menu=options)
        options.add_command(label="Player VS Player", command=self.choice_player_vs_player)
        options.add_command(label="Player VS Bot", command=self.choice_player_vs_bot)
        options.add_command(label="Restart Game", command=self.restart)
        self.height = height
        self.width = width
        self.grid = Grid(self.window, height, width)
        self.choice = ""
        self.count = 0
        self.clicked = True
        self.grid.create_cells(lambda e: self.check_button(e, self.choice))
        self.grid.display_grid()
        self.botidiot = BotIdiot(self.grid.cells)

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

    def choice_player_vs_bot(self):
        """
        Method used to update the value of choice
        :return:
        """
        self.choice = 2

    def player_vs_bot(self, x, y):
        """
        Method that allows a player to play against a bot
        :param x: line number
        :param y: column number
        :return:
        """

        btn_bot = self.botidiot.bot_is_playing(self.height, self.width)

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:  # if player has clicked 1 time
            self.button_click_player1(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

        elif self.grid.cells[btn_bot[0]][btn_bot[1]]["text"] == "" and self.clicked is False and self.count <= 9:  # the other player play
            self.button_click_bot(btn_bot[0], btn_bot[1])
            self.grid.cells[btn_bot[0]][btn_bot[1]].config(state=tkinter.DISABLED)

    def player_vs_player(self, x, y):
        """
        Method which allows a player to be played against another player
        :param x: line number
        :param y: column number
        :return:
        """

        if self.grid.cells[x][y]["text"] == "" and self.clicked is True and self.count <= 9:  # if player has clicked 1 time
            self.button_click_player1(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

        elif self.grid.cells[x][y]["text"] == "" and self.clicked is False and self.count <= 9:  # the other player play
            self.button_click_player2(x, y)
            self.grid.cells[x][y].config(state=tkinter.DISABLED)

    def check_button(self, event: tkinter.Event, choice):
        """
        Method which makes it possible to check that the pressed button is the correct one and that the button is
        well pressable
        :param choice: parameter that lets you know if you throw against a player or against a bot
        :param event: parameter which takes in parameter the pressed button
        :return:
        """
        # print(dir(event))
        # print(event.widget)
        if choice == 1:
            for x in range(len(self.grid.cells)):
                for y in range(len(self.grid.cells[x])):
                    if event.widget == self.grid.cells[x][y] and event.widget["state"] == "normal":
                        self.player_vs_player(x, y)

        elif choice == 2:
            for x in range(len(self.grid.cells)):
                for y in range(len(self.grid.cells[x])):
                    if event.widget == self.grid.cells[x][y] and event.widget["state"] == "normal":
                        self.player_vs_bot(x, y)

    def button_click_player1(self, x, y):
        """
        method print to the screen the character
        :param y: column number
        :param x: line number
        :return:
        """

        self.grid.cells[x][y]["text"] = "O"
        self.clicked = False  # Change the character for the next move
        self.count += 1
        self.check_if_win("O")  # check if the player 'O' win

    def button_click_player2(self, x, y):
        """
        method print to the screen the character
        :param y: column number
        :param x: line number
        :return:
        """

        self.grid.cells[x][y]["text"] = "X"
        self.clicked = True  # Change the character for the next move
        self.count += 1
        self.check_if_win("X")  # check if the player 'O' win

    def button_click_bot(self, btnx, btny):
        """
        method print to the screen the character
        :param btny: line number
        :param btnx: column number
        :return:
        """

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
            self.grid.disable_all_buttons()

    def check_column(self, player):
        """
        method which checks for each column if the player wins
        :param player: Current player's pawn
        :return:
        """

        if self.grid.cells[0][0]["text"] == player and self.grid.cells[1][1]["text"] == player and \
                self.grid.cells[2][2]["text"] == player or self.grid.cells[0][2]["text"] == player and \
                self.grid.cells[1][1]["text"] == player and self.grid.cells[2][0]["text"] == player:
            messagebox.showinfo(self.name, player + " Win ! ")
            self.grid.disable_all_buttons()

    def check_diagonals(self, player):
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
            self.grid.disable_all_buttons()

    def check_draw(self):
        """
        method that checks if there is an equality
        :return:
        """

        if self.count >= 9:  # if all cells are filled
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


class BotIdiot:

    def __init__(self, cells):
        """
        silly bot initialization
        :param cells: list containing buttons
        """
        self.cells = cells

    @staticmethod
    def bot_is_playing(x, y):
        """
        Method that randomly chooses row is column
        :param x: number of lines
        :param y: number of columns
        :return: the coordinates of the pawn
        """
        row = random.randint(0, x - 1)
        column = random.randint(0, y - 1)
        return [row, column]


game = Game(3, 3)
game.window.mainloop()
