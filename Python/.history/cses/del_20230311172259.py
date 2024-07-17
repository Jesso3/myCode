def getFactorial(n):
    if n<2: return 1
    else: return n*getFactorial(n-1)
getFactorial(5)