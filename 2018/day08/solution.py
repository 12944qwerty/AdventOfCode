"""
Day 08: Memory Maneuver

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
    data = map(int, data[0].split())

    def read_tree():
        meta = 0
        children = next(data)
        meta_entries = next(data)
        for _ in range(children):
            meta += read_tree()
        for _ in range(meta_entries):
            meta += next(data)
        return meta
    
    return read_tree()

def part2(data):
    data = map(int, data[0].split())

    def read_tree():
        meta = 0
        children = next(data)
        meta_entries = next(data)
        values = []
        for _ in range(children):
            values.append(read_tree())
        if children == 0:
            for _ in range(meta_entries):
                meta += next(data)
        else:
            for _ in range(meta_entries):
                index = next(data) - 1
                if 0 <= index < len(values):
                    meta += values[index]
            
        return meta
    
    return read_tree()
