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

'''
def gridPaths(m,n):
    if n< 2 or m<2: return 1
    else: return gridPaths(n,m-1)+gridPaths(n-1,m)
print(gridPaths(10,10))
'''

def countPartitions(n,m):
    if n == 0: return 1
    if m == 0: return 0
    else: return countPartitions(n-m,m)+countPartitions(n,m-1)
print(countPartitions(5,1))