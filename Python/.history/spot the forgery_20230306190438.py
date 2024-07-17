import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"DMC Delorean hover conversion kit with Mr Fusion|4820074|d80580002aed11f85a5e0d353351ca5a5b349613b6cab37e2698d54ccfa49290")
print(h.hexdigest())