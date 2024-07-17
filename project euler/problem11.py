import math

with open("/Users/jesse/Desktop/python_code/project euler/problem11.txt", "r") as file:
    lines = file.readlines()

list = [list(map(int, line.split())) for line in lines]

biggest = 0
biggest_nums = []

for row in range(len(list)):
    for i in range(17):
        nums = [list[row][j] for j in range(i,i+4)]
        if math.prod(nums) > biggest:
            biggest = math.prod(nums)
            biggest_nums = nums

for row in range(len(list)):
    for i in range(17):
        nums = [list[j][row] for j in range(i,i+4)]
        if math.prod(nums) > biggest: 
            biggest = math.prod(nums)
            biggest_nums = nums

for row in range(len(list)-4):
    for i in range(17):
        nums = [list[j][row + (j-i)] for j in range(i,i+4)]
        if math.prod(nums) > biggest:
            biggest = math.prod(nums)
            biggest_nums = nums

for row in range(3,len(list)):
    for i in range(17):
        nums = [list[j][row - (j-i)] for j in range(i,i+4)]
        if math.prod(nums) > biggest:
            biggest = math.prod(nums)
            biggest_nums = nums

print(biggest, biggest_nums)

