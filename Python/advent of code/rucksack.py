file = open("rucksack input.txt")
data = file.readlines()
data = list(map(lambda s: s.strip(), data))
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
letters = []
#part 1
'''
for line in data:
    str1 = line[:len(line)//2]
    str2 = line[len(line)//2:]
    for i in str1:
        if i in str2:
            letters.append(i)
            break          
'''
#part 2
'''
for line in range(0,len(data),3):
    for i in data[line]:
        if i in data[line+1] and i in data[line+2]:
            letters.append(i)
            break
'''
for i in letters:
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            total+=j+1
            
print(total)