with open("inventory input.txt") as file:
    input = file.readlines()

categories = {}
for row in input:
  row = row.split()
  if row[2] not in categories:
    categories[f"{row[2]}"] = int(row[1])
  else:
    categories[f"{row[2]}"] += int(row[1])

product = 1
for i in categories.values():
  product *= i % 100

print(product)