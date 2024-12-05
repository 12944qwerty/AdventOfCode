"""
Day 06: Chronal Coordinates

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re, get_numbers, manhattan

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    grid = Grid()
    grid[(0, 0)] = 0
    coords = []
    for line in data:
        x, y = map(int, line.split(", "))
        grid[(x, y)] = 0
        coords.append((x, y))
    
    # really inefficient code...
    
    finites = set(coords)
    
    for x, y in grid.coords():
        min_dist = 10000
        dists = sorted([(manhattan((x, y), coord), i) for i, coord in enumerate(coords)])
        if dists[0][0] != dists[1][0]:
            grid[coords[dists[0][1]]] += 1
            if (x == 0 or y == 0 or x == grid.maxx or y == grid.maxy) and coords[dists[0][1]] in finites:
                finites.remove(coords[dists[0][1]])
        
    return max([grid[coord] for coord in finites])

def part2(data):
    max_sum = 32 if globals()['dummy'] else 10000
    grid = Grid()
    grid[(0, 0)] = 0
    coords = []
    for line in data:
        x, y = map(int, line.split(", "))
        grid[(x, y)] = 0
        coords.append((x, y))
    
    s = 0
    for x, y in grid.coords():
        s += sum([manhattan((x, y), coord) for coord in coords]) < max_sum
        
    return s
