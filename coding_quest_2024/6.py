
alphabet = "abcdefghiklmnopqrstuvwxyz"
key = "codingquest"
code = ""
cipher = "rm qf gs ye gv em qn pu pd ml dc at uy ol zy an pu".split()

done = []
for i in key:
    if i not in code:
        code += i
for i in alphabet:
    if i not in code:
        code += i
table = [[code[i*5+j] for j in range(5)] for i in range(5)] 

for i in table:
    print(i)

def convert(st):
    s = st[0]
    t = st[1]
    print(s,t)
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == s:
                s = (f"{i} {j}").split()
            if table[i][j] == t:
                t = (f"{i} {j}").split()
    if s[0] == t[0]:
        return(f"{table[int(s[0])][(int(s[1])+4)%5]}, {table[int(t[0])][(int(t[1])+4)%5]}")
    elif s[1] == t[1]:
        return(f"{table[(int(s[0])+4)%5][int(s[1])]}, {table[(int(t[0])+4)%5][int(t[1])]}")
    else:
        return(f"{table[int(s[0])][int(t[1])]}, {table[int(t[0])][int(s[1])]}")
for i in cipher:
    done.append(convert(i))
print(done)
#please pick up some milk on thex wayx home
#5 4 2 4 4 2 4 4 4