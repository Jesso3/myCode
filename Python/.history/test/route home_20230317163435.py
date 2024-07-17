import heapq

def dijkstra(beacon_times, start, dest, stop_time):
    # Initialize distances to all beacons as infinity, except the starting beacon as 0
    distances = {beacon: float('inf') for beacon in beacon_times}
    distances[start] = 0

    # Initialize a priority queue to store beacons to be visited, with the starting beacon as the first item
    queue = [(0, start)]
    
    # Initialize a dictionary to keep track of the previous beacon in the shortest path
    previous = {beacon: None for beacon in beacon_times}

    # Iterate until the queue is empty or the destination beacon is reached
    while queue:
        # Get the beacon with the lowest distance from the starting beacon
        current_dist, current_beacon = heapq.heappop(queue)
        
        # Check if the current beacon is the destination beacon
        if current_beacon == dest:
            break
        
        # Check if the current distance to the current beacon is already larger than the stored distance
        if current_dist > distances[current_beacon]:
            continue
        
        # Iterate over the neighbors of the current beacon and update their distances if necessary
        for neighbor, time in beacon_times[current_beacon].items():
            # Calculate the total time to travel to the neighbor beacon, including the stop time
            total_time = current_dist + time + stop_time
            
            # Update the distance to the neighbor beacon if it is shorter than the stored distance
            if total_time < distances[neighbor]:
                distances[neighbor] = total_time
                previous[neighbor] = current_beacon
                heapq.heappush(queue, (total_time, neighbor))
    
    # If the destination beacon was reached, construct the shortest path from the previous dictionary
    if previous[dest] is not None:
        path = [dest]
        current = dest
        while current != start:
            current = previous[current]
            path.append(current)
        path.reverse()
        return path, distances[dest]
    else:
        return None, None

beacon_times = {
    'AAA': {'BBB': 38, 'CCC': 45},
    'BBB': {'AAA': 38, 'DDD': 60, 'ZZZ': 70},
    'CCC': {'AAA': 45, 'DDD': 35},
    'DDD': {'BBB': 60, 'CCC': 35, 'ZZZ': 15},
    'ZZZ': {'BBB': 70, 'DDD': 15},
}

start = 'AAA'
dest = 'ZZZ'
stop_time = 10

path, shortest_time = dijkstra(beacon_times, start, dest, stop_time)

if path is not None:
    print('The shortest path from', start, 'to', dest, 'is', '->'.join(path), 'with a travel time of', shortest_time, 'seconds')
else:
    print('There is no path from', start, 'to', dest)
