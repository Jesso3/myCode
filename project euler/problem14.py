
def collatz(n):
    num.append(int(n))
    if n == 1:
        return 
    elif n % 2 == 0:
        collatz(n/2)
    else:
        collatz(3*n+1)

num = []
longest_chain = []
biggest = 0
length = 0


for i in range(1,1000000):
    collatz(i)
    if len(num) > length:
        biggest = i
        length = len(num)
        longest_chain = num
    num = []

print(biggest, length, longest_chain)