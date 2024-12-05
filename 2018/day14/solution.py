"""
Day 14: Chocolate Charts

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
    start = int(data[0])
    if globals()['dummy'] and start > 10e3:
        return "dummy"
    r = delist([3, 7])
    first = 0
    second = 1
    while len(r) < start + 11:
        r += [int(x) for x in str(r[first] + r[second])]
        first = (first + r[first] + 1) % len(r)
        second = (second + r[second] + 1) % len(r)
    return "".join(map(str, r[start:start+10]))

def part2(data):
    start = data[0]
    # if globals()['dummy'] and start == [2,0,1,8]:
    #     return "dummy"
    r = "37"
    first = 0
    second = 1
    while start not in r[-7:]:
        r += str(int(r[first]) + int(r[second]))
        first = (first + int(r[first]) + 1) % len(r)
        second = (second + int(r[second]) + 1) % len(r)
    return r.index(start)
