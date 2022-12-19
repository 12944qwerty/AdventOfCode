"""
Day 19: Not Enough Minerals

Part 1: 
Part 2: 
"""

import re
from queue import PriorityQueue, Queue

class Blueprint:
    def __init__(self, blueprint):
        self.id = int(blueprint[0])
        self.ore = int(blueprint[1])
        self.clay = int(blueprint[2])
        self.obsidian = (int(blueprint[3]), int(blueprint[4]))
        self.geode = (int(blueprint[5]), int(blueprint[6]))

class Node:
    def __init__(self, ore, clay, obsidian, geode, time, oreAmt=0, clayAmt=0, obsidianAmt=0, geodeAmt=0):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.time = time

        self.oreAmt = oreAmt
        self.clayAmt = clayAmt
        self.obsidianAmt = obsidianAmt
        self.geodeAmt = geodeAmt

    def tick(self):
        self.oreAmt += self.ore
        self.clayAmt += self.clay
        self.obsidianAmt += self.obsidian
        self.geodeAmt += self.geode
        self.time -= 1

    def copy(self):
        cls = self.__class__
        return cls(self.ore, self.clay, self.obsidian, self.geode, self.time, self.oreAmt, self.clayAmt, self.obsidianAmt, self.geodeAmt)

    def __eq__(self, other):
        return self.ore == other.ore and self.clay == other.clay and self.obsidian == other.obsidian and self.geode == other.geode and \
            self.time == other.time and self.oreAmt == other.oreAmt and self.clayAmt == other.clayAmt and \
            self.obsidianAmt == other.obsidianAmt and self.geodeAmt == other.geodeAmt

    def __hash__(self):
        return hash((self.ore, self.clay, self.obsidian, self.geode, self.time, self.oreAmt, self.clayAmt, self.obsidianAmt, self.geodeAmt))

    def __lt__(self, other):
        # return self.obsidian*self.obsidianAmt*self.time > other.obsidian*other.obsidianAmt*other.time
        return self.obsidian > other.obsidian and self.obsidianAmt > other.obsidianAmt and self.time > other.time

def parse_data(f):
    reg = re.compile("^Blueprint (\d+?): Each ore robot costs (\d+?) ore\. Each clay robot costs (\d+?) ore. Each obsidian robot costs (\d+?) ore and (\d+?) clay\. Each geode robot costs (\d+?) ore and (\d+?) obsidian\.$")
    return [Blueprint(reg.match(a).groups()) for a in f.read().splitlines()]

def part1(data):
    total = 0
    for i, blueprint in enumerate(data):
        queue = PriorityQueue(1000000)
        seen = set()
        queue.put(Node(1, 0, 0, 0, 24))
        maxg = 0
        while queue.not_empty:
            current = queue.get()

            if len(seen) % 10000 == 0:
                print(current.time,current.geodeAmt,maxg,len(seen))

            maxg = max(current.geodeAmt, maxg)
            if current.time == 0:
                continue

            omax = max(blueprint.ore, blueprint.clay, blueprint.obsidian[0], blueprint.geode[0])
            current.ore = min(omax, current.ore)
            current.clay = min(current.clay, blueprint.obsidian[1])
            current.obsidian = min(current.obsidian, blueprint.geode[1])

            current.oreAmt = min(current.oreAmt, omax*current.time - current.ore*(current.time-1))
            current.clayAmt = min(current.clayAmt, blueprint.obsidian[1]*current.time - current.clay*(current.time-1))
            current.clayAmt = min(current.clayAmt, blueprint.geode[1]*current.time - current.obsidian*(current.time-1))

            if current in seen:
                continue

            seen.add(current)

            new = current.copy()
            new.tick()
            queue.put(new)
            if current.oreAmt >= blueprint.ore:
                new = current.copy()
                new.tick()
                new.oreAmt -= blueprint.ore
                new.ore += 1
                queue.put(new)
            if current.oreAmt >= blueprint.clay:
                new = current.copy()
                new.tick()
                new.oreAmt -= blueprint.clay
                new.clay += 1
                queue.put(new)
            if current.oreAmt >= blueprint.obsidian[0] and current.clayAmt >= blueprint.obsidian[1]:
                new = current.copy()
                new.tick()
                new.oreAmt -= blueprint.obsidian[0]
                new.clayAmt -= blueprint.obsidian[1]
                new.obsidian += 1
                queue.put(new)
            if current.oreAmt >= blueprint.geode[0] and current.obsidianAmt >= blueprint.geode[1]:
                new = current.copy()
                new.tick()
                new.oreAmt -= blueprint.geode[0]
                new.obsidianAmt -= blueprint.geode[1]
                new.geode += 1
                queue.put(new)

        print(i)

        total += -~i * maxg

    return total

def part2(data):
    pass
