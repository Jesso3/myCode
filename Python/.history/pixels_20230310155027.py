with open("pixel inputs.txt",'r')as f:
    data = f.read().splitlines()
  
board = [['0' for x in range(8)] for y in range(8)]
print(board)
for i in range(len(data)):
    data[i] = data[i].replace(" ", "")

for i in data:
    if len(i) != 4:
        continue  # Skip lines that do not have exactly 4 characters
    x = str(i[0])
    y = str(i[1])
    w = str(i[2])
    h = str(i[3])
    print(x+y+w+h)
    for row in range(int(x)-1, int(x+w)-1):
        for col in range(int(y)-1, int(y+h)-1):
            print(board[row][col])
            # if board[row][col] == '0':
            #     board[row][col] = '1'
            # else:
            #     board[row][col] = '0'
