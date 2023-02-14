"""
Day 13: Transparent Origami

Part 1: 
Part 2: 
"""

def parse_data(f):
    data = f.read().strip()
    points, instr = data.split('\n\n')
    points = [tuple(map(int, a.split(','))) for a in points.strip().splitlines()]
    instr = [a.replace('fold along ', '').split('=') for a in instr.strip().splitlines()]
    instr = [(a[0], int(a[1])) for a in instr]

    return points, instr

def part1(data):
    points: list = data[0]
    instr: list = data[1]

    for d, line in instr:
        if d == 'y':
            for i, coord in enumerate(points):
                if coord[1] > line:
                    points[i] = coord[0], 2 * line - coord[1]
        if d == 'x':
            for i, coord in enumerate(points):
                if coord[0] > line:
                    points[i] = 2 * line - coord[0], coord[1]

        points = list(set(points))
        break

    return len(points)

def part2(data):
    points: list = data[0]
    instr: list = data[1]

    for d, line in instr:
        if d == 'y':
            for i, coord in enumerate(points):
                if coord[1] > line:
                    points[i] = coord[0], 2 * line - coord[1]
        if d == 'x':
            for i, coord in enumerate(points):
                if coord[0] > line:
                    points[i] = 2 * line - coord[0], coord[1]

        points = list(set(points))

    minx = min(points, key=lambda a:a[0])[0]
    maxx = max(points, key=lambda a:a[0])[0]+1
    miny = min(points, key=lambda a:a[1])[1]
    maxy = max(points, key=lambda a:a[1])[1]+1

    for y in range(miny, maxy):
        for x in range(minx, maxx):
            if (x, y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()

    return len(points)
