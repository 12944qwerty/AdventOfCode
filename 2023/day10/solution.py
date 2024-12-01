"""
Day 10: Pipe Maze

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, number_re
from queue import Queue
from copy import deepcopy

def parse_data(f):
    return Grid.from_list([list(a) for a in f.read().split("\n")])

def part1(data):
    start = (0, 0)
    for y in range(data.height):
        for x in range(data.width):
            if data.get((x, y)) == "S":
                start = (x, y)
                break
            
    grid = data
    
    possibleLoops = []
    
    for poss in "-|FLJ7":
        data = deepcopy(grid)
        data[start] = poss
    
        queue = Queue()
        queue.put([start])
        
        while not queue.empty():
            path = queue.get()
            if len(path) > len(set(path)):
                possibleLoops = path
                break
            if path.count(start) > 1:
                continue
            x, y = path[-1]
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x + dx, y + dy
                if (nx, ny) in data:
                    cur = data.get((x, y))
                    nxt = data.get((nx, ny))
                    
                    if len(path) > 1:
                        if path[-2] == (nx, ny):
                            continue
                    
                    if dy == 1: # down
                        if cur in "|7F" and nxt in "|LJ":
                            queue.put([*path, (nx, ny)])
                    if dy == -1: # up
                        if cur in "|LJ" and nxt in "|7F":
                            queue.put([*path, (nx, ny)])
                    if dx == 1: # right
                        if cur in "-LF" and nxt in "-7J":
                            queue.put([*path, (nx, ny)])
                    if dx == -1: # left
                        if cur in "-7J" and nxt in "-LF":
                            queue.put([*path, (nx, ny)])
        else:
            continue
        break
                        
    return len(possibleLoops) // 2

def part2(data):
    start = (0, 0)
    for y in range(data.height):
        for x in range(data.width):
            if data.get((x, y)) == "S":
                start = (x, y)
                break
            
    grid = data
    
    possibleLoops = []
    
    for poss in "-|FLJ7":
        data = deepcopy(grid)
        data[start] = poss
    
        queue = Queue()
        queue.put([start])
        
        while not queue.empty():
            path = queue.get()
            if len(path) > len(set(path)):
                possibleLoops = path
                break
            if path.count(start) > 1:
                continue
            x, y = path[-1]
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                nx, ny = x + dx, y + dy
                if (nx, ny) in data:
                    cur = data.get((x, y))
                    nxt = data.get((nx, ny))
                    
                    if len(path) > 1:
                        if path[-2] == (nx, ny):
                            continue
                    
                    if dy == 1: # down
                        if cur in "|7F" and nxt in "|LJ":
                            queue.put([*path, (nx, ny)])
                    if dy == -1: # up
                        if cur in "|LJ" and nxt in "|7F":
                            queue.put([*path, (nx, ny)])
                    if dx == 1: # right
                        if cur in "-LF" and nxt in "-7J":
                            queue.put([*path, (nx, ny)])
                    if dx == -1: # left
                        if cur in "-7J" and nxt in "-LF":
                            queue.put([*path, (nx, ny)])
        else:
            continue
        break
    
    total = 0
    inside = []
    for y in range(data.miny, data.maxy+1):
        inLoop = False
        prev = "."
        for x in range(data.minx, data.maxx+1):
            cur = data.get((x, y))
            
            if (x, y) in possibleLoops:
                if cur == "|":
                    prev = "|"
                    inLoop = not inLoop
                if cur == "F":
                    prev = "F"
                    inLoop = not inLoop
                if cur == "L":
                    prev = "L"
                    inLoop = not inLoop
                if cur == "J":
                    if prev == "L":
                        inLoop = not inLoop
                if cur == "7":
                    if prev == "F":
                        inLoop = not inLoop
            
            if inLoop and (x, y) not in possibleLoops:
                inside.append((x, y))
                total += 1
                
    return total
