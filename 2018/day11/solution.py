"""
Day 11: Chronal Charge

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
    serial = int(data[0])
    g = Grid({(x,y): (((x+10)*y+serial)*(x+10)//100)%10 - 5 for x in range(1,301) for y in range(1,301)})
    powers = (0, (0, 0))
    for x in range(1, 288):
        for y in range(1, 288):
            sum = 0
            for dx, dy in product(range(3), repeat=2):
                sum += g[(x+dx, y+dy)]
            powers = max(powers, (sum, (x, y)))
    
    return f"{powers[1][0]},{powers[1][1]}"

def part2(data):
    serial = int(data[0])
    g = Grid({(x,y): (((x+10)*y+serial)*(x+10)//100)%10 - 5 for x in range(1,301) for y in range(1,301)})
    m = (0, (0, 0, 0))
    for x, y in g.coords():
        g[(x, y)] += g.get((x-1, y), 0) + g.get((x, y-1), 0) - g.get((x-1, y-1), 0)
    
    for size in range(1, 301):
        for x in range(1, 301-size):
            for y in range(1, 301-size):
                sum = g[(x+size, y+size)] - g[(x, y+size)] - g[(x+size, y)] + g[(x, y)]
                m = max(m, (sum, (x+1, y+1, size)))
    
    return f"{m[1][0]},{m[1][1]},{m[1][2]}"
