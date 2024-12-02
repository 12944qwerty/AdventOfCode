"""
Day 03: No Matter How You Slice It

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re, get_numbers

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    grid = Grid({})
    for line in data:
        id, x, y, w, h = get_numbers(line)
        for i in range(x, x + w):
            for j in range(y, y + h):
                grid[(i, j)] = grid.get((i, j), 0) + 1
    
    c = Counter(grid.values())
    return c.total() - c[1]

def part2(data):
    claims = []
    grid = Grid({})
    for line in data:
        id, x, y, w, h = get_numbers(line)
        claims.append((id, x, y, w, h))
     
    uniq = set()
    for claim in claims:
        uniq.add(claim[0])
        
    for i, claim in enumerate(claims):
        for j, claim2 in enumerate(claims):
            if i != j and claim2[0] in uniq:
                if claim[1] < claim2[1] + claim2[3] and claim[1] + claim[3] > claim2[1] and claim[2] < claim2[2] + claim2[4] and claim[2] + claim[4] > claim2[2]:
                    uniq.remove(claim2[0])
        if len(uniq) == 1:
            return uniq.pop()
    
    return uniq
