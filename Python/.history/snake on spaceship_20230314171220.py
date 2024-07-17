headX = 0
headY = 0
fruits = [3, 3, 2, 5, 7, 7, 6, 0]
fruitIndex = 0
posX = []
posY = []
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
    if headX < 0 or headX >= 8 or headY < 0 or headY >= 8:
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
print(posX,posY)
