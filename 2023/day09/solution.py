"""
Day 09: Mirage Maintenance

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import grid, number_re

def parse_data(f):
    return [list(map(int, a.split())) for a in f.read().split("\n")]

def part1(data):
    sum = 0
    for line in data:
        cur = [line]
        while len(cur[-1]) > 0 and any(a != 0 for a in cur[-1]):
            new = []
            for i in range(0, len(cur[-1])-1):
                new.append(cur[-1][i+1] - cur[-1][i])
            cur.append(new)
        
        inc = 0
        for i in range(len(cur)-1, -1, -1):
            inc += cur[i][-1]
            cur[i].append(inc)
            
        sum += cur[0][-1]
    
    return sum

def part2(data):
    sum = 0
    for line in data:
        cur = [line]
        while len(cur[-1]) > 0 and any(a != 0 for a in cur[-1]):
            new = []
            for i in range(0, len(cur[-1])-1):
                new.append(cur[-1][i+1] - cur[-1][i])
            cur.append(new)
        
        inc = 0
        for i in range(len(cur)-1, -1, -1):
            inc = cur[i][0] - inc
            cur[i].insert(0, inc)
            
        sum += cur[0][0]
    
    return sum
