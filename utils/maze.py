from queue import Queue, PriorityQueue
from .grid import Grid

from typing import Tuple, List

class Maze:
    def __init__(self, grid: Grid, *, diagonals: bool=False):
        self.grid = grid
        
        self.diagonals = diagonals
        
    def neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        near = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if self.diagonals:
            near += [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        nearest, near = near, []
        for dx, dy in nearest:
            nx, ny = x + dx, y + dy
            if (nx, ny) in self.grid:
                near.append((nx, ny))
 
        return near
    
    def fitness(self, start: Tuple[int, int], end: Tuple[int, int]) -> float:
        return abs(end[0] - start[0]) + abs(end[1] - start[1])
    
    def distance(self, start: Tuple[int, int], end: Tuple[int, int]) -> float:
        return round(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
    
    def bfs(self, start: Tuple[int, int], end: Tuple[int, int], *, immediate: bool = True) -> List[Tuple[int, int]]:
        """
        BFS Pathfinding Algorithm
        start ---------> end
        Immediate returns the first path found, otherwise returns all paths found.
        """
        queue = Queue()
        queue.put([start])
        
        paths = []
        
        while not queue.empty():
            path = queue.get()
            if path[-1] == end:
                if immediate:
                    return path
                paths.append(path)
                continue
            x, y = path[-1]
            for nx, ny in self.neighbors(x, y):
                if (nx, ny) not in path:
                    queue.put([*path, (nx, ny)])
                    
        return paths
                    
    def dfs(self, start: Tuple[int, int], end: Tuple[int, int], *, immediate: bool = True) -> List[Tuple[int, int]]:
        """
        DFS Pathfinding Algorithm
        start ---------> end
        Immediate returns the first path found, otherwise returns all paths found.
        """
        stack = [[start]]
        visited = set()
        
        paths = []
        
        while stack:
            path = stack.pop()
            x, y = path[-1]
            if path[-1] == end:
                if immediate:
                    return path
                paths.append(path)
                continue
            visited.add((x, y))
            for nx, ny in self.neighbors(x, y):
                if (nx, ny) not in visited:
                    stack.append([*path, (nx, ny)])
                    
        return paths
    
    def astar(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        A* Pathfinding Algorithm
        start ---------> end
        """
        queue = PriorityQueue()
        queue.put((0, [start]))
        
        paths = []
        seen = set()
        
        while not queue.empty():
            _, path = queue.get()
            if path[-1] == end:
                return path
            x, y = path[-1]
            for nx, ny in self.neighbors(x, y):
                if (nx, ny) not in path and (nx, ny) not in seen:
                    queue.put((self.fitness((nx, ny), end), [*path, (nx, ny)]))
                    
        return paths