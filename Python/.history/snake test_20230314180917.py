# Define the game board size
BOARD_SIZE = 20

# Define the input data
FRUIT_COORDINATES = [(3,3), (2,5), (7,7), (6,0)]
MOVES = "DDDRRRDDLLLDRRRRRRRDD"

# Initialize the game variables
snake = [(0, 0)]  # Start with a snake of length 1 at position (0, 0)
score = 0
fruit_index = 0
fruit_position = FRUIT_COORDINATES[fruit_index]

# Define a function to move the snake
def move_snake(move):
    global snake, score, fruit_index, fruit_position
    
    # Determine the new position of the snake's head
    head = snake[-1]
    if move == "L":
        new_head = (head[0] - 1, head[1])
    elif move == "R":
        new_head = (head[0] + 1, head[1])
    elif move == "U":
        new_head = (head[0], head[1] - 1)
    elif move == "D":
        new_head = (head[0], head[1] + 1)
    
    # Check if the new head position is out of bounds
    if new_head[0] < 0 or new_head[0] >= BOARD_SIZE or new_head[1] < 0 or new_head[1] >= BOARD_SIZE:
        print(f"Game over! Final score: {score}")
        return
    
    # Check if the new head position is on the fruit
    if new_head == fruit_position:
        score += 100
        snake.append(new_head)
        fruit_index += 1
        if fruit_index >= len(FRUIT_COORDINATES):
            print(f"Congratulations! You won! Final score: {score}")
            return
        fruit_position = FRUIT_COORDINATES[fruit_index]
    else:
        snake.pop(0)
        snake.append(new_head)
        score += 1
    
    # Print the current state of the game board
    board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for segment in snake:
        board[segment[1]][segment[0]] = "S"
    board[fruit_position[1]][fruit_position[0]] = "F"
    for row in board:
        print("".join(row))
    print(f"Score: {score}")
    print()
    
# Move the snake according to the input data
for move in MOVES:
    move_snake(move)
