
with open('asteroid input.txt','r')as f:
    grid = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()] # turn data into 2d list
print(grid)

visited = []

def explore(grid, y, x):
    size = 0
    if y>=0 and y<len(grid):
        if x>=0 and x<len(grid[y]):
            if (y,x) not in visited:
                if grid[y][x]>0:
                    visited.append((y,x))
                    size = grid[y][x] + explore(grid, y-1,x) + explore(grid,y,x+1) + explore(grid,y+1,x) + explore(grid,y,x-1)
    return size

total_sizes = 0
total_number = 0
for y in range(0, len(grid)):
    for x in range(0,len(grid[y])):
        if grid[y][x] != 0:
            if (y,x) not in visited:
                size = explore(grid, y, x)
                print("Found Asteroid of size",size)
                total_sizes+=size
                total_number+=1
ave = total_sizes / total_number
print(ave)
print(ave//1)
