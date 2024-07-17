import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Sonic vs Mario: Clash of the titans 2030|2530976|8d69efdf26bd84af641f31382be801f7962db73234b90dbfd0b1bed3545729a7")
print(h.hexdigest())