headX = 0
headY = 0
fruits = [3,3, 2,5, 7,7 ,6,0]
fruitIndex = 0
score = 0
posX = []
posY = []
prevX = 0
prevY = 0
length = 0
moves = "DDDRRRDDLLLDRRRRRRRDD"
grid = [['.' for x in range(20)] for y in range(20)]

def move(direction):
    global headX, headY, length, posX, posY
    
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
    if i == 50:
        print("score at move 50:",score)
    if i == 100:
        print("score at move 100:",score)
    grid[headY][headX] = 'S'
    posX.append(headX)
    posY.append(headY)
    
    if not move(moves[i]):
        print("DEAD")
        print(score)
        break
    grid[fruits[fruitIndex+1]][fruits[fruitIndex]] = 'F'
    
    if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
        fruitIndex += 2
        grid[posY[fruitIndex//2]][posX[fruitIndex//2]] = 'S'
        score += 100
        length += 1
    prevX = headX
    prevY = headY    
    score += 1

for row in grid:
    print(row)
print(score)
