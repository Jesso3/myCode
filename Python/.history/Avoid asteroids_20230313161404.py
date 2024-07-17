with open("avoid asteroid input.txt","r")as f:
    data = [[float(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [['.' for i in range(100)] for j in range(100)]
coords = []

for row in data:
    x,y,dx,dy = row
    
    for i in range(3610):
        x += dx
        y+=dy
        coords.append(x//1)
        coords.append(y//1)
    
for i in range(0,len(coords),2):
    if coords[i]>=0 and coords[i]<100 and coords[i+1]>=0 and coords[i+1]<100:
        grid[int(coords[i])][int(coords[i+1])] = '#'
print(grid)
# for row in range(len(grid)):
#     for col in range(len(grid[row])):
        
#         if grid[row][col] != '#':
#             print("hello")
#             print(row,col)
# print('done')



