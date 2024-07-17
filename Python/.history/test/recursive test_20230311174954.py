'''
def getFactorial(n):
    if n<2: return 1
    else: return n*getFactorial(n-1)
print(getFactorial(5))
'''

'''
def getSum(n):
    if n<2: return 1
    else: return n+getSum(n-1)
print(getSum(5))
'''

def gridPaths(m,n):
    if n< 2 or m<2: return 1
    else: return gridPaths(n,m-1)+gridPaths(n-1,m)
print(gridPaths(20,20))