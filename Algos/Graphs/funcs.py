from __future__ import annotations
from Jellybeans.Structures import Graph, Queue
from Jellybeans.Algos.Graphs.pfuncs import _BFS, _path_construction, _DFS_topo, _DFS, _initializer

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
    visited, parent, mapping = _initializer(True, True, True, graph)
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
    visited, parent, mapping = _initializer(True, True, True, graph)
    vertices = graph.list_vertices()
    adj_list = graph.to_adjList()
    for v in vertices:
        if visited[mapping[v]] == 0:
            components += 1
            _BFS(visited, parent, mapping, v, adj_list)
    return components

def topological_sort(graph:Graph) -> list:
    '''
    Performs a topological sort on the directed graph. Based on Kahn's Algorithm
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

def DFS_toposort(graph:Graph) -> list:
    '''
    Performs a topological sort on the directed graph. This is a DFS implementation
    Args:
        graph: Graph object
    Returns:
        List containing a valid topological ordering
    '''
    vertices = graph.list_vertices()
    toposort =[]
    visited, _, mapping = _initializer(True, True, True, graph)
    for v in vertices:
        if visited[mapping[v]] == 0:
            _DFS_topo(visited, toposort, v, graph.to_adjList(), mapping)
    toposort.reverse()
    return toposort

def count_strong_connected_components(graph:Graph) -> int:
    '''
    Finds the number of strongly connected components (SCC) in a directed graph
    Args:
        graph: Graph object
    Returns:
        Number of SCCs
    '''
    toposort = DFS_toposort(graph)
    SCC = 0
    visited, _, mapping = _initializer(True, True, True, graph)
    for idx in range(len(toposort)):
        ele = toposort[idx]
        if visited[mapping[ele]] == 0:
            SCC += 1
            _DFS(visited, ele, graph.transpose().to_adjList(), mapping)
    return SCC

def minimum_spanning_tree(graph:Graph) -> Graph:
    pass