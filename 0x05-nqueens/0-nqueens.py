#!/usr/bin/python3
import sys

# Function to check if a position is safe for the queen
def is_safe(board, row, col, N):
    # Check this column on the previous rows
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Function to solve the N-Queens problem using backtracking
def solve_nqueens(N, row, board, solutions):
    if row == N:
        # Found a valid solution, add it to the solutions list
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

# Main function to handle input and validate the command line arguments
def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board and solutions list
    board = [-1] * N
    solutions = []
    
    # Solve the N-Queens problem
    solve_nqueens(N, 0, board, solutions)
    
    # Print each solution
    for solution in solutions:
        print(solution)

# Entry point of the script
if __name__ == "__main__":
    main()
