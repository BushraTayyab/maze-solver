# 🏰 Maze Solver (BFS Algorithm)

Finds the shortest path in a 2D maze using Breadth-First Search (BFS), with Matplotlib visualization.

*Developed after studying search algorithms in Harvard’s CS50 AI course, with code implementation assisted by DeepSeek AI.*

![Maze Solution Example]
![image](https://github.com/user-attachments/assets/dce3b4f5-5b46-4b0f-9f24-217bc3b0a111)


## 🚀 Features
- Solves mazes with custom obstacles (`0` = path, `1` = wall)
- Visualizes the optimal path using Matplotlib
- Clean, well-commented Python code

## 🛠️ How to Run
```bash
python maze_solver.py
```

## 📦 Requirements
```bash
pip install matplotlib
```

## 📝 Code Overview
```python
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
```

## 🤝 Contributions  
Ideas for improvements? Open an issue or PR!  
---

*Inspired by Harvard's CS50 AI course*  
