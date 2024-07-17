Li = [1,2,3,6,8,30]
'''
def sum(list,n):
    if n==0:
        return list[n]
    else:
        return list[n]+sum(list,n-1)
print(sum(Li,len(Li)-1))
'''

total = 0
print(((total+=i)for i in Li))