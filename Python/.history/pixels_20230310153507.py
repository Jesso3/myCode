with open("pixel inputs.txt",'r')as f:
    data = f.read().splitlines()
  
board = [[0 for x in range(8)] for y in range(8)]
print(data)
index = 0
for i in data:
    x = int(i[0])
    y = int(i[1])
    w = int(i[2])
    h = int(i[3])
    print(x,y,w,h)
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[x][y]==0:
                board[x][y]==1
            else:
                board[x][y]==0

