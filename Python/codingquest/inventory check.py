file = open("inventory input.txt")
data = file.readlines()
file.close()
data = list(map(lambda s: s.strip(), data))
dict = {}

for line in data:
    discard, quantity, category = line.split()
    if category not in dict.keys():
        dict[category] = int(quantity)
    else:
        dict[category] = dict[category] + int(quantity)
product = 1

for key, value in dict.items():
    product = product * (value%100)

print(product)