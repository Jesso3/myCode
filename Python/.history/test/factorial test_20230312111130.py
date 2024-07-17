'''
def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)
print(factorial(5))
'''

def facto(n):
    fact = 1
    for i in range(n):
        fact*=i+1
    return fact
print(facto(5))