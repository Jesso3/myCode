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

for y in range(0,len(grid)):
    row=grid[y]
    checksum = 0
    for x in range(0, len(row)-1):
        checksum +=row[x]
    checksum = checksum % 256
    if checksum != row[-1]:
        print("Faulty row is",y,"calculated checksum to be",checksum,"but recieved",row[-1])

print(grid)