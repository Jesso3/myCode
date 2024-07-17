input = 33
print(input//1)
while input > 1 and input < 1000000:
    if input % 2 == 0:
        input /= 2
    else:
        input*=3
        input+=1
    print(str(input.replace('.0','')))
