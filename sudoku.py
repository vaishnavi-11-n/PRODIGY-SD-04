import tkinter as tk
from tkinter import messagebox

# Function to check if a number can be placed in a cell
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == num:
                return False
    return True

# Backtracking function to solve Sudoku
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

# GUI class for Sudoku Solver
class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[tk.Entry(root, width=3, font=("Arial", 16), justify="center") for _ in range(9)] for _ in range(9)]
        self.create_grid()
        
        solve_button = tk.Button(root, text="Solve", command=self.solve, font=("Arial", 14))
        solve_button.grid(row=10, column=4, pady=10)
        
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = self.entries[row][col]
                entry.grid(row=row, column=col, padx=2, pady=2)
                if (row % 3 == 2) and row != 8:
                    entry.grid(pady=(2, 5))
                if (col % 3 == 2) and col != 8:
                    entry.grid(padx=(2, 5))
    
    def get_board(self):
        board = []
        for row in self.entries:
            board.append([int(cell.get()) if cell.get().isdigit() else 0 for cell in row])
        return board
    
    def solve(self):
        board = self.get_board()
        if solve_sudoku(board):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()
