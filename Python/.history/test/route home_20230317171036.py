import heapq

def dijkstra(graph, start, end):
    # initialize distances and visited nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    # use a heap to track nodes with smallest tentative distance
    heap = [(0, start)]

    while heap:
        # get the node with smallest tentative distance
        (current_distance, current_node) = heapq.heappop(heap)

        # if the current node is the end node, return the distance
        if current_node == end:
            return current_distance

        # skip already visited nodes
        if current_node in visited:
            continue

        # mark current node as visited
        visited.add(current_node)

        # loop over neighbors and update distances
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    # end node not reached
    return None


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

data = {
    'AAA': {'BBB': 38, 'CCC': 45},
    'BBB': {'AAA': 38, 'DDD': 60, 'ZZZ': 70},
    'CCC': {'AAA': 45, 'DDD': 35},
    'DDD': {'BBB': 60, 'CCC': 35, 'ZZZ': 15},
    'ZZZ': {'BBB': 70, 'DDD': 15}
}
fastest_time = dijkstra(data, 'AAA', 'ZZZ')
print(fastest_time)  # output: 115