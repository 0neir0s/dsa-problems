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
