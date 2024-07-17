with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

listy = [lines[i:i+49] for i in range(0, len(lines), 49)]
lst = [[int(digit) for digit in chunk] for chunk in listy]



#print(lst)
board = [[None for col in range(7)] for row in range(7)]
turn = 'player1'
player1Wins = 0
player2Wins = 0
player3Wins = 0
def checkForWin():
    for row in board:
        if row[0] == row[1] == row[2] == row[3] == row[4] == row[5] == row[6]:
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == board[5][col] == board[6][col]:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == board[5][5] == board[6][6]:
        return board[0][0]
    if board[0][6] == board[1][5] == board[2][4] == board[3][3] == board[4][2] == board[5][1] == board[6][0]:
        return board[0][0]
    
    
for row in range(1000):
    level1 = 0
    level2 = 0
    level3 = 0
    level4 = 0
    level5 = 0
    level6 = 0
    level7 = 0
    for col in range(49):
        if col % 3 == 0:
            turn = 'player1'
        if col % 3 == 1:
            turn = 'player2'
        if col % 3 == 2:
            turn = 'player3'
        if lst[row][col] == 1:
            board[level1][lst[row][col]] = turn
            level1 += 1
        if lst[row][col] == 2:
            board[level2][lst[row][col]] = turn
            level2 += 1
        if lst[row][col] == 3:
            board[level3][lst[row][col]] = turn
            level3 += 1
        if lst[row][col] == 4:
            board[level4][lst[row][col]] = turn
            level4 += 1
        if lst[row][col] == 5:
            board[level5][lst[row][col]] = turn
            level5 += 1
        if lst[row][col] == 6:
            board[level6][lst[row][col]] = turn
            level6 += 1
        if lst[row][col] == 7:
            
            level7 += 1
        if checkForWin() == 'player1':
            player1Wins += 1
        elif checkForWin() == 'player2':
            player2Wins += 1
        elif checkForWin() == 'player3':
            player3Wins += 1
    

print(player1Wins*player2Wins*player3Wins)


