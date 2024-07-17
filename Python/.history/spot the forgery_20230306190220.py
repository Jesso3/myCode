import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Samsung VR headset 2020|13896961|0000005ddad7c05066d35d3dd7cdf874a97d0ed6458bf1b8f1d294969b98fee9")
print(h.hexdigest())