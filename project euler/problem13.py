with open("/Users/jesse/Desktop/python_code/project euler/problem13.txt", "r") as file:
    lines = file.readlines()

num = 0

for i in lines:
    num+=int(i)

print(str(num)[:10])



