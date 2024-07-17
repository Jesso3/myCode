# initialize game state
snake = [(0, 0)]
fruits = [(3, 3), (2, 5), (7, 7), (6, 0)]
score = 0

# define game board size
board_size = (20, 20)

# loop through moves
for move in moves:
    # get current head position
    head = snake[-1]

    # update head position based on move
    if move == "L":
        new_head = (head[0] - 1, head[1])
    elif move == "R":
        new_head = (head[0] + 1, head[1])
    elif move == "U":
        new_head = (head[0], head[1] - 1)
    elif move == "D":
        new_head = (head[0], head[1] + 1)

    # check if new head position is out of bounds
    if (new_head[0] < 0 or new_head[0] >= board_size[0]
        or new_head[1] < 0 or new_head[1] >= board_size[1]):
        break

    # check if new head position is on a fruit
    if new_head in fruits:
        # remove fruit from list
        fruits.remove(new_head)
        # add new fruit to list
        if fruits:
            new_fruit = fruits[0]
        else:
            new_fruit = None
        # update score
        score += 100
        # add new head to snake
        snake.append(new_head)
    else:
        # update score
        score += 1
        # add new head to snake
        snake.append(new_head)

    # remove tail of snake
    if len(snake) > 1:
        snake.pop(0)

    # check if there is a new fruit to place
    if not fruits:
        new_fruit = None
    # update fruits
    if new_fruit is not None:
        fruits.append(new_fruit)

print("Final score:", score)
