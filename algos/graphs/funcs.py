from __future__ import annotations
from Jellybeans.structures import Graph, Queue, PriorityQueue, UFDS
from .pfuncs import (
    _BFS,
    _path_construction,
    _DFS_topo,
    _DFS, _initializer,
    _dfs_sssp_tree,
    _bfs_sssp_unweighted,
    _relax,
    _floyd_SP,
    _floyd_reachability,
    _floyd_detect_cycle
)
from Jellybeans.exceptions.Negativecycle import _Negativecycle


def reachability(graph: Graph, source: int, destination: int) -> tuple:
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


def counting_components(graph: Graph) -> int:
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


def topological_sort(graph: Graph) -> list:
    '''
    Performs a topological sort on the directed graph. Based on Kahn's Algorithm \n
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
    for _, vTo, _ in graph.to_edgeList():
        in_degree[mapping[vTo]] += 1

    for idx in range(len(in_degree)):
        if in_degree[idx] == 0:
            q.enqueue(inv_map[idx])

    while not q.isEmpty():
        tex = q.dequeue()
        toposort.append(tex)
        for v, _ in adj_list[tex]:
            in_degree[mapping[v]] -= 1
            if in_degree[mapping[v]] == 0:
                q.enqueue(v)
    return toposort


def DFS_toposort(graph: Graph) -> list:
    '''
    Performs a topological sort on the directed graph. This is a DFS implementation \n
    Args:
        graph: Graph object
    Returns:
        List containing a valid topological ordering
    '''
    vertices = graph.list_vertices()
    toposort = []
    visited, _, mapping = _initializer(True, False, True, graph)
    for v in vertices:
        if visited[mapping[v]] == 0:
            _DFS_topo(visited, toposort, v, graph.to_adjList(), mapping)
    toposort.reverse()
    return toposort


def count_strong_connected_components(graph: Graph) -> int:
    '''
    Finds the number of strongly connected components (SCC) in a directed graph \n
    Args:
        graph: Graph object
    Returns:
        Number of SCCs
    '''
    toposort = DFS_toposort(graph)
    SCC = 0
    visited, _, mapping = _initializer(True, False, True, graph)
    for idx in range(len(toposort)):
        ele = toposort[idx]
        if visited[mapping[ele]] == 0:
            SCC += 1
            _DFS(visited, ele, graph.transpose().to_adjList(), mapping)
    return SCC


def spanning_tree_prim(graph: Graph, source: int, minimum: bool) -> Graph:
    '''
    Finds the minimum/maximum spanning tree of a graph using Prim's Algorithm \n
    Args:
        graph: Graph Object
        source: Source vertex to begin algorithm
        minimum: True=minimum, False=Maximum
    Returns:
        Graph object of the mst
    '''
    adj_list = graph.to_adjList()
    mst = Graph()
    visited, _, mapping = _initializer(True, True, True, graph)
    pq = PriorityQueue(comparator=(
        lambda x, y: x[2] <= y[2]) if minimum else (lambda x, y: x[2] >= y[2]))
    for v in graph.list_vertices():
        mst.add_vertex(v)

    for vTo, weight in adj_list[source]:
        pq.insert((source, vTo, weight))
    visited[source] = 1
    while not pq.isEmpty():
        vFrom, vTo, weight = pq.extract()
        if visited[mapping[vTo]] == 0:
            mst.add_bidirected_edge(vFrom, vTo, (weight, weight))
            visited[mapping[vTo]] = 1
            for to, w in adj_list[vTo]:
                if visited[mapping[to]] == 0:
                    pq.insert((vTo, to, w))
    return mst


def spanning_tree_kruskal(graph: Graph, minimum: bool) -> Graph:
    '''
    Finds the minimum/maximum spanning tree of a graph using Kruskal's Algorrithm \n
    Args:
        graph: Graph Object
        minimum: True=minimum, False=Maximum
    Returns:
        Graph object of the mst
    '''
    edge_list_sorted = sorted(
        graph.to_edgeList(), key=lambda x: x[2], reverse=not minimum)
    counter = 1
    mapping = {}
    mst = Graph()
    ufds = UFDS(graph.num_vertices())

    for v in graph.list_vertices():
        mst.add_vertex(v)
        mapping[v] = counter
        counter += 1
    for vFrom, vTo, weight in edge_list_sorted:
        if not ufds.isSameSet(mapping[vFrom], mapping[vTo]):
            ufds.union(mapping[vFrom], mapping[vTo])
            mst.add_bidirected_edge(vFrom, vTo, (weight, weight))
    return mst


def sssp_tree(graph: Graph, source: int) -> dict:
    '''
    Finds the single source shortest path of a tree.
    Args:
        graph: Graph Object
        source: Source vertex Number
    Returns:
        A dictionary of vertex -> cost
    '''
    if not graph.is_tree():
        raise TypeError("This graph is not a tree")

    vertices = graph.list_vertices()
    cost = [1000000000 for _ in vertices]
    parent = [-1 for _ in vertices]
    mapping = {vertices: idx for idx, vertices in enumerate(vertices)}
    cost[mapping[source]] = 0
    _dfs_sssp_tree(source, parent, cost, graph.to_adjList(), mapping)
    return {vertices[idx]: cost for idx, cost in enumerate(cost)}


def sssp_unweighted(graph: Graph, source: int) -> dict:
    '''
    Finds the single source shortest path of an unweighted graph.
    Args:
        graph: Graph Object
        source: Source vertex Number
    Returns:
        A dictionary of vertex -> cost
    '''
    if not graph.is_unweighted():
        raise TypeError("This graph is not unweighted")
    vertices = graph.list_vertices()
    cost = [1000000000 for _ in vertices]
    parent = [-1 for _ in vertices]
    mapping = {vertices: idx for idx, vertices in enumerate(vertices)}
    cost[mapping[source]] = 0
    _bfs_sssp_unweighted(source, parent, cost, graph.to_adjList(), mapping)
    return {vertices[idx]: cost for idx, cost in enumerate(cost)}


def sssp_DAG(graph: Graph, source: int) -> dict:
    '''
    Finds the single source shortest path of a Directed Acyclic Graph (DAG).
    Args:
        graph: Graph Object
        source: Source vertex Number
    Returns:
        A dictionary of vertex -> cost
    '''
    if not graph.is_DAG():
        raise TypeError("This graph is not a DAG")
    vertices = graph.list_vertices()
    cost = [1000000000 for _ in vertices]
    parent = [-1 for _ in vertices]
    mapping = {vertices: idx for idx, vertices in enumerate(vertices)}
    cost[mapping[source]] = 0

    topo = topological_sort(graph)

    for v_from in topo:
        for neighbor, weight in graph.to_adjList()[v_from]:
            _relax(mapping[v_from], mapping[neighbor], weight, parent, cost)

    return {vertices[idx]: cost for idx, cost in enumerate(cost)}


def sssp_bellman_ford(graph: Graph, source: int) -> dict:
    '''
    Find the single source shortest path of any weighted graph using the bellman ford algorithm.
    Args:
        graph: Graph Object
        source: Source vertex Number
    Returns:
        A dictionary of vertex -> cost
    '''
    vertices = graph.list_vertices()
    cost = [1000000000 for _ in vertices]
    parent = [-1 for _ in vertices]
    mapping = {vertices: idx for idx, vertices in enumerate(vertices)}
    cost[mapping[source]] = 0
    edge_list = graph.to_edgeList()

    for _ in range(len(vertices) - 1):
        for v_from, v_to, weight in edge_list:
            _relax(mapping[v_from], mapping[v_to], weight, parent, cost)

    for v_from, v_to, weight in edge_list:
        if cost[mapping[v_from]] != 1000000000 and cost[mapping[v_to]] > cost[mapping[v_from]] + weight:
            raise _Negativecycle("Negative Weight Cycle detected!")
    return {vertices[idx]: cost for idx, cost in enumerate(cost)}


def sssp_dijkstra(graph: Graph, source: int) -> dict:
    '''
    Find the single source shortest path of any graph with no negative weight edge.
    Args:
        graph: Graph Object
        source: Source vertex Number
    Returns:
        A dictionary of vertex -> cost
    '''
    if not graph.is_positive():
        raise TypeError("This graph contains negative weight edges")
    vertices = graph.list_vertices()
    pq = PriorityQueue(comparator=lambda x, y: x[0] <= y[0])
    costs = {}
    for v in vertices:
        if v == source:
            costs[v] = 0
            pq.insert([0, v])
        else:
            costs[v] = 1000000000
            pq.insert((1000000000, v))
    while not pq.isEmpty():
        curr_weight, curr_vertex = pq.extract()

        for neighbor, weight in graph.to_adjList()[curr_vertex]:
            if costs[neighbor] > curr_weight + weight:
                pq.update((costs[neighbor], neighbor),
                          (curr_weight + weight, neighbor))
                costs[neighbor] = curr_weight + weight
    return costs


def floyd_warshall(graph: Graph, type: int) -> tuple:
    if type == 1:
        return _floyd_SP(graph.list_vertices(), graph.to_adjList())
    elif type == 2:
        return _floyd_reachability(graph.list_vertices(), graph.to_adjList())
    elif type == 3:
        return _floyd_detect_cycle(graph.list_vertices(), graph.to_adjList())
    else:
        raise TypeError(
            "Invalid parameter type: type should be one of 1, 2, 3")