import hashlib
data = []
with open('spot the forgery input.txt', 'r') as file:
    for line in file:
        data.append(line.strip().split('|'))
print(data)

# h = hashlib.new('sha256')
# h.update(b"Apollo 11 moon rock|0|00000078f97879b26be6baf2adb520b126f84ed10464ed4e9a77b8ed87e07468")
# print(h.hexdigest())