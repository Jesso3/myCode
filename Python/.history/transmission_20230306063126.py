with open("transmission input.txt","r") as f:
    data = f.read().splitlines()

grid = []
for line in data:
    parts = line.split(" ")
    row=[]
    for part in parts:
        row.append(part)
        print(part, end=" ... ")
    print(" end of line")
    grid.append(row)

print(grid)