"""
Day 11: Dumbo Octopus

Part 1: 
Part 2: 
"""

def parse_data(f):
    data = {}
    for i, line in enumerate(f.read().splitlines()):
        for j, col in enumerate(line):
            data[(i, j)] = int(col)

    return data

def part1(data):
    flashes = 0
    flashed = []
    for _ in range(100):
        for i, j in data:
            data[(i, j)] += 1
            if data[(i, j)] > 9:
                data[(i, j)] = 0
                flashed.append((i, j))

        while flashed:
            x, y = flashed.pop()
            flashes += 1
            for dx, dy in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
                c = (x+dx, y+dy)
                if data.get(c):
                    data[c] += 1
                    if data[c] > 9:
                        data[c] = 0
                        flashed.append(c)

    return flashes

def part2(data):
    flashed = []
    step = 1
    while step > 0:
        for i, j in data:
            data[(i, j)] += 1
            if data[(i, j)] > 9:
                data[(i, j)] = 0
                flashed.append((i, j))

        while flashed:
            x, y = flashed.pop()
            for dx, dy in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
                c = (x+dx, y+dy)
                if data.get(c):
                    data[c] += 1
                    if data[c] > 9:
                        data[c] = 0
                        flashed.append(c)

        if not any(list(data.values())):
            break

        step += 1

    return step
