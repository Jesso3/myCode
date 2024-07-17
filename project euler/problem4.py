def palindrome(p):  
    if len(p) % 2 == 0:
        first = [p[i] for i in range(0,int(len(p)/2))]
        second = [p[i] for i in range (int(len(p)/2),int(len(p)))]
        if first == second[::-1]:
            return True
        return False
    else:
        first = [p[i] for i in range(0,int(len(p)/2))]
        second = [p[i] for i in range (int(len(p)/2)+1,int(len(p)))]
        if first == second[::-1]:
            return True
        return False

palins = []
for i in range(1000,0,-1):
    for j in range(1000,0,-1):
        s = str(i*j)
        if palindrome(s) == True:
            palins.append(int(s))
print(max(palins))