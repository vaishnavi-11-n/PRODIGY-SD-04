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
        self.entries = []
        self.create_grid()
        
        solve_button = tk.Button(root, text="Solve", command=self.solve, font=("Arial", 14), bg="#4CAF50", fg="white")
        solve_button.grid(row=10, column=3, columnspan=3, pady=10)
        
        clear_button = tk.Button(root, text="Clear", command=self.clear_board, font=("Arial", 14), bg="#f44336", fg="white")
        clear_button.grid(row=11, column=3, columnspan=3, pady=5)
        
    def create_grid(self):
        for row in range(9):
            entry_row = []
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=("Arial", 16), justify="center", bg="white", relief="solid", bd=2)
                entry.grid(row=row, column=col, padx=2, pady=2)
                
                # Set thicker borders for 3x3 sections
                if row % 3 == 2 and row != 8:
                    entry.grid(pady=(2, 5))
                if col % 3 == 2 and col != 8:
                    entry.grid(padx=(2, 5))
                
                entry_row.append(entry)
            self.entries.append(entry_row)
    
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
                    if not self.entries[i][j].get():
                        self.entries[i][j].config(fg="black")  # Solved numbers in black
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku!")
    
    def clear_board(self):
        for row in self.entries:
            for cell in row:
                cell.delete(0, tk.END)
                cell.config(fg="blue")  # Reset user-inputted cells to blue

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverApp(root)
    root.mainloop()

