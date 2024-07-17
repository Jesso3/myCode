# create a dictionary to store the travel times for each beacon
travel_times = {
    "AAA": {"BBB": 38, "CCC": 45, "DDD": 98},
    "BBB": {"AAA": 38, "DDD": 60, "ZZZ": 70},
    "CCC": {"AAA": 45, "DDD": 35},
    "DDD": {"BBB": 60, "CCC": 35, "ZZZ": 15},
    "ZZZ": {"BBB": 70, "DDD": 15}
}

# set the stop time
stop_time = 10

# define a function to calculate the travel time from a source beacon to a destination beacon
def get_travel_time(source, destination):
    if destination in travel_times[source]:
        return travel_times[source][destination] + stop_time
    else:
        return float('inf')

# define a recursive function to find the shortest travel time from a source beacon to the destination beacon
def find_shortest_time(source, destination, visited):
    if source == destination:
        return 0
    visited.append(source)
    times = []
    for beacon in travel_times[source]:
        if beacon not in visited:
            time = get_travel_time(source, beacon) + find_shortest_time(beacon, destination, visited)
            times.append(time)
    if len(times) == 0:
        return float('inf')
    else:
        return min(times)

# calculate the shortest travel time from AAA to ZZZ
shortest_time = find_shortest_time("AAA", "ZZZ", [])

# output the result
print("Shortest travel time from AAA to ZZZ:", shortest_time, "seconds")
