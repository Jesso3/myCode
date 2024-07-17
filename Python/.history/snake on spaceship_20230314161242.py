with open("snake input.txt","r")as f:
    data = f.read().splitlines()
fruits = []
moves = []
for row in range(4):
    if row == 1:
        for i in range(len(row)):
            print(i)
    #     for i in range(len(row)):
    #         fruits.append(row[i])
    # if row == 4:
    #     for i in range(len(row)):
    #         moves.append(row[i])
# print(fruits)
# print(moves)