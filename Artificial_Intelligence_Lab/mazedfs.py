def dfs(maze, start, end):
    stack = [start]  # Initialize stack with start position
    visited = set()  # Track visited positions
    parent = {}      # To reconstruct path

    while stack:
        position = stack.pop()  # Get current position
        x, y = position

        # Check if we've reached the end
        if position == end:
            # Reconstruct the path from end -> start
            path = []
            while position != start:
                path.append(position)
                position = parent[position]
            path.append(start)
            path.reverse()
            return path

        # Mark the current cell as visited
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            # Check bounds and if the cell is already visited or is a wall
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and new_pos not in visited and new_pos not in stack):
                stack.append(new_pos)
                parent[new_pos] = (x, y)

    return None  # Return None if no path is found


# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and end positions
start = (0, 2)
end = (4, 3)

# Solve the maze
path = dfs(maze, start, end)
print("Path found:" if path else "No path found")
print(path)

