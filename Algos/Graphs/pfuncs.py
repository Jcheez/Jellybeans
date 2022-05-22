from Jellybeans.Structures import Queue

def _BFS(visited:list, parent:list, mapping:dict, source:int, adj_list:dict) -> None:
    '''
    This is a modified version of Breath First Search \n
    Args:
        visited: List to show if they have been visited
        visited: List to show the parent of the current node
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