from __future__ import annotations
from jellybeans.structures import Queue, Graph
from jellybeans.exceptions.negative_cycle import _Negativecycle


def _initializer(visited: bool, parent: bool, mapping: bool, graph: Graph) -> tuple:
    '''
    Initializer function which helps in producing lists used in graph traversals 

    Args:
        visited: init the visited list?
        visited: init the parent list?
        visited: init the mapping dict?
    Returns:
        A tuple containing the lists
    '''
    visited_lst = [] if visited else None
    parent_lst = [] if parent else None
    mapping_dict = {} if mapping else None
    counter = 0
    for v in graph.list_vertices():
        if visited:
            visited_lst.append(0)
        if parent:
            parent_lst.append(-1)
        if mapping:
            mapping_dict[v] = counter
        counter += 1
    return (visited_lst, parent_lst, mapping_dict)


def _BFS(visited: list, parent: list, mapping: dict, source: int, adj_list: dict) -> None:
    '''
    This is a modified version of Breath First Search 

    Args:
        visited: List to show if a vertex has been visited
        parent: List to show the parent of the current vertex
        mapping: Mapping of vertice number to index number
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
    '''
    q = Queue()
    q.enqueue(source)
    visited[mapping[source]] = 1
    while not q.is_empty():
        tex = q.dequeue()
        for v, _ in adj_list[tex]:
            if visited[mapping[v]] == 0:
                visited[mapping[v]] = 1
                parent[mapping[v]] = tex
                q.enqueue(v)


def _dfs(visited: list, source: int, adj_list: dict, mapping: dict) -> None:
    '''
    This is a modified version of Depth First Search 

    Args:
        visited: List to show if a vertex has been visited
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
        mapping: Mapping of vertice number to index number
    '''
    visited[mapping[source]] = 1
    for neighbor, _ in adj_list[source]:
        if visited[mapping[neighbor]] == 0:
            _dfs(visited, neighbor, adj_list, mapping)


def _path_construction(parent: list, mapping: dict, source: int, destination: int) -> tuple:
    '''
    Finds a valid path from the source vertex to the destination vertex 

    Args:
        parent: A list of the vertex's predescessor
        mapping: Mapping of vertice number to index nu
        source: Source vertex
        destination: Destination vertex
    Returns:
        A tuple containing the valid path
    '''
    path = []
    end = mapping[destination]
    end_v = destination
    source = mapping[source]
    while end != source:
        path.append(end_v)
        end_v = parent[end]
        end = mapping[parent[end]]
    path.append(end_v)
    path.reverse()
    return tuple(path)


def _dfs_topo(visited: list, toposort_arr: list, source: int, adj_list: dict, mapping: dict) -> None:
    '''
    This is a helper function used for the DFS implementation of the topological sort 

    Args:
        visited: List to show if a vertex has been visited
        toposort_arr: List that contains the toposort ordering
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
        mapping: Mapping of vertice number to index number
    '''
    visited[mapping[source]] = 1
    for neighbor, _ in adj_list[source]:
        if visited[mapping[neighbor]] == 0:
            _dfs_topo(visited, toposort_arr, neighbor, adj_list, mapping)
    toposort_arr.append(source)


def _relax(vertex_from: int, vertex_to: int, weight: int, parent: list, cost: list) -> None:
    '''
    This is a internal function used to relax weight costs in SSSP Algorithms
    Args:
        vertex_from: Source vertex
        vertex_to: Neighbouring vertex to source
        weight: edge weight connecting vertex_from to vertex_to
        parent: parent list
        cost: cost list
    '''
    if cost[vertex_to] > cost[vertex_from] + weight:
        cost[vertex_to] = cost[vertex_from] + weight
        parent[vertex_to] = vertex_from


