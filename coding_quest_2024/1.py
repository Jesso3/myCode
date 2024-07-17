with open('/Users/jesse/Desktop/python_code/coding_quest_2024/1.txt','r')as f:
    lines = f.readlines()

airlines = {}

addition = ["Seat","Meals","Luggage","Tax","Fee"]
    
for i in lines:
    i = i.split()
    if i[0] in airlines:
        if i[1] in addition:
            airlines[i[0]] += int(i[2])
        else:
            airlines[i[0]] -= int(i[2])
    else:
        if i[1]in addition:
            airlines[i[0]] = int(i[2])
        else:
            airlines[i[0]] = -int(i[2])

for i,j in airlines.items():
    print(i,j)

print(min(airlines.values()))


