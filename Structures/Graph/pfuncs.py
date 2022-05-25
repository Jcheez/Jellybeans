from __future__ import annotations

def _DFS_tree(visited: list, source: int, adj_list:dict, mapping:dict, parent_lst:list) -> bool:
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
            parent_lst[mapping[neighbor]] = mapping[source]
            if not _DFS_tree(visited, neighbor, adj_list, mapping, parent_lst):
                return False
        else:
            if parent_lst[mapping[source]] != mapping[neighbor]:
                return False
    return True
