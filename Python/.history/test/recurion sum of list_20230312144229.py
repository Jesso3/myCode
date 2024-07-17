Li = [1,2,3,6]
def sum(list,start,n):
    if n==0:
        return list[n]
    else:
        return list[n]+sum(Li,list[n-1])
print(sum(Li,1,len(Li)-1))