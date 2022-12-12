"""
Day 09: Rope Bridge

Part 1: Find the amount of places where the tail of a rope has touched.
Part 2: Find the amount of places where the tail of a 10 knot rope has touched

"""

DIR = dict(zip('ULDR', (-1j, -1, 1j, 1)))

def foo(x, y):
    return (x > y) - (x < y)

def parse_data(f):
    return [(a.split()[0], int(a.split()[1])) for a in f.read().splitlines()]

def part1(data):
    head = tail = 0
    seen = {tail}
    
    for dir, amt in data: # shuddup, idc, i'm overwriting dir
        for _ in range(amt):
            head += DIR[dir]
            dist = head - tail
            if abs(dist) >= 2:
                tail += foo(dist.real, 0) + 1j * foo(dist.imag, 0)

            seen.add(tail)

    return len(seen)

def part2(data):
    knots = [0]*10
    seen = {0}
    
    for dir, amt in data: # shuddup, idc, i'm overwriting dir
        for _ in range(amt):
            knots[0] += DIR[dir]
            for i in range(9):
                dist = knots[i] - knots[i + 1]
                if abs(dist) >= 2:
                    knots[i+1] += foo(dist.real, 0) + 1j * foo(dist.imag, 0)

            seen.add(knots[-1])

    return len(seen)
