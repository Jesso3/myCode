import math
with open("tour the stars input.txt", "r") as file:
    lines = file.readlines()
    # create 2D list
    lst = [list(map(int, line.strip().split())) for line in lines]
    number = 0
    answer = 0
for row in range(len(lines)):
    number = 0
    for col in range(3):
        number += ((lst[row][col] - lst[row-1][col])**2)
        if col == 2:
            answer += math.sqrt(number)
print(answer)
    