headX = 0
headY = 0
fruits = [5,5, 8,17, 5,2, 17,14, 2,4, 17,6, 17,17, 1,1, 2,3, 4,9, 13,2, 12,15, 18,15, 12,1, 17,5, 2,14, 7,3, 17,6, 7,13, 6,5, 5,17, 17,12, 16,7, 15,15, 14,14, 10,8, 15,5, 12,12, 9,18, 7,16, 1,3, 16,13, 12,11, 13,6, 11,1, 5,4, 15,8, 6,3, 5,14, 5,3, 5,1, 17,12, 10,14, 13,14, 18,14, 6,14, 7,1, 15,16, 13,4, 18,3, 9,1, 3,13]
fruitIndex = 0
score = 0
posX = []
posY = []
length = 0
moves = "RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDD"
grid = [['.' for x in range(20)] for y in range(20)]

def move(direction):
    global headX, headY, length, grid
    if direction == 'U':
        headY -= 1
    elif direction == 'D':
        headY += 1
    elif direction == 'R':
        headX += 1
    elif direction == 'L':
        headX -= 1
    if length > 0:
        for i in range(1,length+1):
            grid[posY[i]][posX[i]] = 'S'
            grid[posY[length-1]][posX[length-1]] = '.'
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
