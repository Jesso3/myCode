with open('lottery ticket input.txt','r')as f:
    data=f.readlines()
print(data)
winningTicket = [12, 48, 30, 95, 15, 55, 97]

amount = 0
totalMoney=0
for line in data:
    amount = 0
    part = (line.split())
    if part == 12:
        amount+=1
    if part ==48:
        amount+=1    
    if part == 30:
        amount+=1
    if part == 95:
        amount+=1
    if part == 15:
        amount+=1
    if part == 55:
        amount+=1
    if part == 97:
        amount+=1
    totalMoney+=10**amount
    
print(totalMoney)