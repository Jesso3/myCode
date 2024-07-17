with open('lottery ticket input.txt','r')as f:
    data=f.read().splitlines()

winningTicket = [12, 48, 30, 95, 15, 55, 97]

amount = 0
totalMoney=0
for line in data:
    part = (line.split())
    if part == winningTicket[0]:
        amount+=1
    if part == winningTicket[1]:
        amount+=1    
    if part == winningTicket[2]:
        amount+=1
    if part == winningTicket[3]:
        amount+=1
    if part == winningTicket[4]:
        amount+=1
    if part == winningTicket[5]:
        amount+=1
    totalMoney+=10**amount
print(totalMoney)