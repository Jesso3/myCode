def climb_stairs(n):
    if n <= 2:
        return n
    
    ln = [0] * (n + 1)
    ln[0] = 1  
    
    for i in range(1, n + 1):
        ln[i] += ln[i - 1]  
        
        if i >= 2:
            ln[i] += ln[i - 2]  
        
        if i >= 12:
            ln[i] += ln[i - 12]  
        
        if i >= 40:
            ln[i] += ln[i - 40]  
    
    return ln[n]

length = 856
num = climb_stairs(length)
print(num)
