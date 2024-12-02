"""
Day 01: Historian Hysteria

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
    data = [a.split() for a in data]
    sum = 0
    left = []
    right = []
    for line in data:
        left.append(int(line[0]))
        right.append(int(line[-1]))
    
    left = sorted(left)
    right = sorted(right)
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum

def part2(data):
    data = [a.split() for a in data]
    sum = 0
    left = []
    right = []
    for line in data:
        left.append(int(line[0]))
        right.append(int(line[-1]))
        
    for i in left:
        for j in right:
            if i == j:
                sum += i
        
    return sum
