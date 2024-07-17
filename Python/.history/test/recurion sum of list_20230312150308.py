Li = [1,2,3,6,8,30,66,6674473,3252,214453,6354,2,52,634576,3452,345,3574,5634,523252,246,3,525,235,3]
# recursive

def sum(list,n):
    if n==0:
        return list[n]
    else:
        return list[n]+sum(list,n-1)
print(sum(Li,len(Li)-1))

# iterative
'''
total = 0
for i in Li: total+=i
print(total)
'''