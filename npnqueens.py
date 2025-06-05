N = 12
board = [['.']*N for _ in range(N)]

def isSafe(col, row):
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False
    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True
        
def solve(n):
    if n == N:
        return True
    for i in range(N):
        if isSafe(i,n):
            board[n][i] = "Q"
            if solve(n+1):
                return True
            board[n][i] = "."

if solve(0):
    for row in board:
        print(" ".join(row))
else :
    print("false")