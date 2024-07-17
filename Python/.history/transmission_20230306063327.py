with open("transmission input.txt","r") as f:
    data = f.read().splitlines()
""""
grid = []
for line in data:
    parts = line.split(" ")
    row=[]
    for part in parts:
        row.append(int(part, base=16))
        print(part, end=" ... ")
    print(" end of line")
    grid.append(row)
"""
grid = [[int(part,base=16)for part in line.split(" ")]for line in data]

print(grid)