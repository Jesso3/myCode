headX = 0
headY = 0
fruits = [3, 3, 2, 5, 7, 7, 6, 0]
fruitIndex = 0
moves = "DDDRRRDDLLLDRRRRRRRDD"
grid = [['.' for x in range(8)] for y in range(8)]

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
    if headX<0 or headX > 7 or headY<0 or headY>7:
        return 0
        
for i in range(len(moves)):
    print(headX,headY)
    print(fruits[fruitIndex],fruits[fruitIndex+1])
    grid[headX][headY] = '.'
    
    if move(moves[i]) == 0:
        print("DEAD")
    grid[fruits[fruitIndex]][fruits[fruitIndex+1]] = 'F'
    grid[headX][headY] = 'S'
    

    if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
        fruitIndex += 2
