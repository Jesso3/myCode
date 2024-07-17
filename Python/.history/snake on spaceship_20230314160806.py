with open("snake input.txt","r")as f:
    data = f.read().splitlines()
fruits = []
moves = []
for row in data:
    if row == 2:
        for i in range(len(row)):
            fruits.append(i)
    if row == 4:
        for i in range(len(row)):
            moves.append(i)
print(fruits)
print(moves)