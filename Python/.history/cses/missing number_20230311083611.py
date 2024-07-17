
input = '2 3 1 5 '

print(sorted(input))
for i in range(0,len(input)):
    if input[i] == ' ':
        continue
    elif input[i]>'1':
        print(int(input[i]-1))
        if input[i-1] != (int(input[i])-1):
            pass
