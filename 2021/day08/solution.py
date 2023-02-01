"""
Day 08: Seven Segment Search

Part 1: 
Part 2: 
"""

from itertools import permutations

def parse_data(f):
    return [[b.split() for b in a.split(" | ")] for a in f.readlines()]

def part1(data):
    total = 0
    for _, out in data:
        for codes in out:
            total += len(codes) in [2, 4, 3, 7]

    return total


def part2(data):
    displays = {frozenset(v): str(i) for i, v in enumerate([
        "abcefg", # 0
        "cf", # 1
        "acdeg", # 2
        "acdfg", # 3
        "bcdf", # 4
        "abdfg", # 5
        "abdefg", # 6
        "acf", # 7
        "abcdefg", # 8
        "abcdfg", # 9
    ])}

    perms = [str.maketrans("".join(a), "abcdefg") for a in permutations("abcdefg", 7)]

    total = 0
    for inp, out in data:
        for perm in perms:
            if all(frozenset(i.translate(perm)) in displays for i in inp):
                break

        num = ""
        for o in out:
            num += displays[frozenset(o.translate(perm))]

        total += int(num)

    return total
