import re

with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
numbers = []
for i in data:
    if i[:4] == "5555":
        if i[4:12] == "00020164": # must change with different numbers
            if i[14] == 'f':
                for i in range(0, len(i[16:]), 2):
                    decimal_value = int((i[16:])[i:i+2], 16)
                    print(decimal_value)
                
print(sorted(numbers))