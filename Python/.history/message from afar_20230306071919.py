
with open("message from afar lookup.txt","r")as f:
    lookup = [line.split(" ") for line in f.read().splitlines()]

input_data = "c6ab1f512c3fff"
binary_data = ""
answer = ""
for ch in input_data:
    binary_data += bin(int(ch,base=16))[2:].zfill(4)
print(lookup)
print(binary_data)
i=0
while i < len(binary_data):
    first = binary_data[i]
    if first =="o":
        #read 4 characters
        code = binary_data[i:i+4]
        i+=4
    else:
        second = binary_data[i+1]
        if second == "0":
            #read 5 characters
            code = binary_data[i:i+5]
            i+=5
        else:
            #read 7 characters
            code = binary_data[i:i+7]
            i+=7
    print(code)
    #cinvert the code to it's letter value
    for item in lookup:
        if item[1] == code:
            answer += item[0]
print(answer)