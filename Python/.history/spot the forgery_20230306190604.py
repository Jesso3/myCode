import hashlib
# data = []
# with open('spot the forgery input.txt', 'r') as file:
#     for line in file:
#         data.append(line.strip().split('|'))

# #print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
# a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Starwars LVIII: The Force that never quits (Blueray)|3932573|065b0949bede57fc0ab07f80a4369f7a3414ad3c77de84ecceb2dc907d2323ba")
print(h.hexdigest())