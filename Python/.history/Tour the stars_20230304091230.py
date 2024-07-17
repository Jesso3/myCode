import math
with open("tour the stars input.txt", "r") as file:
    lines = file.readlines()
    # create 2D list
    lst = [list(map(int, line.strip().split())) for line in lines]

print(lst)