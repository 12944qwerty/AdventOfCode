"""
Day 12: Subterranean Sustainability

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
    init:str = data[0].split(": ")[1]
    conv = []
    had = set()
    for line in data[2:]:
        conv.append(line.split(" => "))
        had.add(conv[-1][0])
        
    if globals()['dummy']: # only dummy doens't have complete set
        for c in product("#.", repeat=5):
            if "".join(c) not in had:
                conv.append(["".join(c), "."])

    padding = 0
    for i in range(20):
        if init[:4] != "....":
            init = "...." + init
            padding += 4
        if init[-4:] != "....":
            init = init + "...."
            
        matches = []
        for m, c in conv:
            b = init.find(m)
            while b != -1:
                matches.append((b + 2, c))
                b = init.find(m, b + 1)
        for m, c in matches:
            init = init[:m] + c + init[m+1:]

    sum = 0
    for i in range(len(init)):
        if init[i] == "#":
            sum += i - padding
    return sum

def part2(data):
    init:str = data[0].split(": ")[1]
    conv = []
    had = set()
    for line in data[2:]:
        conv.append(line.split(" => "))
        had.add(conv[-1][0])
        
    if globals()['dummy']: # only dummy doens't have complete set
        return
        for c in product("#.", repeat=5):
            if "".join(c) not in had:
                conv.append(["".join(c), "."])

    padding = 0
    for g in range(50000000000):
        if init[:4] != "....":
            init = "...." + init
            padding += 4
        if init[-4:] != "....":
            init = init + "...."
            
        matches = []
        for m, c in conv:
            b = init.find(m)
            while b != -1:
                matches.append((b + 2, c))
                b = init.find(m, b + 1)
        for m, c in matches:
            init = init[:m] + c + init[m+1:]

        sum = 0
        for i in range(len(init)):
            if init[i] == "#":
                sum += i - padding
        if g > 1e3:
            print(g, sum)
    return sum
