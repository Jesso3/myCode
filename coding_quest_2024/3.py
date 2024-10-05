with open('/Users/jesse/Desktop/myCode/coding_quest_2024/3.txt','r')as f:
    lines = f.read()

image = []
symbol = ' '
index = 0

for i in lines.split():
    for j in range(int(i)):
        image.append(symbol)
    if symbol == ' ':
        symbol = '#'
    else:
        symbol = ' '

for i in range(len(image)):
    print(image[i],end='')
    if index % 100 == 0:
        print("\n")
    index+=1
