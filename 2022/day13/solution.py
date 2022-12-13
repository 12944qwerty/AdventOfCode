"""
Day 13: Distress Signal

Part 1: Find the sum of indices of pairs that are sorted already.
Part 2: Sort the entire lists and then multiply the indices of the dividers
"""

from functools import cmp_to_key
import sys

sys.setrecursionlimit(20000)

def parse_data(f):
    return [a for a in f.read().split('\n\n')]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    else:
        i = 0
        while i < len(left) and i < len(right):
            c = compare(left[i], right[i])
            if c == 1:
                return 1
            if c == -1:
                return -1
            i += 1

        if i == len(left) and i < len(right):
            return -1
        elif i == len(right) and i < len(left):
            return 1
        else:
            return 0


def part1(data):
    total = 0
    for i, comparison in enumerate(data):
        comparison = comparison.split('\n')
        total += (i + 1) * (-1 == compare(eval(comparison[0]), eval(comparison[1])))

    return total

def part2(data):
    data = [eval(a) for a in ('\n'.join(data)).splitlines()]
    data.append([[2]])
    data.append([[6]])
    sorte = sorted(data, key=cmp_to_key(lambda left, right: compare(left, right)))

    total = 1
    for i, item in enumerate(sorte):
        if item in [[[2]], [[6]]]:
            total *= i+1

    return total
