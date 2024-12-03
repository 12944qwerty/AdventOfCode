# Took algorithms, here are a ton of graph related structures that I learned

from copy import deepcopy

class Node:
    def __init__(self, value: str):
        self.value = value
        self.indegree = 0
        self.outdegree = 0
        
    @property
    def degree(self):
        return self.indegree + self.outdegree
        
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
    
    def __str__(self):
        return self.value + f"({self.indegree}, {self.outdegree})"
    
    def __repr__(self):
        return self.value + f"({self.indegree}, {self.outdegree})"

class Graph:
    def __init__(self, edges: list=None):
        self.nodes: set[Node] = set()
        self.edges: tuple[Node, Node, int] = []
        
    def find_node_or_add(self, value: str) -> Node:
        for node in self.nodes:
            if node.value == value:
                return node
        n = Node(value)
        self.nodes.add(n)
        return n   
        
    def add_edge(self, a: str, b: str, weight: int=1):
        a = self.find_node_or_add(a)
        b = self.find_node_or_add(b)
        
        self.edges.append((a, b, weight))
        a.outdegree += 1
        b.indegree += 1
        
    def neighbors(self, node: Node) -> list:
        return [b for a, b, w in self.edges if a == node]
    
class DirectedGraph(Graph):
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
