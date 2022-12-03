"""
Day 01: Calorie Counting

Part 1: Get the amount of calories the elf who is carrying the most has.
Part 2: Get the top 3 elves who hold the most calories, and sum them.
"""

def parse_data(f):
    return sorted([sum(list(map(int,a.split('\n')))) for a in f.read().split('\n\n')], reverse=True)

def part1(data):
    return data[0]

def part2(data):
    return sum(data[:3])
