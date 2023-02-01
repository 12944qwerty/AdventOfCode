"""
Day 06: Lanternfish

Part 1: 
Part 2: 
"""

from copy import deepcopy

def parse_data(f):
    return list(map(int, f.read().strip().split(',')))

def part1(data):
    nums = [data.count(0), data.count(1), data.count(2), data.count(3), data.count(4), data.count(5), data.count(6), data.count(7), data.count(8)]

    for _ in "_"*80:
        c = deepcopy(nums)
        nums[0] = c[1]
        nums[1] = c[2]
        nums[2] = c[3]
        nums[3] = c[4]
        nums[4] = c[5]
        nums[5] = c[6]
        nums[6] = c[7] + c[0]
        nums[7] = c[8]
        nums[8] = c[0]

    return sum(nums)

def part2(data):
    nums = [data.count(0), data.count(1), data.count(2), data.count(3), data.count(4), data.count(5), data.count(6), data.count(7), data.count(8)]

    for _ in "_"*256:
        c = deepcopy(nums)
        nums[0] = c[1]
        nums[1] = c[2]
        nums[2] = c[3]
        nums[3] = c[4]
        nums[4] = c[5]
        nums[5] = c[6]
        nums[6] = c[7] + c[0]
        nums[7] = c[8]
        nums[8] = c[0]

    return sum(nums)
