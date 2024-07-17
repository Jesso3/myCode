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