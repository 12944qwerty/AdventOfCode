"""
Day 07: Camel Cards

Part 1: 
Part 2: 
"""
import re
from functools import lru_cache, cmp_to_key
from itertools import combinations, permutations, product, combinations_with_replacement
from collections import Counter, defaultdict, deque
from math import gcd, lcm, floor, ceil, sqrt, prod
from utils import grid, number_re


def parse_data(f):
    return [a.split() for a in f.read().split("\n")]

def part1(data):
    CARDS = "AKQJT98765432"
    scores = {}
    for hand, score in data:
        c = Counter(hand)
        
        if c.most_common()[0][1] > 3:
            scores[hand] = [c.most_common()[0][1] + 1, score]
        elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
            scores[hand] = [4, score]
        elif c.most_common()[0][1] == 3:
            scores[hand] = [3, score]
        elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
            scores[hand] = [2, score]
        elif c.most_common()[0][1] == 2:
            scores[hand] = [1, score]
        else:
            scores[hand] = [0, score]
            
    def sort_cards(a, b):
        if a[1][0] != b[1][0]:
            return (a[1][0] > b[1][0]) * 2 - 1
        
        for i, j in zip(a[0], b[0]):
            if i != j:
                return (CARDS.index(i) < CARDS.index(j)) * 2 - 1
        
        return 0
            
    sorted_scores = list(scores.items())
    sorted_scores.sort(key=lambda a: a[1][0])
    sorted_scores.sort(key=cmp_to_key(sort_cards))
    
    sum = 0
    for i, a in enumerate(sorted_scores):
        sum += (i+1) * int(a[1][1])
    return sum

def part2(data):
    CARDS = "AKQT98765432J"
    scores = {}
    for hand, score in data:
        c = Counter(hand)
        
        jokers = c["J"]
        c.update({"J": -5})
        
        if jokers == 0:        
            if c.most_common()[0][1] > 3:
                scores[hand] = [c.most_common()[0][1] + 1, score]
            elif c.most_common()[0][1] == 3 and c.most_common()[1][1] == 2:
                scores[hand] = [4, score]
            elif c.most_common()[0][1] == 3:
                scores[hand] = [3, score]
            elif c.most_common()[0][1] == 2 and c.most_common()[1][1] == 2:
                scores[hand] = [2, score]
            elif c.most_common()[0][1] == 2:
                scores[hand] = [1, score]
            else:
                scores[hand] = [0, score]
        elif jokers == 5:
            scores[hand] = [6, score]
        else:
            if c.most_common()[0][1] + jokers > 3:
                scores[hand] = [c.most_common()[0][1] + jokers + 1, score]
            elif c.most_common()[0][1] + jokers == 3 and c.most_common()[1][1] == 2:
                scores[hand] = [4, score]
            elif c.most_common()[0][1] + jokers == 3:
                scores[hand] = [3, score]
            elif c.most_common()[0][1] + jokers == 2 and c.most_common()[1][1] == 2:
                scores[hand] = [2, score]
            elif c.most_common()[0][1] + jokers == 2:
                scores[hand] = [1, score]
            else:
                scores[hand] = [0, score]
            
    def sort_cards(a, b):
        if a[1][0] != b[1][0]:
            return (a[1][0] > b[1][0]) * 2 - 1
        
        for i, j in zip(a[0], b[0]):
            if i != j:
                return (CARDS.index(i) < CARDS.index(j)) * 2 - 1
        
        return 0
            
    sorted_scores = list(scores.items())
    sorted_scores.sort(key=lambda a: a[1][0])
    sorted_scores.sort(key=cmp_to_key(sort_cards))
    
    sum = 0
    for i, a in enumerate(sorted_scores):
        sum += (i+1) * int(a[1][1])
    return sum
