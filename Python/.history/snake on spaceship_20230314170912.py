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
    if headX < 0 or headX >= 7 or headY < 0 or headY >= 7:
        return False
    return True
        
for i in range(len(moves)):
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
        if fruitIndex >= len(fruits):
            print("GAME OVER")
            break

for row in grid:
    print(row)
