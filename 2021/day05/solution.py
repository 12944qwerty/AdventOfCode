"""
Day 05: Hydrothermal Venture

Part 1: 
Part 2: 
"""

def parse_data(f):
    return [list(zip(*[tuple(map(int, a.split(','))) for a in b.split(' -> ')])) for b in f.read().splitlines()]

def part1(data):
    tubes = set()
    total = set()
    for a, b in data:
        if a[0] == a[1] or b[0] == b[1]:
            for x in range(min(a), max(a)+1):
                for y in range(min(b), max(b)+1):
                    if (x, y) in tubes:
                        total.add((x, y))
                    tubes.add((x, y))

    return len(total)

def part2(data):
    tubes = set()
    total = set()
    for a, b in data:
        if a[0] == a[1] or b[0] == b[1]:
            for x in range(min(a), max(a)+1):
                for y in range(min(b), max(b)+1):
                    if (x, y) in tubes:
                        total.add((x, y))
                    tubes.add((x, y))
        else:
            x = a[0]
            y = b[0]

            dx = int((a[1] - x) / abs(a[1] - x))
            dy = int((b[1] - y) / abs(b[1] - y))
            while x != a[1] + dx:
                if (x, y) in tubes:
                    total.add((x, y))
                tubes.add((x, y))

                x += dx
                y += dy

    return len(total)
