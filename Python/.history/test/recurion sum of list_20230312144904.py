Li = [1,2,3,6,8]
def sum(list,start,n):
    if n==0:
        return list[n]
    else:
        return list[n]+sum(list,list[n-1],n-1)

print(sum(Li,5,len(Li)-1))