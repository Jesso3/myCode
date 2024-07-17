with open("shopping input.txt","r")as f:
    grid = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
for row in grid:
    print(row)