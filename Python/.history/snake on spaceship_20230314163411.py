headX = 0
headY = 0
fruits = [3, 3, 2, 5, 7, 7, 6, 0]
moves = ["DDDRRRDDLLLDRRRRRRRDD"]
grid = [['.' for x in range(20)] for y in range(20)]
def move(move):
    if move == 'U':
        headY -= 1
    elif move== 'D':
        headY +=1
    elif move == 'R':
        headX += 1
    elif move == 'L':
        headX -=1

    grid[headX][headY] = 'S'
print(grid)