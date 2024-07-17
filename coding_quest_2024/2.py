with open('/Users/jesse/Desktop/python_code/coding_quest_2024/2.txt','r')as f:
    lines = f.readlines()

internal = 0
passengers = 0

for i in lines:
    bytes = []
    byteNums = []
    for j in range(0,len(i),2):

        bytes.append(i[j:j+2])

        try:
            byteNums.append(int(i[j:j+2],16))
        except:
            pass

    length = int(bytes[2]+bytes[3],16)
        
    print(length, byteNums[12:16],byteNums[16:20])
    #print(length, "Source:",(str)byteNums[12]+"."+(str)byteNums[13]+"."+(str)byteNums[14]+"."+(str)byteNums[15],"Destination:",(str)byteNums[16]+"."+(str)byteNums[17]+"."+(str)byteNums[18]+"."+(str)byteNums[19])
    if (int(bytes[12],16) == 10 and int(bytes[13],16) == 0) or (int(bytes[16],16) == 10 and int(bytes[17],16) == 0):
        passengers += length
    elif (int(bytes[12],16) == 192 and int(bytes[13],16) == 168) or (int(bytes[16],16) == 192 and int(bytes[17],16) == 168):
        internal+=length

print(internal,passengers)
        