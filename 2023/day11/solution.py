"""
Day 11: Cosmic Expansion

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re

def parse_data(f):
    return Grid.from_list([list(a) for a in f.read().split("\n")])

def part1(data):
    galaxies = []
    rows = set()
    cols = set()
    for x in data.rangex():
        for y in data.rangey():
            if data[(x, y)] == '#':
                rows.add(y)
                cols.add(x)
                galaxies.append((x, y))
                
    unbound_rows = sorted(list(set(data.rangey()) ^ rows))
    unbound_cols = sorted(list(set(data.rangex()) ^ cols))
    
    sum = 0
    for combo in combinations(range(len(galaxies)), 2):
        start = galaxies[combo[0]]
        end = galaxies[combo[1]]
        
        dist = 0
        for x in range(min(start[0], end[0]), max(end[0], start[0])):
            if x in unbound_cols:
                dist += 1
            dist += 1
        for y in range(min(start[1], end[1]), max(end[1], start[1])):
            if y in unbound_rows:
                dist += 1
            dist += 1
        sum += dist
        
    return sum

def part2(data):
    galaxies = []
    rows = set()
    cols = set()
    for x in data.rangex():
        for y in data.rangey():
            if data[(x, y)] == '#':
                rows.add(y)
                cols.add(x)
                galaxies.append((x, y))
                
    unbound_rows = sorted(list(set(data.rangey()) ^ rows))
    unbound_cols = sorted(list(set(data.rangex()) ^ cols))
    
    sum = 0
    for combo in combinations(range(len(galaxies)), 2):
        start = galaxies[combo[0]]
        end = galaxies[combo[1]]
        
        dist = 0
        for x in range(min(start[0], end[0]), max(end[0], start[0])):
            if x in unbound_cols:
                dist += 999_999
            dist += 1
        for y in range(min(start[1], end[1]), max(end[1], start[1])):
            if y in unbound_rows:
                dist += 999_999
            dist += 1
        sum += dist
        
    return sum
