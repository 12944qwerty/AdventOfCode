"""
Day 04: Camp Cleanup

Part 1: How many pairs of ranges fully wrap the other
Part 2: How many pairs of ranges have common numbers at all
"""

def parse_data(f):
    return [[set(range(int(b.split('-')[0]), int(b.split('-')[1])+1)) for b in a.split(',')] for a in f.read().splitlines()]
    
def part1(data):
    total = 0
    for a, b in data:
        inter = a & b
        if len(inter) in [len(a), len(b)]:
            total += 1

    return total

def part2(data):
    total = 0
    for a, b in data:
        total += bool(a & b)

    return total
