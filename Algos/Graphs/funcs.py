from __future__ import annotations
from Jellybeans.Structures import Graph, Queue
from Jellybeans.Algos.Graphs.pfuncs import _BFS, _path_construction

def reachability(graph:Graph, source:int, destination:int) -> tuple:
    '''
    This function checks if it is possible to travel from a source vertex to a destination vertex \n
    Args:
        graph: Graph object
        source: Source vertex
        destination: Destination vertex
    Returns:
        A tuple consisting of a boolean value and the path to travel from source to destination.
    '''
    visited = []
    parent = []
    mapping = {}
    counter = 0
    for v in graph.list_vertices():
        visited.append(0)
        parent.append(-1)
        mapping[v] = counter
        counter += 1
    adj_list = graph.to_adjList()
    _BFS(visited, parent, mapping, source, adj_list)
    return (True, _path_construction(parent, mapping, source, destination)) if visited[mapping[destination]] == 1 else (False, None)

def counting_components(graph:Graph) -> int:
    '''
    This function checks for the number of components in an UNDIRECTED graph. \n
    Args:
        graph: Graph object
    Returns:
        Number of connected components
    '''
    components = 0
    visited = []
    parent = []
    mapping = {}
    counter = 0
    vertices = graph.list_vertices()
    for v in vertices:
        visited.append(0)
        parent.append(-1)
        mapping[v] = counter
        counter += 1
    adj_list = graph.to_adjList()
    for v in vertices:
        if visited[mapping[v]] == 0:
            components += 1
            _BFS(visited, parent, mapping, v, adj_list)
    return components

def topological_sort(graph:Graph) -> list:
    '''
    Performs a topological sort on the graph. Based on Kahn's Algorithm
    Args:
        graph: Graph object
    Returns:
        List containing a valid topological ordering
    '''
    in_degree = []
    mapping = {}
    toposort = []
    vertices = graph.list_vertices()
    inv_map = [0 for _ in vertices]
    adj_list = graph.to_adjList()
    counter = 0
    q = Queue()
    for v in vertices:
        in_degree.append(0)
        mapping[v] = counter
        inv_map[counter] = v
        counter += 1
    for _, vTo,_ in graph.to_edgeList():
        in_degree[mapping[vTo]] += 1

    for idx in range(len(in_degree)):
        if in_degree[idx] == 0:
            q.enqueue(inv_map[idx])

    while not q.isEmpty():
        tex = q.dequeue()
        toposort.append(tex)
        for v,_ in adj_list[tex]:
            in_degree[mapping[v]] -= 1
            if in_degree[mapping[v]] == 0:
                q.enqueue(v)
    return toposort