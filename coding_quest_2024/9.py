from collections import deque

def shortest_path_maze(maze):
    # Define directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Extract maze dimensions
    rows = len(maze)
    cols = len(maze[0])
    
    # Initialize queue for BFS and visited set
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = set([(0, 0)])
    
    while queue:
        row, col, distance = queue.popleft()
        
        # Check if reached exit
        if (row, col) == (rows-1, cols-1):
            return distance
        
        # Explore adjacent cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check if new position is within bounds and not a wall
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != '#':
                # If elevator, stay at the same level, so distance remains the same
                if maze[new_row][new_col] == '$':
                    if (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, distance))
                        visited.add((new_row, new_col))
                else:
                    if (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, distance + 1))
                        visited.add((new_row, new_col))
    
    # If exit not reachable
    return -1

# Example maze
maze = [
    "#####################",
    "................#...#",
    "###########.###.#.#.#",
    "#...#.......#.#...#. #",
    "#.#.#.#######.#####.##",
    "#.#..$#.#.$....$.....#",
    "#.#####.#.#######.###",
    "#.#.......#.....#.#.#",
    "#.#########.###.#.#.#",
    "#.#...........#.#...#",
    "#.#.#$####$.###$###.#",
    "#...#.....#.#...#...#",
    "#.###.###.###.#.#.###",
    "#...#.#.....#.#.#...#",
    "#####################",
    "#.#.#$..#.$...#$..#. #",
    "#.#.###.###.#.#.###.#",
    "#...#...#...#.....#. #",
    "#.###.###.#.#####.#.#",
    "#...#.....#..........",
    "#####################"
]

# Calculate shortest path
shortest_path = shortest_path_maze(maze)
print("Shortest path out of the maze:", shortest_path)
