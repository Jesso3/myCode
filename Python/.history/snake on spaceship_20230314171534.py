headX = 0
headY = 0
fruits = [3, 3, 2, 5, 7, 7, 6, 0]
fruitIndex = 0
posX = []
posY = []
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
    if headX < 0 or headX >= 20 or headY < 0 or headY >= 20:
        return False
    return True
        
for i in range(len(moves)):
    posX.append(headX)
    posY.append(headY)
    print(headX,headY)
    print(fruits[fruitIndex],fruits[fruitIndex+1])
    grid[headX][headY] = '.'
    
    if not move(moves[i]):
        print("DEAD")
        break
    
    grid[fruits[fruitIndex]][fruits[fruitIndex+1]] = 'F'
    grid[headX][headY] = 'S'

    if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
        fruitIndex += 2
        grid[posX[fruitIndex//2]][posY[fruitIndex//2]] = 'S'
print(posX,posY)
for row in grid:
    print(row)