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
prevX = 0
prevY = 0
def move(direction):
    global headX, headY, length, posX, posY
    prevX, prevY = headX, headY
    if direction == 'U':
        headY -= 1
    elif direction == 'D':
        headY += 1
    elif direction == 'R':
        headX += 1
    elif direction == 'L':
        headX -= 1
    if length > 0:
        for i in range(length-1, 0, -1):
            posX[i] = posX[i-1]
            posY[i] = posY[i-1]
        posX[0] = prevX
        posY[0] = prevY
        for i in range(length):
            grid[posY[i]][posX[i]] = 'S'
            grid[posY[length]][posX[length]] = '.'
    if headX < 0 or headX >= 20 or headY < 0 or headY >= 20 or grid[headY][headX] == 'S':
        return False
    return True


for i in range(len(moves)):
    if i == 50:
        print("score at move 50:",score)
    if i == 100:
        print("score at move 100:",score)
    grid[headY][headX] = '.'
    posX.append(headX)
    posY.append(headY)
    if len(posX) > 0:
        posX[0] = headX
    if not move(moves[i]):
        print("DEAD")
        print(score)
        break
    grid[fruits[fruitIndex+1]][fruits[fruitIndex]] = 'F'
    grid[headY][headX] = 'S'
    if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
        fruitIndex += 2
        grid[posY[fruitIndex//2]][posX[fruitIndex//2]] = 'S'
        score += 100
        length += 1
        print(length)
    score += 1

for row in grid:
    print(row)
print(score)
