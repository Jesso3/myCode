import re

file = open("camp cleanup input.txt")
data = file.readlines()
data = list(map(lambda s: s.strip(), data))
total = 0
def characters(line):
    pattern = r"[-,]"
    matches1 = re.finditer(pattern, line)
    positions1 = [match.start() for match in matches1]
    return positions1

def part1():
    global total
    for line in data:
        stuff = characters(line)
        num1 = int(line[:stuff[0]])
        num2 = int(line[stuff[0]+1:stuff[1]])
        num3 = int(line[stuff[1]+1:stuff[2]])
        num4 = int(line[stuff[2]+1:])
        if num1-1<num3 and num2+1>num4:
            total+=1
            print(line,num1,num2,num3,num4)
        elif num1>num3-1 and num2<num4+1:
            total+=1
            print(line,num1,num2,num3,num4)

def part2():
    global total
    for line in data:
       stuff = characters(line)
       num1 = int(line[:stuff[0]])
       num2 = int(line[stuff[0]+1:stuff[1]])
       num3 = int(line[stuff[1]+1:stuff[2]])
       num4 = int(line[stuff[2]+1:])
       list1 = list(range(num1,num2+1)) 
       list2 = list(range(num3,num4+1))
       for i in list1:
           if i in list2:
               total+=1
               break

print(total)