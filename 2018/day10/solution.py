"""
Day 10: The Stars Align

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
    if globals()['dummy']:
        return None
    g = Grid()
    vels = []
    coords = []
    for line in data:
        x, y, vx, vy = get_numbers(line)
        g[(x, y)] = "#"
        coords.append((x, y))
        vels.append((vx, vy))
    
    i = 0
    m = 10e6
    while True:
        old = set()
        new = set()
        if g.size == 620:
            print(g)
            return
        for j, (vx, vy) in enumerate(vels):
            x, y = coords[j]
            old.add((x, y))
            coords[j] = (x + vx, y + vy)
            x, y = coords[j]
            new.add((x, y))
            g[(x, y)] = "#"
        for x, y in old:
            if (x, y) not in new:
                del g.grid[(x, y)]
        i += 1

def part2(data):
    if globals()['dummy']:
        return None
    g = Grid()
    vels = []
    coords = []
    for line in data:
        x, y, vx, vy = get_numbers(line)
        g[(x, y)] = "#"
        coords.append((x, y))
        vels.append((vx, vy))
    
    i = 0
    m = 10e6
    while True:
        old = set()
        new = set()
        if g.size == 620:
            return i
        for j, (vx, vy) in enumerate(vels):
            x, y = coords[j]
            old.add((x, y))
            coords[j] = (x + vx, y + vy)
            x, y = coords[j]
            new.add((x, y))
            g[(x, y)] = "#"
        for x, y in old:
            if (x, y) not in new:
                del g.grid[(x, y)]
        i += 1