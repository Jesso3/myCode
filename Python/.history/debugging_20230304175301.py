import sys
import math
with open("debugging input.txt", "r") as f:
    data=f.read().splitlines()
list = [[0 for j in range(1)] for i in range(56)]
for i in range(len(data)):
    row = i // 1  
    col = i % 1
    list[row][col] = data[i]
lines = [[s.split() for s in row] for row in list]
for row in lines:
     print(row)

currentBoolean = None
for row in lines:  
    if row[0] == 'ADD':                     
        row[1] += row[2]
        continue
    if row[0] == 'MOD':
        row[1] = row[1] % row[2]
        continue
    if row[0] == 'DIV':
        row[1] = row[1]//row[2]
        continue
    if row[0] == 'MOV':
        row[1] = row[2]
        continue
    if row[0] == 'OUT':
        print(row[2])
        continue
    if row[0] == 'END':
        sys.exit
    if row[0] == 'CEQ':
        if row[1] == row[2]:
            currentBoolean = True
            continue
        else:
            currentBoolean = False
            continue
    if row[0] == 'CGE':
        if row[1] > row[2]:
            currentBoolean = True
            continue
        else:
            currentBoolean = False
            continue
    if row[0] == 'JMP':
        for i in range(1, row[1]):
            continue
    if row[0] == 'JIF':
        if currentBoolean == True:
           for i in range(1, row[1]):
                continue
           
       