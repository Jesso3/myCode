board = [['.' for i in range(20)] for j in range(20)]  # initialize the game board
fruit_positions = input("Enter fruit positions (e.g. '3,3 2,5 7,7 6,0'): ").split()
for f in fruit_positions:
    x, y = map(int, f.split(','))
    board[y][x] = 'F'  # mark fruit positions on the board

moves = input("Enter snake moves (e.g. 'DDDRRRDDLLLDRRRRRRRDD'): ")
x, y = 0, 0  # initialize snake head position
snake_length = 1
score = 0

for move in moves:
    if move == 'L':
        x -= 1
    elif move == 'R':
        x += 1
    elif move == 'U':
        y -= 1
    elif move == 'D':
        y += 1

    if x < 0 or x >= 20 or y < 0 or y >= 20:  # check if snake is out of bounds
        print(f"Game over. Final score: {score}")
        break

    if board[y][x] == 'F':  # check if snake ate fruit
        score += 100
        snake_length += 1
        board[y][x] = '.'  # remove eaten fruit from the board
        fruit_positions.pop(0)  # remove eaten fruit from the list of fruit positions
        if fruit_positions:  # if there are more fruits, place the next one on the board
            fx, fy = map(int, fruit_positions[0].split(','))
            board[fy][fx] = 'F'
        else:  # if there are no more fruits, the game is over
            print(f"Game over. Final score: {score}")
            break

    else:  # if snake didn't eat fruit, just move the head
        score += 1

    if snake_length > 1:  # if the snake is longer than 1 block, move the body
        for i in range(snake_length-1, 0, -1):
            board[y][x+i] = board[y][x+i-1]
        board[y][x] = 'S'
    else:  # if the snake is only 1 block, just mark the head
        board[y][x] = 'S'

    # print the current state of the game board
    for row in board:
        print(' '.join(row))
    print(f"Score: {score}\n")
