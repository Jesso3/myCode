import math
with open('lottery ticket input.txt', 'r') as file:
    f = file.readlines()
winningTicket = [12, 48, 30, 95, 15, 55, 97]

for line in f:
    for word in line:
        for num in winningTicket:
            if word == num