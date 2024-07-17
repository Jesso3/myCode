with open('mayday input.txt','r')as f:
    data=f.read().splitlines()
index = 0
for i in data:
    for j in i:
    # if i[index]=='5' and i[index+1]=='5' and i[index+2]=='5' and i[index+3]=='5':
    #     print(i)
        if j[:4] == '5':
            print(i)