def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, N):
    if row == N:
        print_solution(board, N)
        return True  # stop after one solution
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1, N):  # backtrack only if needed
                return True
    return False

def print_solution(board, N):
    for row in board:
        line = ['.'] * N
        line[row] = 'Q'
        print(' '.join(line))
    print()

# Take input from user
N = int(input("Enter the size of the board (e.g., 8 for 8x8): "))
board = [-1] * N
if not solve(board, 0, N):
    print("No solution exists.")
