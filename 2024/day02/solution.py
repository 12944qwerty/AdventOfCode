"""
Day 02: Red-Nosed Reports

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re, get_numbers, manhattan

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    sum = 0
    for line in data:
        nums = get_numbers(line)
        prev = nums[0]
        inc = nums[0] < nums[1]
        for num in nums[1:]:
            if 1 <= num - prev <= 3 and inc:
                pass
            elif -3 <= num - prev <= -1 and not inc:
                pass
            else:
                break
            prev = num
        else:
            sum += 1
                
    return sum

def part2(data):
    sum = 0
    for line in data:
        nums = get_numbers(line)
        copy = nums[:]
        for i in range(-1, len(nums)):
            if i != -1:
                nums = copy[:i] + copy[i+1:]
            prev = nums[0]
            inc = nums[0] < nums[1]
            for num in nums[1:]:
                if 1 <= num - prev <= 3 and inc:
                    pass
                elif -3 <= num - prev <= -1 and not inc:
                    pass
                else:
                    break
                prev = num
            else:
                sum += 1
                break
                    
    return sum
