with open("avoid asteroid input.txt","r")as f:
    data = [[float(n)for n in line.split(" ")]for line in f.read().splitlines()]

GRID_SIZE = 100
GRID = [[True for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Parse asteroid data
asteroids = []
for row in data:
    asteroids.append(row)
while True:
    try:
        x, y, dx, dy = map(int, input().split())
        asteroids.append((x, y, dx, dy))
    except:
        break

# Mark unsafe grid cells for each asteroid at each second
for asteroid in asteroids:
    x, y, dx, dy = asteroid
    for t in range(3600):
        tx = x + dx * t
        ty = y + dy * t
        if 0 <= tx < GRID_SIZE and 0 <= ty < GRID_SIZE:
            GRID[tx][ty] = False

# Find safe region for 60 seconds after asteroid field is reached
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        if GRID[x][y]:
            is_safe = True
            for t in range(60):
                if not GRID[x][y+t]:
                    is_safe = False
                    break
            if is_safe:
                print(f"{x}:{y}")
                exit()
