import math

with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

board = [[0 for x in range(7)] for y in range(7)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]

turn = 1
p1_wins = 0
p2_wins = 0
p3_wins = 0
# for row in moves:
#     print(row)
def check_win_conditions(board):

    # Check horizontal wins
    for row in range(7):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                if board[row][col] != 0:
                    return board[row][col]

    # Check vertical wins
    for col in range(7):
        for row in range(4):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                if board[row][col] != 0:
                    return board[row][col]

    # Check diagonal wins (top-left to bottom-right)
    for row in range(4):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                if board[row][col] != 0:
                    return board[row][col]

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, 7):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                if board[row][col] != 0:
                    return board[row][col]

    # If no winner yet, return None
    return None

def testRow(col):
    for row in range(6, -1, -1):
        if board[row][col] == 0:
            return row
    return None
    
for row in range(len(moves)):
    
    for col in range(row*49,48+(row*49)):
    
        if check_win_conditions(board) == 1:
            p1_wins+=1
            board = [[0 for x in range(7)] for y in range(7)]
            break
        elif check_win_conditions(board) == 2:
            p2_wins+=1
            board = [[0 for x in range(7)] for y in range(7)]
            break
        elif check_win_conditions(board) == 3:
            p3_wins+=1
            board = [[0 for x in range(7)] for y in range(7)]
            break
        #print("player", check_win_conditions(board),"wins")
        
            
        if turn==1:
            board[testRow(int(lines[col])-1)][int(lines[col])-1]=1
        elif turn==2:
            board[testRow(int(lines[col])-1)][int(lines[col])-1]=2
        elif turn == 3:
            board[testRow(int(lines[col])-1)][int(lines[col])-1]=3
            
        if turn<3:
            turn+=1
        else:
            turn=1
        
            
            
            
    # for rows in board:
    #     print(rows)
    
    

print(p1_wins*p2_wins*p3_wins)