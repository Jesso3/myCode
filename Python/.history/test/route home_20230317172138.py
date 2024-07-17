

with open("home input.txt",'r')as f:
    grid = f.read().splitlines()
graph = {}
travel_lines = []
for i in grid:
    travel_lines.append(i)

# turn travel lines into a dictionary
for line in travel_lines:
    parts = line.split(" => ")
    source = parts[0]
    destinations = parts[1].split(" ")
    times = {}
    for dest in destinations:
        dest_parts = dest.split(":")
        times[dest_parts[0]] = int(dest_parts[1])
    graph[source] = times


import heapq

def dijkstra(graph, start, end, stop_time):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex == end:
            return distances[end]
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if neighbor != end:
                distance += stop_time
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return float('infinity')

start = 'TYC'
end = 'EAR'
stop_time = 10

fastest_time = dijkstra(graph, start, end, stop_time)

print(f"The fastest travel time from {start} to {end} is {fastest_time} seconds.")
