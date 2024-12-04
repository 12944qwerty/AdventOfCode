"""
Day 04: Ceres Search

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
    sum = 0
    for x,y in g:
        if g[(x,y)] == "X":
            for mcoord in g.neighbors(x,y, diagonals=True):
                if g[mcoord] == "M":
                    dx = mcoord[0] - x
                    dy = mcoord[1] - y
                    if g[mcoord[0]+dx, mcoord[1]+dy] == "A":
                        if g[mcoord[0]+2*dx, mcoord[1]+2*dy] == "S":
                            sum += 1
                    
                                    
    return sum

def part2(data):
    g = Grid.from_list(data)
    sum = 0
    for x, y in g:
        if g[(x, y)] == "A":
            if g[(x+1, y+1)] == "M" and g[(x-1, y-1)] == "S" and g[(x+1, y-1)] == "M" and g[(x-1, y+1)] == "S":
                sum += 1
            if g[(x+1, y-1)] == "M" and g[(x-1, y+1)] == "S" and g[(x-1, y-1)] == "M" and g[(x+1, y+1)] == "S":
                sum += 1
            if g[(x-1, y-1)] == "M" and g[(x+1, y+1)] == "S" and g[(x-1, y+1)] == "M" and g[(x+1, y-1)] == "S":
                sum += 1
            if g[(x-1, y+1)] == "M" and g[(x+1, y-1)] == "S" and g[(x+1, y+1)] == "M" and g[(x-1, y-1)] == "S":
                sum += 1
            
    return sum
