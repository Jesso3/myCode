import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"First Mars rock brought to Earth 2048|6802092|d04cee1a2d62aa1b7d55d63551a58d6ee62bfd0b666299b2650d9a512cb2eb3c")
print(h.hexdigest())