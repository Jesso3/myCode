import sys
import math
with open("debugging input.txt", "r") as file:
    lines = file.read().replace('\n', ' ')
lst = [list(map(str, line.strip(" ").split(" "))) for line in lines]
print(lst)   
# for row in lst:  
#     if row[0] == 'ADD':                     
#         row[1] += row[2]
#     if row[0] == 'MOD':
#         row[1] = row[1] % row[2]
#     if row[0] == 'DIV':
#         row[1] = row[1]//row[2]
#     if row[0] == 'MOV':
#         row[1] = row[2]
#     if row[0] == 'OUT':
            #print(row[2])
#   