with open('asteroidinput.txt','r')as f:
    grid = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]
    print(grid)