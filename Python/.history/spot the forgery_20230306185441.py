import hashlib
data = []
with open('spot the forgery input.txt', 'r') as file:
    for line in file:
        data.append(line.strip().split('|'))

#print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
a= str(b+data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"Original iPhone still in box|3595421|0000000000000000000000000000000000000000000000000000000000000000")
print(a.hexdigest())