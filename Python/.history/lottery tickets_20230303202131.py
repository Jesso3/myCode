import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.read())
winningTicket = [12, 48, 30, 95, 15, 55, 97]
wl = []
numOfWinningNums = 0
totalAmountOfMoney = 0
for num in f.split():
    wl.append(int(num))
    
print(wl)    
    
if numOfWinningNums == 3:
    totalAmountOfMoney += 1
elif numOfWinningNums == 4:
    totalAmountOfMoney += 10
elif numOfWinningNums == 5:
    totalAmountOfMoney += 100
elif numOfWinningNums == 6:
    totalAmountOfMoney += 1000
