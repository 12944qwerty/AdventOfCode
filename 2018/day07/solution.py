"""
Day 07: The Sum of Its Parts

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import *
from time import sleep

def parse_data(f):
    return [a for a in f.read().split("\n")]

def part1(data):
    graph = DirectedGraph()
    for line in data:
        graph.add_edge(line[5], line[36])
        
    return "".join(a.value for a in graph.topological())

def part2(data):
    dummy = globals()['dummy']
    graph = DirectedGraph()
    for line in data:
        graph.add_edge(line[5], line[36])
        
    workers = [None for _ in range([5,2][dummy])]
    
    for node in graph.nodes:
        node.seconds = ord(node.value) - [4, 64][dummy]
        
    all_nodes = set(graph.nodes)
    
    sec = 0
    while any(n.seconds != 0 for n in all_nodes):
        for node in sorted(graph.nodes, key=lambda a: (a.indegree, a.value)):
            if node.indegree == 0:
                for i, worker in enumerate(workers):
                    if worker is None:
                        workers[i] = node
                        graph.nodes.remove(node)
                        break
                    
        # print(sec, "\t", "\t".join([a.value + str(a.seconds) if a is not None else "." for a in workers]))
        for i, worker in enumerate(workers):
            if worker is not None:
                worker.seconds -= 1
                if worker.seconds == 0:
                    for n in graph.neighbors(worker):
                        n.indegree -= 1
                    workers[i] = None
        sec += 1

    return sec
