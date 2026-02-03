import tkinter as tk
from tkinter import messagebox

GRID_SIZE = 9

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = cells[i][j].get()
            row.append(int(value) if value.isdigit() else 0)
        board.append(row)
    return board


def solve():
    board = get_board()
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showerror("Error", "No solution exists!")


def clear():
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("Sudoku Solver")

cells = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        cell = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        cell.grid(row=i, column=j, padx=2, pady=2)
        cells[i][j] = cell

tk.Button(root, text="Solve", command=solve, bg="green", fg="white", width=10).grid(row=10, column=2, columnspan=2)
tk.Button(root, text="Clear", command=clear, bg="red", fg="white", width=10).grid(row=10, column=5, columnspan=2)

root.mainloop()
