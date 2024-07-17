with open("transmission input.txt","r") as f:
    data = f.read().splitlines()
""""
grid = []
for line in data:
    row=[]
    for part in line.splits(" "):
        row.append(int(part, base=16))
    print(" end of line")
"""
grid = [[int(part,base=16)for part in line.split(" ")]for line in data]
print(grid)

row_difference = 0
bad_row = 0
for y in range(0,len(grid)-1):
    row=grid[y]
    checksum = 0
    for x in range(0, len(row)-1):
        checksum +=row[x]
    checksum = checksum % 256
    if checksum != row[-1]:
        print("Faulty row is",y,"calculated checksum to be",checksum,"but recieved",row[-1])
        row_difference = checksum-row[-1]
        bad_row = y

column_difference=0
bad_column = 0
for x in range(0, len(grid[0])-1):
    checksum=0
    for y in range(0, len(grid)-1):
        checksum += grid[y][x]
    checksum = checksum % 256
    if checksum != grid[-1][x]:
        print("fualty column is",x,"calculated to be",checksum,"but recieved",grid[-1][x])
        column_difference = checksum-grid[-1][x]
        bad_column = x

while column_difference <0: column_difference+=256
while row_difference<0: row_difference += 256
print(column_difference)
print(row_difference)
print("the offending byte is ",grid[bad_row][bad_column],hex(grid[bad_row][bad_column]))
corrected_value = grid[bad_row][bad_column]- row_difference
while corrected_value<0: corrected_value += 256
print("the corrected value is ",corrected_value,hex(corrected_value))
answer = grid[bad_row][bad_column]*corrected_value
print("the final answer is ",answer)