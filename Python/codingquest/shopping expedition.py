import itertools

# input data
distances = [
    [0, 1971, 2868, 2102, 2368, 420, 2377, 629, 1866, 2419, 2417, 2249],
    [1971, 0, 670, 367, 341, 2651, 1001, 703, 2789, 2090, 2006, 350],
    [2868, 670, 0, 2594, 2485, 2199, 669, 1466, 2929, 2256, 532, 742],
    [2102, 367, 2594, 0, 149, 1051, 2023, 2156, 897, 2633, 348, 1490],
    [2368, 341, 2485, 149, 0, 706, 1171, 2274, 1724, 748, 531, 2708],
    [420, 2651, 2199, 1051, 706, 0, 1404, 865, 1922, 1977, 2469, 1499],
    [2377, 1001, 669, 2023, 1171, 1404, 0, 2118, 2421, 263, 1532, 1686],
    [629, 703, 1466, 2156, 2274, 865, 2118, 0, 2496, 426, 2463, 1633],
    [1866, 2789, 2929, 897, 1724, 1922, 2421, 2496, 0, 1868, 1772, 1943],
    [2419, 2090, 2256, 2633, 748, 1977, 263, 426, 1868, 0, 1906, 2683],
    [2417, 2006, 532, 348, 531, 2469, 1532, 2463, 1772, 1906, 0, 1937],
    [2249, 350, 742, 1490, 2708, 1499, 1686, 1633, 1943, 2683, 1937, 0]
]

def tsp(distances):
    # number of cities
    n = len(distances)

    # generate all possible tours (permutations)
    tours = list(itertools.permutations(range(n)))

    # calculate tour distances
    tour_distances = []
    for tour in tours:
        distance = 0
        # calculate the distance of the current tour
        for i in range(n-1):
            distance += distances[tour[i]][tour[i+1]]
        # add the distance between the last city and the first city
        distance += distances[tour[-1]][tour[0]]
        # append the distance to the tour_distances list
        tour_distances.append(distance)

    # find the shortest tour
    shortest_tour_index = tour_distances.index(min(tour_distances))
    # get the shortest tour using the index found above
    shortest_tour = tours[shortest_tour_index]
    # get the length of the shortest tour using the index found above
    shortest_tour_distance = tour_distances[shortest_tour_index]

    return shortest_tour, shortest_tour_distance

# call the tsp function with the input data
shortest_tour, shortest_tour_distance = tsp(distances)

# print the result
print(shortest_tour,shortest_tour_distance)
