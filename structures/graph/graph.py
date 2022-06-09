from __future__ import annotations
from jellybeans.exceptions.graph_property import _GraphProperty
from .private_funcs import _is_connected_n_acyclic, _topo_sort


class Graph:
    '''
    Basic Graph data structure.
    '''

    def __init__(self) -> None:
        self.__adj_list = {}
        self.__reachable_by = {}
        self.__unweighted = [True, None]
        self.__positive_weighted = True

    def add_vertex(self, node_id:int) -> None:
        '''
        Add a vertex into the graph 

        Args:
            node_id: Unique identifier of the vertice
        '''
        if node_id not in self.__adj_list and node_id not in self.__reachable_by:
            self.__adj_list[node_id] = []
            self.__reachable_by[node_id] = []
        else:
            raise _GraphProperty("Vertex already present in graph")

    def delete_vertex(self, vertex:int) -> None:
        '''
        Delete a vertex from the graph 

        Args:
            vertex: Unique identifier of the vertice
        '''
        if vertex not in self.__adj_list or vertex not in self.__reachable_by:
            raise _GraphProperty(f"Vertex {vertex} not present in graph")
        reachable = self.can_reach(vertex)
        connected = self.neighbours_of(vertex)

        for tex in reachable:
            self.delete_edge([tex, vertex])

        for node in connected:
            self.delete_edge([vertex, node])

        del self.__adj_list[vertex]
        del self.__reachable_by[vertex]
        
    def list_vertices(self) -> list:
        '''
        List the vertices in the graph 

        Returns:
            A list containing the unique identifiers of the vertices
        '''
        return list(self.__adj_list.keys())

    def num_vertices(self) -> int:
        '''
        Find the number of vertices in the graph 

        Returns:
            The number of vertices present in the graph
        '''
        return len(self.__adj_list)

    def add_edge(self, v_from:int, v_to:int, weight:int = 1) -> None:
        '''
        Add a directed edge into the graph 

        Args:
            v_from: The origin vertice
            v_to: The destination vertice
            weight: The weight/cost of the edge
        '''
        if v_from == v_to:
            raise _GraphProperty("Edges must connect 2 different vertices together")
        if v_from not in self.__adj_list or v_to not in self.__adj_list:
            raise _GraphProperty(f"Unable to add edge as vertex {v_from} or {v_to} not present in graph")
        edges = self.__adj_list[v_from]
        for v,_ in edges:
            if v == v_to:
                raise _GraphProperty(f"Edge {v_from} -> {v_to} already present in graph")
        edges.append((v_to, weight))
        if self.__unweighted[1] is None:
            self.__unweighted[1] = weight
        else:
            if self.__unweighted[0]:
                self.__unweighted[0] = weight == self.__unweighted[1]

        if self.__positive_weighted:
            self.__positive_weighted = weight >= 0
        self.__reachable_by[v_to].append(v_from)
    
    def add_bidirected_edge(self, v_from:int, v_to:int, weight:tuple = (1,1)) -> None:
        '''
        Add a bi-directed edge into the graph 

        Args:
            v_from: The origin vertice
            v_to: The destination vertice
            weight: The weight/cost of the edge in the form of a tuple
        '''
        self.add_edge(v_from, v_to, weight[0])
        self.add_edge(v_to, v_from, weight[1])
    
    def delete_edge(self, edge:list) -> None:
        '''
        Remove a directed edge from the graph 

        Args:
            edge: A list in the form of --> [source vertice, destination vertice]
        '''
        v_from, v_to = edge

        new_adj_list = []
        edge_counter = 0
        for e in self.__adj_list[v_from]:
            if e[0] != v_to:
                new_adj_list.append(e)
                edge_counter += 1
        if edge_counter == len(self.__adj_list[v_from]):
            raise _GraphProperty(f"Edge {edge} not found in the graph")
        
        self.__adj_list[v_from] = new_adj_list
        self.__reachable_by[v_to].remove(v_from)

    def update_edge_weight(self, edge:list, newWeight:int) -> None:
        '''
        Update the weight of an edge 

        Args:
            edge: A list in the form of --> [source vertice, destination vertice]
            newWeight: new weight of the edge
        '''
        vFrom, vTo = edge
        self.delete_edge(edge)
        self.add_edge(vFrom, vTo, newWeight)

    def neighbours_of(self, vertex:int) -> list:
        '''
        FInd the neighbours of a vertice 

        Args:
            vertex: Source vertex
        Returns:
            A list containing the neighbours
        '''
        return [x[0] for x in self.edges_of(vertex)]

    def num_neighbours(self, vertex:int) -> int:
        '''
        FInd the total number of neighbours of a vertice 

        Args:
            vertex: Source vertex
        Returns:
            Sum of neighbours
        '''
        return len(self.neighbours_of(vertex))

    def edges_of(self, vertex:int) -> list:
        '''
        FInd the outgoing edges of a vertex 

        Args:
            vertex: Source vertex
        Returns:
            list containing the outgoing edges
        '''
        return self.__adj_list[vertex].copy()

    def can_reach(self, vertex:int) -> list:
        '''
        FInd the outgoing edges of a vertex 

        Args:
            vertex: Source vertex
        Returns:
            list containing the incoming edges
        '''
        return self.__reachable_by[vertex].copy()

    def to_edge_list(self) -> list:
        '''
        Generate an edge list from the graph 
        
        Returns:
            The edge list
        '''
        res = []
        for vertex in self.list_vertices():
            edges = self.__adj_list[vertex]
            for e in edges:
                complete_edge = (vertex,) + e
                res.append(complete_edge)
        return res

    def transpose(self) -> Graph:
        '''
        Transpose the current graph
        
        Returns:
            The transposed graph
        '''
        new_g = Graph()
        for v in self.list_vertices():
            new_g.add_vertex(v)
        for v_from, v_to, weight in self.to_edge_list():
            new_g.add_edge(v_to, v_from, -weight)
        return new_g
        
    def to_adj_list(self) -> dict:
        '''
        Generate an adjancency list from the graph 
        
        Returns:
            The adjacency list in the form of a dictionary
        '''
        return self.__adj_list.copy()

    def to_adjMatrix(self):
        '''
        Generate an adjacency matrix from the graph 
        
        Returns:
            The adjacency matrix
        '''
        vertices = self.list_vertices()
        mapping = {v:idx for idx,v in enumerate(vertices)}
        res = [[0 for _ in vertices] for _ in vertices]
    
        for v in vertices:
            for neighbor, weight in self.__adj_list[v]:
                res[mapping[v]][mapping[neighbor]] = weight
        return mapping, res

    def is_tree(self) -> bool:
        '''
        Check if the graph is a tree
        
        Returns:
            true if the graph is a tree
        '''
        vertices = self.list_vertices()
        for v in vertices:
            res = _is_connected_n_acyclic(vertices, self.__adj_list, v)
            if not res:
                return False
        return True
        
    def is_unweighted(self) -> bool:
        '''
        Check if the graph is unweighted
        
        Returns:
            true if the graph is unweighted
        '''
        return self.__unweighted[0]

    def is_positive(self) -> bool:
        '''
        Check if the graph contains only positive edge weights
        
        Returns:
            true if the graph has no negative edge weights
        '''
        return self.__positive_weighted

    def is_dag(self) -> bool:
        '''
        Check if the graph is a Directed Acyclic Graph
        
        Returns:
            true if the graph is a directed acyclic graph
        '''
        toposort = _topo_sort(self.list_vertices(), self.to_adj_list(), self.to_edge_list())
        
        if len(toposort) < len(self.__adj_list):
            return False
        idxs = {toposort[idx]: idx for idx in range(len(toposort))}
        for v,edges in self.__adj_list.items():
            for edge,_ in edges:
                idx_v = idxs[v]
                idx_w = idxs[edge]
                if idx_v > idx_w:
                    return False
        return True