import sys
import math
with open("debugging input.txt", "r") as f:
    data=f.read().splitlines()
list = [[0 for j in range(1)] for i in range(56)]

lines = [[s.split() for s in row] for row in list]
numOfIterationsToSkip = 0
print(lines)

currentBoolean = None
for row in lines:  
    if numOfIterationsToSkip > 0:
        numOfIterationsToSkip -= 1
        continue
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
        print(row[1])
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
        numOfIterationsToSkip = row[1] - 1
        continue

    if row[0] == 'JIF':
        if currentBoolean == True:
            numOfIterationsToSkip = row[1] - 1
            continue
           
       