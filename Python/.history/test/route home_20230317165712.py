with open("home input.txt","r")as f:
    grid = f.read().splitlines()
travel_data = {}
travel_lines = []
for i in grid:
    travel_lines.append(i)
print(travel_lines)