with open("connect 4 input.txt", "r") as file:
    lines = file.read().replace('\n', '')
digits = list(str(lines))
moves = [[0 for x in range(49)] for y in range(1000)]
index=0
print(moves)
for row in range(1000):
    for col in range(49):
        moves[row][col]=digits[index]
        index+=1
num=moves[0][0]
print(num)