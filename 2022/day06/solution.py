"""
Day 06: Tuning Trouble

Part 1: How many characters till you reach the end of 4 consecutive, distinct characters?
Part 2: How many characters till you reach the end of 14 consecutive, distinct characters?
"""

def parse_data(f):
    return f.read().strip()

def part1(data):
    i = 0
    while len(set(_:=data[i:i+4])) != 4 and i < len(data)-4:
        i += 1

    return i+4

def part2(data):
    i = 0
    while len(set(_:=data[i:i+14])) != 14 and i < len(data)-14:
        i += 1

    return i+14
