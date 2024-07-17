with open("pixel inputs.txt",'r')as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()] 
board = [[' ' for x in range(50)] for y in range(10)]
for rectangle in data:
    x, y, w, h = rectangle
    for row in range(y - 1, y + h - 1):
        for col in range(x - 1, x + w - 1):
            if board[row][col] == ' ':
                board[row][col] = 'o'
            else:
                board[row][col] = ' '
           
for row in board:
    print(''.join(row))