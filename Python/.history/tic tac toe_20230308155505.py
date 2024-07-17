
with open("tic input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[' ' for i in range(3)] for j in range(3)]
turn = "O"
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
    turn = "O"
    
    grid = [[' ' for i in range(3)] for j in range(3)]
    for col in range(len(data[row])):
        if check_win(grid) == 'Draw':
            draws+=1
            break
        if check_win(grid)=="X":
            xWins+=1
            break
        if check_win(grid)=="O":
            oWins+=1 
            break
        if turn == "X":
            
            turn = "O"
        else:
            
            turn = "X"    
        if check_win(grid)==None:
            
            if data[row][col]==int('1'):
                grid[0][0]= turn
            elif data[row][col]==int('2'):
                grid[0][1]= turn
            elif data[row][col]==int('3'):
                grid[0][2]= turn
            elif data[row][col]==int('4'):
                grid[1][0]= turn
            elif data[row][col]==int('5'):
                grid[1][1]= turn
            elif data[row][col]==int('6'):
                grid[1][2]= turn
            elif data[row][col]==int('7'):
                grid[2][0]= turn
            elif data[row][col]==int('8'):
                grid[2][1]= turn
            elif data[row][col]==int('9'):
                grid[2][2]= turn
                
        
    
    for x in grid:
        print(x)  
draws = 100-(xWins+oWins)        
print(xWins,oWins,draws)
print(xWins*oWins*draws)

