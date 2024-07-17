'''
def getFactorial(n):
    if n<2: return 1
    else: return n*getFactorial(n-1)
print(getFactorial(5))
'''

def getSum(n):
    if n<2: return 1
    else: getSum(n-1)
print(getSum(5))