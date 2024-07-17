with open("heat input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[0 for x in range(10)] for y in range(10)]
print(data)
for row in data:
    print(row)