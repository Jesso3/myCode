'''
def factorial(n):
    if n == 1: return 1
    else: return n*factorial(n-1)
print(factorial(5))
'''
fact = 1
for i in range(5):
    fact*=i+1
print(fact)