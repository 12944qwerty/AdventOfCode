"""
Day 08: Treetop Tree House

Part 1: Find the amount of trees you can see from the outside
Part 2: Find the tree which can see the most trees.
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

def parse_data(f):
    return [list(map(int,a)) for a in f.read().splitlines()]

def part1(data):
    total = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            tree = data[i][j]
            for x, y in directions:
                i_, j_ = i, j

                while 0 < i_ < len(data) - 1 and 0 < j_ < len(data[0]) - 1: 
                    j_ += x
                    i_ += y
                    if data[i_][j_] >= tree:
                        break
                else:
                    break
            else:
                continue
            total += 1

    return total + len(data) * 2 + (len(data[0]) - 2) * 2

def part2(data):
    max = 0
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            tree = data[i][j]
            distance = 1
            for x, y in directions:
                i_, j_ = i, j
                d = 0

                while 0 < i_ < len(data) - 1 and 0 < j_ < len(data[0]) - 1:
                    j_ += x
                    i_ += y
                    d += 1
                    if data[i_][j_] >= tree:
                        break
                distance *= d
            if distance > max:
                max = distance

    return max