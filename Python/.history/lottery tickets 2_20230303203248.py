with open('lottery ticket input.txt','r')as f:
    data=f.read().splitlines()

for line in data:
    print(line.split())