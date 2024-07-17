
inp = '2 3 1 5 4 7 8 6 10'

input  = sorted(inp)
print(input)
for i in range(0,len(input)):
    if input[i] == ' ':
        continue
    elif input[i]>'1':
        if int(input[i-1]) != int(input[i])-1:
            print(int(input[i])-1)
