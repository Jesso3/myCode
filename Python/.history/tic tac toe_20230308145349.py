
with open("tic input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[1,2,3],[4,5,6],[7,8,9]]
turn = "X"
xindex = 0
yindex = 0
xWins = 0
oWins = 0
draws = 0
def check_win(board, player):
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns for a win
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    # Check for a draw
    if all(mark != ' ' for row in board for mark in row):
        return True

    # If no win or draw conditions met, return False
    return False
for row in range(len(data)):
    xindex=0
    yindex=0
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    for col in range(len(data[row])):
        while check_win(grid,"X")==False and check_win(grid,"O")==False:
            while data[row][col]!=grid[xindex][yindex]:
                if xindex<3:
                    xindex+=1
                else:
                    xindex=0
                    yindex+=1
            else:
                grid[xindex][yindex]=turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
        else:
            print(grid)
            if check_win(grid,"X")==True and check_win(grid,"O")==True:
                draws+=1
            elif check_win(grid,"X")==True:
                xWins+=1
            elif check_win(grid,"O")==True:
                oWins+=1
print(xWins,oWins,draws)

