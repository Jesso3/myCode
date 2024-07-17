
with open("message from afar lookup.txt","r")as f:
    lookup = [line.split(" ") for line in f.read().splitlines()]

input_data = "1724cf8567eb02c3d384b21a63f588c5fd0b87a65c03ea4534a3fbf47e9d7207ac2b3f409a570847d18fbf585670f58002394a99fd0afa3ae482e60f42e1eb24172c82ade8923eb2488702c2beb11ca5eb287aace8fe8b2648050c8423efd6236734c7eb0acfd0660861f4d3a5019bd1a7ac2b387aa2d724c421e9a860940f582633807bf4afe8923e85c3d12362087a36f5d397aace427924611f5970fae9cbdfa80632845bd6429cbd6529d71940413dfff"
binary_data = ""
answer = ""
for ch in input_data:
    binary_data += bin(int(ch,base=16))[2:].zfill(4)
print(lookup)
print(binary_data)
i=0
while i < len(binary_data):
    first = binary_data[i]
    if first =="0":
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
            if item[0] == "*":
                i= len(binary_data)
                break
print(answer)