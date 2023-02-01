"""
Day 02: Dive!

Part 1: 
Part 2: 
"""

def parse_data(f):
    return [(a.split()[0], int(a.split()[1])) for a in f.read().splitlines()]

def part1(data):
    depth = horiz = 0
    for direction, amount in data:
        if direction == 'forward':
            horiz += amount
        if direction == 'up':
            depth -= amount
        if direction == 'down':
            depth += amount

    return depth * horiz

def part2(data):
    aim = depth = horiz = 0
    for direction, amount in data:
        if direction == 'forward':
            horiz += amount
            depth += amount * aim
        if direction == 'up':
            aim -= amount
        if direction == 'down':
            aim += amount

    return depth * horiz
