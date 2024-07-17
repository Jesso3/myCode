
with open("message from afar lookup.txt","r")as f:
    data = [line.split(" ") for line in f.read().splitlines()]

input_data = "c6ab1f512c3fff"
binary_data = ""
for ch in input_data:
    print(bin(int(ch,base=16)))