# Input data
fruit_positions = [(3,3), (2,5), (7,7), (6,0)]
moves = "DDDRRRDDLLLDRRRRRRRDD"

# Initialize game variables
snake = [(0,0)]
score = 0
fruit_index = 0
fruit = fruit_positions[fruit_index]

# Game loop
for move in moves:
    # Determine new position of snake's head
    if move == "L":
        new_head = (snake[0][0]-1, snake[0][1])
    elif move == "R":
        new_head = (snake[0][0]+1, snake[0][1])
    elif move == "U":
        new_head = (snake[0][0], snake[0][1]-1)
    elif move == "D":
        new_head = (snake[0][0], snake[0][1]+1)

    # Check if new head is out of bounds
    if new_head[0] < 0 or new_head[0] > 19 or new_head[1] < 0 or new_head[1] > 19:
        break

    # Check if new head is on the fruit
    if new_head == fruit:
        score += 100
        snake.append(fruit)
        fruit_index += 1
        if fruit_index >= len(fruit_positions):
            break
        new_fruit = fruit_positions[fruit_index]
    else:
        snake.pop()

    # Move the snake's head to the new position
    snake.insert(0, new_head)
    score += 1
    fruit = new_fruit

print("Final Score:", score)
