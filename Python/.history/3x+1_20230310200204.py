input = 5555555555587654456789876544567763265432098765432485443564356363634345365356356456437453747474747
print(input//1)
while input > 1:
    if input % 2 == 0:
        input /= 2
    else:
        input*=3
        input+=1
    print(int(input))
