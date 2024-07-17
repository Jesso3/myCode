with open('/Users/jesse/Desktop/python_code/coding_quest_2024/5(1).txt','r')as f:
    lines = f.readlines()

table = [[0 for x in range(len(lines))] for y in range(len(lines))] 

row = 0

for i in lines:
    i = i.split()
    for j in range(len(i)):
        table[row][j] = i[j]
    row+=1
    
with open('/Users/jesse/Desktop/python_code/coding_quest_2024/5(2).txt','r')as f:
    lines = f.readlines()

distance = 0

for i in lines:
    path = i.split()
    for j in range(len(path)):
        if path[j] == "->":
            pos1 = path[j-1]
            pos2 = path[j+1]
            index1 = 0
            index2 = 0
            for k in range(len(table)):
                if table[k][0] == pos1:
                    index1 = k
            for k in range(len(table)):
                if table[k][0] == pos2:
                    index2 = k
            distance += (int(table[index1][index2]))
print(distance)
                    

