with open('lottery ticket input.txt','r')as f:
    data=f.read().splitlines()

winningTicket = [12, 48, 30, 95, 15, 55, 97]
wl = []
amount = 0
totalMoney=0
for line in data:
    parts = line.split(" ")
    wl.append([int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])])

for row in range(0,5000):
    totalMoney+=10**amount
    amount=0
    for col in range(0,6):
        if wl[row][col] == 12 or wl[row][col] == 48 or wl[row][col] == 30 or wl[row][col] == 95 or wl[row][col] == 15 or wl[row][col] == 55 or wl[row][col] == 97:
            amount+=1


#     for i in parts:
#         if int(parts[i])%5==0:

#             if parts[i] == 12 or parts[i] == 48 or parts[i] == 30 or parts[i] == 95 or parts[i] == 15 or parts[i] == 55 or parts[i] == 97:
#                 amount+=1
#             if parts[int(i-1)] == 12 or parts[int(i-1)] == 48 or parts[int(i-1)] == 30 or parts[int(i-1)] == 95 or parts[int(i-1)] == 15 or parts[int(i-1)] == 55 or parts[int(i-1)] == 97:
#                 amount+=1  
#             if parts[int(i-2)] == 12 or parts[int(i-2)] == 48 or parts[int(i-2)] == 30 or parts[int(i-2)] == 95 or parts[int(i-2)] == 15 or parts[int(i-2)] == 55 or parts[int(i-2)] == 97:
#                 amount+=1  
#             if parts[int(i-3)] == 12 or parts[int(i-3)] == 48 or parts[int(i-3)] == 30 or parts[int(i-3)] == 95 or parts[int(i-3)] == 15 or parts[int(i-3)] == 55 or parts[int(i-3)] == 97:
#                 amount+=1  
#             if parts[int(i-4)] == 12 or parts[int(i-4)] == 48 or parts[int(i-4)] == 30 or parts[int(i-4)] == 95 or parts[int(i-4)] == 15 or parts[int(i-4)] == 55 or parts[int(i-4)] == 97:
#                 amount+=1  
            
#             
print(totalMoney)            
            