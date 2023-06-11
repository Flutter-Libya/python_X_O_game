import tkinter as tk
from tkinter import messagebox

class XOGame:
    def __init__(self, master):
        self.master = master
        self.master.title("XO Game")

        self.current_player = "X"  
        self.board = [[" ", " ", " "] for _ in range(3)]

        self.create_board()

    def create_board(self):
        self.buttons = [[0, 0, 0] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, 
                                 text=" ", 
                                 font=('Arial', 60),
                                 width=4, height=2,
                                 command=lambda i=i, j=j: self.move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def move(self, row, col):
        if self.buttons[row][col]['text'] == " ":
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.master.quit()
            elif " " not in [cell for row in self.board for cell in row]:
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.master.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for row in self.board:
            if row.count(player) == 3:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

root = tk.Tk()
app = XOGame(root)
root.mainloop()
