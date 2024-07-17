import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"The Amazing Spiderman vol 1, 1962 comic book|36500223|000000508045c3d258f12d08b20b30cfda3365ee3e8096e1c88d2826e7aa851d")
print(h.hexdigest())