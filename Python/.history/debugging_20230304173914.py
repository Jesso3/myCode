import sys
import math
with open("debugging input.txt", "r") as f:
    data=f.read().splitlines()
new_list = [[0 for j in range(1)] for i in range(56)]

# Iterate over the original list and add elements to sub-lists
for i in range(len(data)):
    row = i // 5  # Determine row index
    col = i % 5   # Determine column index
    new_list[row][col] = data[i]

# Output the new 2D list
print(new_list)
   
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
#      if row[0] == 'END':
#            sys.exit
#       if row[0] == 'CEQ':
#           if row[1] == row[2]:
#               r