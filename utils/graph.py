# Took algorithms, here are a ton of graph related structures that I learned

from collections import deque
from copy import deepcopy
from functools import cache

class Node:
    def __init__(self, value: object):
        self.value = value
        self.indegree = 0
        self.outdegree = 0
        self.outedges = []
        self.inedges = []
        
    @property
    def degree(self):
        return self.indegree + self.outdegree
    
    @property
    def edges(self):
        return self.outedges + self.inedges
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        return str(self.value) + f"({self.indegree}, {self.outdegree})"
    
    def __repr__(self):
        return str(self.value) + f"({self.indegree}, {self.outdegree})"
    
class Edge:
    def __init__(self, a: Node, b: Node, weight: int):
        self.a = a
        self.b = b
        self.weight = weight
        
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    
    def __hash__(self):
        return hash((self.a, self.b))
    
    def __contains__(self, node):
        return node == self.a or node == self.b
    
    def __str__(self):
        return f"{self.a} -> {self.b} ({self.weight})"
    
    def __repr__(self):
        return f"{self.a} -> {self.b} ({self.weight})"

class Graph:
    def __init__(self, edges: list=None):
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        
    def find_node_or_add(self, value: object) -> Node:
        for node in self.nodes:
            if node.value == value:
                return node
        n = Node(value)
        self.nodes.append(n)
        return n  
    
    def find_node(self, value: object) -> Node:
        for node in self.nodes:
            if node.value == value:
                return node
        return None 
        
    def add_edge(self, a: object, b: object, weight: int=1):
        a = self.find_node_or_add(a)
        b = self.find_node_or_add(b)
        
        self.edges.append(Edge(a, b, weight))
        a.outedges.append(self.edges[-1])
        b.inedges.append(self.edges[-1])
        a.outdegree += 1
        b.indegree += 1
        
    def neighbors(self, node: Node) -> list:
        return [e.b if e.a == node else e.a for e in self.edges if node in e]
    
class DirectedGraph(Graph):
    def neighbors(self, node: Node) -> list:
        return [e.b for e in self.edges if e.a == node]

    def topological(self):
        g = deepcopy(self) # clone since nodes get removed
        while g.nodes:
            for node in sorted(g.nodes, key=lambda a: (a.indegree, a.value)):
                if node.indegree == 0:
                    g.nodes.remove(node)
                    for neighbor in g.neighbors(node):
                        neighbor.indegree -= 1
                    yield node
                    break
            else:
                return
    
    @cache
    def bfs(self, start: Node, end: Node):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node == end:
                return visited
            queue.extend(self.neighbors(node))
        return visited
