import hashlib
data = []
with open('spot the forgery input.txt', 'r') as file:
    for line in file:
        data.append(line.strip().split('|'))

#print(data[0][0]+"|"+data[0][1]+"|"+data[0][2])
#for line in range(len(data)):
h = hashlib.sha256(b"hello")
print(h.hexdigest())