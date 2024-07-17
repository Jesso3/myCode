with open('snake and ladder input.txt','r')as f:
    data=f.read().splitlines()

grid = [[int(n) for n in line.split(" ")] for line in data[0:20]]
#moves= []
#for line in data[6:]:
#    parts=(line.split(" "))
#    moves.append([int(parts[0]), int(parts[1])])

moves = [[int(line.split(" ")[0]), int(line.split(" ")[1])] for line in data[20:]]

for i in range(0, len(moves)):
    print("move ",i,"player 1",moves[i][0]," player 2 rolls ",moves[i][1]) 

for row in range(0, len(grid)):
    for col in range(0,len(grid[row])):
        print(grid[row][col], end=" ")
    print()

game = []
for row in range(len(grid)-1, -1, -1):
    if row % 2 ==1: #odd row - process left to right
        for col in range(0, len(grid[row])):
            game.append( grid[row][col])
    else: #even row - process right to left
        for col in range( len(grid[row])-1, -1, -1):
            game.append(grid[row][col])
print(game)

# play the game
p1_loc = 0
p2_loc = 0
for i in range(len(moves)):
    p1_move = moves[i][0]
    p2_move = moves[i][1]
    if p1_move + p1_loc >= len(game):
        print("Player 1 Wins after",i+1,"moves")
        exit()
    p1_loc += p1_move
    while game[p1_loc] != 0:
        if p1_loc + game[p1_loc] > len(game):
            print("Player 1 Wins after",i+1,"moves")
            exit()
        p1_loc +=game[p1_loc]
    if p2_move + p2_loc >= len(game):
            print("Player 2 Wins after",i+1,"moves")
            exit()
    p2_loc += p2_move
    while game[p2_loc] != 0:
        if p2_loc + game[p2_loc] > len(game):
            print("Player 2 Wins after",i+1,"moves")
            exit()
        p2_loc +=game[p2_loc]
