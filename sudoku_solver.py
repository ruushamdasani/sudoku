# Sudoku Solver using Backtracking

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Function to find an empty cell in the grid (returns row, col)
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # 0 represents an empty cell
                return row, col
    return None  # No empty cell found

# Function to check if placing a number at grid[row][col] is valid
def is_valid(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# Backtracking function to solve the Sudoku puzzle
def solve_sudoku(grid):
    empty_cell = find_empty(grid)
    
    # If there's no empty cell, the puzzle is solved
    if not empty_cell:
        return True

    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            # Recursively try to solve the rest of the grid
            if solve_sudoku(grid):
                return True

            # If placing num didn't work, reset the cell (backtrack)
            grid[row][col] = 0

    return False  # If no solution was found

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the initial Sudoku grid
print("Initial Sudoku grid:")
print_grid(sudoku_grid)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku grid:")
    print_grid(sudoku_grid)
else:
    print("\nNo solution exists.")
