headX = 0
headY = 0
fruits = [3, 3, 2, 5, 7, 7, 6, 0]
fruitIndex = 0
moves = "DDDRRRDDLLLDRRRRRRRDD"
grid = [['.' for x in range(20)] for y in range(20)]

def move(move):
    global headX,headY
    if move == 'U':
        headY -= 1
    elif move== 'D':
        headY +=1
    elif move == 'R':
        headX += 1
    elif move == 'L':
        headX -=1
for i in range(len(moves)):
    grid[headX][headY] = '.'
    move(moves[i])
    grid[fruits[fruitIndex+1]][fruits[fruitIndex]] = 'F'
    grid[headX][headY] = 'S'
    if headX == fruits[fruitIndex+1] and headY == fruits[fruitIndex]:
        fruitIndex += 2
for row in grid:
    print(row)
