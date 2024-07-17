import hashlib
with open("spot the forgery input.txt","r")as f:
    grid = [[int(n)for n in line.split("|")]for line in f.read().splitlines()] # turn data into 2d list
print(grid) 

# h = hashlib.new('sha256')
# h.update(b"Apollo 11 moon rock|0|00000078f97879b26be6baf2adb520b126f84ed10464ed4e9a77b8ed87e07468")
# print(h.hexdigest())