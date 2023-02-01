"""
Day 07: The Treachery of Whales

Part 1: 
Part 2: 
"""

def parse_data(f):
    return list(map(int, f.read().strip().split(',')))

def part1(data):
    fuel = 1e9
    for i in range(min(data), max(data) + 1):
        b = sum(abs(num - i) for num in data)
        if fuel > b:
            fuel = b
        else:
            return fuel

def part2(data):
    fuel = 1e9
    for i in range(min(data), max(data) + 1):
        b = sum(abs(num - i) * -~abs(num - i)/2 for num in data)
        if fuel > b:
            fuel = b
        else:
            return round(fuel)
