"""
Day 15: Beacon Exclusion Zone

Part 1: Find the number of spots that you know for a fact don't contain a beacon.
Part 2: Find the only spot that a beacon isn't picked up by a sensor.
"""

import re

def parse_data(f):
    reg = re.compile("Sensor at x=(-?\d+?), y=(-?\d+?): closest beacon is at x=(-?\d+?), y=(-?\d+)")
    data = [list(map(int,reg.match(a).groups())) for a in f.read().splitlines()]
    for i, coords in enumerate(data):
        x1, y1, x2, y2 = coords
        data[i] = [*coords, abs(y2 - y1) + abs(x2 - x1)]
    
    return data

def part1(data):
    beacons = set()
    minx = 1e9
    maxx = 0
    yLevel = 10 if globals()['dummy'] else 2000000
    for x1, y1, x2, y2, mdist in data:
        if (dist:=abs(yLevel-y1)) < mdist: # sensor in range of line
            rem = mdist - dist
            minx = min(minx, x1 - rem)
            maxx = max(maxx, x1 + rem+1)

        if y2 == yLevel:
            beacons.add(x2)

    return maxx - minx - len(beacons)


def part2(data):
    maxc = 20 if globals()['dummy'] else 4000000
    for sx, sy, _, _, mdist in data:
        for y1 in range(mdist+2):
            x1 = (mdist+1) - y1

            for dx, dy in (-1,-1),(1,-1),(-1,1),(1,1):
                x = sx + dx*x1
                y = sy + dy*y1

                if not(0<=x<=maxc and 0<=y<=maxc):
                    continue
                
                for sx1, sy1, _, _, dist in data:
                    if abs(x-sx1) + abs(y-sy1) <= dist:
                        break
                else:
                    return int(4000000*x + y)
    
    return "ewhguwogh"
