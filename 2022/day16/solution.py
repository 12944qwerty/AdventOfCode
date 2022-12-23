"""
Day 16: Proboscidea Volcanium

Part 1: 
Part 2: 
"""

import re
from queue import PriorityQueue

class Node:
    def __init__(self, valve, rate, tunnel):
        self.valve = valve
        self.rate = int(rate)
        self.tunnels = tunnel.split(', ')
        self.open = False

    def neighbors(self, graph):
        nodes = []

        for i in self.tunnels:
            nodes.append(graph[i])

        return nodes

    def __str__(self):
        return f"<Node valve='{self.valve}' rate='{self.rate}'>"

    def __repr__(self):
        return f"<Node valve='{self.valve}' rate='{self.rate}'>"

def parse_data(f):
    reg = re.compile("Valve (\w\w) has flow rate=(\d+?); tunnels? leads? to valves? ((?:\w\w,? ?)+)")
    stuff = [reg.match(a).groups() for a in f.read().splitlines()]
    data = {}
    for valve, rate, tunnel in stuff:
        data[valve] = Node(valve, rate, tunnel)

    return data
    
def part1(data):
    total = 0
    current = data['AA']
    opening = False
    travel = False
    foundPath = None

    seen = set()
    queue = PriorityQueue()
    queue.put((0, [current]))
    possiblePaths = []
    while queue.not_empty:
        pressure, path = queue.get()
        pressure *= -1
        if len(set(path)) == len(data) and len(path) < 18:
            foundPath = path
            break
        if len(path) > 28:
            if len(set(path)) == len(data):
                foundPath = path
                break
            continue

        neighbors = path[-1].neighbors(data)
        seen.add(path[-1])

        for node in neighbors:
            if len(set(path)) == len(data) or len(path) > 28:
                possiblePaths.append(len(path))
                break
        else:
            for node in neighbors:
                queue.put((-(pressure + node.rate), path+[node]))

    total = 0
    min = 0
    for node in foundPath:
        if node.open:
            continue
        else:
            print(node)
            total += (30 - min) * node.rate
            node.open = True

    return total

    # return min(possiblePaths)

def part2(data):
    pass
