li = [1,2,3,4,5,6,7,8,9,10]
def sum(n):
    if n == li[len(li)-1]:
        return li[len(li)-1]
    else:
        return n+sum(n-1)
print(sum(5))
