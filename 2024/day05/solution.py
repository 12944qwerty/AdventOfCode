"""
Day 05: Print Queue

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
    graph = DirectedGraph()
    i = 0
    while data[i] != "":
        graph.add_edge(*list(map(int, data[i].split("|"))))
        i += 1
    i += 1

    finished = []
    for line in data[i:]:
        manual = list(map(int, line.split(",")))
        for edge in graph.edges:
            if edge.a.value in manual and edge.b.value in manual:
                if manual.index(edge.a.value) > manual.index(edge.b.value):
                    break
        else:
            finished.append(manual)
        
    sum = 0
    for line in finished:
        sum += line[len(line) // 2]
    
    return sum

def part2(data):
    graph = DirectedGraph()
    i = 0
    while data[i] != "":
        graph.add_edge(*list(map(int, data[i].split("|"))))
        i += 1
    i += 1

    finished = []
    for line in data[i:]:
        manual = list(map(int, line.split(",")))
        broken = False
        while True:
            av = bv = 0
            for edge in graph.edges:
                if edge.a.value in manual and edge.b.value in manual:
                    av = manual.index(edge.a.value)
                    bv = manual.index(edge.b.value)
                    if av > bv:
                        break
            else:
                if broken:
                    finished.append(manual)
                break
            broken = True
            manual[av], manual[bv] = manual[bv], manual[av]
        
    sum = 0
    for line in finished:
        sum += line[len(line) // 2]
    
    return sum
