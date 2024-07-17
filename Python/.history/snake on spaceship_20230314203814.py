headX = 0
headY = 0
fruits = [3,3, 2,5, 7,7 ,6,0]
fruitIndex = 0
score = 0
posX = []
posY = []
prevX = 0
prevY = 0
length = 1
moves = "DDDRRRDDLLLDRRRRRRRDD"
grid = [['.' for x in range(20)] for y in range(20)]

def move(direction):
    global headX, headY, length, posX, posY, grid, score
    
    if direction == 'U':
        headY -= 1
    elif direction == 'D':
        headY += 1
    elif direction == 'R':
        headX += 1
    elif direction == 'L':
        headX -= 1
    
    if length > 1:
        grid[posY[-1]][posX[-1]] = '.'
        posX.pop()
        posY.pop()
    if headX < 0 or headX >= 8 or headY < 0 or headY >= 8 or grid[headY][headX] == 'S':
        return False
    
    return True


for i in range(len(moves)):
    
    if move(moves[i])==False:
        print("DEAD")
        print(score)
        break
    else:
        
        posY.append(prevY)
        posX.append(prevX)
        grid[headY][headX] = 'S'
        grid[int(posY[len(posY)-length])][int(posX[len(posX)-length])] = '.'
        grid[fruits[fruitIndex+1]][fruits[fruitIndex]] = 'F'
        
        if i == 50:
            print("score at move 50:", score)
        if i == 100:
            print("score at move 100:", score)

        if headX == fruits[fruitIndex] and headY == fruits[fruitIndex+1]:
            fruitIndex += 2
            score += 100
            length += 1
            
        
        prevX = headX
        prevY = headY    
        score += 1
print(posX)
print(posY)
for row in grid:
    print(row)
    
print(score)
