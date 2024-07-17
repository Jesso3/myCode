import decimal

def reciprocal(n):
    num =  (repr(1/n))[2:]
    print(n,num)
    for i in range(1,len(str(num))):
        if num[1:i] == num[i:i*2]:
            print(i)
            return i

        
biggest = 0
biggest_cycle = 0
for i in range(1,1000):
    if reciprocal(i) != None and reciprocal(i) > biggest_cycle:
        biggest_cycle = reciprocal(i)
        biggest = i
print(biggest,biggest_cycle)