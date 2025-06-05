n = 4
board = [[0 for _ in range(n)] for _ in range(n)]

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def NQueens(row):
    if row == n:
        print("Solution:")
        # print("\n".join(board))
        print("\n".join(map(str, board)))
        exit()

    for col in range(n):
        if is_safe(row, col):
            board[row][col] = 1
            NQueens(row + 1)    
            board[row][col] = 0

NQueens(0)