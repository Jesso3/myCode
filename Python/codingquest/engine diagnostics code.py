import math
file= open('engine diagnostics data.txt','r')
f=file.readlines()
data=[]
numberOfAnomolies=0
avg=0
num=0
#ln = line number
ln=0
for line in f:
    data.append(line)
    num +=int(line)
    ln+=1
    if ln>=60:
        avg=num/60
        num-=int(data[int(ln-60)])
        if avg < 1500 or avg > 1600:
           numberOfAnomolies+=1
           avg=0
        else:
            avg=0
print(numberOfAnomolies)
        
