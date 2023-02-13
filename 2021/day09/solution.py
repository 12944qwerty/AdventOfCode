"""
Day 09: Smoke Basin

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
    total = 0
    for i, j in data:
        col = data[(i, j)]
        if col < data.get((i, j+1), 9) and \
                col < data.get((i, j-1), 9) and \
                col < data.get((i+1, j), 9) and \
                col < data.get((i-1, j), 9):
            total += 1 + col

    return total


def part2(data):
    seen = set()

    def floodfill(area, x, y, prev):
        val = area.get((x, y), 9)
        if val == 9 or (x, y) in seen or prev >= val:
            return 0

        seen.add((x, y))

        return 1 + floodfill(area, x+1, y, val) + \
            floodfill(area, x-1, y, val) + \
            floodfill(area, x, y+1, val) + \
            floodfill(area, x, y-1, val)

    floods = []

    for i, j in data:
        col = data[(i, j)]
        if col < data.get((i, j+1), 9) and \
                col < data.get((i, j-1), 9) and \
                col < data.get((i+1, j), 9) and \
                col < data.get((i-1, j), 9):
            floods.append(floodfill(data, i, j, col-1))

    total = 1
    for i in sorted(floods)[:-4:-1]:
        total *= i

    return total
