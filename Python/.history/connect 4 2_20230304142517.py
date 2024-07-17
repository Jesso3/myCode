with open("connect 4 input.txt", "r") as file:
    lines = file.read().split()
moves = [[0 for j in range(49)]for i in range(1000)]
print(moves)