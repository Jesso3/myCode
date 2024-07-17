import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.readlines()
winningTicket = [12, 48, 30, 95, 15, 55, 97]
numOfWinningNums = 0
totalAmountOfMoney = 0
for line in f:
    words = (line.splits(" "))
    print(words)

if numOfWinningNums == 3:
    totalAmountOfMoney += 1
elif numOfWinningNums == 4:
    totalAmountOfMoney += 10
elif numOfWinningNums == 5:
    totalAmountOfMoney += 100
elif numOfWinningNums == 6:
totalAmountOfMoney += 1000
print(totalAmountOfMoney)