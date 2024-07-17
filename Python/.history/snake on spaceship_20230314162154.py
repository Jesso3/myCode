with open("snake input.txt","r")as f:
    data = f.read().splitlines()
fruits = []
moves = []
for row in data:
    print(row)