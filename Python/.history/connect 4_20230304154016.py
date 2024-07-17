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
def check_win():
    """
    Check if there is a win on the Connect 4 board.

    Parameters:
    - board: a 7x7 list representing the game board.

    Returns:
    - 'R' if red wins, 'Y' if yellow wins, or None if there is no winner.
    """
    # Check rows
    for row in range(7):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != '-':
                return board[row][col]

    # Check columns
    for col in range(7):
        for row in range(4):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != '-':
                return board[row][col]

    # Check diagonal (top-left to bottom-right)
    for row in range(4):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] != '-':
                return board[row][col]

    # Check diagonal (bottom-left to top-right)
    for row in range(3, 7):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] != '-':
                return board[row][col]

    return None
    
    
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
            board[6][lst[row][col]] = turn
            level7 += 1
    if check_win() == 'player1':
        player1Wins += 1
    elif check_win() == 'player2':
        player2Wins += 1
    elif check_win() == 'player3':
        player3Wins += 1
    

print(player1Wins*player2Wins*player3Wins)

