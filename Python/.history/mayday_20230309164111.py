import re
with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
index = 0
order = []
numbers = []
for i in data:
  
    if i[:4] == "5555":
        if i[4:12] == "00000058": # must change with different numbers
                