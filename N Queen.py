
def is_safe(i,j,matrix):

    for k in range(10):

        if j+k < len(matrix):
            if matrix[i][j+k] == "Q":
                return False

        if j-k >= 0:
            if matrix[i][j-k] == "Q":
                return False

        if i-k >= 0:
            if matrix[i-k][j] == "Q":
                return False

        if i-k >=0 and j-k >= 0:
            if matrix[i-k][j-k] == "Q":
                return False

        if j+k < len(matrix) and i-k >= 0:
            if matrix[i-k][j+k] == "Q":
                return False

    return True

def print_board(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j] , end="  ")
        print(" ")
    print(" ")


def get_board(n):
    b = []
    for i in range(n):
        b.append([0 for _ in range(n)])
    return b


def N_queen(board,row=0,count=0):
    global solutions
    if count == len(board):
        print_board(board)
        solutions += 1
        return

    for col in range(len(board)):
        if is_safe(row,col,board):
            board[row][col] ="Q"
            N_queen(board,row+1,count+1)
            board[row][col] = 0

solutions = 0
board = get_board(8)
N_queen(board)
print(solutions)
