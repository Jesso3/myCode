with open("transmission input.txt","r") as f:
    data = f.read().splitlines()

grid = []
for row in data:
    print(row)