import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the distance to each node
    distance = {node: float('inf') for node in graph}
    # Set the distance to the starting node to 0
    distance[start] = 0

    # Create a priority queue to store nodes to visit
    queue = [(0, start)]

    while queue:
        # Get the node with the smallest distance from the start
        (current_distance, current_node) = heapq.heappop(queue)

        # If we have already visited this node, skip it
        if current_distance > distance[current_node]:
            continue

        # Visit each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to this neighbor through the current node
            new_distance = distance[current_node] + weight

            # If the new distance is smaller than the current distance to this neighbor, update the distance
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                # Add the neighbor to the queue with its new distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distance

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

distances = dijkstra(graph, 'TYC')
print(distances)