"""
Day 04: Repose Record

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import Grid, Maze, number_re, get_numbers

def parse_data(f):
    return [a for a in f.readlines()]

def part1(data):
    guards: dict[int, list[int]] = {}
    sleep = {}
    recent = 0
    start = 0
    end = 0
    for event in data:
        year, month, day, hour, minute, *rest = get_numbers(event)
        if len(rest) == 1:
            recent = rest[0]
        elif "falls asleep" in event:
            start = minute
        elif "wakes up" in event:
            end = minute
            sleep[recent] = sleep.get(recent, 0) + end - start
            if recent not in guards:
                guards[recent] = [0] * 60
            for i in range(start, end + 1):
                guards[recent][i] += 1
    
    most = max(sleep, key=sleep.get)
    print(most, guards[most].index(max(guards[most])))
    return most * guards[most].index(max(guards[most]))

def part2(data):
    data = sorted(data)
    guards: dict[int, list[int]] = {}
    sleep = {}
    recent = 0
    start = 0
    end = 0
    for event in data:
        year, month, day, hour, minute, *rest = get_numbers(event)
        if len(rest) == 1:
            recent = rest[0]
        elif "falls asleep" in event:
            start = minute
        elif "wakes up" in event:
            end = minute
            sleep[recent] = sleep.get(recent, 0) + end - start
            if recent not in guards:
                guards[recent] = [0] * 60
            for i in range(start, end + 1):
                guards[recent][i] += 1
    
    most = 0
    most_id = 0
    guard_id = 0
    for guard in guards:
        if most < max(guards[guard]):
            most = max(guards[guard])
            guard_id = guard
            most_id = guards[guard].index(most)
            
    # for guard in guards:
    #     print(f"#{guard}\t", " ".join([str(a).zfill(2) for a in guards[guard]]), max(guards[guard]), guards[guard].index(max(guards[guard])))
            
    # print(guard_id, most_id)
            
    return guard_id * most_id
