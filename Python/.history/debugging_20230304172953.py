import math
with open("debugging input.txt", "r") as f:
    line = [[int(n)for n in line.split('\n')]for line in f.read().splitlines()]
    print(line)
print(line)   
for row in lst:  
    if row[0] == 'ADD':
        row[1] += row[2]
    if row[0] == 'MOD':
        row[1] = row[1] % row[2]
    if row[0] == 'DIV':
        row[1] = row[1]//row[2]
    if row[0] == 'MOV':
        row[1] = row[2]    