with open("heat input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[0] * 20000 for _ in range(1000000)]
#print(data)
# for row in data:
#     print(row)
ans = 0
ri = -1  
for i in range(len(data)):
    ri+=1
    for row in range(data[ri][0],((data[ri][0])+data[ri][2])):
        for col in range(data[ri][1],((data[ri][1])+data[ri][3])):
            grid[col][row]="x"
    
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 0:
            ans +=1
print(ans)