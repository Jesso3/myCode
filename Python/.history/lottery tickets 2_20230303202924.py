import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.read()
winningTicket = [12, 48, 30, 95, 15, 55, 97]

numOfWinningNums = 0
totalAmountOfMoney = 0
for line in f:
    pass
# sample document containing space-separated numbers
document = "12 34 56 78 90"

# split document into a list of strings using the split method
number_strings = document.split()

# convert the list of strings to a list of integers
numbers = [int(num) for num in number_strings]

# print the list of numbers
print(numbers)