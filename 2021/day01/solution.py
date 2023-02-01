"""
Day 01: Sonar Sweep

Part 1: 
Part 2: 
"""

def parse_data(f):
    return list(map(int, f.read().splitlines()))

def part1(data):
    total = 0
    prev = data[0]
    for num in data[1:]:
        if num > prev:
            total += 1
        prev = num

    return total

def part2(data):
    total = 0
    prev = sum(data[:3])
    for i in range(len(data)):
        if prev < sum(data[i:i+3]):
            total += 1
        prev = sum(data[i:i+3])

    return total
