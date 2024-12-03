"""
Day 03: Mull It Over

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
    reg = re.compile("mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    sum = 0
    for line in data:
        for match in reg.finditer(line):
            sum += int(match.group(1)) * int(match.group(2))
    
    return sum

def part2(data):
    reg = re.compile("mul\((\d+,\d+)\)|do\(\)|don't\(\)")
    sum = 0
    do = True # bruh i had it inside the loop so i took 20 minutes to get this solved
    for line in data:
        for match in reg.finditer(line):
            if match.group() == "do()":
                do = True
            elif match.group() == "don't()":
                do = False
            elif do:
                sum += prod([int(a) for a in match.group(1).split(",")])
            
    
    return sum
