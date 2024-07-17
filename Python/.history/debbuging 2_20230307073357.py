lines = []
intList = []
with open("debugging input.txt", "r") as f:
    for line in f:
        values = line.strip().split()
        for item in values:
            if item.isdigit():
                intList.append(int(item))
            else:
                intList.append(item)
        lines.append(intList)
        intList = []

ip = 0
bool = False
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
while ip < len(lines):
    if lines[ip][0]=="ADD":
        lines[ip][1] += lines[ip][2]
    if lines[ip][0]=="MOD":
        lines[ip][1] = (lines[ip][1] % lines[ip][2])
    if lines[ip][0]=="DIV":
        lines[ip][1] = (lines[ip][1] // lines[ip][2])
    if lines[ip][0]=="MOV":
        lines[ip][1] = lines[ip][2]
    if lines[ip][0]=="JMP":
        ip += (lines[ip][1])
    if lines[ip][0]=="JIF":
        if bool == True: 
            ip += (lines[ip][1])
        else:
            continue
    if lines[ip][0]=="CEQ":
        if lines[ip][1] == lines[ip][2]:
            bool = True
        else:
            bool = False
    if lines[ip][0]=="CGE":
        if lines[ip][1] >= lines[ip][2]:
            bool = True
        else:
            bool = False
    if lines[ip][0]=="OUT":
        print(lines[ip][1])
    if lines[ip][0]=="END":
        exit()

    ip +=1