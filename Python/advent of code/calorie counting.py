f = open("Calorie counting input.txt")
data = f.readlines()
data = list(map(lambda s: s.strip(), data))
values = []
highestVal = 0
value = 0
for i in data:
    if i == '':
        if value > highestVal:
            highestVal = value
        values.append(value)
        value = 0
    else:
        i = int(i)
        value+=i
ans = sorted(values,reverse = True)
sum = 0
for i in range(3):
    sum += ans[i]
print(sum)
