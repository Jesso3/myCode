import heapq

def dijkstra(graph, start, end):
    # initialize distances and visited nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    # use a heap to track nodes with smallest tentative distance
    heap = [(0, start, [])]

    while heap:
        # get the node with smallest tentative distance
        (current_distance, current_node, current_path) = heapq.heappop(heap)

        # if the current node is the end node, return the distance and path
        if current_node == end:
            return (current_distance, current_path + [current_node])

        # skip already visited nodes
        if current_node in visited:
            continue

        # mark current node as visited
        visited.add(current_node)

        # loop over neighbors and update distances
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            path = current_path + [current_node]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor, path))

    # end node not reached
    return (None, [])


with open("home input.txt",'r')as f:
    grid = f.read().splitlines()
travel_data = {}
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
    travel_data[source] = times
print(travel_data)

shortest_time, shortest_path = dijkstra(travel_data, 'AAA', 'ZZZ')
print(f'Time: {shortest_time}, Path: {shortest_path}')  # output: Time: 115, Path: ['AAA', 'CCC', 'DDD', 'ZZZ']