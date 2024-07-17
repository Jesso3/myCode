with open("shopping input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)

def distance(p1,p2):
    return data[p1-1][p2-1]
print(len(data))
