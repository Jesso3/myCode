headX = 0
headY = 0
fruits = [3,3, 2,5, 7,7 ,6,0]
fruitIndex = 0
score = 0
posX = []
posY = []
length = 0
moves = "DDDRRRDDLLLDRRRRRRRDD"
grid = [['.' for x in range(20)] for y in range(20)]

def move(direction):
    global headX, headY
    if direction == 'U':
        headY -= 1
    elif direction == 'D':
        headY += 1
    elif direction == 'R':
        headX += 1
    elif direction == 'L':
        headX -= 1

    if headX < 0 or headX >= 8 or headY < 0 or headY >= 8 or grid[headY][headX] == 'S':
        return False

    return True

for i in range(len(moves)):
   
    posX.append(headX)
    posY.append(headY)
    print(headX, headY)
    print(fruits[fruitIndex], fruits[fruitIndex+1])
    grid[headY][headX] = '.'

    if not move(moves[i]):
        print("DEAD")
        print(score)
        break

    # update snake body positions
    for j in range(length-1, 0, -1):
        posX[j] = posX[j-1]
        posY[j] = posY[j-1]
    posX[0] = headX
    posY[0] = headY

    grid[fruits[fruitIndex+1]][fruits[fruitIndex]] = 'F'
    grid[headY][headX] = 'S'
   

    if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
        fruitIndex += 2
        grid[posY[fruitIndex//2]][posX[fruitIndex//2]] = 'S'
        score += 100
        length += 1

    score += 1

print(posX, posY)
for row in grid:
    print(row)
print(score)
