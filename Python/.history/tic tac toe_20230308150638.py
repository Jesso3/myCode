
with open("tic input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[1,2,3],[4,5,6],[7,8,9]]
turn = "X"
xindex = 0
yindex = 0
xWins = 0
oWins = 0
draws = 0
def check_win(board):
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Check columns for a win
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for a draw
    if all(mark != ' ' for row in board for mark in row):
        return 'Draw'

    # If no win or draw conditions met, return None
    return None

for row in range(len(data)):
    xindex=0
    yindex=0
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    for col in range(len(data[row])):
        while check_win(grid)==None:
            for i in range(3):
                for j in range(3):
                    if grid[i][j]==data[row][col]:
                        grid[i][j]=turn
            
                
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"
        else:
            print(grid)
            if check_win(grid) == 'draw':
                draws+=1
            elif check_win(grid)=="X":
                xWins+=1
            elif check_win(grid)=="O":
                oWins+=1
print(xWins,oWins,draws)

