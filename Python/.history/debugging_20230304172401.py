with open("connect 4 input.txt", "r") as file:
    line=file.readlines()
print(line)   
for row in lst:  
    if row[0] == 'ADD':
        row[1] = row[2]
    if row[0] 