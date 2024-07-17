# initialize game state
board = [['.' for j in range(20)] for i in range(20)]
snake = [(0, 0)]
fruit = [(5, 5), (8, 17), (5, 2), (17, 14), (2, 4), (17, 6), (17, 17), (1, 1), (2, 3), (4, 9), (13, 2), (12, 15), (18, 15), (12, 1), (17, 5), (2, 14), (7, 3), (17, 6), (7, 13), (6, 5), (5, 17), (17, 12), (16, 7), (15, 15), (14, 14), (10, 8), (15, 5), (12, 12), (9, 18), (7, 16), (1, 3), (16, 13), (12, 11), (13, 6), (11, 1), (5, 4), (15, 8), (6, 3), (5, 14), (5, 3), (5, 1), (17, 12), (10, 14), (13, 14), (18, 14), (6, 14), (7, 1), (15, 16), (13, 4), (18, 3), (9, 1), (3, 13)]

# initialize game variables
score = 0
fruit_idx = 0
moves = 'RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDD'
new_fruit = None

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
