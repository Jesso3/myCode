with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

board = [[0 for x in range(7)] for y in range(7)]
chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
move = 1
#print(moves)
for row in range(1):
    for col in range(45):
        if move % 3 == 0:
            board[row][(lines[move])]=3
        elif move % 2 == 0:
            board[row][(lines[move])]=2
        else:
            board[row][(lines[move])]=1
        move+=1