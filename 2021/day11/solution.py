"""
Day 11: Dumbo Octopus

Part 1: 
Part 2: 
"""
from utils import Grid

def parse_data(f):
    data = {}
    for i, line in enumerate(f.read().splitlines()):
        for j, col in enumerate(line):
            data[(j, i)] = int(col)

    return Grid(data)

def part1(data: Grid):
    flashes = 0
    flashed = []
    check = lambda a, _: 0 < a
    for _ in range(100):
        for i, j in data:
            data[(i, j)] += 1
            if data[(i, j)] > 9:
                data[(i, j)] = 0
                flashed.append((i, j))

        while flashed:
            x, y = flashed.pop()
            flashes += 1
            for c in data.neighbors(x, y, diagonals=True, check=check):
                if data.get(c):
                    data[c] += 1
                    if data[c] > 9:
                        data[c] = 0
                        flashed.append(c)

    return flashes

def part2(data):
    flashed = []
    step = 1
    check = lambda a, _: 0 < a
    while step > 0:
        for i, j in data:
            data[(i, j)] += 1
            if data[(i, j)] > 9:
                data[(i, j)] = 0
                flashed.append((i, j))

        while flashed:
            x, y = flashed.pop()
            for c in data.neighbors(x, y, diagonals=True, check=check):
                if data.get(c):
                    data[c] += 1
                    if data[c] > 9:
                        data[c] = 0
                        flashed.append(c)

        if not any(list(data.values())):
            break

        step += 1

    return step
