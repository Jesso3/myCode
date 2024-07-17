with open("tic input.txt","r")as f:
    data = [[int(n)for n in line.split(" ")]for line in f.read().splitlines()]\
grid = [[1,2,3],[4,5,6],[7,8,9]]