"""
Day 12: Hill Climbing Algorithm

My first time actually doing pathfinding. BFS
I have not tried optimizing or shorter solutions. Everything has been expanded so I can learn.

Part 1: Find shortest path to top of the mountain
Part 2: 
"""

class Node:
    def __init__(self, position=None, height=None):
        self.position = position
        self.height = height
        self.discovered = False
        self.parent = None

    def neighbors(self, graph, part2=False):
        nodes = []
        x, y = self.position

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            try:
                neighbor = graph[(i + x, j + y)]

                if part2:
                    if self.height - neighbor.height < 2:
                        nodes.append(neighbor)
                elif neighbor.height < self.height + 2:
                    nodes.append(neighbor)
            except KeyError:
                pass

        return nodes

    def __str__(self):
        return f"<Node at position={str(self.position)} height={str(self.height)}>"

    def __repr__(self):
        return f"<Node at position={str(self.position)} height={str(self.height)}>"

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return int(str(self.position[0]).zfill(3) + str(self.position[1]).zfill(3))

def parse_data(f):
    startingIndex = endingIndex = None
    path = [list(a) for a in f.read().splitlines()]
    graph = {}
    a = []
    for i in range(len(path)):
        for j in range(len(path[i])):
            if path[i][j] == 'S':
                path[i][j] = 1
                startingIndex = i, j
            elif path[i][j] == 'E':
                path[i][j] = 26
                endingIndex = i, j
            else:
                path[i][j] = ord(path[i][j]) - 96
            
            if path[i][j] == 1:
                a.append((i, j))
            graph[(i, j)] = Node((i, j), path[i][j])

    return graph, startingIndex, endingIndex, a

def part1(data):
    graph, start, end, _ = data
    start = graph[start]
    end = graph[end]

    seen = set()
    queue = [[start]]
    possiblePaths = []
    while len(queue):
        neighbors = queue[0][-1].neighbors(graph)
        seen.add(queue[0][-1])
        if end in neighbors:
            possiblePaths.append(queue[0])

        for node in neighbors:
            for path in queue:
                if node in path:
                    break
            else:
                if node not in seen:
                    queue.append(queue[0]+[node])
        queue.pop(0)

    return len(min(possiblePaths, key=lambda a: len(a)))

def part2(data):
    graph, _, start, lowest = data
    start = graph[start]

    seen = set()
    queue = [[start]]
    possiblePaths = []
    while len(queue):
        neighbors = queue[0][-1].neighbors(graph, True)
        seen.add(queue[0][-1])

        for node in neighbors:
            if node.height == 1:
                possiblePaths.append(len(queue[0]))
                break
        else:
            for node in neighbors:
                for path in queue:
                    if node in path:
                        break
                else:
                    if node not in seen:
                        queue.append(queue[0]+[node])
        queue.pop(0)

    return min(possiblePaths)
