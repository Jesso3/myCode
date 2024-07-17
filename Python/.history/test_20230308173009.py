with open("tic input.txt", "r") as f:
    data = [list(map(int, line.split())) for line in f]

grid = [[' '] * 3 for _ in range(3)]
xWins, oWins, draws = 0, 0, 0

def check_win(board):
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] or \
           board[0][i] == board[1][i] == board[2][i]:
            if board[i][0] != ' ':
                return board[i][0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] != ' ':
            return board[1][1]

    # Check for a draw
    if all(mark != ' ' for row in board for mark in row):
        return 'Draw'

for row in data:
    turn = "O"
    grid = [[' '] * 3 for _ in range(3)]

    for col in row:
        if check_win(grid) is None:
            i, j = (col-1) // 3, (col-1) % 3
            grid[i][j] = turn

            winner = check_win(grid)
            if winner == 'Draw':
                draws += 1
                break
            elif winner == 'X':
                xWins += 1
                break
            elif winner == 'O':
                oWins += 1
                break

        turn = 'XO'[turn == 'X']

    for x in grid:
        print(x)

print(xWins, oWins, draws)
print(xWins * oWins * draws)