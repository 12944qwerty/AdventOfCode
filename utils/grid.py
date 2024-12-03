"""
A 2D or 3D grid with common features like neighbors, and more.
"""

from typing import Any, Callable, Dict, Generator, List, Tuple
from collections import defaultdict

class Grid:
    def __init__(self, grid: Dict[Tuple[int, int], Any] = defaultdict(int)):
        self.grid = grid
        
    @classmethod
    def from_list(cls, grid: List[List[Any]]):
        return cls({(x, y): grid[y][x] for y in range(len(grid)) for x in range(len(grid[y]))})

    @property
    def minx(self) -> int:
        return min(list(self.grid.keys()), key=lambda a: a[0])[0]

    @property
    def maxx(self) -> int:
        return max(list(self.grid.keys()), key=lambda a: a[0])[0]

    @property
    def miny(self) -> int:
        return min(list(self.grid.keys()), key=lambda a: a[1])[1]

    @property
    def maxy(self) -> int:
        return max(list(self.grid.keys()), key=lambda a: a[1])[1]

    @property
    def width(self) -> int:
        return self.maxx - self.minx + 1

    @property
    def height(self) -> int:
        return self.maxy - self.miny + 1
    
    @property
    def size(self) -> int:
        return self.width * self.height
    
    def rangex(self, step: int=1) -> Generator[int, None, None]:
        i = self.minx
        while i <= self.maxx:
            yield i
            i += step
    
    def rangey(self, step: int=1) -> Generator[int, None, None]:
        i = self.miny
        while i <= self.maxy:
            yield i
            i += step

    def neighbors(self, x: int, y: int, *, diagonals=False, check: Callable[[Any, Any], bool]=None) -> List[Tuple[int, int]]:
        near = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if diagonals:
            near += [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        nearest, near = near, []
        for dx, dy in nearest:
            nx, ny = x + dx, y + dy
            if (nx, ny) in self.grid:
                if check:
                    if check(self.grid[nx, ny], self.grid[x, y]):
                        near.append((nx, ny))
                else:
                    near.append((nx, ny))
 
        return near

    def get(self, key: Tuple[int, int], default: Any=None) -> Any:
        return self.grid.get(key, default)

    def items(self) -> List[Tuple[Tuple[int, int], Any]]:
        return list(self.grid.items())

    def keys(self) -> List[Tuple[int, int]]:
        return list(self.grid.keys())

    def values(self) -> List[Any]:
        return list(self.grid.values())

    def __setitem__(self, key: Tuple[int, int], value: Any):
        self.grid[key] = value

    def __getitem__(self, item: Tuple[int, int]) -> Any:
        return self.grid[item]
        
    def __iter__(self):
        return iter(self.grid.keys())
    
    def coords(self) -> Generator[Tuple[int, int], None, None]:
        for y in range(self.miny, self.maxy + 1):
            for x in range(self.minx, self.maxx + 1):
                yield x, y
    
    def __str__(self):
        msg = ""
        for y in range(self.miny, self.maxy + 1):
            for x in range(self.minx, self.maxx + 1):
                msg += str(self.grid.get((x, y), " "))
            msg += "\n"
            
        return msg