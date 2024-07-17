import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Queen Charlotte coronation photo 2062 NFT|12039128|b5aa84176e33b9b8debeaa1cc13b8550c4e5ae442a559a7421463fc4a807259a")
print(h.hexdigest())