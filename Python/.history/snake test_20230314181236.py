# game board dimensions
BOARD_WIDTH = 20
BOARD_HEIGHT = 20

# initialize game state variables
score = 0
snake_pos = [(0, 0)]
fruit_pos = (3, 3)
moves = "DDDRRRDDLLLDRRRRRRRDD"

# iterate through each move in the game
for move in moves:
    # update the position of the head of the snake based on the move
    x, y = snake_pos[-1]
    if move == "L":
        x -= 1
    elif move == "R":
        x += 1
    elif move == "U":
        y -= 1
    elif move == "D":
        y += 1
    
    # check if the new head of the snake is out of bounds
    if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
        print("Out of bounds")
        break
    
    # check if the new head of the snake is on a piece of fruit
    if (x, y) == fruit_pos:
        score += 100
        snake_pos.append((x, y))
        # generate new position for fruit
        fruit_pos = (randint(0, BOARD_WIDTH-1), randint(0, BOARD_HEIGHT-1))
    else:
        # remove the tail of the snake and update the head position
        snake_pos.pop(0)
        snake_pos.append((x, y))
        score += 1
    
    # print the current state of the game board
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if (col, row) == fruit_pos:
                print("F", end="")
            elif (col, row) in snake_pos:
                print("S", end="")
            else:
                print(".", end="")
        print()
    print(f"Score: {score}\n")
