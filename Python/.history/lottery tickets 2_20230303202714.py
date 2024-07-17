import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.read()
winningTicket = [12, 48, 30, 95, 15, 55, 97]

numOfWinningNums = 0
totalAmountOfMoney = 0
for line in f:
    number_strings = line.split()
    numbers = [int(num) for num in number_strings]
print(numbers)    
   
    
    
            