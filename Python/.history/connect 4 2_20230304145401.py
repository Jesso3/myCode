with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')

chunks = [lines[i:i+49] for i in range(0, len(lines), 49)]
moves = [[int(digit) for digit in chunk] for chunk in chunks]
print(moves)

