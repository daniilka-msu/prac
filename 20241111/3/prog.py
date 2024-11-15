from collections import deque

class Maze:
    def __init__(self, N):
        self.N = N
        self.grid = [['█' for _ in range(2 * N + 1)] for _ in range(2 * N + 1)]
        self.rooms = set()
        for i in range(N):
            for j in range(N):
                self.grid[2 * i + 1][2 * j + 1] = '·'
                self.rooms.add((2 * i + 1, 2 * j + 1))

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        x0, y0 = 2 * x0 + 1, 2 * y0 + 1
        x1, y1 = 2 * x1 + 1, 2 * y1 + 1
        return self.bfs_path_exists((x0, y0), (x1, y1))

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        x0, y0 = 2 * x0 + 1, 2 * y0 + 1
        x1, y1 = 2 * x1 + 1, 2 * y1 + 1
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                self.grid[y][x0] = value
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                self.grid[y0][x] = value

    def bfs_path_exists(self, start, goal):
        if start == goal:
            return True
        rows, cols = len(self.grid), len(self.grid[0])
        visited = set()
        queue = deque([start])
        while queue:
            x, y = queue.popleft()
            if (x, y) == goal:
                return True
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < cols and 0 <= ny < rows and self.grid[ny][nx] == '·' and (nx, ny) not in visited:
                    queue.append((nx, ny))
        return False

import sys

exec(sys.stdin.read())
