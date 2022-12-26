"""
Day 25: Full of Hot Air

Part 1: 
Part 2: 
"""

def parse_data(f):
    return f.read().splitlines()

def get_max(place):
    if place == 1:
        return 2

    return place*2 + get_max(place // 5)

def snafu(num, place):
    directions = ['=', '-', '0', '1', '2']
    if -3 < num < 3:
        return directions[num+2]

    for dir in [-2, -1, 0, 1, 2]:
        new = num - place*dir
        if abs(new) <= get_max(place // 5):
            return directions[dir+2] + snafu(new, place // 5)

def part1(data):
    nums = 0
    for line in data:
        total = 0
        place = 1
        for c in line[::-1]:
            if c == '=':
                total -= 2*place
            elif c == '-':
                total -= place
            else:
                total += place * int(c)
            place *= 5

        nums += total

    place = 1
    while abs(nums) > get_max(place):
        place *= 5

    return snafu(nums, place)



def part2(data):
    pass
