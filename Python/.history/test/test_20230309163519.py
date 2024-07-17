import re

with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
for i in data:
    if i[:4] == "5555":
        if i[4:12] == "00020164": # must change with different numbers
            if i[14] == 'f':
                numbers.append(i)
print(sorted(numbers))