import hashlib
data = []
with open('spot the forgery input.txt', 'r') as file:
    for line in file:
        data.append(line.strip().split('|'))

#print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
a= str(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
h = hashlib.new('sha256')
#for line in range(len(data)):
h.update(b"{a}")
print(h.hexdigest())