def _dfs_sssp_tree(vertex: int, parent: list, cost: list, adj_list: list, mapping: list) -> None:
    '''
    DFS implementation of doing SSSP on trees
    Args:
        vertex: Source vertex
        parent: Parent list
        cost: Cost list
        adj_list: Adjacency list
        mapping: mapping of vertices to indexes
    '''
    for neighbor, weight in adj_list[vertex]:
        if cost[mapping[neighbor]] == 1000000000:
            _relax(mapping[vertex], mapping[neighbor], weight, parent, cost)
            _dfs_sssp_tree(neighbor, parent, cost, adj_list, mapping)
        else:
            if cost[mapping[vertex]] + weight < cost[mapping[neighbor]]:
                raise _Negativecycle("Edge with negative weight detected!")


def _bfs_sssp_unweighted(vertex: int, parent: list, cost: list, adj_list: list, mapping: list) -> None:
    '''
    BFS implementation of doing SSSP on unweighted graphs
    Args:
        vertex: Source vertex
        parent: Parent list
        cost: Cost list
        adj_list: Adjacency list
        mapping: mapping of vertices to indexes
    '''
    q = Queue()
    q.enqueue(vertex)

    while not q.is_empty():
        curr = q.dequeue()
        for neighbor, weight in adj_list[curr]:
            if cost[mapping[neighbor]] == 1000000000:
                cost[mapping[neighbor]] = cost[mapping[curr]] + weight
                parent[mapping[neighbor]] = mapping[curr]
                q.enqueue(neighbor)
            else:
                if cost[mapping[curr]] + weight < cost[mapping[neighbor]]:
                    raise _Negativecycle("Edge with negative weight detected!")


def _floyd_sp(vertices: list, adj_list: list) -> tuple:
    '''
    Floyd Warshall algorithm to find the shortest path estimate for every pair of vertices
    Args:
        vertices: List of vertices
        adj_list: Adjacency list for every matrix
    '''
    mapping = {v: idx for idx, v in enumerate(vertices)}
    res = [[1000000000 for _ in vertices] for _ in vertices]

    for v in vertices:
        res[v][v] = 0
        for neighbor, weight in adj_list[v]:
            res[mapping[v]][mapping[neighbor]] = weight

    for a in range(len(vertices)):
        for b in range(len(vertices)):
            for c in range(len(vertices)):
                if res[b][a] != 1000000000 and res[a][c] != 1000000000:
                    res[b][c] = min(res[b][c], res[b][a] + res[a][c])
    return res, mapping


def _floyd_reachability(vertices: list, adj_list: list) -> tuple:
    '''
    Floyd Warshall algorithm to find reachability for every pair of vertices
    Args:
        vertices: List of vertices
        adj_list: Adjacency list for every matrix
    '''
    mapping = {v: idx for idx, v in enumerate(vertices)}
    res = [[0 for _ in vertices] for _ in vertices]

    for v in vertices:
        for neighbor, _ in adj_list[v]:
            res[mapping[v]][mapping[neighbor]] = 1

    for a in range(len(vertices)):
        for b in range(len(vertices)):
            for c in range(len(vertices)):
                if res[b][a] != 0 and res[a][c] != 0:
                    res[b][c] = 1 if res[b][c] or (
                        res[b][a] and res[a][c]) else 0
    return res, mapping


def _floyd_detect_cycle(vertices: list, adj_list: list) -> tuple:
    '''
    Floyd Warshall algorithm to detect cycles for every pair of vertices
    Args:
        vertices: List of vertices
        adj_list: Adjacency list for every matrix
    '''
    mapping = {v: idx for idx, v in enumerate(vertices)}
    res = [[1000000000 for _ in vertices] for _ in vertices]

    for v in vertices:
        for neighbor, weight in adj_list[v]:
            res[mapping[v]][mapping[neighbor]] = weight

    for a in range(len(vertices)):
        for b in range(len(vertices)):
            for c in range(len(vertices)):
                if res[b][a] != 1000000000 and res[a][c] != 1000000000:
                    res[b][c] = min(res[b][c], res[b][a] + res[a][c])
    return res, mapping
