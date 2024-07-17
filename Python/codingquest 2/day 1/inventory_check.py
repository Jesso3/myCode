with open("inventory_input.txt", "r") as file:
    input = file.readlines()

count = {}
for row in input:
    row = row.split()
    if row[2] not in count.keys():
        count[row[2]] = int(row[1])
    else:
        count[row[2]] += int(row[1])

sum = 1
for i in count.values():
    sum *= i % 100
  
print(sum)