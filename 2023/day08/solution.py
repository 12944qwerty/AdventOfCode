"""
Day 08: Haunted Wasteland

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
    return [a for a in f.read().split("\n")]

def part1(data):
    seq = data[0]
    data = [a.split(" = ") for a in data[2:]]
    data = {a: [b[1:4], b[6:9]] for a, b in data}
    
    steps = 0
    
    i = 0
    cur = "AAA"
    while cur != "ZZZ":
        cur = data[cur][seq[i] == "R"]
        i = (i + 1) % len(seq)
        steps += 1
    
    return steps

def part2(data):
    seq = data[0]
    data = [a.split(" = ") for a in data[2:]]
    data = {a: [b[1:4], b[6:9]] for a, b in data}
    
    current = [a for a in data if a.endswith("A")]
    
    stepss = []
    for cur in current:
        steps = 0
        i = 0
        while not cur.endswith("Z"):
            cur = data[cur][seq[i] == "R"]
            i = (i + 1) % len(seq)
            steps += 1
            
            if steps % 1000000 == 0:
                print(steps, cur)
        stepss += [steps]
    
    return lcm(*stepss)
