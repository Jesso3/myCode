with open("heat input.txt","r")as f:
    data = f.read().splitlines()
grid = [[0 for x in range(10)] for y in range(10)]
numbers = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
for row in numbers:
    print(row)