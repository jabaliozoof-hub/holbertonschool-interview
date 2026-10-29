#!/usr/bin/python3
import sys


def print_usage_and_exit():
    """Print usage error message and exit with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_arguments():
    """Validate command line arguments based on project requirements"""
    # Check if the number of arguments is incorrect
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is less than 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the given row and column"""
    for i in range(row):
        # Check if the queen threatens vertically or diagonally
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(n, row=0, board=[], results=[]):
    """Backtracking algorithm to find all possible solutions"""
    # Base case: If all queens are placed, save the solution
    if row == n:
        result = [[i, board[i]] for i in range(n)]
        results.append(result)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            # Recurse for the next row with the updated board state
            solve_nqueens(n, row + 1, board + [col], results)

    return results


def main():
    # Get validated N value from command line arguments
    n = validate_arguments()
    results = []
    
    # Run the N queens solver
    solve_nqueens(n, 0, [], results)

    # Print each found solution
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
