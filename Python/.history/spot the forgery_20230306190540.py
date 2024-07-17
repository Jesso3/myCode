import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Fast and the furious 37 (Blueray)|17745258|50d60cdb1cbc5b034dc4c66f62ef1259bafc49992e4618a142d9d9281a5e3dc2")
print(h.hexdigest())