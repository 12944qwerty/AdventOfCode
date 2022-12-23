"""
Day 20: Grove Positioning System

Part 1: 
Part 2: 
"""

from copy import copy

def parse_data(f):
    return [(i, int(a)) for i,a in enumerate(f.read().splitlines())]

def part1(data):
    instr = copy(data)
    l = len(instr)

    for ins in instr:
        ind = data.index(ins)
        data.insert((ins[1]+ind)%(l-1), data.pop(ind))

    for zero, i in instr:
        if i == 0:
            break

    first = (1000 + zero) % l
    second = (2000 + zero) % l
    third = (3000 + zero) % l

    return data[first][1] + data[second][1] + data[third][1]

def part2(data):
    pass
