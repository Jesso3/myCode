with open("avoid asteroid input.txt","r")as f:
    data = [[float(n)for n in line.split(" ")]for line in f.read().splitlines()]
grid = [['.' for i in range(8)] for j in range(8)]
coords = []
for row in data:
    x,y,dx,dy = row
    if dx != 0:
        for i in range(3660):
            x += dx
            y+=dy
            coords.append(x//1)
            coords.append(y//1)
print(coords)





'''    
    if dx>0:
        for i in range(3600):
            if int(x)<8 and int(y)<8:
                if int(x//1)>=0 and int(y//1)>=0:
                    grid[int(x//1)][int(y//1)] = '#'
            x+=dx
    if dx>0:
        for i in range(3600):
            if int(x)<8 and int(y)<8:
                if int(x//1)>=0 and int(y//1)>=0:
                    grid[int(x//1)][int(y//1)] = '#'
            y+=dy
    
    if int(x)<8 and int(y)<8:
        if int(x//1)>=0 and int(y//1)>=0:
            grid[int(x//1)][int(y//1)] = '#'
        print(x,y)
    for i in range(60):
        x+=dx
        y+=dy
        
        if int(x)<8 and int(y)<8:
            if int(x//1)>=0 and int(y//1)>=0:
                grid[int(x//1)][int(y//1)] = '#'
        
for row in grid:
    print(row)
'''