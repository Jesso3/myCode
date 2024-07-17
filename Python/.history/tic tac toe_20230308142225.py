
with open("tic input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [[1,2,3],[4,5,6],[7,8,9]]
turn = "X"
for row in range(len(data)):
    for col in range(len(data[row])):
        print(data[row][col])