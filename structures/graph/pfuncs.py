from __future__ import annotations
from jellybeans.structures import Queue

def _DFS_tree(visited: list, source: int, adj_list:dict, mapping:dict, parent:int) -> bool:
    '''
    This is a modified version of Depth First Search used to check if a graph is a tree \n
    Args:
        visited: List to show if a vertex has been visited
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
        mapping: Mapping of vertice number to index number
        parent_lst: List of parents of a node
    '''
    visited[mapping[source]] = 1
    for neighbor, _ in adj_list[source]:
        if visited[mapping[neighbor]] == 0:
            if not _DFS_tree(visited, neighbor, adj_list, mapping, source):
                return False
        elif neighbor != parent:
            return False
    return True

def _is_connected_n_acyclic(vertices:list, adj_list:list, source:int):
    visited = [0 for v in vertices]
    mapping = {vertices[idx]:idx for idx in range(len(vertices))}
    if not _DFS_tree(visited, source, adj_list, mapping, source):
        return False
    for v in visited:
        if v != 1:
            return False
    return True

def _topo_sort(vertices:list, adj_list:list, edge_list:list) -> list:
    '''
    Performs a topological sort on the graph. Based on Kahn's Algorithm \n
    Args:
        graph: Graph object
    Returns:
        List containing a valid topological ordering
    '''
    in_degree = []
    mapping = {}
    toposort = []
    inv_map = [0 for _ in vertices]
    counter = 0
    q = Queue()
    for v in vertices:
        in_degree.append(0)
        mapping[v] = counter
        inv_map[counter] = v
        counter += 1
    for _, vTo,_ in edge_list:
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