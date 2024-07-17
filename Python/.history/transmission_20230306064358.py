with open("transmission input.txt","r") as f:
    data = f.read().splitlines()
""""
grid = []
for line in data:
    row=[]
    for part in line.splits(" "):
        row.append(int(part, base=16))
    print(" end of line")
"""
grid = [[int(part,base=16)for part in line.split(" ")]for line in data]
print(grid)

for y in range(0,len(grid)-1):
    row=grid[y]
    checksum = 0
    for x in range(0, len(row)-1):
        checksum +=row[x]
    checksum = checksum % 256
    if checksum != row[-1]:
        print("Faulty row is",y,"calculated checksum to be",checksum,"but recieved",row[-1])
for x in range(0, len(grid[0])-1):
    checksum=0
    for y in range(0, len(grid)-1):
        checksum += grid[y][x]
    checksum = checksum % 256
    if checksum != grid[-1][x]:
        print("fualty column is",x,"calculated to be",checksum,"but recieved",grid[-1][x])