import itertools
list(itertools.permutations([1, 2, 3]))
with open("shopping input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
answer = 9999999999
def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)

def distance(p1,p2):
    return data[p1-1][p2-1]
for i in range(factorial(len(data)-1)):
    pass
