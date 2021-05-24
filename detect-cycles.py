from math import inf
from heapq import heappush, heappop
from collections import defaultdict

class Graph(object):
    def __init__(self,vertices):
        self.nodes = vertices
        self.adj = defaultdict(list)

    def addEdge(self,a,b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.adj[a].append(b)

#------------------------------------------------------------------------
def detectCyclesDirected(graph):
    """ Detect if cycles present in a directed graph """

    def dfs(node):
        """ DFS from a node checking for cycles """
        if node in visited:
            return node in recursion
        visited.add(node)
        recursion.add(node)
        hasCycle = any(dfs(neighbor) for neighbor in graph.adj[node])
        if not hasCycle:
            recursion.remove(node)
        return hasCycle

    visited = set()
    recursion = set()
    return any(dfs(node) for node in graph.nodes)

g = Graph({0,1,2,3})
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(detectCyclesDirected(g))

#-----------------------------------------------------------------------
def detectCycleUndirected(graph):
    """ Detect if cycles present in an undirected graph """
    
    def dfs(node, parent):
        """ check if cycles are there from a node  """
        visited.add(node)
        for nbr in graph.adj[node]:
            if nbr in visited:
                if nbr != parent:
                    return True
                continue
            if dfs(nbr, node):
                return True
        return False 

    visited = set()
    return any(dfs(node, None) for node in graph.nodes if node not in visited)

g = Graph({0,1,2,3,4})
g.addEdge(1, 0)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(3, 0)
g.addEdge(3, 4)
g.addEdge(4, 3)
print(detectCycleUndirected(g))

g = Graph({0,1,2})
g.addEdge(0,1)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(2,1)
print(detectCycleUndirected(g))

#------------------------------------------------------------------------

def getTopologicalSort(graph):
    """ get topological sort of a graph """
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.adj[node]:
            dfs(neighbor)
        topology.append(node)

    topology, visited = [], set()
    for node in graph.nodes:
        dfs(node)
    while topology:
        print(topology.pop())

g = Graph({0,1,2,3,4,5})
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
getTopologicalSort(g)

#-------------------------------------------------------------------------

def allTopologies(graph):
    
    def dfs():
        nexts = [ v for v, e in outEdges.items() if (not e) and (v not in visited) ]
        if not nexts:
            output.append(list(path))
        for nxt in nexts:
            path.append(nxt)
            visited.add(nxt)
            for neighbor in graph[nxt]:
                outEdges[neighbor] -= 1
            dfs()
            for neighbor in graph[nxt]:
                outEdges[neighbor] += 1
            visited.remove(nxt)
            path.pop()

    path, output, visited, outEdges = [], [], set(), {v:0 for v in graph}
    for neighbors in graph.values():
        for neighbor in neighbors:
            outEdges[neighbor] += 1
    dfs()
    return output

print(allTopologies({0:[], 1:[], 2:[3], 3:[1], 4:[0,1], 5:[0,2]})) 

#-----------------------------------------------------------------------

def dijkstras(graph, source):
    distances = {vertex: inf for vertex in graph}
    distances[source] = 0
    pq = [(0, source)] 
    while len(pq) > 0:
        distance, vertex = heappop(pq)
        if distance > distances[vertex]:
            continue
        for neighbor, weight in graph[vertex].items():
            nDistance = distance + weight
            if nDistance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    return distances

example = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkstras(example, 'X'))
