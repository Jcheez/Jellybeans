from __future__ import annotations

def _DFS(visited: list, source: int, adj_list:dict, mapping:dict, parent:int) -> bool:
    '''
    This is a modified version of Depth First Search used to check if a graph is a tree \n
    Args:
        visited: List to show if a vertex has been visited
        source: Source Vertex
        adj_List: Graph structure stored in the form of an adjacency list
        mapping: Mapping of vertice number to index number
        parent: The parent vertex
    '''
    visited[mapping[source]] = 1
    for neighbor, _ in adj_list[source]:
        if visited[mapping[neighbor]] == 0:
            if not _DFS(visited, neighbor, adj_list, mapping, source):
                return False
        else:
            if parent != -1 and mapping[parent] != mapping[neighbor]:
                return False
    return True
