with open('/Users/jesse/Desktop/python_code/coding_quest_2024/4.txt','r')as f:
    lines = f.readlines()
import math
from decimal import *

dists = []

def dist (x1,x2,y1,y2,z1,z2):
    xd = (x1-x2)**2
    yd = (y1-y2)**2
    zd = (z1-z2)**2

    return math.sqrt(xd+yd+zd)

for i in lines:
    i = i.split()
    for j in lines:
        j = j.split()
        if i != j:            
            dists.append(dist(Decimal(i[len(i)-3]),Decimal(j[len(j)-3]),Decimal(i[len(i)-2]),Decimal(j[len(j)-2]),Decimal(i[len(i)-1]),Decimal(j[len(j)-1])))

print(min(dists))
print(round(min(dists),3))




      


