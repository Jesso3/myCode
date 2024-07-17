with open("home input.txt",'r')as f:
    grid = f.read().splitlines()
travel_data = {}
travel_lines = []
for i in grid:
    travel_lines.append(i)

for line in travel_lines:
    # split the line into source, destinations, and times
    parts = line.split(" => ")
    source = parts[0]
    destinations = parts[1].split(" ")
    times = {}
    for dest in destinations:
        dest_parts = dest.split(":")
        times[dest_parts[0]] = int(dest_parts[1])
    # add the source, destinations, and times to the travel data dictionary
    travel_data[source] = times

# print the travel data dictionary
print(travel_data)