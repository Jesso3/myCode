Li = [1]
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