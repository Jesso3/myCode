with open('lottery ticket input.txt','r')as f:
    data=f.read().splitlines()

winningTicket = [12, 48, 30, 95, 15, 55, 97]
parts = []
amount = 0
totalMoney=0
for line in data:
    amount = 0
    parts.append(line.split(" "))
print(parts)





#     if part == 12:
#         amount+=1
#     if part ==48:
#         amount+=1    
#     if part == 30:
#         amount+=1
#     if part == 95:
#         amount+=1
#     if part == 15:
#         amount+=1
#     if part == 55:
#         amount+=1
#     if part == 97:
#         amount+=1
#     totalMoney+=10**amount
    
# print(totalMoney)