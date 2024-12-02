"""
Day 02: Inventory Management System

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
    return [a for a in f.read().split("\n")]

def part1(data):
    twos = 0
    threes = 0
    for line in data:
        c = Counter(line)
        twos += 2 in c.values()
        threes += 3 in c.values()
    
    return twos * threes

def part2(data):
    twos = 0
    threes = 0
    for line in data:
        for line2 in data:
            diff = 0
            for i in range(len(line)):
                if line[i] != line2[i]:
                    diff += 1
            if diff == 1:
                return "".join([line[i] for i in range(len(line)) if line[i] == line2[i]])
    
    return None