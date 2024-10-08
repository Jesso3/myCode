theDictionary = {}
lines = []
intList = []
with open("debugging input.txt", "r") as f:
    for line in f:
        values = line.strip().split()
        for item in values:
            if item.isdigit():
                intList.append(int(item))
            else:
                intList.append(item)
        lines.append(intList)
        intList = []
for row in lines:
    print(row)
numOfIterationsToSkip = 0
currentBoolean = None
for row in lines:  
    if numOfIterationsToSkip > 0:
        numOfIterationsToSkip -= 1
        continue
    if row[0] == 'ADD':
       theDictionary[(row[1])] += row[2]
       continue
    if row[0] == 'MOD':
        theDictionary[(row[1])] = theDictionary[row[1]] % row[2]
        continue
    if row[0] == 'DIV':
        theDictionary[(row[1])] = theDictionary[(row[1])]//row[2]
        continue
    if row[0] == 'MOV':
        theDictionary[(row[1])] = row[2]
        continue
    if row[0] == 'OUT':
        print(theDictionary[(row[1])])
        continue
    if row[0] == 'END':
        exit()
    if row[0] == 'CEQ':
        if theDictionary[(row[1])] == row[2]:
            currentBoolean = True
            continue
        else:
            currentBoolean = False
            continue
    if row[0] == 'CGE':
        if theDictionary[(row[1])] > row[2]:
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
           
       