"""
Day 06: Guard Gallivant

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import *

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    g = Grid.from_list(data)
    guard = None
    for x,y in g:
        if g[x,y] in ">v<^":
            guard = (x,y)
            break
    assert guard is not None
    
    seen = set()
    
    i = 0
    minx = g.minx - 1
    miny = g.miny - 1
    maxx = g.maxx + 1
    maxy = g.maxy + 1
    while minx < guard[0] < maxx and miny < guard[1] < maxy:
        i += 1
        dir = g[guard]
        dx, dy = guard
        if g[guard] == ">":
            dx += 1
        elif g[guard] == "v":
            dy += 1
        elif g[guard] == "<":
            dx -= 1
        elif g[guard] == "^":
            dy -= 1
        if g[dx, dy] == "#":
            g[guard] = "^<v>"["^<v>".index(g[guard]) - 1]
        else:
            g[guard] = "."
            guard = (dx, dy)
            g[guard] = dir
            seen.add(guard)
    
    return len(seen)
        
    
def part2(data):
    g = Grid.from_list(data)
    guard = None
    direction = None
    for x,y in g:
        if g[x,y] in ">v<^":
            guard = (x,y)
            direction = g[guard]
            g[guard] = "."
            break
    assert guard is not None and direction is not None
    
        
    sum = 0
    minx = g.minx - 1
    miny = g.miny - 1
    maxx = g.maxx + 1
    maxy = g.maxy + 1
    copy = guard[:]
    startingdir = direction
    for wx, wy in g:
        if g[wx,wy] != ".":
            continue
        
        seen = set()
        guard = copy[:]
        direction = startingdir
        while minx < guard[0] < maxx and miny < guard[1] < maxy:
            dx, dy = guard
            if direction == ">":
                dx += 1
            elif direction == "v":
                dy += 1
            elif direction == "<":
                dx -= 1
            elif direction == "^":
                dy -= 1
            if g[dx, dy] == "#" or dx == wx and dy == wy:
                direction = "^<v>"["^<v>".index(direction) - 1]
            elif (dx, dy, direction) in seen:
                sum += 1
                break
            else:
                guard = (dx, dy)
                seen.add((dx, dy, direction))
                
    return sum