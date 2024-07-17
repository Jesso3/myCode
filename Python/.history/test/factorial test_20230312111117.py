'''
def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)
print(factorial(5))
'''
fact = 1
def facto(n):
    for i in range(n):
        fact*=i+1
    return fact
print(facto(5))