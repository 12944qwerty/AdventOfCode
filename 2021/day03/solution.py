"""
Day 03: Binary Diagnostic

Part 1: 
Part 2: 
"""

def parse_data(f):
    return f.read().splitlines()

def part1(data):
    data = list(zip(*data))
    b = o = ""
    for digit in data:
        b += str(int(digit.count("1") > digit.count("0")))
        o += str(int(digit.count("1") < digit.count("0")))

    gamma = int(b, 2)
    epsilon = int(o, 2)

    return epsilon * gamma

def part2(data):
    oxy = co = data
    i = 0
    while len(oxy) > 1 or len(co) > 1:
        oxyzip = list(zip(*oxy))
        cozip = list(zip(*co))
        if len(oxy) > 1:
            oxy = [a for a in oxy if a[i] == str(int(oxyzip[i].count("1") >= oxyzip[i].count("0")))]
        if len(co) > 1:
            co = [a for a in co if a[i] == str(int(cozip[i].count("1") < cozip[i].count("0")))]

        i += 1

    oxy = int(oxy[0], 2)
    co = int(co[0], 2)

    return oxy * co
