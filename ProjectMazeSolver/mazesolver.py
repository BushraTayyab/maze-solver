# Maze Solver (BFS)
from collections import deque
import matplotlib.pyplot as plt

def solve_maze(grid, start, end):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:  # Moves that could me made
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "WALL" and (nx, ny) not in visited:
                queue.append(path + [(nx, ny)])
                visited.add((nx, ny))
    return None

# Example maze (0 = empty, "WALL" = obstacle)
grid = [
    [0, 0, 0, 0],
    ["WALL", "WALL", 0, "WALL"],
    [0, 0, 0, 0]
]
path = solve_maze(grid, (0, 0), (2, 3))
print("Path:", path)

# Visualization
plt.imshow([[0 if cell == 0 else 1 for cell in row] for row in grid], cmap='binary')
plt.plot([y for x, y in path], [x for x, y in path], 'r-')
plt.show()