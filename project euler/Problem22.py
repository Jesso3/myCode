with open("/Users/jesse/Desktop/python_code/project euler/problem22.txt") as file:
    line = file.read()

names = sorted(line.split(","))
values = [0]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(names)):
    for j in names[i]:
        if j.isalpha():
            values[i] += alphabet.index(j)+1
    values[i] *= (i+1)
    values.append(0)
print(values[930:950])
print(sum(values))