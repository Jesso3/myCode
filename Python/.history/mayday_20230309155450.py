with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
index = 0
for i in data:
    
    if i[0:4]==5:
        print(i)