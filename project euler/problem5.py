divisibles = [i for i in range(1,20)]

def divisible(num):
    for i in divisibles:
        if num % i != 0:
            return False
    return True

i = 1
while(True):
    if divisible(i) == True:
        print(i)
        break
    i+=1