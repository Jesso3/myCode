with open("heat input.txt","r")as f:
    data = f.read().splitlines()
grid = [[0 for x in range(10)] for y in range(10)]
index = 0
for i in data:
    grid[i[0]:i[2]][i[1]:i[3]]="x"
print(grid)