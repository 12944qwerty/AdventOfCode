"""
Day 12: Passage Pathing

Part 1: 
Part 2: 
"""

from queue import Queue
from copy import deepcopy

class Node:
    def __init__(self, name: str):
        self.name = name
        self.connections = set()
        self.small = name.lower() == name
        self.visited = False

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"<Node {self.small} {self.name} with {[a.name for a in list(self.connections)]}>"

def parse_data(f):
    system = {}
    for a, b in [a.split('-') for a in f.read().splitlines()]:
        if a not in system:
            system[a] = Node(a)
        if b not in system:
            system[b] = Node(b)

        system[a].connections.add(system[b])
        system[b].connections.add(system[a])
    return system

def part1(system):
    queue = Queue()
    queue.put([system['start']])
    fin = set()
    while not queue.empty():
        q = queue.get()

        for c in q[-1].connections:
            if c.name == 'end':
                fin.add(tuple([*q, c]))
                continue
            elif c in q and c.small:
                continue
            else:
                queue.put([*q, c])

    return len(fin)

def part2(system):
    queue = Queue()
    queue.put([False, system['start']])
    fin = 0
    while not queue.empty():
        q = queue.get()

        for c in q[-1].connections:
            if c.name == 'start':
                pass
            elif c.name == 'end':
                fin += 1
            elif c.small and c in q:
                if not q[0]:
                    new = q[:]
                    new[0] = True
                    new.append(c)
                    queue.put(new)
            else:
                queue.put([*q, c])

    return fin
