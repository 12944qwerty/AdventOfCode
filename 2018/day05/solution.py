"""
Day 05: Alchemical Reduction

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
    data = data[0]
    prev = ""
    while prev != data:
        prev = data
        for a in "abcdefghijklmnopqrstuvwxyz":
            data = data.replace(a + a.upper(), "").replace(a.upper() + a, "")
    
    return len(data)

@lru_cache
def react(data):
    prev = ""
    while prev != data:
        prev = data
        for a in "abcdefghijklmnopqrstuvwxyz":
            data = data.replace(a + a.upper(), "").replace(a.upper() + a, "")
    
    return len(data)

def part2(data):
    data = data[0]
    copy = data
    
    lens = {}
    for b in "abcdefghijklmnopqrstuvwxyz":
        data = copy
        data = data.replace(b, "").replace(b.upper(), "")
        prev = ""
        while prev != data:
            prev = data
            for a in "abcdefghijklmnopqrstuvwxyz":
                data = data.replace(a + a.upper(), "").replace(a.upper() + a, "")
        lens[b] = len(data)
    
    return min(lens.values())
