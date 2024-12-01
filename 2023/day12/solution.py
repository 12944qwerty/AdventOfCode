"""
Day 12: Hot Springs

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re
from copy import copy

def parse_data(f):
    return [a.split(" ") for a in f.read().split("\n")]

def part1(data):
    sum = 0
    j = 0
    for line in data:
        springs = line[0]
        pattern = list(map(int, line[1].split(",")))
        
        marks = []
        for i in range(len(springs)):
            if springs[i] == "?":
                marks.append(i)
        
        possible = 0
        for combo in combinations_with_replacement([-1] + marks, len(marks)):
            spring = copy(springs)
            for i in range(len(combo)):
                if combo[i] != -1:
                    spring = spring[:combo[i]] + "#" + spring[combo[i]+1:]
                            
            spring = [len(a) for a in spring.split(".") if a]
            
            if len(spring) == len(pattern):
                if all([a == b for a, b in zip(spring, pattern)]):
                    possible += 1
                
        sum += possible
        j += 1
        print(f"{j} / {len(data)}")
        
    return sum

def part2(data):
    sum = 0
    for line in data:
        sum += 1
    
    return sum
