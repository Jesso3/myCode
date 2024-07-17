import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.read()
winningTicket = [12, 48, 30, 95, 15, 55, 97]
wl = []
numOfWinningNums = 0
totalAmountOfMoney = 0
for word in f.split():
    
    wl.append(int(word))
    for win in winningTicket:
        if word == win:
            numOfWinningNums +=1
   
    
    if numOfWinningNums == 3:
        totalAmountOfMoney += 1
    elif numOfWinningNums == 4:
        totalAmountOfMoney += 10
    elif numOfWinningNums == 5:
        totalAmountOfMoney += 100
    elif numOfWinningNums == 6:
        totalAmountOfMoney += 1000
    numOfWinningNums = 0
print(totalAmountOfMoney)