"""
Day 09: Marble Mania

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
    n, p = get_numbers(data[0])
    marbles = deque([0])
    players = [0] * n
    cur = 0
    for i in range(1, p + 1):
        if i % 23 == 0:
            marbles.rotate(7)
            players[cur] += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)
        cur = (cur + 1) % n
        
    return max(players)

def part2(data):
    n, p = get_numbers(data[0])
    marbles = deque([0])
    players = [0] * n
    cur = 0
    for i in range(1, p * 100 + 1):
        if i % 23 == 0:
            marbles.rotate(7)
            players[cur] += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)
        cur = (cur + 1) % n
        
    return max(players)
