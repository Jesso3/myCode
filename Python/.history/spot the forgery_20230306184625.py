import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))
# for row in data:
#     print(row)

h = hashlib.new('sha256')
# for line in range(len(data)):
h.update(b"Original iPhone still in box35954210000000000000000000000000000000000000000000000000000000000000000")
print(h.hexdigest())