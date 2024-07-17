import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Light sabre|9442793|e1c7c57ed542f369951b9fa3ec81a0276b2f981e005cdc5b7fd7c99681b0acbe")
print(h.hexdigest())