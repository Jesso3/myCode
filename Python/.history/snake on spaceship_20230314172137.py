headX = 0
headY = 0
fruits = [5,5, 8,17, 5,2, 17,14, 2,4, 17,6, 17,17, 1,1, 2,3, 4,9, 13,2, 12,15, 18,15, 12,1, 17,5, 2,14, 7,3, 17,6, 7,13, 6,5, 5,17, 17,12, 16,7, 15,15, 14,14, 10,8, 15,5, 12,12, 9,18, 7,16, 1,3, 16,13, 12,11, 13,6, 11,1, 5,4, 15,8, 6,3, 5,14, 5,3, 5,1, 17,12, 10,14, 13,14, 18,14, 6,14, 7,1, 15,16, 13,4, 18,3, 9,1, 3,13]
fruitIndex = 0
score = 0
posX = []
posY = []
moves = "RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDD"
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
        score+=100
    score+=1
print(posX,posY)
for row in grid:
    print(row)
print(score)