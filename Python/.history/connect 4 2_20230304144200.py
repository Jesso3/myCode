with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')
digits = list(str(lines))
moves = [[0 for x in range(49)] for y in range(1000)]
print(moves)