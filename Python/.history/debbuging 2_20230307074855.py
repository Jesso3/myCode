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
def variable(check):
    if check == 'a':
        return a
    if check == 'b':
        return b
    if check == 'c':
        return c
    if check == 'd':
        return d
    if check == 'e':
        return e
    if check == 'f':
        return f
    if check == 'g':
        return g
    if check == 'h':
        return h
    if check == 'i':
        return i
    if check == 'j':
        return j
    if check == 'k':
        return k
    if check == 'l':
        return l
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
        variable(lines[ip][1]) += lines[ip][2]
    if lines[ip][0]=="MOD":
        variable(lines[ip][1]) = (variable(lines[ip][1]) % lines[ip][2])
    if lines[ip][0]=="DIV":
        variable(lines[ip][1]) = (variable(lines[ip][1]) // lines[ip][2])
    if lines[ip][0]=="MOV":
        variable(lines[ip][1]) = lines[ip][2]
    if lines[ip][0]=="JMP":
        ip += (variable(lines[ip][1]))
    if lines[ip][0]=="JIF":
        if bool == True: 
            ip += (variable(lines[ip][1]))
        else:
            continue
    if lines[ip][0]=="CEQ":
        if variable(lines[ip][1]) == lines[ip][2]:
            bool = True
        else:
            bool = False
    if lines[ip][0]=="CGE":
        if variable(lines[ip][1]) >= lines[ip][2]:
            bool = True
        else:
            bool = False
    if lines[ip][0]=="OUT":
        print(variable(lines[ip][1]))
    if lines[ip][0]=="END":
        exit()

    ip +=1
