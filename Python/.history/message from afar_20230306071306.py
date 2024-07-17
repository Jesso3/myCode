
with open("message from afar lookup.txt","r")as f:
    lookup = [line.split(" ") for line in f.read().splitlines()]

input_data = "c6ab1f512c3fff"
binary_data = ""
for ch in input_data:
    binary_data += bin(int(ch,base=16))[2:].zfill(4)
print(lookup)
print(binary_data)