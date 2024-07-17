import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Oxford Urban dictionary 2050 edition|18550296|0e7d7d4397d42f857e0623433d88a5d7e5c74fb7d617073109f723c12d0d5248")
print(h.hexdigest())