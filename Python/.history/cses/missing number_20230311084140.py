inp = '3 1 5 4 7 8'
input  = sorted(inp)
for i in range(0,len(input)):
    if input[i] == ' ':
        continue
    elif input[i]>= '2':
        if int(input[i-1]) != int(input[i])-1:
            print(int(input[i])-1)
            