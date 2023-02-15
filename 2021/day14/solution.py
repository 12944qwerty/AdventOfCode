"""
Day 14: Extended Polymerization

Part 1: 
Part 2: 
"""

from collections import Counter

def parse_data(f):
    data = f.read().splitlines()

    return data[0], dict(a.split(' -> ') for a in data[2:])

def part1(data):
    poly = Counter(a+b for a, b in zip(data[0], data[0][1:]))
    counter = Counter(data[0])
    pairs = data[1]
    
    for i in range(10):
        new = Counter()
        for ab, count in poly.items():
            new[ab[0] + pairs[ab]] += count
            new[pairs[ab] + ab[1]] += count

            counter += {pairs[ab]: count}

        poly = new


    return max(counter.values()) - min(counter.values())

def part2(data):
    poly = Counter(a+b for a, b in zip(data[0], data[0][1:]))
    counter = Counter(data[0])
    pairs = data[1]
    
    for i in range(40):
        new = Counter()
        for ab, count in poly.items():
            new[ab[0] + pairs[ab]] += count
            new[pairs[ab] + ab[1]] += count

            counter += {pairs[ab]: count}

        poly = new


    return max(counter.values()) - min(counter.values())
