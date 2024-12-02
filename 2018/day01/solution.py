"""
Day 01: Chronal Calibration

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
    ops = []
    for line in data:
        for i in line.split(", "):
            ops.append(i)
    sum = 0
    for i in ops:
        sum += int(i)
    return sum

def part2(data):
    ops = []
    freq = set()
    freq.add(0)
    for line in data:
        for i in line.split(", "):
            ops.append(i)
    sum = 0
    while True:
        for i in ops:
            sum += int(i)
            if sum in freq:
                return sum
            freq.add(sum)
    return None
