"""
Day 14: Regolith Reservoir

Part 1: 
Part 2: 
"""

def display(graph):
    minimumx = min(499, min(graph, key=lambda a: a[0])[0])
    maximumx = max(501, max(graph, key=lambda a: a[0])[0])
    maximumy = max(graph, key=lambda a: a[1])[1]

    for j in range(-1, maximumy+1):
        for i in range(minimumx-1, maximumx+2):
            # print(i, j, end='')
            if (i, j) in graph:
                print(graph[(i, j)], end='')
            else:
                print(' ', end='')
        print()

def parse_data(f):
    data = [[list(map(int, b.split(','))) for b in a.split(' -> ')] for a in f.read().splitlines()]

    rocks = {}

    for stuff in data:
        path = []
        for i in range(0,len(stuff)-1):
            ranges = list(zip(stuff[i], stuff[i+1]))
            if ranges[0][0] == ranges[0][1]:
                l = [(ranges[0][0], j) for j in range(min(ranges[1]), 1+max(ranges[1]))]
            elif ranges[1][0] == ranges[1][1]:
                l = [(j, ranges[1][0]) for j in range(min(ranges[0]), 1+max(ranges[0]))]
            else:
                print('hi')
            path += l

        for coord in path:
            rocks[coord] = '#'
    return rocks

def part1(rocks):
    didRest = True
    lowest = max(rocks, key=lambda a: a[1])[1]

    count = 0
    while didRest:
        didRest = False
        sand = [500, 0]

        while sand[1] < lowest + 2:
            sand[1] += 1
            if tuple(sand) in rocks: # falling into rock
                sand[0] -= 1
                if tuple(sand) in rocks: # left side is blocked?
                    sand[0] += 2
                    if tuple(sand) in rocks: # right side blocked?
                        didRest = True # now rest
                        sand[0] -= 1
                        sand[1] -= 1
                        rocks[tuple(sand)] = '+'
                        count += 1
                        break

    return count


def part2(rocks):
    didRest = True
    lowest = max(rocks, key=lambda a: a[1])[1]

    for i in range(300, 700):
        rocks[(i, lowest+2)] = '#'

    count = 0
    while didRest and (500, 0) not in rocks:
        didRest = False
        sand = [500, 0]

        while sand[1] < lowest + 2:
            sand[1] += 1
            if tuple(sand) in rocks: # falling into rock
                sand[0] -= 1
                if tuple(sand) in rocks: # left side is blocked?
                    sand[0] += 2
                    if tuple(sand) in rocks: # right side blocked?
                        didRest = True # now rest
                        sand[0] -= 1
                        sand[1] -= 1
                        rocks[tuple(sand)] = '+'
                        count += 1
                        break

    return count