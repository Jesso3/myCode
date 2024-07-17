with open('lottery inputdata test.txt','r')as f:
    data=f.read().splitlines()

winningTicket = [12, 48, 30, 95, 15, 55, 97]
wl = []
amount = 0
totalMoney=0
for line in data:
    parts = line.split(" ")
    wl.append([int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])])

for row in range(int(len(data))):
    
    if amount == 3:
        totalMoney+=1
        amount=0
    if amount == 4:
        totalMoney+=10
        amount=0
    if amount == 5:
        totalMoney+=100
        amount=0
    if amount == 6:
        totalMoney+=1000
        amount=0
    for col in range(6):
        if wl[row][col] == 12 or wl[row][col] == 48 or wl[row][col] == 30 or wl[row][col] == 95 or wl[row][col] == 15 or wl[row][col] == 55 or wl[row][col] == 97:
            amount+=1
print(wl[0][0])

           
            