from Jellybeans.Structures import Queue

def _BFS(visited:list, parent:list, mapping:dict, source:int, adj_list:dict) -> None:
    '''
    This is a modified version of Breath First Search \n
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
    while not q.isEmpty():
        tex = q.dequeue()
        for v,_ in adj_list[tex]:
            if visited[mapping[v]] == 0:
                visited[mapping[v]] = 1
                parent[mapping[v]] = tex
                q.enqueue(v)

def _DFS(visited: list, source: int, adj_list:dict, mapping:dict) -> None:
    '''
    This is a modified version of Depth First Search \n
    Args:
        visited: List to show if a vertex has been visited
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
        mapping: Mapping of vertice number to index number
    '''
    visited[mapping[source]] = 1
    for neighbor, _ in adj_list[source]:
        if visited[mapping[neighbor]] == 0:
            _DFS(visited, neighbor, adj_list, mapping)
    
def _path_construction(parent: list, mapping:dict, source:int, destination:int) -> tuple:
    '''
    Finds a valid path from the source vertex to the destination vertex \n
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

def _DFS_topo(visited: list, toposort_arr: list, source: int, adj_list:dict, mapping:dict) -> None:
    '''
    This is a helper function used for the DFS implementation of the topological sort \n
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
            _DFS_topo(visited, toposort_arr, neighbor, adj_list, mapping)
    toposort_arr.append(source)