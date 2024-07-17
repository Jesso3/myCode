with open('asteroid input.txt','r')as f:
    grid = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()] # turn data into 2d list
print(grid)

def explore(grid, y, x):
    return 0

total_sizes = 0
total_number = 0
for y in range(0, len(grid)):
    for x in range(0,len(grid[y])):
        if grid[y][x] != 0:
            size = explore(grid, y, x)
            total_sizes+=size
            total_number+=1
ave = total_sizes / total_number
print(ave)