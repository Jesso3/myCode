Li = [1,2,3]
def sum(list,n):
    if n==0:
        return list[n]
    else:
        return list[n]+list[n-1]
print(sum(Li,len(Li)-1))