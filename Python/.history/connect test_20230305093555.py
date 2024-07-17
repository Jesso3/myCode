def test_row(col, board):
    for i in range(7, -1, -1):
        if board[i][col] == 0:
            return i
    return -1

def check_win_conditions(board):
    for i in range(6):
        # Check horizontal win conditions
        for j in range(4):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] and board[i][j]!=0:
                return board[i][j]
        # Check vertical win conditions
        for j in range(7):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] and board[i][j]!=0:
                return board[i][j]
    # Check diagonal win conditions (top left to bottom right)
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] and board[i][j]!=0:
                return board[i][j]
    # Check diagonal win conditions (top right to bottom left)
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] and board[i][j]!=0:
                return board[i][j]
    return 0  # No win condition found

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')
moves = [[int(digit) for digit in lines[i:i+49]] for i in range(0, len(lines), 49)]

p1_wins = 0
p2_wins = 0
p3_wins = 0
for row in range(len(moves)):
    board = [[0 for x in range(8)] for y in range(8)]
    turn = 1
    for col in range(49):
        if check_win_conditions(board) == 0:
            r = test_row(moves[row][col], board)
            if r != -1:
                board[r][moves[row][col]] = turn
                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 3
                else:
                    turn = 1
        else:
            if check_win_conditions(board) == 1:
                p1_wins += 1
            elif check_win_conditions(board) == 2:
                p2_wins += 1
            elif check_win_conditions(board) == 3:
                p3_wins += 1
            break
