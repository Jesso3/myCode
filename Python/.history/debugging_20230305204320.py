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
currentRow = -1
shouldBreak = False
rowNumberToJumpTo = 0
currentBoolean = None

    
while 2 > 1:
    for row in lines: 
        currentRow += 1
        if shouldBreak == True:
            shouldBreak = False
            currentRow = 0
            break
        if rowNumberToJumpTo > 0:
            rowNumberToJumpTo -= 1
            continue 
        
        
        
        
        print(currentRow)
        if row[0] == 'ADD':
            if row[1] in theDictionary:

                try:
                    theDictionary[row[1]] += theDictionary[row[2]]
                    continue
                except:
                
                    theDictionary[row[1]] += int(row[2])
                    continue
            else:
                theDictionary[row[1]] = int(row[2])
                continue
        if row[0] == 'MOD':
            
            if theDictionary[row[1]] >= int(row[2]):
                theDictionary[row[1]] = theDictionary[row[1]] % int(row[2])
                continue
           
                    
            
        if row[0] == 'DIV':
            try:

                theDictionary[(row[1])] = theDictionary[(row[1])]//theDictionary[row[2]]
                continue
            except:
                theDictionary[(row[1])] = theDictionary[(row[1])]//row[2]
                continue
        if row[0] == 'MOV':
            try:
                theDictionary[row[1]] = theDictionary[row[2]]
                continue
            except:
                theDictionary[row[1]] = int(row[2])
                continue
        if row[0] == 'OUT':
            try:
                print('           ', theDictionary[row[1]], 'Look Here!')
                continue
            except:
                print('           ', int(row[1]), 'Look Here!')
                continue
        if row[0] == 'END':
            exit()
        if row[0] == 'CEQ':
            try:
                if theDictionary[(row[1])] == theDictionary[row[2]]:
                    currentBoolean = True
                    continue
                else:
                    currentBoolean = False
                    continue
            except:
                if theDictionary[(row[1])] == row[2]:
                    currentBoolean = True
                    continue
                else:
                    currentBoolean = False
                    continue
        if row[0] == 'CGE':
            try:
                if theDictionary[(row[1])] > theDictionary[(row[2])]:
                    currentBoolean = True
                    continue
                else:
                    currentBoolean = False
                    continue
            except:
                if theDictionary[(row[1])] > int(row[2]):
                    currentBoolean = True
                    continue
                else:
                    currentBoolean = False
                    continue
        if row[0] == 'JMP':
            print('yes')
            rowNumberToJumpTo = currentRow + int(row[1])
            shouldBreak = True
            continue

        if row[0] == 'JIF':
            if currentBoolean == True:
                rowNumberToJumpTo = currentRow + int(row[1]) 
                shouldBreak = True
                continue
            
        