import re

with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
for i in data:
    if i[:4] == "5555":
        if i[4:12] == "00020164": # must change with different numbers
            if i[14] == 'f':
                num = i[16:]
                for i in range(0, len(num), 2):
                    decimal_value = int(num[i:i+2], 16)
                    print(decimal_value)
                
print(sorted(numbers))