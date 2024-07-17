# initialize game state
board = [['.' for j in range(20)] for i in range(20)]
snake = [(0, 0)]
fruit = [(3, 3), (2, 5), (7, 7), (6, 0)]
moves = "DDDRRRDDLLLDRRRRRRRDD"
# initialize game variables
score = 0
fruit_idx = 0

# helper function to print board state
def print_board(board, snake, fruit):
    for i in range(len(board)):
        row = ''
        for j in range(len(board[i])):
            if (i, j) in snake:
                row += 'S'
            elif (i, j) in fruit:
                row += 'F'
            else:
                row += board[i][j]
        print(row)

# play game
for move in moves:
    # update snake position
    head = snake[-1]
    if move == 'L':
        new_head = (head[0], head[1]-1)
    elif move == 'R':
        new_head = (head[0], head[1]+1)
    elif move == 'U':
        new_head = (head[0]-1, head[1])
    elif move == 'D':
        new_head = (head[0]+1, head[1])
    
    # check if new head is out of bounds
    if new_head[0] < 0 or new_head[0] > 19 or new_head[1] < 0 or new_head[1] > 19:
        print('OUT OF BOUNDS.')
        break
    
    # check if new head hits snake body
    if new_head in snake:
        print('SNAKE HIT ITSELF.')
        break
    
    # update snake and score
    snake.append(new_head)
    if new_head in fruit:
        score += 100
        fruit.remove(new_head)
        if fruit_idx < len(fruit):
            new_fruit = fruit[fruit_idx]
            fruit_idx += 1
        else:
            new_fruit = None
    else:
        score += 1
        snake.pop(0)
    
    # update board state
    board = [['.' for j in range(20)] for i in range(20)]
    for pos in snake:
        board[pos[0]][pos[1]] = 'S'
    if new_fruit is not None:
        board[new_fruit[0]][new_fruit[1]] = 'F'
    
    # print current board state and score
    print_board(board, snake, fruit)
    print('Score:', score)
